todos = []

while True:
    action = input("what would you like to do? Add or show?")
    
    match action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "quit":
            break
        
        
        

fruits = []

while True:
    action = input("what would you like to do? Add or show?")
    
    match action:
        case "add":
            fruit = input("enter a fruit: ")
            fruits.append(fruit)
        case "show":
            print(fruits)
        case "quit":
            break
        