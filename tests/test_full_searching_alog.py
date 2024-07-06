# test_app.py
"""
Unit test checking if the whole searching algorithm works as expected and returns an HTML results page or an HTML error page
"""

import pytest
from bs4 import BeautifulSoup
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_search(client):
    search_query = "Capture the flag (CTF)"
    page = 1
    # Simulate a GET request with query parameters
    response = client.get(f"/search?q={search_query}&page={page}")

    assert response.status_code == 200  # Ensure the request was successful

    # Parse the response data using BeautifulSoup
    soup = BeautifulSoup(response.data, "html.parser")

    # Check for issues
    if not soup.find():
        print("HTML is invalid or empty")
    else:
        print("HTML parsed successfully")

    # Check that the response is an HTML code
    assert soup.find()
