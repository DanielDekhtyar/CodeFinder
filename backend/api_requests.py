"""
Code that preforms the API requests to GitHub and returns the relevant data
"""

import requests
import time
import os

from backend import helpers
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env file
load_dotenv()

# Store the last user search request in memory. eg. "Websites with flask"
LAST_USER_SEARCH_REQUEST = None
# Store the last GitHub search query in memory eg. "websites AND flask"
LAST_SEARCH_QUERY = None


def openai_api_request(user_search_request, context_message):
    """
    The `openai_api_request` function takes a user search request and a context message, checks if it is
    different from the last query, and if the request is different from the last request,
    it makes a new request to OpenAI API to get a GitHub search query using a fine-tuned model.

    Args:
    user_search_request: The `user_search_request` parameter in the `openai_api_request` function
    represents the search query input by the user. This query is used to make a request to the OpenAI
    API to retrieve relevant information based on the user's input. The function checks if the new user
    query is different from
    context_message: The `context_message` parameter in the `openai_api_request` function is used to
    provide additional context or information to the OpenAI API when making a request. This context
    message helps the API better understand the user's query and provide more accurate responses. It can
    include relevant information or details that can

    Returns:
    The function `openai_api_request` returns the search query obtained from the OpenAI API response.
    If the user search request is different from the last user search request, a new request is made to
    the OpenAI API to get the search query using a fine-tuned model. The function then returns this
    search query. If the user search request is the same as the last user search request, the
    """
    # Get the global variables
    global LAST_USER_SEARCH_REQUEST
    global LAST_SEARCH_QUERY

    # Print the last user query
    print(f"Last user request: {LAST_USER_SEARCH_REQUEST}")
    # Print the user search query
    print(f"User request: {user_search_request}")

    # Check if the user query is the same as the last query, if so, no need to make a new request
    if user_search_request == LAST_USER_SEARCH_REQUEST:
        # If the user query is the same as the last query, no need to make a new request
        print("Not making new request to OpenAI")
        return LAST_SEARCH_QUERY

    else:  # Make a new request to OpenAI's API
        # Set the LAST_USER_SEARCH_REQUEST to the new user request, so next time we can compare
        LAST_USER_SEARCH_REQUEST = user_search_request
        print("Making new request to OpenAI")

        """ Use OpenAI API to get the GitHub search query using the fine-tuned model """

        # Get the OpenAI API key
        api_key = os.getenv("OPENAI_API_KEY")

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        # Make OpenAI API request
        completion = client.chat.completions.create(
            # Set the fine-tuned model name
            model=os.getenv("OPENAI_REPO_MODEL"),
            # Set the messages
            messages=[
                {"role": "system", "content": f"{context_message}"},
                {"role": "user", "content": f"{user_search_request}"},
            ],
        )

        # Set the response as the user query
        search_query = completion.choices[0].message.content
        LAST_SEARCH_QUERY = search_query
        return search_query


def repositories(user_search_request, page):
    """
    The function `repositories` takes a user search request, formats it for GitHub search query using the OpenAI API,
    makes API requests to GitHub, processes the results, and returns search results along with time
    taken and total count.

    Args:
    user_search_request: The `user_search_request` parameter is the user's search query or request for
    repositories on GitHub. This could be a specific topic, language, or any other criteria the user
    wants to search for on GitHub repositories.
    page: The `page` parameter in the `repositories` function is used to specify the page number of
    the search results to retrieve from the GitHub API. It helps in paginating the results when there
    are multiple pages of search results available.

    Returns:
    The `repositories` function returns a tuple containing three elements:
    1. `search_results`: a list of dictionaries containing information about repositories retrieved from
    the GitHub API based on the user's search request and page number.
    2. `time_it_took`: a float value representing the time taken to retrieve the results in seconds,
    rounded to 2 decimal places.
    3. `result_count`: an integer representing
    """

    # Get the current time
    start_time = time.time()

    # Set the context message for the OpenAI API request
    context_message = "You are a helpful assistant that takes user requests and converts them into queries for GitHub search according to the syntax. If the topic is related to AI, Machine Learning, Deep Learning or Data Science and the requested language is Python, add Jupyter Notebook as a language to the query. Respond with just the query and nothing else."

    # Make an OpenAI API request
    # search_query is the request that will be sent to GitHub. It is formatted in a specific syntax to get the best results from GitHub
    search_query = openai_api_request(user_search_request, context_message)

    print(f"The GitHub search query is: {search_query}")

    # Set the search URL for the GitHub API
    search_url = "https://api.github.com/search/repositories"

    # Prepare the parameters for the GitHub API request
    params = {
        "q": search_query,  # Search query
        "per_page": 30,  # Number of results per page
        "page": page,  # Page number
    }

    # Add the personal access token to the headers
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_API_TOKEN')}"}

    # Make the API request and get the response from GitHub API
    response = requests.get(search_url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    # Get the JSON data from the response
    data: dict = response.json()

    # Check if the API limit was reached
    if data.get("incomplete_results", 0) == True:
        search_results = "API limit reached"
    else:

        time_start = time.time()
        # Get the list of repositories from the response
        api_request_results = data.get("items", [])

        # Call the ranking algorithm to rank the results based on relevance
        ranked_results = helpers.repo_results_ranking_algorithm(api_request_results)

        print(f"It took {time.time() - time_start} seconds to rank the results")

        # Create an empty list to store the search results
        search_results = []

        # Get all the relevant data from the JSON and append it to the search_results list
        for repo in ranked_results:  # Iterate over each item in the 'items' list

            search_results.append(
                {
                    "title": repo["full_name"],
                    "owners_page": repo["owner"]["html_url"],
                    "avatar_url": repo["owner"]["avatar_url"],
                    "language": repo["language"],
                    "license": (
                        repo["license"]["name"] if repo.get("license") else None
                    ),  # Check if 'license' exists
                    "license_key": (
                        repo["license"]["key"] if repo.get("license") else None
                    ),
                    "description": (
                        repo["description"] if repo.get("description") else None
                    ),  # Check if 'description' exists
                    "pushed_at": helpers.format_date(repo["pushed_at"]),
                    "repo_url": repo["html_url"],
                    "topics": (
                        repo["topics"]
                        if len(repo["topics"]) < 8
                        else repo["topics"][:8]
                    ),
                    "homepage": repo["homepage"],
                }
            )

    # Calculate how much time it took to get the results
    time_it_took: float = time.time() - start_time

    # Round the time to the 2 decimal places
    time_it_took = round(time_it_took, 2)

    # Get the total number of results
    result_count: int = data.get("total_count", 0)

    return search_results, time_it_took, result_count
