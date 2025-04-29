class ToDoList:
    def __init__(self):
        self.todo_list = []

    def is_empty(self):
        """Ye function check karta hai ke task list khaali hai ya nahi."""
        return len(self.todo_list) == 0

    def view_tasks(self):
        """Agar tasks maujood hain to unhe display karta hai, warna message deta hai."""
        if self.is_empty():
            print("❌ No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(self.todo_list, 1):
                status = "✅ Completed" if task["completed"] else "❌ Not completed"
                print(f"{i}. {task['Task']} - {status}")

    def add_task(self):
        """User se new task leta hai aur list mein add karta hai."""
        task = input("📝 Enter a new task: ").strip()
        if task:
            self.todo_list.append({"Task": task, "completed": False})
            print("✅ Task added successfully.")
        else:
            print("⚠️ You entered nothing.")

    def delete_task(self):
        """Task delete karta hai agar available hon."""
        self.view_tasks()
        try:
            task_num = int(input("🗑️ Enter the task number to delete: "))
            if 1 <= task_num <= len(self.todo_list):
                removed = self.todo_list.pop(task_num - 1)
                print(f"✅ Removed task: {removed['Task']}")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    def complete_task(self):
        """Task ko complete mark karta hai."""
        self.view_tasks()
        try:
            compl = int(input("✔️ Enter the number of the task you completed: "))
            if 1 <= compl <= len(self.todo_list):
                self.todo_list[compl - 1]["completed"] = True
                print("✅ Task marked as completed.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    def update_task(self):
        """Existing task ka text update karta hai."""
        self.view_tasks()
        try:
            task_num = int(input("✏️ Enter the task number to update: "))
            if 1 <= task_num <= len(self.todo_list):
                new_task = input("🆕 Enter the new task description: ").strip()
                if new_task:
                    self.todo_list[task_num - 1]["Task"] = new_task
                    print("✅ Task updated successfully.")
                else:
                    print("⚠️ Task description cannot be empty.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    def show_menu(self):
        """Dynamic menu display based on whether tasks exist or not."""
        print("\n--- 📘 To-Do List Menu ---")
        if not self.is_empty():
            print("1. View tasks")
            print("2. Add task")
            print("3. Delete task")
            print("4. Complete a task")
            print("5. Update task")
            print("6. Exit")
            return "123456"  # All options available
        else:
            print("1. Add task")
            print("2. Exit")
            return "12"  # Only add and exit available

    def run(self):
        """Yeh method app ko run karne ka main loop hai."""
        while True:
            valid_options = self.show_menu()
            choice = input("👉 Choose an option: ").strip()

            if choice == '1' and '1' in valid_options:
                if not self.is_empty():
                    self.view_tasks()
                else:
                    self.add_task()
            elif choice == '2' and '2' in valid_options:
                if len(valid_options) == 6:  # All options available
                    self.add_task()
                else:  # Only add/exit menu
                    print("👋 Exiting... Have a productive day!")
                    break
            elif choice == '3' and '3' in valid_options:
                self.delete_task()
            elif choice == '4' and '4' in valid_options:
                self.complete_task()
            elif choice == '5' and '5' in valid_options:
                self.update_task()
            elif choice == '6' and '6' in valid_options:
                print("👋 Exiting... Have a productive day!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


# App ko sirf tab run kare jab yeh file direct run ho
if __name__ == "__main__":
    todo = ToDoList()
    todo.run()