# CIS129_AlexPiller_Lab12.py
# AlexPiller
# 5/16/25

class Pet:
    def __init__(self, name="", type="", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age


def main():
    # Create a Pet object
    my_pet = Pet()

    # Set pet information directly
    my_pet.setName("Sophie")
    my_pet.setType("Pug")
    my_pet.setAge(5)

    # Display the pet information
    print("The pet name is:", my_pet.getName())
    print("The pet type is:", my_pet.getType())
    print("The pet age is:", my_pet.getAge())


# Call the main function
if __name__ == "__main__":
    main()
