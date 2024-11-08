"""
Code that preforms the API requests to GitHub and returns the relevant data
"""

import requests
import time
import os

from backend import helpers, rank_repo
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from .env file
load_dotenv()

# Store the last user search requests in memory. eg. "[[Websites with flask][Websites with flask]]"
# All the 'I feel lucky' requests are stored in this dictionary, because we know what the API response will be
LAST_USER_SEARCH_REQUESTS: dict = {
    "speech recognition using DeepSpeech": "speech-recognition AND deepspeech",
    "data analysis with Pandas in Jupyter Notebook": "data-analysis AND pandas language:python language:Jupyter-Notebook",
    "Find repositories related to chatbot development with Rasa": "chatbot-development AND rasa",
    "serverless computing AWS Lambda": "serverless AND aws-lambda",
    "data visualization with D3.js": "data-visualization AND d3",
    "snake game using pygame": "snake-game AND pygame",
    "web application using the Flask framework": "web-application AND flask",
    "Capture the flag (CTF)": "capture-the-flag OR ctf",
    "all the repos by microsoft": "user:microsoft",
    "IoT using Arduino": "iot AND arduino",
    "cryptography with the apache license": "cryptography license:apache-2.0",
    "clones of the super mario game": "super-mario",
    "microservices architecture with Spring Boot": "microservices AND spring-boot",
    "virtual reality development with Unity3D": "virtual-reality AND unity3d",
    "QA tools": "qa-tools",
    "calculator app with tkinter": "calculator AND tkinter",
    "Find repositories related to web development with React": "web-development AND react",
    "data science using Pandas library": "data-science AND pandas",
    "facial recognition in python": "facial-recognition language:python",
    "Android development with Kotlin": "android-development language:kotlin",
}


def openai_api_request(user_search_request):
    """
    The `openai_api_request` function processes user search requests, checks if an API request is
    needed, and makes a request to OpenAI's API to get search queries using a fine-tuned model.

    Args:
    user_search_request: The `user_search_request` parameter in the `openai_api_request` function
    represents the search query inputted by the user. This query is used to determine if an API request
    to OpenAI is needed to retrieve relevant information based on the user's input.
    context_message: The `context_message` parameter in the `openai_api_request` function is used to
    provide additional context or information to the OpenAI API when making a request. This context
    message helps the API better understand the user's search request and generate a more accurate
    response. It can include relevant details or previous

    Returns:
    The function `openai_api_request` returns the search query obtained from the OpenAI API after
    processing the user's search request. If a new request to the OpenAI API is not needed, it returns
    the existing search query directly without making a new API request.
    """

    global LAST_USER_SEARCH_REQUESTS

    # Print the user search query
    print(f"User request: {user_search_request}")

    # Check if an API request is needed. Returns 'str' if not needed, and 'bool' if needed.
    need_api_request_check = helpers.need_to_make_request_to_openai_api(
        user_search_request, LAST_USER_SEARCH_REQUESTS
    )

    # If a string, return the string as it is and don't make the API request
    if isinstance(need_api_request_check, str):
        print("Not making new request to OpenAI")
        return need_api_request_check
    # If a bool, make the OpenAI API request
    elif isinstance(need_api_request_check, bool):
        pass

    # Make a new request to OpenAI's API
    print("Making new request to OpenAI")

    """ Use OpenAI API to get the GitHub search query using the fine-tuned model """

    # Check how long it takes for OpenAI API request
    openAI_time = time.time()

    # Get the OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Set the context message for the OpenAI API request
    context_message = "You are a helpful assistant that takes user requests and converts them into queries for GitHub search according to the syntax. If the topic is related to AI, Machine Learning, Deep Learning or Data Science and the requested language is Python, add Jupyter Notebook as a language to the query. Respond with just the query and nothing else."

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
    search_query: str = completion.choices[0].message.content

    print(f"OpenAI API request time: {time.time() - openAI_time}")

    # Set the LAST_USER_SEARCH_REQUEST to the new user request, so next time we can compare
    LAST_USER_SEARCH_REQUESTS[user_search_request] = (
        search_query  # Add the new user request
    )
    return search_query


def repositories(user_search_request, page, filters):
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

    # Make an OpenAI API request
    # search_query is the request that will be sent to GitHub. It is formatted in a specific syntax to get the best results from GitHub
    search_query = openai_api_request(user_search_request)

    # Check how long it takes for GitHub API request
    github_time = time.time()

    # Unpack the filters from the tuple 'filters'
    selected_languages, author, last_update, stars = filters

    # Get the string with all the filters formatted as required
    filter_string = helpers.add_filters_to_search_query(
        selected_languages, author, last_update, stars
    )

    # Only add the filters if there is any filters to start with
    if filter_string:
        # Add the search filters to the search request before it is submitted to GitHub API
        search_query += filter_string

    print(f"The GitHub search query is: {search_query}")

    # Set the search URL for the GitHub API
    search_url = "https://api.github.com/search/repositories"

    # Prepare the parameters for the GitHub API request
    params = {
        "q": search_query,  # Search query
        "per_page": 100,  # Number of results per page
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
        # Get the list of repositories from the response
        api_request_results = data.get("items", [])

        print(f"GitHub API request time: {time.time() - github_time}")

        rank_algorithm_time = time.time()

        # Get the README texts for each repository
        readme_texts = rank_repo.get_readme_texts(api_request_results)

        print(
            f"It took {time.time() - rank_algorithm_time} seconds to get the README texts"
        )

        time_to_rank_after_readme = time.time()

        # Call the ranking algorithm to rank the results based on relevance
        ranked_results = rank_repo.repo_results_ranking_algorithm(
            user_search_request, api_request_results, readme_texts
        )

        print(f"Ranking algorithm time: {time.time() - rank_algorithm_time}")
        print(f"Time to rank after README: {time.time() - time_to_rank_after_readme}")

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
                    "stars": repo["stargazers_count"],
                }
            )

    # Calculate how much time it took to get the results
    time_it_took: float = time.time() - start_time

    # Round the time to the 2 decimal places
    time_it_took = round(time_it_took, 2)

    # Get the total number of results
    result_count: int = data.get("total_count", 0)

    return search_results, time_it_took, result_count
