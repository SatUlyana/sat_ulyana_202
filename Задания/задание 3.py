tasks = {"Бэклог": [], "В работе": [], "Выполнено": []}

def add_task(task, column):
    tasks[column].append(task)
    print(f"Задача '{task}' добавлена в колонку '{column}'.")

def remove_task(task, column):
    if task in tasks[column]:
        tasks[column].remove(task)
        print(f"Задача '{task}' удалена из колонки '{column}'.")
    else:
        print(f"Задача '{task}' не найдена в колонке '{column}'.")

def move_task(task, current_column, new_column):
    if task in tasks[current_column]:
        tasks[current_column].remove(task)
        tasks[new_column].append(task)
        print(f"Задача '{task}' перемещена из колонки '{current_column}' в колонку '{new_column}'.")
    else:
        print(f"Задача '{task}' не найдена в колонке '{current_column}'.")

def display_board():
    for column, tasks_list in tasks.items():
        print(f"{column}:")
        for task in tasks_list:
            print(f"- {task}")
        print()


