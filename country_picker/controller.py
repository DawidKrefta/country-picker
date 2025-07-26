# country_picker/controller.py

from PyQt6.QtWidgets import QComboBox, QLabel
from .api import fetch_sorted_country_names


def load_countries_into_ui(combo_box: QComboBox, label: QLabel) -> None:
    """
    Loads country names into the provided combo box and handles UI errors.

    Args:
        combo_box (QComboBox): The UI element to populate.
        label (QLabel): The label to show error messages, if any.
    """
    try:
        countries = fetch_sorted_country_names()
        combo_box.addItems(countries)
    except Exception:
        label.setText("Failed to load countries.")
