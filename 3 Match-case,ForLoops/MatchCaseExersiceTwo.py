cars = []

while True:
    action = input ("what would you like to do? Add or show? or quit?")
    
    match action:
        case "add":
            car = input("enter a car: ")
            cars.append(car)
        case "show":
            print(cars)
        case "quit":
            break