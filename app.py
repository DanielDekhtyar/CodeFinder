from flask import *
from flask_session import Session

import os

from backend import api_requests

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
    
    api_response = api_requests.repositories(user_query, page)
    
    # Error handling
    if len(api_response) != 3:
        return render_template("error.html", query=user_query , text="You broke the search engine", gif="break computer.gif", error=422)
    
    # Unpack the API response
    search_results, time_it_took, result_count = api_response

    # If API limit reached display error message
    if search_results == "API limit reached":
        return render_template("error.html", query=user_query , text="You've reached GitHub's API limit :)", gif="break computer.gif", error=422)
    # If there are no results display error message
    elif result_count == 0:
        return render_template("error.html", query=user_query , text="No results found", gif="i-cant-find-anything.gif", error=404)
    else:
        # Render the search results
        return render_template("repo_results.html", query=user_query, search_results=search_results, time_it_took=time_it_took, result_count=result_count, os=os)


if __name__ == '__main__':
    app.run()
