"""
Here are just helper functions to be used in other functions in the backend
"""

import json
import requests

from datetime import datetime, timedelta
from backend import config


def format_date(date_str):
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
    # Set your GitHub personal access token
    access_token = config.get_github_token()

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
        return f"Error: {response.status_code} - {response.text}"
