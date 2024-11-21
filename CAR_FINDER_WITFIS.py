import os 

AllowedVehiclesList = [] #List 

def cars():
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")


def menu():
    print(" ")     
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")


def populate_configs():
    
    if not os.path.isfile("carfinderfile.txt"):
        with open("carfinderfile.txt", "x") as db:
            onload_list = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
            for truck in onload_list:
                db.write(f"{truck}\n")
            db.close()

  
    with open("carfinderfile.txt") as db:
        global AllowedVehiclesList  
        AllowedVehiclesList = [lines.strip() for lines in db]
        db.close()



def print_all_authorized_vehicles():
    print(" ")
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    



def search_authorized_vehicle():
    name = input("Please Enter the full Vehicle name: ")
    found = False  
    for vehicle in AllowedVehiclesList:
        if name == vehicle:  
            found = True
    if found == True:
        print(name, "is an authorized vehicle")
            #found = True 
    
    if not found:
        print(name, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
    



def add_authorized_vehicle():
    Usercar = input("Please Enter the full Vehicle name you would like to add: ")
    AllowedVehiclesList.append(Usercar)
    print("You have added", Usercar, "as an authorized vehicle")
    



def delete_authorized_vehicle():
    RemoveCar = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if RemoveCar in AllowedVehiclesList:
        print(f"Are you sure you want to remove {RemoveCar} from the Authorized Vehicles List?")
        Confirm = input("Type 'yes' to confirm: ")
        if Confirm.lower() == 'yes':
            AllowedVehiclesList.remove(RemoveCar)
            print(f"You have REMOVED {RemoveCar} as an authorized vehicle")
        else:
            print(f"{RemoveCar} was not removed.")
    else:
        print(f"{RemoveCar} is not in the list of authorized vehicles.")
    


def startup():
    populate_configs()
    menu()



startup()

finder = int(input("Please Enter a Number: "))

while True:
    if finder == 1:
        print_all_authorized_vehicles()
        cars()
        finder = int(input("Please Enter a Number: "))
    elif finder == 2:
        search_authorized_vehicle()
        cars()
        finder = int(input("Please Enter a Number: "))
    elif finder == 3:
        add_authorized_vehicle()
        cars()
        finder = int(input("Please Enter a Number: "))
    elif finder == 4:
        delete_authorized_vehicle()
        cars()
        finder = int(input("Please Enter a Number: "))
    elif finder == 5:
        exit_choice = input("Would you like to exit, yes or no? ")
        if exit_choice.lower() == "yes":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
    else:
        print("Invalid option. Please try again.")
        cars()
        finder = int(input("Please Enter a Number: "))