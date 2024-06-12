"""
Ranking algorithm for GitHub repositories

Created by Daniel Dekhtyar
Copyright (c) 2024 Daniel Dekhtyar
Email: denik2707@gmail.com
"""

import aiohttp
import asyncio
import markdown
import re


def repo_results_ranking_algorithm(search_query, search_results, readme_texts):
    """
    The function `repo_results_ranking_algorithm` ranks search results based on various criteria
    including owner reputation, stars, forks, watchers, and keyword matches in readme texts.
    
    Args:
    search_query: The `search_query` parameter is the query string used to search for repositories. It
    could be keywords or phrases that the user is looking for in repositories.
    search_results: Search results is a list of dictionaries where each dictionary represents a
    repository returned from a search query. Each dictionary contains information about a repository
    such as the owner, stargazers count, forks count, watchers count, and other relevant details.
    readme_texts: A list of readme texts corresponding to the search results. This parameter is used
    in the `repo_results_ranking_algorithm` function to analyze the readme content and calculate a score
    for each search result based on the presence of keywords from the search query in the readme texts.
    
    Returns:
    The function `repo_results_ranking_algorithm` returns a sorted list of search results based on a
    ranking algorithm that assigns scores to each search result. The search results are sorted in
    descending order based on the calculated score for each result.
    """
    # Used in `api_requests.py`

    # If the owner of the repo is in the list of reputable users, add 50 points
    for repo in search_results:
        score = 0
        owner = repo["owner"]["login"]
        if is_owner_is_in_list(owner):
            # Add 300 points if the owner is in the list of reputable users
            score += 300

        # Add points based on the amount of stars. Give 40% weight to stars
        stars = repo["stargazers_count"]
        score += stars * 0.4

        # Add points based on the amount of forks. Give 25% weight to forks
        forks = repo["forks_count"]
        score += forks * 0.25

        # Add points based on the amount of watchers. Give 15% weight to watchers
        watchers = repo["watchers_count"]
        score += watchers * 0.15
        
        # Add points based on the presence of words from the search query in the readme. Give 20% weight to readme
        keyword_number = keyword_counter(search_query, readme_texts, repo)
        score += keyword_number * 0.2

        # Set the score in the result["score"] key
        repo["score"] = score

    # Sort the results based on the score
    sorted_results = sorted(
        search_results, key=lambda repo: repo["score"], reverse=True
    )

    return sorted_results


def is_owner_is_in_list(owner_name):
    """
    The function checks if a given owner name is in a list of reputable users stored in a file.

    Args:
    owner_name: The function `is_owner_is_in_list(owner_name)` reads a file named
    "reputable_users_list.txt" and checks if the `owner_name` provided as an argument is present in the
    list. If the `owner_name` is found in the list, it prints a message and returns `

    Returns:
    The function `is_owner_is_in_list(owner_name)` returns a boolean value. It returns `True` if the
    `owner_name` is found in the "reputable_users_list.txt" file, and `False` if the `owner_name` is not
    found in the list.
    """
    with open("backend/reputable_users_list.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            line.strip()

            if line.startswith("//"):
                # Skip the comment lines
                continue
            else:
                # Check if the search string is in the line
                if owner_name in line:
                    # If the repo owner is in the list, return True
                    return True

    # If the repo owner is not in the list, return False
    return False


"""
Make an async function to fetch the README.md file for each repo. It is done asynchronously to speed up the process.
"""

async def fetch_readme(session: aiohttp.ClientSession, repo: tuple) -> tuple:
    """
    The function fetches the README file of a GitHub repository in various formats and converts it to
    plain text if it's in markdown format.
    
    Args:
    session (aiohttp.ClientSession): The `session` parameter in the `fetch_readme` function is an
    instance of `aiohttp.ClientSession`, which is used to make asynchronous HTTP requests. It allows you
    to communicate with web servers and retrieve data from URLs. In this function, the `session` is used
    to make GET
    repo (tuple): ('UserName/RepoName', 'main')
    
    Returns:
    The function `fetch_readme` returns a tuple containing the repo name and the readme text. If the
    README file is successfully fetched and processed, it returns the repo name and the plain text
    content of the README file. If the README file is not found or there is an issue with fetching it,
    it returns the repo name and `None`.
    """
    
    # Get the repo name and default branch from the tuple. eg. "owner/repo_name", "main"
    user_and_repo_name, default_branch = repo
    
    # List of possible README file formats
    readme_formats = ['README.md', 'readme.md', 'README.rst', 'readme.rst', 'README.txt', 'readme.txt']

    # Iterate through the list of possible README file formats and try to fetch the file
    for readme_format in readme_formats:
        # Create the URL for the README file
        readme_url = f"https://raw.githubusercontent.com/{user_and_repo_name}/{default_branch}/{readme_format}"
        
        # Make the request and get the response
        async with session.get(readme_url) as response:
            # Check if the request was successful
            if response.status == 200:
                try:
                    # Read the response as text
                    readme_text = await response.text()
                
                # Exception if the encoding in UTF-8 fails
                except UnicodeDecodeError:
                    try:
                        # Retry with a different encoding if UnicodeDecodeError occurs
                        readme_text = await response.text(encoding='latin1')
                    # If the encoding fails, print an error message and return None
                    except UnicodeDecodeError:
                        print(f"Failed to decode README. Repo: {user_and_repo_name}. Status code: {response.status}")
                        return user_and_repo_name, None

                # If the file is in the markdown format, convert it to plain text
                if readme_format.endswith('.md'):
                    # Convert the markdown to plain text
                    html = markdown.markdown(readme_text)
                    # Remove HTML tags
                    plain_text = re.sub(r'<[^>]+>', '', html)
                    # Set the readme_text to the plain text
                    readme_text = plain_text

                # Return the repo name and the readme text
                return user_and_repo_name, readme_text

    # If the file is not found, return None
    print(f"Failed to fetch README. Repo: {user_and_repo_name}. Status code: {response.status}")
    return user_and_repo_name, None


async def get_readme_texts_async(repos) -> dict:
    """
    This Python function uses aiohttp to asynchronously fetch readme texts for a list of repositories.
    
    Args:
    repos: A list of repository names for which you want to fetch the README texts asynchronously.
    
    Returns:
    The function `get_readme_texts_async` returns a dictionary where the keys are the repository names
    and the values are the readme texts fetched asynchronously for each repository in the input list
    `repos`.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_readme(session, repo) for repo in repos]
        readme_texts = await asyncio.gather(*tasks)
        return dict(readme_texts)

def get_readme_texts(search_results) -> dict:
    """
    The function `get_readme_texts` takes a list of search results, extracts the full name and default
    branch of each repository, and then asynchronously retrieves the readme texts for those
    repositories. It is done asynchronously to speed up the process.
    
    Args:
    search_results: A list of dictionaries containing search results for repositories. Each dictionary
    should have keys "full_name" and "default_branch" to identify the repository and its default branch.
    
    Returns:
    A dictionary containing the readme texts of repositories specified in the search results.
    """
    repos = [[result["full_name"], result["default_branch"]] for result in search_results]
    return asyncio.run(get_readme_texts_async(repos))


def keyword_counter(search_query, readme_texts, repo):
    """
    The function `keyword_counter` takes a search query, a dictionary of readme texts, and a repository,
    and counts the number of times the search query words appear in the readme of the specified
    repository.
    
    Args:
    search_query: The `search_query` parameter is a string containing the words that you want to
    search for in the readme text of a repository. It can consist of one or more words separated by
    spaces.
    readme_texts: The `readme_texts` parameter is a dictionary containing the readmes of different
    repositories. The keys in the dictionary are the full names of the repositories, and the values are
    the content of the respective readmes.
    repo: The `repo` parameter in the `keyword_counter` function is expected to be a dictionary
    representing a repository. It likely contains information about the repository such as its full
    name.
    
    Returns:
    The function `keyword_counter` returns the number of times the search query words appear in the
    readme of a specific repository. If the readme for the repository is not found or fetched
    successfully, it returns 0.
    """
    
    # Get the readme for the respective repo from the dictionary of all the readmes
    readme = readme_texts[repo["full_name"]]
    
    # Count the number of times the search query words appears in the readme
    keyword_count = 0
    
    # If readme was successfully fetched
    if readme:
        # Make sure readme is a string
        if type(readme) == str:
            # Make the readme lowercase
            readme = readme.lower()
            
            # Count the number of times the search query words appears in the readme
            for word in search_query.split():
                # Make the word lowercase
                word = word.lower()
                
                # Check if the word is in the readme
                if word in readme:
                    keyword_count += readme.count(word)
    
    # Return the number of times the search query words appears in the readme. If not readme was fetched, return 0
    return keyword_count
