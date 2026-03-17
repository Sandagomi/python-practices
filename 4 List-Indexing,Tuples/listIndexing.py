todos = []

while True:
    
    user_action = input("Enter the user action (add,edit,show, quit): ")
    user_action = user_action.strip()
    
    
    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
            
        case "edit":
            number = int(input("Number of the to do to edit: "))
            number = number - 1
            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo
            
        case "show" | "display":
            for item in todos:
                print(item)
                
        case "quit":
            break
        
        case _:
            print("entered command is wrong")