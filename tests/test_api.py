from unittest.mock import patch
from country_picker.api import fetch_sorted_country_names


@patch("country_picker.api.requests.get")
def test_fetch_sorted_country_names(mock_get):
    mock_get.return_value.json.return_value = [
        {"name": "Italy"}, {"name": "Germany"}, {"name": "Austria"}
    ]

    result = fetch_sorted_country_names()
    assert result == ["Austria", "Germany", "Italy"]
