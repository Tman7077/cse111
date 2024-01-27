from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest
global first_name, last_name, full_name
first_name = "Sally"
last_name = "Brown"
def test_make_full_name():
     assert make_full_name(first_name, last_name) == f"{last_name}; {first_name}"
     global full_name
     full_name = make_full_name(first_name, last_name)

def test_extract_family_name():
     assert extract_family_name(full_name) == last_name

def test_extract_given_name():
     assert extract_given_name(full_name) == first_name

pytest.main(["-v", "--tb=line", "-rN", __file__])