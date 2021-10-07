from utils import normalize_json


def test_normalization():
    example_list = [
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "not interesting"
        },
        {
            "name": "isAuthorized",
            "boolVal": "false",
            "lastSeen": "not interesting"
        },
    ]

    expected = {
        "device": "iPhone",
        "isAuthorized": "false"
    }

    assert normalize_json(example_list) == expected
