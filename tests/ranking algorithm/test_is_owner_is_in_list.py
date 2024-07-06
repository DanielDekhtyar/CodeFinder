"""
Test the functionality of is_owner_is_in_list()
"""

import sys

print(f"path : {sys.path}")
import os
from backend.rank_repo import is_owner_is_in_list


def test_reputable_list_txt_file_opens():
    # Open reputable_users_list.txt file
    file_path = os.path.join("..", "..", "backend", "reputable_users_list.txt")
    file = open(file_path, "r")

    if file:
        assert True
    else:
        assert False

    file.close()


def test_find_users_in_the_list():
    # Check that Microsoft is found in the list
    microsoft_result = is_owner_is_in_list("microsoft")
    assert microsoft_result

    # Check that the NSA is found in the list
    nsa_result = is_owner_is_in_list("NationalSecurityAgency")
    assert nsa_result

    # Check that jQuery is found in the list
    jquery = is_owner_is_in_list("jquery")
    assert jquery

    # Check that Mamma Mia is not in the list
    mamma_mia_result = is_owner_is_in_list("mamma-mia")
    assert mamma_mia_result == False

    # Check that Sam Altman is not in the list. He does not have a GitHub account :( [or at least I didn't found it]
    sam_result = is_owner_is_in_list("sama")
    assert sam_result == False

    # Check that Tony Stark is not in the list
    iron_man_result = is_owner_is_in_list("iron-man")
    assert iron_man_result == False
