"""
unit tests to test if all the API calls go as planed
"""

from backend import api_requests, helpers


def test_need_to_make_request_to_openai_api():
    """
    Testing need_to_make_request_to_openai_api() from helpers.py
    """
    
    # Store the last user search requests in memory. eg. "[[Websites with flask][Websites with flask]]"
    # All the 'I feel lucky' requests are stored in this dictionary, because we know what the API response will be
    LAST_USER_SEARCH_REQUESTS: dict = {
        "Find repositories related to web development with React": "web-development AND react",
        "data science using Pandas library": "data-science AND pandas",
        "facial recognition in python": "facial-recognition language:python",
        "Android development with Kotlin": "android-development language:kotlin",
    }
    
    # Set the search request that the user might search for
    search_request = "data science using Pandas library"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == "data-science AND pandas"
    
    
    # Set the search request that the user might search for
    search_request = "Android development with Kotlin"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == "android-development language:kotlin"
    
    
    # Set the search request that the user might search for
    search_request = "hello world"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == "hello world"
    
    
    # Set the search request that the user might search for
    search_request = "123456"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == "123456"
    
    
    # Set the search request that the user might search for
    search_request = "react"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == "react"
    
    
    # Set the search request that the user might search for
    search_request = "machine learning scripts written in python"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == True
    
    
    # Set the search request that the user might search for
    search_request = "ml databases in a json format"
    
    # Make the function call and store the return value as 'result'
    result = helpers.need_to_make_request_to_openai_api(search_request, LAST_USER_SEARCH_REQUESTS)
    
    assert result == True
