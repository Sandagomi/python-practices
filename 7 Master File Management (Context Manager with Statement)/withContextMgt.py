
with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    action = input ("Enter the action: Add, view, update, delete or exit: :")
    action = action.strip().lower()
    
    match action:
        
        case "add":
            todo = input("Enter the item: ") + "\n"
            todos.append(todo)
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)
           
            
        case "view":
            for index, item in enumerate(todos): 
                row = f"{index + 1} - {item}" 
                print(row)
        
        case "delete":
            todo = int(input("Enter the index of the item to delete:  "))
            todo = todo - 1
            
            todos.pop(todo)
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "update":
            todo = int(input("Enter the index of the item to update:  "))
            todo = todo - 1
            
            new_todo = input("Enter the new item: ") + "\n"
            todos[todo] = new_todo
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "exit":
            break