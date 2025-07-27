import os
from PyQt6.QtCore import QByteArray
from .ui import MainWindow
from .loader import CountryLoader
from .logger import logger

class AppController:
    def __init__(self, window: MainWindow, selected_country: str | None = None):
        self.window = window
        self.selected_country = selected_country
        self.country_list = []
        self._connect_signals()
        self._start_background_load()

    def _connect_signals(self):
        self.window.combo_box.currentTextChanged.connect(self._on_country_selected)

    def _on_country_selected(self, country_name: str):
        self.window.label.setText(country_name)
        iso_code = self._get_iso_for_country(country_name)
        svg_path = get_flag_svg_path(iso_code) if iso_code else None

        if svg_path:
            try:
                with open(svg_path, "rb") as f:
                    svg_data = f.read()
                self.window.flag_label.load(QByteArray(svg_data))
                logger.info(f"Displayed flag for {country_name} ({iso_code})")
            except Exception as e:
                logger.error(f"Failed to load flag SVG for {country_name} ({iso_code}): {e}")
                self.window.flag_label.load(QByteArray())
        else:
            logger.warning(f"No flag SVG found for {country_name} ({iso_code})")
            self.window.flag_label.load(QByteArray())

    def _start_background_load(self):
        self.loader = CountryLoader()
        self.loader.countries_loaded.connect(self._on_countries_loaded)
        self.loader.error_occurred.connect(self._on_loading_error)
        self.loader.start()

    def _on_countries_loaded(self, countries: list[tuple[str, str]]):
        self.country_list = countries
        self.window.combo_box.clear()
        country_names = [name for name, _ in countries]
        self.window.combo_box.addItems(country_names)
        self.window.combo_box.setCurrentIndex(-1)
        self.window.label.setText("")
        logger.info(f"Loaded {len(countries)} countries into combo box")

        if self.selected_country:
            index = self.window.combo_box.findText(self.selected_country)
            if index >= 0:
                self.window.combo_box.setCurrentIndex(index)
                self._on_country_selected(self.selected_country)
            else:
                logger.warning(f'Selected country "{self.selected_country}" not found in list')
                self.window.label.setText(f'Country "{self.selected_country}" not found.')

    def _on_loading_error(self, message: str):
        logger.error(f"Failed to load countries: {message}")
        self.window.label.setText(f"Failed to load countries: {message}")
    
    def _get_iso_for_country(self, name: str) -> str | None:
        for n, iso in self.country_list:
            if n == name:
                return iso
        logger.warning(f"ISO code not found for country: {name}")
        return None


def get_flag_svg_path(iso_code: str) -> str | None:
    if not iso_code:
        return None
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "flags", f"{iso_code}.svg")
    exists = os.path.exists(path)
    if not exists:
        logger.warning(f"Flag SVG file does not exist: {path}")
    return path if exists else None