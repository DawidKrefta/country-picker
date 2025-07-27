import sys
import os
import argparse
from PyQt6.QtWidgets import QApplication
from .ui import MainWindow
from .controller import AppController
from .logger import logger


def parse_args():
    parser = argparse.ArgumentParser(description="Choose a default country")
    parser.add_argument("--select", help="Country to pre-select by default")
    return parser.parse_args()


def main():
    args = parse_args()
    app = QApplication(sys.argv)

    try:
        with open(os.path.join(os.path.dirname(__file__), "style.qss")) as f:
            app.setStyleSheet(f.read())
    except Exception as e:
        logger.warning(f"Could not load stylesheet: {e}")

    window = MainWindow()
    controller = AppController(window, selected_country=args.select)
    window.show()
    sys.exit(app.exec())
