from uppgift44 import split_regno


def test_regno_split():
    assert split_regno("OMZ516") == ("OMZ", "516")
