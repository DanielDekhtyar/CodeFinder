# GitHub Search

## 📝 Changelog:

> ### Last Version : 0.3.6.1
>
> ### Last Update : 24/04/2024
>
> _Date format DD-MM-YYYY_


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
- When searching for language:C++ or language:C#, the ++ or # part of the query disappears when you change to a different page.
- If a repo does not have a description, the topics will be inline with the title.


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