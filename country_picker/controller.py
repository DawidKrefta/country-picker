from .api import fetch_sorted_country_names
from .ui import MainWindow


class AppController:
    def __init__(self, window: MainWindow):
        self.window = window
        self._connect_signals()
        self._load_countries()

    def _connect_signals(self):
        self.window.combo_box.currentTextChanged.connect(
            self._on_country_selected
        )

    def _on_country_selected(self, country_name: str):
        self.window.label.setText(f"{country_name}")

    def _load_countries(self):
        try:
            countries = fetch_sorted_country_names()
            self.window.combo_box.addItems(countries)
            self.window.combo_box.setCurrentIndex(-1)
            self.window.label.setText("")
        except Exception:
            self.window.label.setText("Failed to load countries.")
