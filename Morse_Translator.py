import sys

from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout,
)

def translating(text):
    code_morse = ""
    for char in text:
        if char.upper() in Morse:
            code_morse += Morse[char.upper()] + " "
        else:
            code_morse += char + " "
    return code_morse

# Словарь с азбукой Морзе
Morse = {"А":"*-","Б":"-***","В":"*--","Г":"--*","Д":"-**",
"Е":"*","Ж":"***-","З":"--**","И":"**",
"Й":"*---","К":"-*-","Л":"*-**","М":"--","Н":"-*",
"О":"---","П":"*--*","Р":"*-*","С":"***","Т":"-",
"У":"**-","Ф":"**-*","Х":"****","Ц":"-*-*","Ч":"---*",
"Ш":"----","Щ":"--*-","Ъ":"*--*-*","Ы":"-*--","Ь":"-**-",
"Э":"**-**","Ю":"**--","Я":"*-*-"}

class MorseTranslator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Переводчик на азбуку Морзе")

        #Создание окна
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.resize(350, 350)
        self.setMinimumSize(QSize(350, 350))
        self.setMaximumSize(QSize(350, 350))
        self.setStyleSheet(u"background-color: rgb(151, 154, 170);")

        self.logo_label = QLabel("Morse code Translator")
        self.logo_label.setGeometry(QRect(0, 1, 350, 20)) #Почему не работает??
        self.logo_label.setMinimumSize(QSize(350, 20))
        self.logo_label.setMaximumSize(QSize(350, 20))
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setStyleSheet(u'font: 800 16pt "Montserrat";')
        self.layout.addWidget(self.logo_label)

        #Текст перед вводом
        self.input_label = QLabel("Введите текст на русском языке:")
        self.input_label.setGeometry(QRect(-5, 100, 350, 20)) #Почему не работает??
        self.input_label.setMinimumSize(QSize(350,20))
        self.input_label.setMaximumSize(QSize(350,20))
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setStyleSheet(u'font: italic 12pt "Montserrat";')
        self.layout.addWidget(self.input_label)

        #Поле для ввода
        self.input_field = QLineEdit()
        self.input_field.setMinimumSize(QSize(325, 35))
        self.input_field.setMaximumSize(QSize(325, 35))
        self.input_field.setClearButtonEnabled(True)
        self.layout.addWidget(self.input_field)

        #Кнопка "Перевести"
        self.translate_button = QPushButton("Перевести")
        self.translate_button.setMinimumSize(QSize(325, 35))
        self.translate_button.setMaximumSize(QSize(325, 35))
        self.translate_button.clicked.connect(self.translate_text)
        self.layout.addWidget(self.translate_button)

        #Текст перед выводом
        self.output_label = QLabel("Текст в азбуке Морзе:")
        self.output_label.setGeometry(QRect(-5, 100, 350, 20)) #Почему не работает??
        self.output_label.setMinimumSize(QSize(350,20))
        self.output_label.setMaximumSize(QSize(350,20))
        self.output_label.setAlignment(Qt.AlignCenter)
        self.output_label.setStyleSheet(u'font: italic 12pt "Montserrat";')
        self.layout.addWidget(self.output_label)

        #Поле вывода
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setMinimumSize(QSize(325, 35))
        self.output_field.setMaximumSize(QSize(325, 35))
        self.layout.addWidget(self.output_field)

    def translate_text(self):
        input_text = self.input_field.text().strip()
        self.output_field.setText("")
        if input_text:
            morse_code = translating(input_text)
            self.output_field.setText(morse_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = MorseTranslator()
    translator.show()
    sys.exit(app.exec())