from PyQt6.QtWidgets import (
    QWidget, QLabel, QComboBox, QVBoxLayout, QMainWindow
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Country Picker")
        self._init_ui()

    def _init_ui(self):
        self.combo_box = QComboBox()
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)