"""
Here are just helper functions to be used in other functions in the backend
"""

import requests
import os

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import render_template


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

    try:
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

    except TypeError:
        return None


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


def get_variables_from_web_page_error_handling(user_query: str, page: int):
    # Check if the user query is not empty or None
    if not user_query or user_query == None:
        return (
            "You didn't search for anything! Try to put something in to the search bar! 🔍",
            "If you think there is a bug, please use the Contact Me form and write to me",
            "break computer.gif",
            422,
        )

    # Check if the user query is a string
    elif type(user_query) != str:
        # return a 422 error code
        # Main error message, second line error message, gif, error code
        return (
            "You encountered an error and I have no idea how you got here 😱",
            "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
            "break computer.gif",
            422,
        )

    # Strip all the trailing and preceding white spaces from the search query
    user_query.strip()

    # Check if all the characters in the string are whitespaces
    if user_query.isspace():
        return (
            "You didn't search for anything! Try to put something in to the search bar! 🔍",
            "If you think there is a bug, please use the Contact Me form and write to me",
            "break computer.gif",
            422,
        )

    # Check if the page is not Integer
    if type(page) is not int:
        return (
            "You encountered an error and I have no idea how you got here 😱",
            "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
            "break computer.gif",
            422,
        )

    # Check that the page requested is between 1 and 34
    elif page < 1:
        return (
            "You are looking for a non existing page",
            "If you think there is a bug, please use the Contact Me form and write to me",
            "break computer.gif",
            422,
        )

    # Can have maximum 34 pages. If more pages requested, return an error
    elif int(page) > 34:
        # return a 422 error code
        # Main error message, second line error message, gif, error code
        return (
            "No more pages to display 😱",
            "Only 34 pages are allowed due to API limitations! Stop hacking my website! 🔨",
            "break computer.gif",
            422,
        )

    return None


def GitHub_API_rate_limit_error_handling():
    """
    The function performs error handling before making the GitHub API request, checking for various conditions
    and returning appropriate error messages if necessary.

    Args:
    user_query (str): The `user_query` parameter is expected to be a string representing the user's
    query for the API request. If the `user_query` is not a string, the function will return an error
    message indicating that an error occurred and suggest contacting you via the Contact Me page.
    page (int): The `page` parameter in the `error_handling_before_API_request` function is used to
    specify the page number for the API request. The function includes error handling logic to check if
    the page number exceeds the maximum allowed value of 34. If the page number is greater than 34, it
    returns

    Returns:
    The function `error_handling_before_API_request` returns a tuple containing the main error
    message, second line error message, gif, and error code if a specific error condition is met. If no
    error is found, it returns `None`.
    """

    """
    Here we catch an error when the user request is not a string
    I don't know how this error happens and I don't yet know how to fix it
    """

    # Before the request is made, get the GitHub API rate limit information
    rate_limit_info = get_rate_limit_info()

    # Unpack the rate limit information
    limit, used, remaining = rate_limit_info

    # Print the rate limit information to the console
    print(f"Rate limit: {limit}, Used: {used}, Remaining: {remaining}")

    # If for some reason the limit of GitHub API is not 5000, return an error. aka I will be very sad, mad and confused
    if limit != 5000:
        # return a 422 error code
        # Main error message, second line error message, gif, error code
        return (
            "GitHub API limit is not 5000 😰!!! There is a bug 🐞!",
            "Use the Contact Me form to write to me and I will fix it ASAP!!!",
            "break computer.gif",
            422,
        )

    # If the remaining is less than 150, return an error
    # Set to 150 because it takes time till the info is refreshed, so a margin of error is given
    elif remaining <= 150:
        # return a 422 error code
        # Main error message, second line error message, gif, error code
        return (
            "GitHub's API limit has been reached 😲",
            "Try again soon!",
            "break computer.gif",
            422,
        )
    else:
        # If no error was found, return None
        return None


def error_handling_after_API_request(api_response):
    """
    The function `error_handling_after_API_request` checks the API response for errors and returns
    appropriate messages based on the response.

    Args:
    user_query (str): The function `error_handling_after_API_request` takes two parameters:
    `user_query`, which is a string representing the user's query, and `api_response`, which is a tuple
    containing search results, time it took, and result count from an API request.
    api_response: The `api_response` parameter is expected to be a tuple containing three elements:
    `search_results`, `time_it_took`, and `result_count`. The function
    `error_handling_after_API_request` checks the length of the `api_response` tuple and the number of
    results returned by the API to

    Returns:
    If the length of the `api_response` tuple is not 3, an error message along with an error code is
    returned. If there are no search results (result count is 0), an error message is returned.
    Otherwise, `None` is returned.
    """
    # If the length of the api_response is not 3, return an error
    # The API response is a tuple containing the search_results, time_it_took, and result_count
    if type(api_response) != tuple or len(api_response) != 3:
        return "You broke the search engine 💥", "break computer.gif", 422

    # Get the number of results returned by the API from the api_response tuple
    result_count = api_response[2]

    # If there are no results display error message
    if result_count == 0:
        return "No results found 🔍", "i-cant-find-anything.gif", 404

    else:
        return None


def render_error_page(user_query, error_page_components):
    """
    The function `render_error_page` renders an error page with specified components based on the input
    error page components.

    Args:
    user_query: The `user_query` parameter in the `render_error_page` function represents the query or
    input provided by the user that led to the error page being rendered. This could be any information
    or data that the user entered or requested before encountering the error.
    error_page_components: The `error_page_components` parameter is a list that contains the
    components needed to render an error page. The components include the error message, second line
    error message (optional), gif image for the error page, and the error code. The function
    `render_error_page` unpacks these components from the

    Returns:
    The function `render_error_page` returns a rendered error page template with the provided user
    query, error message, second line error message, gif, and error code.
    """
    # Unpack the error page components
    if len(error_page_components) == 4:
        error_message, second_line_error_message, gif, error_code = (
            error_page_components
        )
    elif len(error_page_components) == 3:
        error_message, gif, error_code = error_page_components
        # If there is no second line error message, set it to None
        second_line_error_message = None
    else:
        error_message = (
            "Can't get the error messages 😱",
            "Screenshot the whole page and write me using the Contact Me page please! Thanks!",
            "break computer.gif",
            422,
        )

    # Render the error page
    return render_template(
        "error.html",
        query=user_query,
        error_message=error_message,
        second_line=second_line_error_message,
        gif=gif,
        error_code=error_code,
    )


def need_to_make_request_to_openai_api(user_search_request, LAST_USER_SEARCH_REQUESTS):
    """
    The function checks if a user search request needs to be made to the OpenAI API based on previous
    requests and keyword matches in a file.
    
    Args:
    user_search_request: The `user_search_request` parameter in the function
    `need_to_make_request_to_openai_api` represents the search query input by the user. The function
    checks if this search query is the same as the last query made by the user. If it is the same, there
    is no need to make
    LAST_USER_SEARCH_REQUESTS: `LAST_USER_SEARCH_REQUESTS` is a dictionary that contains the last user
    search requests made. The keys in this dictionary are the user search requests, and the values are
    the corresponding responses or results of those requests. The function
    `need_to_make_request_to_openai_api` checks if the current user
    
    Returns:
    The function `need_to_make_request_to_openai_api` returns different values based on certain
    conditions:
    """
    # Check if the user query is the same as the last query, if so, no need to make a new request
    if user_search_request in LAST_USER_SEARCH_REQUESTS.keys():
        # If the user query is the same as the last query, no need to make a new request
        return LAST_USER_SEARCH_REQUESTS.get(user_search_request)

    # If the length of the search query is just one word, no need to do a request to OpenAI
    elif len(user_search_request.split()) == 1:
        return user_search_request

    # Make the user request all lowercase. Done for simplicity
    user_search_request = user_search_request.lower()

    try:
        with open("backend/search_keywords.txt", "r") as file:
            content = file.read().split()  # Read file content and split into words

            for word in user_search_request.split():
                if word in content:
                    return True

            return user_search_request  # None of the words found in the file

    except FileNotFoundError:
        print(f"Error: File 'backend/search_keywords.txt' not found.")
        return user_search_request


def add_filters_to_search_query(selected_languages: str, author: str, last_update: str, stars: int) -> str:
    filter_str: str = ""
    
    # Check if there is any language filter
    if selected_languages:
        # Get all the languages in the correct format
        lang_filter: str = filter_languages(selected_languages)
        filter_str += lang_filter
    
    # Check if there is any author filter
    if author:
        filter_str += f" owner:{author}"
    
    # Check if there is any last update filter
    if last_update:
        filter_str += f" pushed:>={last_update}"
    
    # Check if there is any star filter
    if stars:
        filter_str += f" stars:>={stars}"
    
    return filter_str


def filter_languages(selected_languages: str) -> str:
    # Check that the selected languages are str
    if type(selected_languages) is not str:
        print("Error : selected_languages not a str")
        return "Error : selected_languages not a str"
    
    # Split 'selected_languages' in the 'languages' tuple
    languages = selected_languages.split(",")
    
    # Store the result. eg. language:"Python" language:"C++"
    lang_filter: str = ""
    
    # Go over each language and add it to 'lang_filter'
    for lang in languages:
        if type(lang) is not str:
            print(f"Error : lang '{lang}' is not a str")
            return (f"Error : lang '{lang}' is not a str")
        
        # Remove any white-spaces
        lang.strip()
        # Add the language to the string of languages according to the format that GitHub requires
        lang_filter += f' language:"{lang}"'
    
    # Return the result
    return lang_filter


def get_language_filter_options():
    languages = [
        {"name": "JavaScript"},
        {"name": "HTML"},
        {"name": "CSS"},
        {"name": "Python"},
        {"name": "SQL"},
        {"name": "TypeScript"},
        {"name": "Java"},
        {"name": "C#"},
        {"name": "C++"},
        {"name": "C"},
        {"name": "PHP"},
        {"name": "PowerShell"},
        {"name": "Go"},
        {"name": "Rust"},
        {"name": "Kotlin"},
        {"name": "Dart"},
        {"name": "Lua"},
        {"name": "Jupyter Notebook"},
        {"name": "Assembly"},
        {"name": "Ruby"},
        {"name": "Swift"},
        {"name": "R"},
        {"name": "Visual Basic .NET"},
        {"name": "Shell"},
        {"name": "Bash"},
        {"name": "MATLAB"},
        {"name": "Groovy"},
        {"name": "Scala"},
        {"name": "Perl"},
        {"name": "GDScript"},
        {"name": "Objective-C"},
        {"name": "Elixir"},
        {"name": "Haskell"},
        {"name": "Common Lisp"},
        {"name": "Clojure"},
        {"name": "Julia"},
        {"name": "Zig"},
        {"name": "Fortran"},
        {"name": "Solidity"},
        {"name": "Ada"},
        {"name": "Erlang"},
        {"name": "F#"},
        {"name": "Apex"},
        {"name": "Prolog"},
        {"name": "OCaml"},
        {"name": "COBOL"},
        {"name": "Crystal"},
        {"name": "Nim"},
        {"name": "SAS"},
        {"name": "Pascal"},
        {"name": "D"},
        {"name": "CoffeeScript"},
        {"name": "UnrealScript"},
        {"name": "WebAssembly"},
        {"name": "TSQL"},
        {"name": "PLSQL"},
        {"name": "Scheme"},
        {"name": "ABAP"},
        {"name": "APL"},
        {"name": "Haxe"},
        {"name": "Racket"},
        {"name": "Astro"},
        {"name": "Forth"},
        {"name": "Raku"},
        {"name": "VHDL"},
        {"name": "Verilog"},
        {"name": "Smarty"},
        {"name": "Gherkin"},
        {"name": "Jinja"},
        {"name": "DM"},
        {"name": "Nunjucks"},
        {"name": "Puppet"},
        {"name": "HCL"},
        {"name": "Mustache"},
        {"name": "Pug"},
        {"name": "JSON"},
        {"name": "XML"},
        {"name": "YAML"},
        {"name": "Markdown"},
        {"name": "Dockerfile"},
    ]
    
    # Return the list of the languages to later be used to generate the filter options
    return languages
