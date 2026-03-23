todos = []

while True:
    
    user_action = input("Enter the user action (add, show, quit): ")
    
    
    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "quit":
            break