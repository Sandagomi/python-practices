todos = []

while True:
    action = input ("Enter the action: Add, view, update, delete or exit: :")
    action = action.strip().lower()
    
    match action:
        
        case "add":
            todo = input("Enter the item: ") + "\n"
            todos.append(todo)
            file = open("todos.txt", "w")
            file.writelines(todos)
           
            
        case "view":
            for index, item in enumerate(todos): 
                row = f"{index + 1} - {item}" 
                print(row)
        
        case "delete":
            todo = int(input("Enter the index of the item to delete:  "))
            todo = todo - 1
            todos.pop(todo)
            
        case "update":
            todo = int(input("Enter the index of the item to update:  "))
            todo = todo - 1
            
            new_todo = input("Enter the new item: ")
            todos[todo] = new_todo
            
        case "exit":
            break