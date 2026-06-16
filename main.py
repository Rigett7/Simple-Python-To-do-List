# main.py
from todo import load_tasks, save_tasks, add_task, delete_task, complete_task

def display_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить задачу как выполненную")
    print("5. Выйти")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Введите текст задачи: ")
            tasks = add_task(tasks, new_task)
            print("Задача добавлена.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Введите номер задачи для удаления: ")) - 1
                tasks = delete_task(tasks, idx)
                print("Задача удалена, если индекс был корректным.")
            except ValueError:
                print("Введите число.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                idx = int(input("Введите номер задачи, которую нужно отметить выполненной: ")) - 1
                tasks = complete_task(tasks, idx)
                print("Задача отмечена как выполненная, если индекс был корректным.")
            except ValueError:
                print("Введите число.")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()