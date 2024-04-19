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
    
    search_results, time_it_took, result_count = api_requests.repositories(user_query, page)

    # Redirect to the GitHub search URL
    return render_template("results_template.html", query=user_query, search_results=search_results, time_it_took=time_it_took, result_count=result_count, os=os)


if __name__ == '__main__':
    app.run()
