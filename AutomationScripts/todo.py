todos = []

while True:
    action = input ("Enter the action: Add, view, update, delete or exit: :")
    action = action.strip().lower()
    
    match action:
        
        case "add":
            todo = input("Enter the item: ")
            todos.append(todo)
            
        case "view":
            for i in todos:
                print(i)
        
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