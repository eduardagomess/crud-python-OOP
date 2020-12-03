
from register import RegisterControl

print("Option 1: Insert a client")
print("Option 2: Remove a client")
print("Option 3: Show client information")
print("Option 4: Show all clients information")
print("Option 5: Generate a json file with all the clients email")
print("Option 6: Change client information")

register = RegisterControl()

options = {1: register.registerClient, 2: register.removeClient, 3: register.clientInformation,
           4: register.showAllClientInformation, 5: register.contactsEmail, 6: register.changeClientInformation}

finish = "no"

while finish != "yes":
    option = int(input("Enter an option: "))
    function = options[option]
    function()
    finish = input("Finish yes our no: ")