"""
    I'm making a pet Pokemon. Because I can.


        Define a Pet Class:
            Create private properties: owner_first_name, owner_last_name, pokemon_id, pokemon_nickname, and pokemon_species.
            Set a default value for pet_type as "Pokemon".
            Implement getter and setter methods for all properties.
            Include a class variable vet_name set to the name of your veterinary office.
            Add a method display_pet_info to print all details of the pet and owner.
        Create Pet Objects:
            Instantiate at least three pet objects with different details.
            Show the use of setter methods for at least one pet object.
        Implement Property Existence Check:
            Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
        Display Information:
            Use display_pet_info to print details for each pet.
            Show three examples of check_property being used on various properties and pets.
            show two examples of display_pet_info on different instances of pet that you create

    """


class Pokemon:
    def __init__(self, owner_fn, owner_ln, pokemon_id, pokemon_nickname, pokemon_species):
        self.__owner_fn = owner_fn
        self.__owner_ln = owner_ln
        self.__pokemon_id = pokemon_id
        self.__pokemon_nickname = pokemon_nickname
        self.__pokemon_species = pokemon_species

    def get_owner_fn(self):
        return f"{self.__owner_fn}"

    def get_owner_ln(self):
        return f"{self.__owner_ln}"

    def get_pokemon_id(self):
        return f"{self.__pokemon_id}"

    def get_pokemon_nickname(self):
        return f"{self.__pokemon_nickname}"

    def get_pokemon_species(self):
        return f"{self.__pokemon_species}"

    def set_owner_fn(self, owner_fn):
        self.__owner_fn = owner_fn

    def set_owner_ln(self, owner_ln):
        self.__owner_ln = owner_ln

    def set_pokemon_id(self, pokemon_id):
        self.__pokemon_id = pokemon_id

    def set_pokemon_nickname(self, pokemon_nickname):
        self.__pokemon_nickname = pokemon_nickname

    def set_pokemon_species(self, pokemon_species):
        self.__pokemon_species = pokemon_species

    def display_pokemon_info(self):
        return f"{self.__owner_fn}, {self.__owner_ln}, {self.__pokemon_id}, {self.__pokemon_nickname}, {self.__pokemon_species}"

    def check_property(self, property):
        if hasattr(self, property):
            print(f"{property} exists.")
        else:
            print(f"{property} does not exist.")


def main():
    pip = Pokemon("Sylvia", "Reviar", "#0393", "Pip", "Piplup")
    fluffy = Pokemon("Sylvia", "Reviar", "#0333", "Fluffy", "Swablu")
    grover = Pokemon("Jack", "Reviar", "#0387", "Grover", "Turtwig")

    grover.check_property("_Pokemon__pokemon_id")
    pip.check_property("_Pokemon__owner_fn")
    fluffy.check_property("_Pokemon__pokemon_nickname")

    print(pip.display_pokemon_info())
    print(fluffy.display_pokemon_info())
    print(grover.display_pokemon_info())

    print(f"Pip is a type of {type(pip)}.")
    print(f"Fluffy is a type of {type(fluffy)}.")
    print(f"Grover is a type of {type(grover)}.")


main()
