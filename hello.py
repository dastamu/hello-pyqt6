import sys
# pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class OknoAplikacji(QWidget):

    def __init__(self):
        super().__init__()
        self.inicjalizuj_ui()

    def inicjalizuj_ui(self):
        # Ustawienia okna
        self.setWindowTitle("PyQt6 Hello World")
        self.resize(350, 200)

        # Układ pionowy (układa elementy jeden pod drugim)
        uklad = QVBoxLayout()

        # Tworzenie etykiety
        self.etykieta = QLabel("Hello, World of PyQt6", self)
        # Ustawienie stylu za pomocą StyleSheet
        self.etykieta.setStyleSheet("""
            font-size: 20pt;
            border: 1px solid gray;
            border-radius: 5px; /* zaokrąglenie rogów */
            padding: 3px;      /* odstęp tekstu od ramki */
        """)
        # Wyśrodkowanie tekstu w pionie i poziomie
        self.etykieta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Tworzenie przycisku
        self.przycisk = QPushButton("Click Me", self)

        # Połączenie kliknięcia przycisku z funkcją (slotem)
        self.przycisk.clicked.connect(self.akcja_przycisku)

        # Dodanie elementów do układu
        uklad.addWidget(self.etykieta)
        uklad.addWidget(self.przycisk)

        # Ustawienie układu w oknie
        self.setLayout(uklad)

    def akcja_przycisku(self):
        # Funkcja wykonywana po kliknięciu
        self.etykieta.setText("Hello, World of PyQt6.\nClicked!")


# Uruchomienie aplikacji
if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = OknoAplikacji()
    okno.show()
    sys.exit(app.exec())
