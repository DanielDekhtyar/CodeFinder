"""
Code to test error handling during the search process
"""

from backend import helpers, api_requests


# user_query is not a string
def test_user_query_not_a_string():
    """
    Testing get_variables_from_web_page_error_handling()
    """

    # Call the function with an invalid user_query (not a string)
    user_query = 123456789
    page = 10
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that the correct error message and code are returned.
    assert result == (
        "You encountered an error and I have no idea how you got here 😱",
        "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
        "break computer.gif",
        422,
    )

    # Call the function with a valid user_query
    user_query = "hello world"
    page = 2
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that None is returned as no errors were found
    assert result == None


def test_page_number_greater_than_34():
    """
    Testing get_variables_from_web_page_error_handling()
    """

    # Call the function with a page number greater than 34
    user_query = "hello world"
    page = 35
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == (
        "No more pages to display 😱",
        "Only 34 pages are allowed due to API limitations! Stop hacking my website! 🔨",
        "break computer.gif",
        422,
    )

    user_query = "hello world"
    page = 38
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == (
        "No more pages to display 😱",
        "Only 34 pages are allowed due to API limitations! Stop hacking my website! 🔨",
        "break computer.gif",
        422,
    )

    # Call the function with a page number between 1 and 34
    user_query = "hello world"
    page = 1
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == None

    user_query = "hello world"
    page = 15
    result = helpers.get_variables_from_web_page_error_handling(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == None


def test_api_response_not_a_tuple_of_three_variables():
    """
    Testing error_handling_after_API_request()
    """

    # Check the function in normal condition. Pass
    # Give a tuple of 3, just like a real response from the repositories() function in api_requests.py
    api_response = "some response text", 1.43, 105483

    result = helpers.error_handling_after_API_request(api_response)

    assert result == None

    # Check if the function returns something that is not a tuple of 3
    # Giving it a string
    api_response = "some random string"

    result = helpers.error_handling_after_API_request(api_response)

    assert result == ("You broke the search engine 💥", "break computer.gif", 422)

    # Check if the function returns something that is not a tuple of 3
    # Giving it a tuple of 4
    api_response = "hello world", 1.22, 12312, "hello world"

    result = helpers.error_handling_after_API_request(api_response)

    assert result == ("You broke the search engine 💥", "break computer.gif", 422)


def test_no_results_found():
    """
    Testing error_handling_after_API_request()
    Check the function for a search request with no results.
    """

    user_query = "sdfsdfsdfsdfsdfsdsdsdfsdf"
    page = 1

    # Make GitHub API request and get the response
    api_response = api_requests.repositories(user_query, page)

    result = helpers.error_handling_after_API_request(api_response)

    assert result == ("No results found 🔍", "i-cant-find-anything.gif", 404)


def test_user_query_is_none():
    """
    Testing get_variables_from_web_page_error_handling()
    Check that an error accrues if the search request is None
    """
    user_query = None

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == (
        "You didn't search for anything! Try to put something in to the search bar! 🔍",
        "If you think there is a bug, please use the Contact Me form and write to me",
        "break computer.gif",
        422,
    )


def test_user_query_is_str_type():
    """
    Testing get_variables_from_web_page_error_handling()
    Check that an error accrues if the search request is not a string
    """

    error_message = (
        "You encountered an error and I have no idea how you got here 😱",
        "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
        "break computer.gif",
        422,
    )

    # Check error handling for Integer variables.
    user_query = 1234567890

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for Float variables.
    user_query = 123.456

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for Dict variables.
    user_query = {"hello": "world", "GitHub": "GitLab", "www": "https"}

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for Boolean variables.
    user_query = True

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for List variables.
    user_query = ["Captain America", "Hulk", "Thor", "Spider-Man", "Storm"]

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for Set variables.
    user_query = {"Captain America", "Hulk", "Thor", "Spider-Man", "Storm"}

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for Tuple variables.
    user_query = ("Captain America", "Hulk", "Thor", "Spider-Man", "Storm")

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == error_message

    # Check error handling for String variables.
    user_query = "Hello World"

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == None


def test_user_query_not_empty():
    """
    Testing get_variables_from_web_page_error_handling()
    Check that an error accrues if the search request is not empty
    """

    # Check an empty string.
    user_query = ""

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == (
        "You didn't search for anything! Try to put something in to the search bar! 🔍",
        "If you think there is a bug, please use the Contact Me form and write to me",
        "break computer.gif",
        422,
    )

    # Check when there are some white spaces.
    user_query = "   "

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == (
        "You didn't search for anything! Try to put something in to the search bar! 🔍",
        "If you think there is a bug, please use the Contact Me form and write to me",
        "break computer.gif",
        422,
    )

    # Check a valid string.
    user_query = "Hello World"

    result = helpers.get_variables_from_web_page_error_handling(user_query, 1)

    assert result == None


def test_page_is_not_int():
    """
    Testing get_variables_from_web_page_error_handling()
    Check that an error accrues if the 'page' is None
    """

    error_message = (
        "You encountered an error and I have no idea how you got here 😱",
        "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
        "break computer.gif",
        422,
    )

    # Check if page is None.
    page = None

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a Float.
    page = 123.456

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a String.
    page = "Hello World"

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a Dictionary.
    page = {"hello": "world", "GitHub": "GitLab", "www": "https"}

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a Boolean.
    page = True

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a List.
    page = ["Captain America", "Hulk", "Thor", "Spider-Man", "Storm"]

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a Set.
    page = {"Captain America", "Hulk", "Thor", "Spider-Man", "Storm"}

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if page is a Tuple.
    page = ("Captain America", "Hulk", "Thor", "Spider-Man", "Storm")

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == error_message

    # Check if the page is in the correct range.
    page = 1

    result = helpers.get_variables_from_web_page_error_handling("Hello World", 1)

    assert result == None


def test_page_is_in_range():
    """
    Testing get_variables_from_web_page_error_handling()
    Check that an error accrues if the 'page' is not in the range 1-34
    """

    non_existing_page_error = (
        "You are looking for a non existing page",
        "If you think there is a bug, please use the Contact Me form and write to me",
        "break computer.gif",
        422,
    )

    no_more_pages_error = (
        "No more pages to display 😱",
        "Only 34 pages are allowed due to API limitations! Stop hacking my website! 🔨",
        "break computer.gif",
        422,
    )

    # Check for page '0'
    page = 0

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == non_existing_page_error

    # Check for page '-1'
    page = -1

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == non_existing_page_error

    # Check for page '35'
    page = 35

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == no_more_pages_error

    # Check for page '100'
    page = 100

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == no_more_pages_error

    # Check for page '3'
    page = 3

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == None

    # Check for page '12'
    page = 12

    result = helpers.get_variables_from_web_page_error_handling("Hello World", page)

    assert result == None
