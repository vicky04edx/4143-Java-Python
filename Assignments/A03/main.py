##################################################################################
#   Author:           Victoria Heredia
#   Email:            vdheredia1128@my.msutexas.edu
#   Label:            A03
#   Title:            Program 3: Pet Daycare database
#   Course:           CMPS 4143 
#   Semester:         Fall 2025
#  
#   Description:
#       This program manages a simple pet daycare database using a list of dictionaries.
#       Users can: add a new pet, view all pets, update pet preferences or information, search pets 
#       by species and exit the program. Each pet entry includes: Name, specie, preference
#       The program uses functions for each operation and loops through a menu until
#       the user chooses to exit.        
###################################################################################

print("===============================================================")
print("Author: Victoria Heredia")
print("Title: Program 3 - Pet Daycare Database")
print("Course: CMPS 4143")
print("Description: This program manages a simple pet daycare database using")
print("a list of dictionaries. Users can add new pets, view all pets, update")
print("pet preferences, search pets by species, and exit the program.")
print("Each pet entry includes: Name, Species, and Preference.")
print("===============================================================")

#Initial pet list (database)
petList = [
    {"Name": "Bella", "Species": "Dog", "Preference": "Belly rubs"},    
    {"Name": "Poly", "Species": "Parrot", "Preference": "Cursing"},

    #Two new animals added by me :)
    {"Name": "Toby", "Species": "Dog", "Preference": "Treats"},
    {"Name": "Missy", "Species": "Cat", "Preference": "Play"},
]


# Public : addNewPet()
# 
#  Description:
#       Prompts the user to input information for a new pet (name, species, and preference)
#       and adds the new pet as a dictionary to the petList.
# 
#  Params:
#       petList : list
#           A list containing all pet dictionaries in the database.
# 
#  Returns:
#       None
# 
def addNewPet(petList):
    #Ask the user for pet details
    newName = input("Enter pet's name: ")
    newSpecies = input("Enter pet's species: ")
    newPreference = input("Enter pet's preferences: ")

    #Create a new pet dictionary using the provided details
    newPet = {"Name": newName, "Species": newSpecies, "Preference": newPreference}
    
    #Add the new pet to the main list
    petList.append(newPet)
    print("New pet added to the list of dictionaries, to see the full list use option 2!")

# Public : viewPets()
# 
#  Description:
#      Displays all pets stored in the petList in a neatly aligned table format.
#      Each column represents Name, Species, and Preference.
# 
#  Params:
#       petList : list
#           A list containing all pet dictionaries in the database.
# 
#  Returns:
#       None
# 
def viewPets(petList):
    #I Googled how to properly display the names, 
    #species, and preferences so they were aligned properly like in a table

    #This was the original code:
    # print("Name | Species | Preference")
    # for pet in petList:
    # print(pet["Name"], pet["Species"], pet["Preference"])

    #Print table header
    print(f"{'Name |':<10} {'Species |':<10} {'Preference':<10}")
    print("---------------------------------")

    #Print each pet's details aligned under the headers
    for pet in petList:
        print(f"{pet['Name']:<10} {pet['Species']:<10} {pet['Preference']:<10}")

# Public : updatePetPref()
# 
#  Description:
#      Prompts the user to enter a pet's name and, if found in the list,
#      allows updating the pet's preference field.
#      If no match is found, a message is displayed.
# 
#  Params:
#       petList : list
#           A list containing all pet dictionaries in the database.
# 
#  Returns:
#       None
#
def updatePetPref(petList):
    #Ask the user for the pet’s name
    identifyPet = input("Enter pet's name: ")

    #Loop through the list to find a matching name (case-insensitive)
    for pet in petList:
        if pet["Name"].lower() == identifyPet.lower(): 
                #Ask for the new preference
                newPref = input("Enter the new value for Preference: ")
                #Update the preference field
                pet["Preference"]  = newPref
                print("Preference updated for " + pet["Name"] + " in the database, to see the update use option 2!")
                break
    else: 
        #If no pet name matched show an error message
        print("Pet not found in the list")

# Public : searchBySpecies()
# 
#  Description:
#      Allows the user to search for pets by species and displays
#      all pets that match the entered species (case-insensitive).
# 
#  Params:
#       petList : list
#           A list containing all pet dictionaries in the database.
# 
#  Returns:
#       None
#
def searchBySpecies(petList):
    #Ask the user for the species to search
    identifySpecies = input("Enter pet's species: ")
    #Loop through each pet to find matches (case-insensitive)
    for pet in petList:
        if pet["Species"].lower() == identifySpecies.lower():
            print("Name: " + pet["Name"] + ", Species: " + pet["Species"] + ", Preference: " + pet["Preference"])

       
#Main Menu loop
num = 0
while num != 5:
    print("\n")
    print("Pet Daycare Menu:")
    print("1. Add new pet")
    print("2. View all pets")
    print("3. Update pet preferences")
    print("4. Search pets by species")
    print("5. Exit")

    #Ask user for menu choice
    num = int(input("Enter your choice (Number from 1-4, press 5 to exit): "))
    
    #Perform action based on the user’s choice
    if num == 1:
        print("\n")
        addNewPet(petList)
    elif num == 2:
        print("\n")
        viewPets(petList)
    elif num == 3:
        print("\n")
        updatePetPref(petList)
    elif num == 4:
        print("\n")
        searchBySpecies(petList)
    elif num == 5:
        print("Bye, have a nice day!")
    else:
        print("Choice is not valid")