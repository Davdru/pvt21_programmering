

TODO_FILE = "todo.txt"


class Todo:
    task: str

    def __init__(self, task):
        self.task = task

    def __str__(self):
        return f"Task: {self.task}"


class TodoList:
    todos: list[Todo]

    def __init__(self):
        self.todos = []

    def print_todo_list(self):
        for i, todo in enumerate(self.todos, start=1):
            print(f"[{i}] {todo}")

    def add_todo(self, todo: Todo):
        self.todos.append(todo)


def load_todos() -> TodoList:
    tl = TodoList()
    with open(TODO_FILE, encoding="utf-8") as f:
        for line in f.readlines():
            tl.add_todo(Todo(line.strip()))
    return tl


def save_todos(todo_list: TodoList):
    with open(TODO_FILE, 'w') as f:
        for todo in todo_list.todos:
            f.write(todo.task + "\n")



def print_menu():
    print("[1] List todos")
    print("[4] Quit")




def main():
    todo_list = load_todos()

    while True:
        print_menu()
        user_inp = input(">")
        if user_inp == "1":
            print("----------TODOS----------")
            todo_list.print_todo_list()
            print("-------------------------")
        elif user_inp == "4":
            break





if __name__ == '__main__':
    main()