# Домашнее задание к лекции 1.7 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:
# - Коровы, козы, овцы, свиньи;
# - Утки, куры, гуси.
#
# Условия:
# - Должен быть один базовый класс, который наследуют все остальные животные.
# - Базовый класс должен определять общие характеристики и интерфейс.


class DomesticAnimals:
    weight = 10  # kg
    height = 50  # cm
    favorite_food = None
    animal_name = None
    legs = None

    def __init__(self, weight, height, favorite_food, animal_name):
        self.weight = weight
        self.height = height
        self.favorite_food = favorite_food
        self.animal_name = animal_name

    def eat(self, value):
        self.weight += value

    def about_oneself(self):
        print('animal_name = {}; weight = {}; height = {}; favorite_food = {}; legs = {}; class = {}'
              .format(self.animal_name, self.weight, self.height, self.favorite_food, self.legs, type(self)))
        print('-----------------------------------------')


class FourLegsAnimal(DomesticAnimals):
    legs = 4


class TwoLegsAnimal(DomesticAnimals):
    legs = 2


class Cows(FourLegsAnimal):
    def give_milk(self):
        print("You have cow's milk")
        self.weight -= 0.5
        print('-----------------------------------------')


class Goats(FourLegsAnimal):
    def give_milk(self):
        print("You have goat's milk")
        self.weight -= 0.3
        print('-----------------------------------------')


class Sheep(FourLegsAnimal):
    def give_wool(self):
        print("You have sheep's wool")
        self.weight -= 10
        print('-----------------------------------------')


class Pigs(FourLegsAnimal):
    def kill_pig(self):
        print("You have pig's meat")
        self.weight = 0
        print('-----------------------------------------')


class Ducks(TwoLegsAnimal):
    height = 30  # cm

    def kill_duck(self):
        print("You have duck's meat and feathers")
        self.weight = 0
        print('-----------------------------------------')


class Chickens(TwoLegsAnimal):
    def kill_chicken(self):
        print("You have chicken's meat and you can cook some chicken nuggets!")
        self.weight = 0
        print('-----------------------------------------')

    def make_egg(self):
        print("You have chicken's egg")
        self.weight -= 0.1
        print('-----------------------------------------')


class Geese(TwoLegsAnimal):
    weight = 15
    height = 20  # cm

    def save_rome(self):
        print("The geese have saved Rome!!!")
        self.animal_name = 'Great geese'
        print('-----------------------------------------')

    def give_feathers(self):
        print("You got some feathers and you can make a pen!")
        self.weight -= 0.1
        print('-----------------------------------------')


if __name__ == '__main__':
    x1 = Cows(100, 500, "Сено", "Буренка")
    x1.about_oneself()
    x1.give_milk()
    x1.about_oneself()

    y1 = Geese(40, 20, "трава", "ГуГу")
    y1.about_oneself()
    y1.give_feathers()
    y1.about_oneself()
    pass
