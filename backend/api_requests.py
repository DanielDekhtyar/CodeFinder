"""
Code that preforms the API requests to GitHub and returns the relevant data
"""


import requests
import json
import time

from backend import helpers

def repositories(user_query, page):
    start_time = time.time() # Get the current time
    
    search_url = "https://api.github.com/search/repositories"
    params = {
        "q": user_query, # Search query
        "per_page": 30, # Number of results per page
        "page": page # Page number
    }

    response = requests.get(search_url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    # Get the JSON data from the response
    data:dict = response.json()
    
    # Check if the API limit was reached
    if data.get('incomplete_results', 0) == True:
        search_results = "API limit reached"
    else:
        # Create an empty list to store the search results
        search_results = []

        # Get all the relevant data from the JSON and append it to the search_results list
        for repo in data.get('items', []):  # Iterate over each item in the 'items' list

            search_results.append({
                'title': repo['full_name'],
                'owners_page': repo['owner']['html_url'],
                'avatar_url': repo['owner']['avatar_url'],
                'language': repo['language'],
                'license': repo['license']['name'] if repo.get('license') else None,  # Check if 'license' exists
                'license_key': repo['license']['key'] if repo.get('license') else None,
                'description': repo['description'] if repo.get('description') else None,  # Check if 'description' exists
                'pushed_at': helpers.format_date(repo['pushed_at']),
                'repo_url': repo['html_url'],
                'topics' : repo['topics'] if len(repo['topics']) < 5 else repo['topics'][:5]
            })
        
    # Calculate how much time it took to get the results
    time_it_took:float = time.time() - start_time
    
    # Round the time to the 2 decimal places
    time_it_took = round(time_it_took, 2)
    
    # Get the total number of results
    result_count:int = data.get('total_count', 0)

    return search_results, time_it_took, result_count
