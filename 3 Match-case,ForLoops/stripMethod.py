todos = []

while True:
    
    user_action = input("Enter the user action (add, show, quit): ")
    user_action = user_action.strip()
    
    
    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                print(item)
        case "quit":
            break
        case _:
            print("entered command is wrong")