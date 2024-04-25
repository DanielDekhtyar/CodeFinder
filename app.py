from flask import *
from flask_session import Session

import os

from backend import api_requests, helpers

# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    # Retrieve form data
    user_query = request.args.get('q')
    user_query.strip()
    page = request.args.get('page')
    
    # Before the request is made, get the rate limit information
    rate_limit_info = helpers.get_rate_limit_info()
    
    # Unpack the rate limit information
    limit, used, remaining = rate_limit_info
    
    print(f"Rate limit: {limit}, Used: {used}, Remaining: {remaining}")

    # Error handling
    if limit != 5000:
        return render_template("error.html", query=user_query , error_message="GitHub API limit is not 5000 😰", second_line="Check the rate limit!", gif="break computer.gif", error_code=422)
    elif remaining <= 150: # Set to 150 because it takes time till the info is refreshed, so a margin of error is given
        return render_template("error.html", query=user_query , error_message="GitHub's API limit has been reached 😲", second_line="Try again soon!", gif="break computer.gif", error_code=422)
    
    # Make the API request and get the response
    api_response = api_requests.repositories(user_query, page)
    
    # Error handling
    if len(api_response) != 3:
        return render_template("error.html", query=user_query , error_message="You broke the search engine 💥", gif="break computer.gif", error_code=422)
    
    # Unpack the API response
    search_results, time_it_took, result_count = api_response

    # If there are no results display error message
    if result_count == 0:
        return render_template("error.html", query=user_query , error_message="No results found 🔍", gif="i-cant-find-anything.gif", error_code=404)
    else:
        # Render the search results
        return render_template("repo_results.html", query=user_query, search_results=search_results, time_it_took=time_it_took, result_count=result_count, os=os, used=used)


if __name__ == '__main__':
    app.run()
