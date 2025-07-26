from PyQt6.QtCore import QThread, pyqtSignal
from .api import fetch_sorted_country_names


class CountryLoader(QThread):
    countries_loaded = pyqtSignal(list)
    error_occurred = pyqtSignal(str)

    def run(self):
        try:
            countries = fetch_sorted_country_names()
            self.countries_loaded.emit(countries)
        except Exception as e:
            self.error_occurred.emit(str(e))