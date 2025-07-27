from unittest.mock import patch
from country_picker.api import fetch_sorted_countries


@patch("country_picker.api.requests.get")
def test_fetch_sorted_countries(mock_get):
    mock_get.return_value.json.return_value = [
        {"name": "Italy", "alpha2Code": "IT"},
        {"name": "Germany", "alpha2Code": "DE"},
        {"name": "Austria", "alpha2Code": "AT"}
    ]

    result = fetch_sorted_countries()

    assert result == [
        ("Austria", "at"),
        ("Germany", "de"),
        ("Italy", "it"),
    ]
