# tests/test_todo.py
import os
import unittest
import tempfile
from todo import load_tasks, save_tasks, add_task, delete_task, complete_task

class TestTodo(unittest.TestCase):

    def setUp(self):
        """Создаём временный файл для каждого теста и подменяем константу TASKS_FILE."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_filename = self.temp_file.name
        # Подменяем путь к файлу задач внутри модуля todo
        import todo
        todo.TASKS_FILE = self.test_filename
        self.todo = todo

    def tearDown(self):
        """Удаляем временный файл после теста."""
        if os.path.exists(self.test_filename):
            os.unlink(self.test_filename)

    def test_load_tasks_empty(self):
        # Файл не существует — load_tasks вернёт пустой список
        tasks = load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load(self):
        tasks = ["Задача 1", "Задача 2"]
        save_tasks(tasks)
        loaded = load_tasks()
        self.assertEqual(loaded, tasks)

    def test_add_task(self):
        tasks = []
        tasks = add_task(tasks, "Купить молоко")
        self.assertIn("Купить молоко", tasks)
        # Проверяем, что файл создан и содержит задачу
        with open(self.test_filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
        self.assertEqual(content, "Купить молоко")

    def test_add_task_empty(self):
        tasks = ["Существующая задача"]
        tasks = add_task(tasks, "   ")   # пустая строка
        self.assertEqual(tasks, ["Существующая задача"])  # не добавилось

    def test_delete_task(self):
        tasks = ["Задача A", "Задача B", "Задача C"]
        tasks = delete_task(tasks, 1)   # удаляем "Задача B"
        self.assertEqual(tasks, ["Задача A", "Задача C"])

    def test_delete_task_invalid_index(self):
        tasks = ["Задача A"]
        tasks = delete_task(tasks, 5)   # несуществующий индекс
        self.assertEqual(tasks, ["Задача A"])  # ничего не изменилось

    def test_complete_task(self):
        tasks = ["Сделать ДЗ"]
        tasks = complete_task(tasks, 0)
        self.assertEqual(tasks, ["[x] Сделать ДЗ"])

    def test_complete_task_already_completed(self):
        tasks = ["[x] Уже выполнено"]
        tasks = complete_task(tasks, 0)
        self.assertEqual(tasks, ["[x] Уже выполнено"])  # не дублируем пометку

    def test_complete_task_invalid_index(self):
        tasks = ["Задача"]
        tasks = complete_task(tasks, 10)
        self.assertEqual(tasks, ["Задача"])  # без изменений