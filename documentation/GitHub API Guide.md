# GitHub API Guide
---

## Retrieve info about a repo
**Here is an example code of how you can get JSON information about a repo:**

```
import requests

# Set your GitHub API endpoint and search query
search_query = "Hello World"
search_url = "https://api.github.com/search/repositories" # Can search for Repositories, Code, Commits, Issues, Users, Topics
params = {
    "q": search_query,
    "per_page": 30, # Number of results per page
    "page": 1 # Page number
}

# Make the API request
response = requests.get(search_url, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    search_results = response.json()

    # Print the total number of results and the first few repository names
    print(f"Total results: {search_results['total_count']}")
    for index, repo in enumerate(search_results['items'][:30]):
        print(f"- {index + 1}. Name: {repo['name']} | Language: {repo['language']} | URL: {repo['html_url']}")
else:
    print(f"Error: {response.status_code} - {response.text}") # Error message
```

- You use the requests library to request from `https://api.github.com/search/PLACEHOLDER` and add the `params` with the `q` (Look and the code snippet above ^).  
  You can look up different types of searches like:
  - Repositories: https://api.github.com/search/repositories?q=YOUR_SEARCH_QUERY
  - Code: https://api.github.com/search/code?q=YOUR_SEARCH_QUERY
  - Commits: https://api.github.com/search/commits?q=YOUR_SEARCH_QUERY
  - Issues: https://api.github.com/search/issues?q=YOUR_SEARCH_QUERY
  - Users: https://api.github.com/search/users?q=YOUR_SEARCH_QUERY
  - Topics: https://api.github.com/search/topics?q=YOUR_SEARCH_QUERY

<br>

**Getting a full printout of the API JSON response:**  
To get the full JSON printed out and understand how to use it you can use the following code.  
It will print the JSON into your terminal.  
Make sure you have `requests` installed. `pip install requests`

```
import requests
import json

search_query = "Hello World"
search_url = "https://api.github.com/search/CHANGE-TO-THE-DESIRED-TYPE-OF-INFORMATION"
""" Copy instead of the placeholder above ^^^: repositories, code, commits, issues, users, topics """

params = {
    "q": search_query,
    "per_page": 1, # Number of results per page
    "page": 1 # Page number
}
response = requests.get(search_url, params=params)

if response.status_code == 200:
    search_results = response.json()
    formatted_json = json.dumps(search_results, indent=4)
    # Print the formatted JSON string
    print(formatted_json)
else:
    print(f"Error: {response.status_code} - {response.text}") # Error message
```
