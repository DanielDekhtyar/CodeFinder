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
    The `search` function retrieves user input, performs error handling before and after
    making a GitHub API request, and then, if no errors occurred, renders search results on a webpage.

    Returns:
    The `search()` function returns the search results rendered in the "repo_results.html" template
    along with some additional information such as the user query, search results, time it took to
    retrieve the results, and the result count.
    """

    # Retrieve data from the search form on the website
    user_query = request.args.get("q")
    page = request.args.get("page")

    # If page is None, set it to '1'
    # Usually happens if we are on the first '1' page of the results page
    if page == None:
        page = 1
    else:
        page = int(page)

    # Error handling checking that there is no errors in the data received from the webpage
    get_variables_from_web_page_error_handling_results = (
        helpers.get_variables_from_web_page_error_handling(user_query, page)
    )
    if get_variables_from_web_page_error_handling_results is not None:
        return helpers.render_error_page(
            user_query, get_variables_from_web_page_error_handling_results
        )

    # Strip all the trailing and preceding white spaces from the search query
    user_query.strip()

    GitHub_API_rate_limit_error_handling_results = (
        helpers.GitHub_API_rate_limit_error_handling()
    )
    if GitHub_API_rate_limit_error_handling_results is not None:
        return helpers.render_error_page(
            user_query, GitHub_API_rate_limit_error_handling_results
        )

    # Make GitHub API request and get the response
    api_response = api_requests.repositories(user_query, page)

    """
    Error handling after making GitHub API request
    Checking:
    - A tuple with 3 elements is returned: search_results, time_it_took, result_count
    - The number of results returned by the API is not 0
    If the tests fail, an error page is displayed. See error.html
    """
    after_api_request_error_handling_results = helpers.error_handling_after_API_request(
        api_response
    )
    if after_api_request_error_handling_results is not None:
        # Render the error page
        return helpers.render_error_page(
            user_query, after_api_request_error_handling_results
        )

    # Unpack the API response tuple in to variables
    search_results, time_it_took, result_count = api_response

    # Print the time it took to make the API request to the console
    print(f"Time it took: {time_it_took}")

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


# Serve the sitemap.xml file
@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    return send_from_directory("backend", "sitemap.xml")


if __name__ == "__main__":
    app.run()
