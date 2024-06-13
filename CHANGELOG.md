# Code Finder

## 📝 Changelog:

> ### Last Version : 1.3.6
>
> ### Last Update : 13/06/2024
>
> _Date format DD-MM-YYYY_

<br>

### 🗓️ _Version 1.3.6 - 13/06/2024 ([commit a1fb544](https://github.com/DanielDekhtyar/github-search/commit/a1fb544))_

---

#### 🚀 Added
- In `api_requests.py`, `openai_api_request()` was modified to prevent unnecessary API requests to OpenAI API.  
  It was achieved by adding a 2D array that keeps all the user search requests and the respective search queries.  
  If a user search request is repeated, the old search query is used, instead of reporting OpenAI API again.


### 🗓️ _Version 1.3.5 - 12/06/2024 ([commit d23a59a](https://github.com/DanielDekhtyar/github-search/commit/d23a59a))_

---

#### 🚀 Added
- In `results_template.html` a fork icon is added.  
  When clicked, it opens GitHub and allows you to for the repository to your account


### 🗓️ _Version 1.3.0 - 12/06/2024 ([commit ea3c3ef](https://github.com/DanielDekhtyar/github-search/commit/ea3c3ef))_

---

#### 🚀 Added
- In `repo_results.html`, star count added to each repository ⭐


### 🗓️ _Version 1.2.1 - 12/06/2024 ([commit e930f1e](https://github.com/DanielDekhtyar/github-search/commit/e930f1e))_

---

### 🔥 Enhancements
- In `rank_repo.py` the repository scoring algorithm was adjusted to get better results.  
  The main change is the weight that is given to each parameter in the total score.
- In `fetch_readme()` some error handling was added in case the README can't be encoded using UTF-8.
- In `keyword_counter()` error handling was added to check that the README is indeed a `string` and not something else.


### 🗓️ _Version 1.2.0 - 11/06/2024 ([commit e93d2e6](https://github.com/DanielDekhtyar/github-search/commit/e93d2e6))_

---

#### 🚀 Added
- `rank_repo.py` was created. In this file, you can find all the functions used to rank repositories.
- In `rank_repo.py` 3 functions are responsible for asynchronously fetching the README files for GitHub.  
  Those functions are `get_readme_texts()`, `get_readme_texts_async()` and `fetch_readme()`.
- In `rank_repo.py`, `keyword_counter()` takes the search request and the readme of a repository and counts how many times words from the search request appear in the readme file.
- In `rank_repo.py`, `repo_results_ranking_algorithm()` was adjusted to take advantage of the readme analysis functions mentioned above.


### 🗓️ _Version 1.1.6 - 29/05/2024 ([commit 9552c52](https://github.com/DanielDekhtyar/github-search/commit/9552c52))_

---

#### 🚀 Added
- In `results_template.html`, when scrolling down, the header disappears, and when scrolling up, the header appears again.


### 🗓️ _Version 1.1.5 - 25/05/2024 ([commit 8932c4e](https://github.com/DanielDekhtyar/github-search/commit/8932c4e))_

---

#### 🚀 Added
- `About` page was added
- All the pages have a footer allowing the user to navigate to the `About` page, and later to other pages.
- The footer includes a TM symbol.
  

### 🗓️ _Version 1.1.0 - 25/05/2024 ([commit d7ddbcf](https://github.com/DanielDekhtyar/github-search/commit/d7ddbcf))_

---

#### 🚀 Added
- When clicking on the `I'm Feeling Lucky` button, a random search query is chosen for the array and it is searched.
- At `index.html` the `Search` button and the `I'm Feeling Lucky` button are located right below the input box.
- The style of the buttons changed. No background color when hovering. The Border appears only when hovering over the button.
- In `index.js`, `randomSearch()` was implemented to randomly choose a search query.
- `searchQueries[]` is an array containing all the search queries from which a random one is chosen.


### 🗓️ _Version 1.0.1 - 24/05/2024 ([commit e099bb5](https://github.com/DanielDekhtyar/github-search/commit/e099bb5))_

---

### 🔥 Enhancements
- In `results_template.js`, When a search request is made, the page scrolls up and hides all the search result cards to prevent scrolling down. (The loading animation is only at the top part of the page)



### 🗓️ _Version 1.0.0 - 04/05/2024 ([commit bcaba50](https://github.com/DanielDekhtyar/github-search/commit/bcaba50))_

---

#### The main parts of the search engine were implemented successfully

#### 🚀 Added
- In `helpers.py` a basic search results ranking algorithm was implemented to rank the results based on what would probably be the most relevant to the search request.


### 🗓️ _Version 0.9.1.2 - 03/05/2024 ([commit e6bbbd9](https://github.com/DanielDekhtyar/github-search/commit/e6bbbd9))_

---

#### 🚀 Added
- When a new search request is submitted or a new result page is requested, a loading animation appears.

<br>

### 🗓️ On 1.5.2024 the website was published to the World Wide Web under the domain name [codefinder.dev](https://codefinder.dev) 🌐 !

<br>


### 🗓️ _Version 0.9.1.1 - 29/04/2024 ([commit dec0890](https://github.com/DanielDekhtyar/github-search/commit/dec0890))_

---

### 🔥 Enhancements
- SEO optimization of the pages 🔍


### 🗓️ _Version 0.9.1 - 27/04/2024 ([commit 2de524b](https://github.com/DanielDekhtyar/github-search/commit/2de524b))_

---

### 🔥 Enhancements
- CSS was updated to make the website look good on different screen sizes, especially desktops and laptops.
- `repo_results.js`; homepage link truncation was changed from a max of 55 chars to a max of 50 chars.  
  If a homepage link is longer than 55 characters it will be truncated to the first 55 characters and end with '...'.


### 🗓️ _Version 0.9.0 - 27/04/2024 ([commit d8d4d5a](https://github.com/DanielDekhtyar/github-search/commit/d8d4d5a))_

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