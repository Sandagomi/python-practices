flights = []

while True:
    action = input("Enter to add, show, edit and quit Flights: ")
    action = action.strip()
    
    match action:
        case "add":
            airbus = input("add a flight: ")
            flights.append(airbus)
        
        case "show" | "display":
            for f in flights:
                print(f.title())
        
        case "edit":
            newAction = int(input("which flight you want to change?: "))
            newAction = newAction - 1
            newFlight = input("Enter the new flight: ")
            flights[newAction] = newFlight
            
        case "quit":
            break