date = input("enter the date: ")
mood = input("enter the mood: ")
thoughts = input("enter the thoughts: ")

with open (f"{date}.txt", 'w') as file:
    file.write(f"date: {date} \n")
    file.write(f"mood: {mood} \n")
    file.write(f"thoughts: {thoughts} \n")
    
    