import json
from client import Client

class RegisterControl:

    def __init__(self):
        self.client_list = []

    def registerClient(self):
        name = input("Enter the contact name: ")
        telephone = input("telefone: ")
        email = input("email: ")
        self.client_list.append(Client(name, telephone, email))

    def removeClient(self):
        name = input("Enter the contact name: ")
        for index, client in enumerate(self.client_list):
            if client.getName() == name:
                self.client_list.pop(index)
                return self.client_list


    def searchClient(self):
        name = input("Enter the client name: ")
        for index, client in enumerate(self.client_list):
            if client.getName() == name:
                return index


    def clientInformation(self):
        register = RegisterControl
        index = register.searchClient(self)
        json_file_client_information = open("client-information.json", "w")
        client_information = {"name": self.client_list[index].getName(), "email": self.client_list[index].getEmail(),"telephone": self.client_list[index].getTelephone()}
        json.dump(client_information, json_file_client_information)

    def showAllClientInformation(self):
        for client in self.client_list:
            print(client)

    def contactsEmail(self):
        json_file_email = open("email-file.json", "w")
        for client in self.client_list:
            email_information = {"name": client.getName(), "email": client.getEmail()}
            json.dump(email_information, json_file_email)

    def changeClientInformation(self):
        change_information = input("Do you want to change name, telephone or email?")
        name_client = input("Enter the name of the client that you want to update: ")
        new_information = input("What is the change?: ")
        for index, client in enumerate(self.client_list):
            if client.getName() == name_client:
                if change_information == "name":
                    self.client_list[index].changeName(new_information)
                elif change_information == "email":
                    self.client_list[index].changeEmail(new_information)
                else:
                    self.client_list[index].changeTelephone(new_information)
