import _json

phonebook = "./phonebook.json"

with open(phonebook, "r+") as file:
    file.write(
        "Add new entries \n" 
        "Search by first name \n" 
        "Search by last name \n" 
        "Search by full name \n" 
        "Search by telephone number \n" 
        "Search by city or state \n"
        "Delete a record for a given telephone number \n" 
        "Update a record for a given telephone number \n")
    file.close()

with open(phonebook) as file:
    print(file.read())


