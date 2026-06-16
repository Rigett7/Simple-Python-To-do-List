import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Загружает задачи из файла tasks.txt. Если файла нет, возвращает пустой список."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    """Сохраняет список задач в файл tasks.txt."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks, new_task):
    """Добавляет новую задачу в список (если она не пуста) и сохраняет в файл."""
    if new_task.strip():
        tasks.append(new_task.strip())
        save_tasks(tasks)
    return tasks

def delete_task(tasks, index):
    """Удаляет задачу по индексу (индексация с 0) и сохраняет изменения."""
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    return tasks

def complete_task(tasks, index):
    """Помечает задачу как выполненную (добавляет '[x] ' в начало) и сохраняет."""
    if 0 <= index < len(tasks):
        task = tasks[index]
        if not task.startswith("[x] "):
            tasks[index] = "[x] " + task
            save_tasks(tasks)
    return tasks