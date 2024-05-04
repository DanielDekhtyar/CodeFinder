"""
Here are just helper functions to be used in other functions in the backend
"""

import requests
import os

from datetime import datetime, timedelta
from dotenv import load_dotenv


def format_date(date_str):
    """
    The `format_date` function takes a date string and returns a formatted representation of the date
    based on the time difference from the current date and other conditions.
    
    Args:
    date_str: It looks like you have provided the code for formatting a date string into a more
    human-readable format. However, you have not provided the actual date string that you want to
    format. If you provide me with the `date_str` parameter, I can help you format it according to the
    logic in the
    
    Returns:
    The `format_date` function takes a date string in the format "%Y-%m-%dT%H:%M:%SZ" and returns a
    formatted string indicating how long ago the date occurred or the specific date in a readable
    format. The specific return value depends on the difference between the given date and the current
    date and time. The function returns different strings based on the time difference, such as "less
    """
    
    # Convert the date string to a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

    # Get today's date and time
    now = datetime.utcnow()

    # Calculate the difference between now and the given date
    delta = now - date

    # Get the current year
    current_year = now.year

    # If the difference is less than a minute
    if delta < timedelta(minutes=1):
        return "less than a minute ago"
    # If the difference is less than an hour
    elif delta < timedelta(hours=1):
        return f"{delta.seconds // 60} minutes ago"
    # If the difference is less than 24 hours
    elif delta < timedelta(days=1):
        return f"{delta.seconds // 3600} hours ago"
    # If the date is today
    elif delta.days == 0:
        return "today"
    # If the date is yesterday
    elif delta.days == 1:
        return "yesterday"
    # If the date is within the past 7 days
    elif 1 < delta.days <= 7:
        return f"{delta.days} days ago"
    # If the year is the current year, emit only the day and month
    elif date.year == current_year:
        return date.strftime("on %B %d")
    # Otherwise, format the date as 'on month day, year'
    else:
        return f'on {date.strftime("%B %d, %Y")}'


def get_rate_limit_info():
    """
    The `get_rate_limit_info` function retrieves rate limit information from the GitHub API using a
    personal access token.
    
    Returns:
    The `get_rate_limit_info` function returns a tuple containing the rate limit, rate used, and rate
    remaining from the GitHub API. If the API request is unsuccessful (status code other than 200), it
    returns an error message with the status code and response text.
    """
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Set your GitHub personal access token
    access_token = os.getenv("GITHUB_API_TOKEN")

    # Set the API endpoint URL
    rate_limit_url = "https://api.github.com/rate_limit"

    # Set the headers for the request
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {access_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Make the API request
    response = requests.get(rate_limit_url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        limit = int(response.json()["rate"]["limit"])
        used = int(response.json()["rate"]["used"])
        remaining = int(response.json()["rate"]["remaining"])

        return limit, used, remaining
    else:
        return f"Error: {response.status_code} - {response.text}", None, None


def repo_results_ranking_algorithm(search_results):
    # Give a score to each result
    
    # If the owner of the repo is in the list of reputable users, add 50 points
    for result in search_results:
        score = 0
        owner = result["owner"]["login"]
        if is_owner_is_in_list(owner):
            score += 500
        
        # Add points based on the amount of stars. Give 1 point for every 100 stars
        stars = result["stargazers_count"]
        score += round(stars / 100)
        
        # Add points based on the amount of forks. Give 1 point for every 80 forks
        forks = result["forks_count"]
        score += round(forks / 80)
        
        # Add points based on the amount of watchers. Give 1 point for every 30 watchers
        watchers = result["watchers_count"]
        score += round(watchers / 30)
        
        # Set the score in the result["score"] key
        result["score"] = score
    
    # Sort the results based on the score
    sorted_results = sorted(search_results, key=lambda repo: repo["score"], reverse=True)
    
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
    with open("backend/reputable_users_list.txt", 'r') as file:
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
