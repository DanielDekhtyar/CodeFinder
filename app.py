from flask import *
from flask_session import Session
import webbrowser

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/searchGithub", methods=["GET"])
def searchGithub():
    # Retrieve form data
    user_query = request.args.get('q')
    user_query.strip()
    
    # Construct the GitHub search URL
    search_query = "https://github.com/search?q=" + user_query
    
    # Redirect to the GitHub search URL
    return redirect(search_query)

if __name__ == '__main__':
    app.run()
