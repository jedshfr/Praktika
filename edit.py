import os
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QComboBox, QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from database import Partner, TypePartner, Address, session

class EditPartnerWindow(QDialog):
    """Класс для окна редактирования партнера."""
    def __init__(self, main_window, partner_id):
        super().__init__()
        self.main_window = main_window
        self.partner_id = partner_id  # Сохраняем ID партнера для редактирования
        self.setWindowTitle("Редактирование партнера")
        
        icon_path = os.path.expanduser("D:/icon.ico")  # Путь к иконке
        self.setWindowIcon(QIcon(icon_path))

        # Получаем данные партнера из базы данных
        self.partner = session.query(Partner).get(self.partner_id)

        # Получаем данные адреса партнера
        self.address = session.query(Address).get(self.partner.address)  # Теперь извлекаем сам объект Address

        # Инициализация флага изменений
        self.is_modified = False

        # Поля ввода
        self.name_input = QLineEdit(self.partner.name_partners)
        self.name_input.setFont(QFont("Segoe UI", 12))
        self.name_input.setStyleSheet("color: #67BA80;")
        self.name_input.textChanged.connect(self.mark_modified)
        
        self.type_combo = QComboBox()
        self.type_combo.addItems(["ОАО", "ООО", "ПАО", "ЗАО"])
        self.type_combo.setCurrentText(self.partner.type_partner.type_partners)  # Устанавливаем текущий тип
        self.type_combo.setFont(QFont("Segoe UI", 12))
        self.type_combo.setStyleSheet("color: #67BA80;")
        self.type_combo.currentTextChanged.connect(self.mark_modified)
        
        self.phone_input = QLineEdit(self.partner.phone)
        self.phone_input.setFont(QFont("Segoe UI", 12))
        self.phone_input.setStyleSheet("color: #67BA80;")
        self.phone_input.textChanged.connect(self.mark_modified)
        
        self.email_input = QLineEdit(self.partner.email)
        self.email_input.setFont(QFont("Segoe UI", 12))
        self.email_input.setStyleSheet("color: #67BA80;")
        self.email_input.textChanged.connect(self.mark_modified)
        
        self.rating_input = QLineEdit(str(self.partner.rating))
        self.rating_input.setFont(QFont("Segoe UI", 12))
        self.rating_input.setStyleSheet("color: #67BA80;")
        self.rating_input.textChanged.connect(self.mark_modified)
        
        self.director_input = QLineEdit(self.partner.director)
        self.director_input.setFont(QFont("Segoe UI", 12))
        self.director_input.setStyleSheet("color: #67BA80;")
        self.director_input.textChanged.connect(self.mark_modified)

        # Поля для адреса
        self.index_input = QLineEdit(str(self.address.index))  # Используем атрибут объекта Address
        self.index_input.setFont(QFont("Segoe UI", 12))
        self.index_input.setStyleSheet("color: #67BA80;")
        self.index_input.textChanged.connect(self.mark_modified)
        
        self.region_input = QLineEdit(self.address.region)  # Используем атрибут объекта Address
        self.region_input.setFont(QFont("Segoe UI", 12))
        self.region_input.setStyleSheet("color: #67BA80;")
        self.region_input.textChanged.connect(self.mark_modified)
        
        self.country_input = QLineEdit(self.address.country)  # Используем атрибут объекта Address
        self.country_input.setFont(QFont("Segoe UI", 12))
        self.country_input.setStyleSheet("color: #67BA80;")
        self.country_input.textChanged.connect(self.mark_modified)
        
        self.street_input = QLineEdit(self.address.street)  # Используем атрибут объекта Address
        self.street_input.setFont(QFont("Segoe UI", 12))
        self.street_input.setStyleSheet("color: #67BA80;")
        self.street_input.textChanged.connect(self.mark_modified)
        
        self.house_input = QLineEdit(str(self.address.house))  # Используем атрибут объекта Address
        self.house_input.setFont(QFont("Segoe UI", 12))
        self.house_input.setStyleSheet("color: #67BA80;")
        self.house_input.textChanged.connect(self.mark_modified)

        # Кнопки
        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.save_partner)
        save_button.setFont(QFont("Segoe UI", 12))
        save_button.setStyleSheet("background-color: #67BA80; color: white;")
        
        back_button = QPushButton("Вернуться назад")
        back_button.clicked.connect(self.close)
        back_button.setFont(QFont("Segoe UI", 12))
        back_button.setStyleSheet("background-color: #67BA80; color: white;")

        # Макет формы
        form_layout = QFormLayout()
        form_layout.addRow("Наименование партнера", self.name_input)
        form_layout.addRow("Тип партнера", self.type_combo)
        form_layout.addRow("ФИО директора", self.director_input)
        form_layout.addRow("Телефон", self.phone_input)
        form_layout.addRow("Email", self.email_input)
        form_layout.addRow("Рейтинг", self.rating_input)
        form_layout.addRow("Индекс", self.index_input)
        form_layout.addRow("Регион", self.region_input)
        form_layout.addRow("Город", self.country_input)
        form_layout.addRow("Улица", self.street_input)
        form_layout.addRow("Дом", self.house_input)
        
        # Макет кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(back_button)
        button_layout.addWidget(save_button)

        # Общий макет
        main_layout = QVBoxLayout(self)
        header_label = QLabel("<h2>Редактирование партнера</h2>")
        header_label.setFont(QFont("Segoe UI", 18))
        header_label.setStyleSheet("color: #67BA80;")
        header_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(header_label)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def mark_modified(self):
        """Отмечаем, что данные были изменены."""
        self.is_modified = True

    def closeEvent(self, event):
        """Переопределяем закрытие окна с предупреждением о несохраненных изменениях."""
        if self.is_modified:
            reply = QMessageBox.question(
                self, "Сохранить изменения?", 
                "Вы изменили данные. Хотите сохранить изменения?", 
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.save_partner()  # Сохраняем данные, если нажали "Да"
                event.accept()  # Закрываем окно после сохранения
            else:
                event.ignore()  # Просто игнорируем закрытие окна, если нажали "Нет"
        else:
            event.accept()  # Просто закрыть окно, если изменений нет

    def save_partner(self):
        # Получаем данные из полей ввода
        name = self.name_input.text()
        type_partner_text = self.type_combo.currentText()
        phone = self.phone_input.text()
        email = self.email_input.text()
        rating = int(self.rating_input.text())
        director = self.director_input.text()
        index = int(self.index_input.text())
        region = self.region_input.text()
        country = self.country_input.text()
        street = self.street_input.text()
        house = int(self.house_input.text())

        # Получение или создание типа партнера
        type_partner = session.query(TypePartner).filter_by(type_partners=type_partner_text).first()
        if not type_partner:
            type_partner = TypePartner(type_partners=type_partner_text)
            session.add(type_partner)
            session.commit()

        # Проверка на существующий адрес
        existing_address = session.query(Address).filter_by(
            index=index, region=region, country=country, street=street, house=house
        ).first()

        if existing_address:
            address = existing_address  # Используем существующий адрес
        else:
            # Создание и сохранение нового адреса
            address = Address(index=index, region=region, country=country, street=street, house=house)
            session.add(address)
            session.commit()

        # Обновление данных партнера
        partner = session.query(Partner).get(self.partner_id)
        partner.name_partners = name
        partner.type_partners = type_partner.id_type_partners
        partner.director = director
        partner.phone = phone
        partner.email = email
        partner.rating = rating
        partner.address = address.id_address  # Здесь мы сохраняем только ID адреса, а не сам объект

        session.commit()

        # Обновление списка партнеров в главном окне
        self.main_window.update_partners()
        self.close()  # Закрыть окно после сохранения
