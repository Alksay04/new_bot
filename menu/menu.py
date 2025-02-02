class Meal:
    def __init__(self, price: int, 
                 ingredients: list[str], 
                 name: str, description: str):
        self.price = price
        self.ingredients = ingredients
        self.name = name
        self.description = description

    def __str__(self):
        result = f'Название {self.name}\n'
        result += 'Ингредиенты:\n'
        for ingredient in self.ingredients:
            result += f'\t-{ingredient}\n'
        result += f'Цена: {self.price} рублей\n'
        result += f'Описание: {self.description}\n\n'
        return result

class MealContainer:
    def __init__(self, meals: list[Meal]):
        self.meals = meals

    def write_to_file(self):
        f = open('meals.txt', 'w+', encoding='utf-8')
        f.write('Блюда:\n')
        for meal in self.meals:
            f.write(str(meal))
        f.close()

kurica = Meal(price=4000, 
              ingredients=['просроченая курица'],
              name='Просроченая курица',
              description='Вкуснейщий курица')
potato = Meal(price=200, 
              ingredients=['картошка'],
              name='картошка',
              description='картошка.')
soup = Meal(price=1_000_000, 
              ingredients=['вода', 'соль', 'лук', 'перец'],
              name='Суп',
              description='нету')
meal_container = MealContainer(meals=[kurica, potato, soup])
meal_container.write_to_file()