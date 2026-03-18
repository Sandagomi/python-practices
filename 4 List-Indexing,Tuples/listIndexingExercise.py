todos = []

while True:
    
    user_action = input("Enter Add, Edit, Show and quit: ")
    user_action = user_action.strip()
    
    match user_action:
        
        case "add":
            todo = input ("Enter an item: ")
            todos.append(todo)
        
        case "edit":
            findNumber = int(input("enter the item you want to edit:   "))
            findNumber = findNumber - 1
            newTodo = input("enter the new item: ")
            todos[findNumber] = newTodo
            
        case "show" | "display":
            for item in todos:
                print(item)
        
        case "quit":
            break
        
        