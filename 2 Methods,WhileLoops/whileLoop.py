text = "Enter to do: "
todos = []

while True:
    todo = input(text)
    todos.append(todo)

    if todo == "quit":
        break
      
    print("Your to-do list:", todos)
    
  