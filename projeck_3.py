import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout,
    QWidget, QPushButton, QLineEdit, QMessageBox, QListWidget, QInputDialog
)
from PyQt6.QtCore import Qt


class Database:
    """Класс для управления базой данных."""
    def __init__(self, db_name="quiz.db"):
        self.sp = list()
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Создание таблицы, если она не существует
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                correct_answer TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def insert_question(self, question, answer):
        """Добавление вопроса в базу данных."""
        self.cursor.execute("INSERT INTO questions (question, correct_answer) VALUES (?, ?)", (question, answer))
        self.connection.commit()

    def reset_id_counter(self):
        """Сброс автоинкрементного счетчика ID."""
        self.cursor.execute("DELETE FROM questions")
        self.cursor.execute("DELETE FROM sqlite_sequence WHERE name='questions';")  # Сброс счетчика
        self.connection.commit()

    def get_questions(self):
        """Получение всех вопросов из базы данных."""
        self.cursor.execute("SELECT id, question, correct_answer FROM questions")
        return self.cursor.fetchall()

    def delete_question(self, question_id):
        """Удаление вопроса из базы данных по ID."""
        self.cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
        self.connection.commit()

    def close(self):
        """Закрытие соединения с базой данных."""
        self.connection.close()


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Программа для проверки знаний")
        self.setGeometry(100, 100, 400, 300)

        self.database = Database()

        self.initUI()

    def initUI(self):
        """Инициализация главного пользовательского интерфейса."""
        layout = QVBoxLayout()

        student_button = QPushButton("Ученик")
        teacher_button = QPushButton("Учитель")


        student_button.clicked.connect(self.name_lastname)
        teacher_button.clicked.connect(self.ask_password)


        layout.addWidget(student_button)
        layout.addWidget(teacher_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def name_lastname(self):
        """Запрос имени и фамилии ученика"""
        name, last_name = QInputDialog.getText(self, "Имя фамилия ", "Введите свое имя и фамилию:")
        if name and last_name:
            self.show_student_window()
        else:
            QMessageBox.warning(self, "Ошибка", "Вы не ввели имя и фамилию")

    def proverka(self):
        self.show_admin_window()


    def ask_password(self):
        """Запрос пароля для доступа к окну учителя"""
        password, ok = QInputDialog.getText(self, "Пароль", "Введите пароль:")

        if ok and password == "1234":
            self.proverka()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный пароль.")

    def show_student_window(self):
        """Показать окно ученика."""
        self.student_window = StudentWindow(self.database, self)
        self.student_window.show()
        self.close()
    def show_admin_window(self):
        self.teacher_window_prov = TeacherWindow1(self.database, self)
        self.teacher_window_prov.show()
        self.close()

    def show_teacher_window(self):
        """Показать окно учителя."""
        self.teacher_window = TeacherWindow(self.database, self)
        self.teacher_window.show()
        self.close()


class StudentWindow(QWidget):
    def __init__(self, database, parent):
        super().__init__()
        self.database = database
        self.parent = parent

        self.setWindowTitle("Ученик")
        self.setGeometry(100, 100, 400, 300)

        self.question_label = QLabel(self)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем текст
        self.question_label.setStyleSheet("font-size: 18px; font-weight: bold;")  # Увеличиваем размер шрифта и выделяем
        self.answer_input = QLineEdit(self)
        self.submit_button = QPushButton("Ответить", self)
        self.back_button = QPushButton("Назад", self)  # Кнопка назад

        self.initUI()

        self.score = 0
        self.questions = self.database.get_questions()  # Получаем все вопросы один раз
        self.current_question_index = 0

        if self.questions:
            # Загружаем первый вопрос
            self.load_question()

    def initUI(self):
        """Инициализация пользовательского интерфейса окна ученика"""
        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.back_button)  # Добавляем кнопку назад

        self.submit_button.clicked.connect(self.check_answer)
        self.back_button.clicked.connect(self.go_back)  # Подключаем кнопку назад

        self.setLayout(layout)

    def load_question(self):
        """Загрузка следующего вопроса из базы данных"""
        if self.current_question_index < len(self.questions):
            self.question_label.setText(self.questions[self.current_question_index][1])  # Текст вопроса
            self.answer_input.clear()  # Очищаем поле ввода
        else:
            self.end_quiz()  # Если вопросы закончились, завершить викторину

    def check_answer(self):
        """Проверка ответа пользователя"""
        answer = self.answer_input.text()
        correct_answer = self.questions[self.current_question_index][2]\
            if self.current_question_index < len(self.questions) else None
        if answer == '':
            QMessageBox.information(self, "Ошибка!", 'Вы не ввели ответ ')
        elif correct_answer:
            if answer.strip().lower() == correct_answer.strip().lower():
                self.score += 1

            else:
                QMessageBox.warning(self, "Неправильно!",
                               f"Правильный ответ: {correct_answer}")

            self.current_question_index += 1
            self.load_question()  # Загружаем следующий вопрос

    def end_quiz(self):
        """Завершение викторины и вывод результата"""
        grade = self.calculate_grade(self.score)
        QMessageBox.information(self, "Викторина завершена!", f"Ваш результат: {self.score}"
                                                              f" из {len(self.questions)}.\nВаша оценка: {grade}.")
        self.parent.show()  # Показываем родительское окно (главное окно)
        self.close()

    def calculate_grade(self, score):
        """Подсчёт оценки на основе баллов"""
        total_questions = len(self.questions)
        if total_questions == 0:  # Защита от деления на ноль
            return "Нет вопросов"

        if score >= total_questions * 0.75:
            return "Отлично\n оценка 5"
        elif score >= total_questions * 0.5:
            return "Хорошо "
        elif score >= total_questions * 0.25:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    def go_back(self):
        """Возврат к главному окну"""
        self.parent.show()  # Показываем родительское окно (главное окно)
        self.close()  # Закрываем текущее окно

class TeacherWindow1(QWidget):
    def __init__(self, database, parent):
        super().__init__()
        self.database = database
        self.parent = parent



        self.setWindowTitle("Админ")
        self.setGeometry(100, 100, 400, 300)
        self.submit_button = QPushButton("Проверить результаты учеников", self)
        self.delete_button1 = QPushButton("Изменение вопросов", self)
        self.back_button = QPushButton("Назад", self)  # Кнопка назад



        self.initUI()

    def initUI(self):
        """Инициализация пользовательского интерфейса окна учителя"""
        layout = QVBoxLayout()

        layout.addWidget(self.submit_button)
        layout.addWidget(self.delete_button1)
        layout.addWidget(self.back_button)  # Добавляем кнопку назад
        self.setLayout(layout)
        self.back_button.clicked.connect(self.go_back)
        self.delete_button1.clicked.connect(self.show_correct_window)
    def go_back(self):
        """Возврат к главному окну."""
        self.parent.show()  # Показываем родительское окно (главное окно)
        self.close()  # Закрываем текущее окно

    def show_correct_window(self):
        """Показать окно учителя."""
        self.correct_window = TeacherWindow(self.database, self)
        self.correct_window.show()
        self.close()

class TeacherWindow(QWidget):
    def __init__(self, database, parent):
        super().__init__()
        self.database = database
        self.parent = parent

        self.setWindowTitle("Учитель")
        self.setGeometry(100, 100, 400, 300)

        self.question_input = QLineEdit(self)
        self.answer_input = QLineEdit(self)
        self.submit_button = QPushButton("Добавить вопрос", self)
        self.delete_button = QPushButton("Удалить вопрос", self)
        self.back_button = QPushButton("Назад", self)  # Кнопка назад
        self.question_list = QListWidget(self)

        self.initUI()

        # Загрузка вопросов из базы данных
        self.load_questions()

    def initUI(self):
        """Инициализация пользовательского интерфейса окна учителя"""
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Введите вопрос:"))
        layout.addWidget(self.question_input)
        layout.addWidget(QLabel("Введите правильный ответ:"))
        layout.addWidget(self.answer_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(QLabel("Список вопросов:"))
        layout.addWidget(self.question_list)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.back_button)  # Добавляем кнопку назад

        self.submit_button.clicked.connect(self.add_question)
        self.delete_button.clicked.connect(self.delete_question)
        self.back_button.clicked.connect(self.go_back)  # Подключаем кнопку назад

        self.setLayout(layout)

    def load_questions(self):
        """Загрузка вопросов из базы данных в список"""
        self.question_list.clear()
        questions = self.database.get_questions()
        for question in questions:
            self.question_list.addItem(f"{question[0]}: {question[1]}")  # Добавление ID и текста вопроса

    def add_question(self):
        """Добавление вопроса в базу данных."""
        question = self.question_input.text()
        answer = self.answer_input.text()

        if question and answer:
            if not self.database.get_questions():  # Проверяем, пустая ли таблица
                self.database.reset_id_counter()  # Сброс автоинкрементного счетчика

            self.database.insert_question(question, answer)
            QMessageBox.information(self, "Успех!", "Вопрос добавлен!")
            self.question_input.clear()
            self.answer_input.clear()
            self.load_questions()  # Обновляем список вопросов
        else:
            QMessageBox.warning(self, "Ошибка!", "Пожалуйста, заполните оба поля.")

    def delete_question(self):
        """Удаление выбранного вопроса из базы данных"""
        selected_items = self.question_list.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            question_id = int(selected_item.text().split(":")[0])  # Извлечение ID из текста
            self.database.delete_question(question_id)
            QMessageBox.information(self, "Успех!", "Вопрос успешно удален!")
            self.load_questions()  # Обновляем список вопросов
        else:
            QMessageBox.warning(self, "Ошибка!", "Пожалуйста, выберите вопрос для удаления.")

    def go_back(self):
        """Возврат к главному окну."""
        self.parent.show()  # Показываем родительское окно (главное окно)
        self.close()  # Закрываем текущее окно


if __name__ == '__main__':
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec())