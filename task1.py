from inverter import invert

def test_that_inverted_string_is_returned_for_an_argument_with_more_than_two_chars():
    inverted_str = invert("cat")
    assert inverted_str == "tac"
    assert True

def test_that_same_string_is_returned_for_an_argument_with_one_char():
    string_with_one_character = invert("a")
    assert string_with_one_character == "a"
    assert True

def test_that_empty_string_is_returned_when_argument_is_an_empty_string():
    empty_str = invert("")
    assert empty_str == ""
    assert True

def test_that_empty_str_is_returned_when_argument_is_null():
    null_arg = invert(None)
    assert null_arg == ""
    assert True

def test_that_empty_str_is_not_returned_when_argument_is_a_string():
    string_argument = invert("string")
    assert string_argument != ""
    assert True

def test_that_non_empty_string_is_not_returned_when_argument_is_None():
    null_argument = invert(None)
    null_argument != "string"
    assert True

def test_that_str_is_not_more_than_two_chars_if_argument_is_one_char():
    one_char_argument = invert("a")
    assert one_char_argument != "ac"
    assert True
