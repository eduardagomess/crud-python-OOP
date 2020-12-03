class Client:

    def __init__(self, name, telephone, email):
        self.__name = name
        self.__telephone = telephone
        self.__email = email


    def __str__(self):
        return (f"Name: {self.__name}\nTelephone: {self.__telephone}  Email: {self.__email}")

    def getName(self):
        return self.__name

    def getTelephone(self):
        return self.__telephone

    def getEmail(self):
        return self.__email

    def changeName(self, new_name):
        self.__name = new_name
        return self.__name

    def changeTelephone(self, new_telephone):
        self.__telephone = new_telephone
        return self.__telephone

    def changeEmail(self, new_email):
        self.__email = new_email
        return self.__email
