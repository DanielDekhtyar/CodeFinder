# GitHub Search

## 📝 Changelog:

> ### Last Version : 0.3.0
>
> ### Last Update : 19/04/2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 0.3.0 - 19/04/2024 ([commit 42d6304](https://github.com/DanielDekhtyar/github-search/commit/42d6304))_

---

#### 🚀 Added
- The results page is now interactive and can display information about repositories based on JSON received from GitHub via their API.
- `api_requests.py` has all the functions making the API requests. Now it only has `repositories()`
  
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