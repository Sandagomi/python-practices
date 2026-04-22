
while True:
    action = input ("Enter the action: Add, view, update, delete or exit: :")
    action = action.strip().lower()
    
    match action:
        
        case "add":
            todo = input("Enter the item: ") + "\n"
            
            file = open("/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/todos.txt", "r", encoding="utf-8")
            todos = file.readlines()
            todos.append(todo)
            file.close()
            
            file = open("/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/todos.txt", "w", encoding="utf-8")
            file.writelines(todos)
            file.close()
           
            
        case "view":
            
            file = open("/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/todos.txt", "r", encoding="utf-8")
            todos = file.readlines()
            file.close()
            
            for index, item in enumerate(todos): 
                row = f"{index + 1} - {item}" 
                print(row)
        
        case "delete":
            todo = int(input("Enter the index of the item to delete:  "))
            todo = todo - 1
            todos.pop(todo)
            file = open("/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/todos.txt", "w", encoding="utf-8")
            file.writelines(todos)
            file.close()

        case "update":
            todo = int(input("Enter the index of the item to update:  "))
            todo = todo - 1
            
            new_todo = input("Enter the new item: ")
            todos[todo] = new_todo
            file = open("/Users/sandagomithilakarathne/Desktop/Python practice/5 Processing Text Files/todos.txt", "w", encoding="utf-8")
            file.writelines(todos)
            file.close()

        case "exit":
            break