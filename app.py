from flask import *
from flask_session import Session

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

    # Construct the GitHub search URL
    search_query = "https://github.com/search?q=" + user_query
    
    search_results = [
        {'title': 'Result 1', 'snippet': 'Description of result 1', 'url': 'https://example.com/result1'},
        {'title': 'Result 2', 'snippet': 'Description of result 2', 'url': 'https://example.com/result2'},
        {'title': 'Result 3', 'snippet': 'Description of result 3', 'url': 'https://example.com/result3'},
        {'title': 'Result 4', 'snippet': 'Description of result 4', 'url': 'https://example.com/result4'},
        {'title': 'Result 5', 'snippet': 'Description of result 5', 'url': 'https://example.com/result5'},
        {'title': 'Result 6', 'snippet': 'Description of result 6', 'url': 'https://example.com/result6'},
        {'title': 'Result 7', 'snippet': 'Description of result 7', 'url': 'https://example.com/result7'},
        {'title': 'Result 8', 'snippet': 'Description of result 8', 'url': 'https://example.com/result8'},
        {'title': 'Result 9', 'snippet': 'Description of result 9', 'url': 'https://example.com/result9'},
        {'title': 'Result 10', 'snippet': 'Description of result 10', 'url': 'https://example.com/result10'},
        # Add more search results as needed
    ]

    # Redirect to the GitHub search URL
    return render_template("results_template.html", query=user_query, search_results=search_results)


if __name__ == '__main__':
    app.run()
