from .api import fetch_sorted_country_names
from .ui import MainWindow


class AppController:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window
        self._load_countries()

    def _load_countries(self):
        try:
            countries = fetch_sorted_country_names()
            self.main_window.combo_box.addItems(countries)
        except Exception:
            self.main_window.label.setText("Failed to load countries.")
