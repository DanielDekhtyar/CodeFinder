from flask import *

import os
import datetime

from backend import api_requests, helpers

# Configure application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    """
    The `search` function in Python retrieves form data, checks API rate limits, makes an API request,
    handles errors, and renders search results or error messages based on the response.

    Returns:
    The `search()` function returns either an error template or the search results template based on
    various conditions and API responses. If certain conditions are met, it will render an error
    template with specific error messages. If the API response is successful and there are valid
    search results, it will render the search results template with the search results, time it took for
    the search, result count, and other relevant information
    """

    # Retrieve form data
    user_query = request.args.get("q")
    user_query.strip()
    page = request.args.get("page")
    
    # Can have maximum 34 pages. If more pages requested, return an error
    if page is not None:
        if int(page) > 34:
            return render_template(
                "error.html",
                query=user_query,
                error_message="No more pages to display 😱",
                second_line="Only 34 pages are allowed due to API limitations!",
                gif="break computer.gif",
                error_code=422,
            )

    # Before the request is made, get the rate limit information
    rate_limit_info = helpers.get_rate_limit_info()

    # Unpack the rate limit information
    limit, used, remaining = rate_limit_info

    print(f"Rate limit: {limit}, Used: {used}, Remaining: {remaining}")

    # Error handling
    if limit != 5000:
        return render_template(
            "error.html",
            query=user_query,
            error_message="GitHub API limit is not 5000 😰",
            second_line="Check the rate limit!",
            gif="break computer.gif",
            error_code=422,
        )
    elif (
        remaining <= 150
    ):  # Set to 150 because it takes time till the info is refreshed, so a margin of error is given
        return render_template(
            "error.html",
            query=user_query,
            error_message="GitHub's API limit has been reached 😲",
            second_line="Try again soon!",
            gif="break computer.gif",
            error_code=422,
        )

    # Make the API request and get the response
    api_response = api_requests.repositories(user_query, page)

    # Error handling
    if len(api_response) != 3:
        return render_template(
            "error.html",
            query=user_query,
            error_message="You broke the search engine 💥",
            gif="break computer.gif",
            error_code=422,
        )

    # Unpack the API response
    search_results, time_it_took, result_count = api_response

    # If there are no results display error message
    if result_count == 0:
        return render_template(
            "error.html",
            query=user_query,
            error_message="No results found 🔍",
            gif="i-cant-find-anything.gif",
            error_code=404,
        )
    else:
        # Render the search results
        return render_template(
            "repo_results.html",
            query=user_query,
            search_results=search_results,
            time_it_took=time_it_took,
            result_count=result_count,
            os=os,
        )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact-me")
def contact_me():
    return render_template("contact_me.html")

if __name__ == "__main__":
    app.run()
