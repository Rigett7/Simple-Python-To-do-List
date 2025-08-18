def todo_app():
    tasks = []
    print(
        "\n---------------------------- 📝 Welcome to the Simple To-Do App! ----------------------------\n"
    )

    total_tasks = int(input("How many tasks do you want to add initially? "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append({"name": task_name, "done": False})

    while True:
        print("\n----------------------------")
        print("Choose an option:")
        print("1 - Add a task")
        print("2 - Update a task")
        print("3 - Remove a task")
        print("4 - View tasks")
        print("5 - Mark a task as done/undone")
        print("6 - Exit")
        print("----------------------------")

        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if operation == 1:  # Add task
            add = input("Enter the task you want to add: ")
            tasks.append({"name": add, "done": False})
            print(f"✅ Task '{add}' added successfully!")

        elif operation == 2:  # Update task
            task_index = int(input("Enter the task number to update: "))
            if 1 <= task_index <= len(tasks):
                new_task_name = input("Enter the new task name: ")
                tasks[task_index - 1]["name"] = new_task_name
                print(f"✏️ Task {task_index} updated to '{new_task_name}'!")
            else:
                print("⚠️ Invalid task number!")

        elif operation == 3:  # Remove task
            task_index = int(input("Enter the task number to remove: "))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f"🗑️ Task '{removed_task['name']}' removed successfully!")
            else:
                print("⚠️ Invalid task number!")

        elif operation == 4:  # View tasks
            if tasks:
                print("\n📋 Current Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    status = "✅ Done" if task["done"] else "❌ Not done"
                    print(f"{idx}. {task['name']} [{status}]")
            else:
                print("⚠️ No tasks available!")

        elif operation == 5:  # Mark as done
            task_index = int(input("Enter the task number to mark as done/undone: "))
            if 1 <= task_index <= len(tasks):
                tasks[task_index - 1]["done"] = not tasks[task_index - 1]["done"]
                status = "✅ Done" if tasks[task_index - 1]["done"] else "❌ Not done"
                print(f"Task {task_index} marked as {status}!")
            else:
                print("⚠️ Invalid task number!")

        elif operation == 6:  # Exit
            print("👋 Exiting the app. Goodbye!")
            break

        else:
            print("⚠️ Invalid option! Please try again.")


todo_app()
