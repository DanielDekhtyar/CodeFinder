import requests
from backend import helpers, api_requests


# user_query is not a string
def test_user_query_not_a_string():
    """
    Testing error_handling_before_API_request()
    """
    
    # Call the function with an invalid user_query (not a string)
    user_query = 123456789
    page = 10
    result = helpers.error_handling_before_API_request(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == (
        "You encountered an error and I have no idea how you got here 😱",
        "Could you please contact me via the Contact Me page to help me fix it? Thanks!",
        "break computer.gif",
        422
    )
    
    # Call the function with a valid user_query
    user_query = "hello world"
    page = 2
    result = helpers.error_handling_before_API_request(user_query, page)

    # Assert that None is returned as no errors were found
    assert result == None


def test_page_number_greater_than_34():
    """
    Testing error_handling_before_API_request()
    """
    
    # Call the function with a page number greater than 34
    user_query = "hello world"
    page = 35
    result = helpers.error_handling_before_API_request(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == (
        "No more pages to display 😱",
        "Only 34 pages are allowed due to API limitations! Stop hacking my website!",
        "break computer.gif",
        422
    )
    
    user_query = "hello world"
    page = 38
    result = helpers.error_handling_before_API_request(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == (
        "No more pages to display 😱",
        "Only 34 pages are allowed due to API limitations! Stop hacking my website!",
        "break computer.gif",
        422
    )

    # Call the function with a page number between 1 and 34
    user_query = "hello world"
    page = 1
    result = helpers.error_handling_before_API_request(user_query, page)

    # Assert that the correct error message and code are returned
    assert result == None
    
    user_query = "hello world"
    page = 15
    result = helpers.error_handling_before_API_request(user_query, page)

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
    # Check the function for a search request with no results. Fail
    user_query = "sdfsdfsdfsdfsdfsdsdsdfsdf"
    page = 1
    
    # Make GitHub API request and get the response
    api_response = api_requests.repositories(user_query, page)
    
    result = helpers.error_handling_after_API_request(api_response)