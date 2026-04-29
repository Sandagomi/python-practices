
with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    action = input ("Enter the action: Add, view, update, delete or exit: :")
    action = action.strip().lower()
    
    if 'add' in action:
        todo = input("Enter the item: ") + "\n"
        todos.append(todo)
        
        with open("todos.txt", "w") as file:
            file.writelines(todos)
           
    elif 'view' in action:
        for index, item in enumerate(todos): 
            row = f"{index + 1} - {item}" 
            print(row)
        
    elif 'delete' in action:
        todo = int(input("Enter the index of the item to delete:  "))
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todo = todo - 1
        todo_to_delete = todos[todo].strip("\n")
        todos.pop(todo)
        
        with open("todos.txt", "w") as file:
            file.writelines(todos)
        
        message = f"{todo_to_delete} was deleted from the list"
        print(message)
           
            
    elif 'update' in action:
        todo = int(input("Enter the index of the item to update:  "))
        todo = todo - 1
        
        new_todo = input("Enter the new item: ") + "\n"
        todos[todo] = new_todo
        
        with open("todos.txt", "w") as file:
            file.writelines(todos)
            
    elif 'exit' in action:
        break