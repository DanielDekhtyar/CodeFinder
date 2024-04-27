# GitHub Search

## 📝 Changelog:

> ### Last Version : 0.4.1
>
> ### Last Update : 27/04/2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 0.4.1 - 27/04/2024 ([commit 2de524b](https://github.com/DanielDekhtyar/github-search/commit/2de524b))_

---

### 🔥 Enhancements
- CSS was updated to make the website look good on different screen sizes, especially desktops and laptops.
- `repo_results.js`; homepage link truncation was changed from a max of 55 chars to a max of 50 chars.  
  If a homepage link is longer than 55 characters it will be truncated to the first 55 characters and end with '...'.


### 🗓️ _Version 0.4.0 - 27/04/2024 ([commit d8d4d5a](https://github.com/DanielDekhtyar/github-search/commit/d8d4d5a))_

---

#### 🚀 Added
- In `api_requests.py`, `openai_api_request()` was implemented to use OpenAI's API to access the fine-tuned model to get the GitHub search queries based on the user's search request.
- In `api_requests.py`, `repositories()` was changed to take advantage of `openai_api_request()` to get accurate GitHub search queries based on the user's search request.
- In `app.py` an error message is added when a user is trying to get to page 35 and above.  
  A maximum of 34 pages are available due to GitHub's API limitations.
- If the user attempts to submit an empty search request, no search request will be sent and the search bar borders will become red.
- If a description is longer than 50 words, it will be truncated to the first 50 words and end with '...'. (Code in `repo_results.js`)  
  If a homepage link is longer than 55 characters it will be truncated to the first 55 characters and end with '...'. (Code in `repo_results.js`)

### 🔥 Enhancements
- Small style changes were done on `index.html` and `results_template.html`.
- Information about API keys and tokens moved from `config.py` to `.env`. Changes may be seen wherever `config.py` was used.
- In `index.html` and `results_template.html` the style of the search bar was slightly changed.



### 🗓️ _Version 0.3.7 - 26/04/2024 ([commit 2233d08](https://github.com/DanielDekhtyar/github-search/commit/2233d08))_

---

#### 🚀 Added
- `api_requests.py` uses a GitHub API token instead of just making an API request as an unauthenticated user. Now the API limit is up from 60 to 5000 API calls per hour.  
The token is stored in `config.py` which is not committed to the repository.
- `get_rate_limit_info()` is in `helpers.py`. The function checks the current API limit and how many API requests are left.
- In `app.py`, before doing the API request, the API limit is checked. If the API limit was reached then no request will be made and an error message will appear.
- The number of API requests that were done in the last hour is printed into the console. Check it in the dev tool in the browser.
- In `error.html` a `second_line` may be provided. It will be displayed between the `error_message` and `error_code`.

### 🔥 Enhancements
- In `index.html` the title is now an image (`title image.png`) instead of a text and an icon image.
- Some style changes in the results card. Particularly the borer, topics and title
- If a repo has a `homepage` link provided, it will appear but the language and the license.
- The pagination (page selection) part of `results_template.html` was completely redesigned.


### 🗓️ _Version 0.3.6.1 - 24/04/2024 ([commit 9acae80](https://github.com/DanielDekhtyar/github-search/commit/9acae80))_

---

### 🔥 Enhancements
- bugfix: Previously, if the topics don't fit into the line, they wrap around.
- bugfix: Previously, if there were topics but no description, the topics would be in line with the title. Now they are right below the title.



### 🗓️ _Version 0.3.6 - 22/04/2024 ([commit 46ce1c3](https://github.com/DanielDekhtyar/github-search/commit/46ce1c3))_

---

### 🔥 Enhancements
- `results_template.html` was divided into multiple templates (`error.html`, `repo_results.html`) and now all the search result pages inherit from `results_template.html` as the parent template.
- When the input box is not in focus, the placeholder text changes to `Type [/] to search`.
- If the user types `/` at any point on the screen, the pointer will move to the search screen and the user can type.
- In `index.html` the search bar will be automatically in focus.
- In `app.py` error handling was added to work when there were no results, the query was broken or the API limit was reached.
- In `api_requests.py` error handling was added in case the GitHub API limit was reached.


#### 🐞 To-Do
- When searching for language: C++ or language: C#, the ++ or # part of the query disappears when you change to a different page.
- If a repo does not have a description, the topics will be in line with the title.


### 🗓️ _Version 0.3.5 - 20/04/2024 ([commit 71dadb0](https://github.com/DanielDekhtyar/github-search/commit/71dadb0))_

---

#### 🚀 Added
- On the results page, I've added pagination functionality to allow to display of information on multiple pages.


### 🗓️ _Version 0.3.0 - 19/04/2024 ([commit 42d6304](https://github.com/DanielDekhtyar/github-search/commit/42d6304))_

---

#### 🚀 Added
- The results page is now interactive and can display information about repositories based on JSON received from GitHub via their API.
- `api_requests.py` has all the functions making the API requests. Now it only has `repositories()`.
  
### 🔥 Enhancements
- In the `index.html` page, when clicking on the link in the disclaimer, the link opens in a new tab.


### 🗓️ _Version 0.2.0 - 17/04/2024 ([commit 33fff86](https://github.com/DanielDekhtyar/github-search/commit/33fff86))_

---

#### 🚀 Added
- `results_template.html` created and the page is functioning as expected.
- In `app.py`, `/search` is implemented to give the search results to `results_template.html`.


### 🔥 Enhancements
- In `index.html` the `<footer>` is outside the `<body>`.
- In `app.py`, `/searchGithub` was renamed to `/search`.
- `github-search.png` renamed to `icon.png`.


### 🗓️ _Version 0.1.0 - 16/04/2024 ([commit 5e4e3f2](https://github.com/DanielDekhtyar/github-search/commit/5e4e3f2))_

---

#### 🚀 Added
- Created the front end in `index.html`.
- Added search bar functionality using `Flask`.
- When submitting a search query using the search box, it redirects the user to GitHub search and finds the relevant data.

#### 🐞 To-Do
- Allows to submit empty queries.