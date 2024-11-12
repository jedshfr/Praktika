from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from database import PartnerProduct, Products, Partner, session
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


class HistoryWindow(QDialog):
    def __init__(self, partner_id):
        super().__init__()
        self.partner_id = partner_id
        self.setWindowTitle("История реализации продукции")
        self.setGeometry(100, 100, 800, 600)
        
        # Устанавливаем иконку окна
        icon_path = os.path.expanduser("D:/icon.ico")  # Укажите путь к иконке
        self.setWindowIcon(QIcon(icon_path))

        # Основной макет
        main_layout = QVBoxLayout()

        # Заголовок, выровнен по центру
        title_label = QLabel("История реализации продукции")
        title_label.setFont(QFont("Segoe UI", 18))
        title_label.setStyleSheet("color: #67BA80;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Поле для поиска по продукции
        search_layout = QHBoxLayout()

        self.product_search_input = QLineEdit(self)
        self.product_search_input.setPlaceholderText("Поиск по продукции")
        self.product_search_input.textChanged.connect(self.update_sales_history)
        self.product_search_input.setFont(QFont("Segoe UI", 12))
        self.product_search_input.setStyleSheet("color: #67BA80;")
        search_layout.addWidget(self.product_search_input)

        main_layout.addLayout(search_layout)

        # Таблица для отображения истории продаж
        self.sales_table = QTableWidget(self)
        self.sales_table.setColumnCount(4)
        self.sales_table.setHorizontalHeaderLabels(["Продукция", "Партнер", "Количество", "Дата"])
        self.sales_table.setFont(QFont("Segoe UI", 12))
        
        # Стиль для таблицы 
        self.sales_table.setStyleSheet(""" 
            QTableWidget {
                background-color: white;
                color: black;
                gridline-color: black;
            }
            QHeaderView::section {
                background-color: white;
                color: black;
                font-weight: bold;
                border: 1px solid black;
            }
            QTableWidget::item {
                border: 1px solid black;
            }
        """)
        main_layout.addWidget(self.sales_table)

        # Кнопки внизу
        button_layout = QHBoxLayout()

        # Кнопка "Вернуться назад"
        back_button = QPushButton("Вернуться назад")
        back_button.clicked.connect(self.close)
        back_button.setFont(QFont("Segoe UI", 12))
        back_button.setStyleSheet("background-color: #67BA80; color: white;")

        # Кнопка "Отчет"
        report_button = QPushButton("Отчет")
        report_button.setFont(QFont("Segoe UI", 12))
        report_button.setStyleSheet("background-color: #67BA80; color: white;")
        report_button.clicked.connect(self.generate_pdf_report)  # Связываем кнопку с методом генерации PDF

        button_layout.addWidget(back_button)
        button_layout.addWidget(report_button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.load_sales_data()

    def load_sales_data(self):
        """Загружаем данные о продажах партнера из базы данных."""
        partner_products = session.query(PartnerProduct).filter(PartnerProduct.id_partner == self.partner_id).all()
        self.sales_table.setRowCount(len(partner_products))

        for row, partner_product in enumerate(partner_products):
            product = session.query(Products).filter(Products.id_product == partner_product.product).first()
            partner = session.query(Partner).filter(Partner.id_partners == partner_product.id_partner).first()

            self.sales_table.setItem(row, 0, QTableWidgetItem(product.name_product))
            self.sales_table.setItem(row, 1, QTableWidgetItem(partner.name_partners))
            self.sales_table.setItem(row, 2, QTableWidgetItem(str(partner_product.count_product)))
            self.sales_table.setItem(row, 3, QTableWidgetItem(str(partner_product.date_sale)))

    def update_sales_history(self):
        """Обновляем таблицу на основе введенных данных в поле поиска."""
        product_filter = self.product_search_input.text().lower()
        partner_products = session.query(PartnerProduct).filter(PartnerProduct.id_partner == self.partner_id).all()

        filtered_data = [
            partner_product for partner_product in partner_products
            if product_filter in session.query(Products).filter(
                Products.id_product == partner_product.product
            ).first().name_product.lower()
        ]

        self.sales_table.setRowCount(len(filtered_data))

        for row, partner_product in enumerate(filtered_data):
            product = session.query(Products).filter(Products.id_product == partner_product.product).first()
            partner = session.query(Partner).filter(Partner.id_partners == partner_product.id_partner).first()

            self.sales_table.setItem(row, 0, QTableWidgetItem(product.name_product))
            self.sales_table.setItem(row, 1, QTableWidgetItem(partner.name_partners))
            self.sales_table.setItem(row, 2, QTableWidgetItem(str(partner_product.count_product)))
            self.sales_table.setItem(row, 3, QTableWidgetItem(str(partner_product.date_sale)))

    def generate_pdf_report(self):
        """Генерирует PDF отчет с информацией о продажах."""
        file_path = os.path.expanduser("D:/sales_report.pdf")
        c = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4
        pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))

        # Заголовок
        c.setFont("DejaVuSans", 16)
        c.drawString(200, height - 100, "Отчет: История реализации продукции")

        # Подзаголовок
        c.setFont("DejaVuSans", 12)
        c.drawString(50, height - 140, "История реализации продукции")

        # Заголовки таблицы
        c.setFont("DejaVuSans", 10)
        headers = ["Продукция", "Партнер", "Количество", "Дата"]
        # Увеличиваем расстояние между столбцами
        x_positions = [50, 200, 350, 500]  # Увеличили шаг между столбцами
        y_position = height - 160

        for i, header in enumerate(headers):
            c.drawString(x_positions[i], y_position, header)

        # Заполнение таблицы
        y_position -= 20
        c.setFont("DejaVuSans", 10)
        
        for row in range(self.sales_table.rowCount()):
            if y_position < 50:  # Проверяем, не выходит ли строка за пределы страницы
                c.showPage()
                y_position = height - 100
            for col in range(self.sales_table.columnCount()):
                item = self.sales_table.item(row, col)
                if item:
                    c.drawString(x_positions[col], y_position, item.text())
            y_position -= 20

        # Сохраняем PDF
        c.save()

        # Открытие модального окна с сообщением
        self.show_pdf_generation_success_message(file_path)

    def show_pdf_generation_success_message(self, file_path):
        """Показывает сообщение о успешном создании отчета."""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Отчет создан")
        msg_box.setText(f"Отчет успешно создан и сохранен: {file_path}")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
