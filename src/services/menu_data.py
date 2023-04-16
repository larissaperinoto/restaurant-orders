from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.increase_menu()

    def increase_menu(self):
        list = self.read_file(self.path)

        for line in list[1:]:

            dish_name = line[0]
            price = float(line[1])
            ingredient = Ingredient(line[2])
            amount = int(line[3])

            dish = Dish(dish_name, price)

            if dish in self.dishes:

                for d in self.dishes:
                    if d == dish:
                        d.add_ingredient_dependency(ingredient, amount)
            else:
                dish.add_ingredient_dependency(ingredient, amount)
                self.dishes.add(dish)

    def read_file(self, path: str):
        with open(path, encoding="utf-8") as file:
            file = csv.reader(file, delimiter=",", quotechar='"')
            return list(file)
