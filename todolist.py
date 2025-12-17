import json
def print_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
def save_tasks(tasks):
    # הפקודה with open מבטיחה שהקובץ ייסגר אוטומטית בסוף - כמו smart pointer
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved to file.")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # אם הקובץ לא קיים (הרצה ראשונה), נחזיר רשימה ריקה
        return []

def main():
    # בפייתון לא צריך להגדיר גודל למערך מראש (כמו malloc).
    # הרשימה הזו דינמית ויכולה לגדול ולקטון אוטומטית.
    tasks = load_tasks()
    print(f"loaded {len(tasks)} tasks from memory")

    while True:  # שקול ל- while(1) ב-C
        print_menu()

        # input תמיד מחזיר מחרוזת (string)
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_name = input("Enter the task description: ")
            # TODO: כאן אתה צריך להוסיף את המשימה לרשימה
            tasks.append(task_name)
            # רמז: חפש בגוגל "python list append"
            print("Task added!")

        elif choice == '2':
            print("\nYour Tasks:")
            # TODO: כאן אתה צריך לרוץ על הרשימה ולהדפיס כל משימה
            for task in tasks:
                print(task)
            # רמז: for task in tasks:
            pass  # pass זו מילה שאומרת "אל תעשה כלום", רק כדי שהקוד ירוץ כרגע

        elif choice == '3':
            # נסה למחוק משימה לפי השם שלה או המיקום שלה
            task_to_remove = input("Enter task name to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print("Task removed!")
            else:
                print("Invalid task name, please try again.")
            pass

        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


# זה מוודא שהקוד ירוץ רק אם מריצים את הקובץ ישירות
if __name__ == "__main__":
    main()