import csv
todos = []

stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    todos.append(title)
    

def print_list():
    global todos
    count=1
    print(" Tareas pendientes")
    for row in todos:       
        print(f"{count}. {row}")
        count+=1

def delete_task(number_to_delete):
    # your code here
    todos.pop(number_to_delete - 1)

def save_todos():
     with open('todos.csv', 'w', newline="\n") as csvfile:
        writer = csv.writer(csvfile, delimiter='\n')
        writer.writerow(todos)
    
def load_todos():
    with open('todos.csv', 'w', newline="\n") as file:
        reader = csv.reader(file, delimiter='\n')
        for row in reader:
            todos.append(*row)
        print("Tareas cargadas")
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")