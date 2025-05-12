class DevilFruitUser:
    def __init__(self, name, fruit_type):
        self.name = name
        self.__devil_fruit = fruit_type

    def reveal_fruit(self):
        #print(f"{self.name} has the {self.__devil_fruit} fruit!")
        return self.__devil_fruit
    
    def use_power(self):
        print(f"{self.name} uses the power of the {self.__devil_fruit}!")

name = "Nico Robin"
devil_fruit = "Hana Hana no Mi"

robin = DevilFruitUser(name, devil_fruit)
robin.use_power()