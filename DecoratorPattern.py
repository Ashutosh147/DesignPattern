from abc import ABC, abstractmethod

# Component - Pizza Interface
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Component - Plain Pizza
class PlainPizza(Pizza):
    def get_description(self) -> str:
        return "Plain pizza"

    def get_cost(self) -> float:
        return 5.00  # Base cost for plain pizza

# Decorator - Abstract Topping Class
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Decorators
class OlivesDecorator(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.50  # Olives cost 1.50

class CheeseDecorator(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Extra Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 2.00  # Extra cheese costs 2.00

class MushroomsDecorator(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.75  # Mushrooms cost 1.75

# Client code
if __name__ == "__main__":
    # Order a plain pizza
    pizza = PlainPizza()
    print(f"{pizza.get_description()} | Cost: ${pizza.get_cost()}")

    # Add olives and mushrooms
    pizza_with_olives = OlivesDecorator(pizza)
    pizza_with_mushrooms = MushroomsDecorator(pizza_with_olives)
    print(f"{pizza_with_mushrooms.get_description()} | Cost: ${pizza_with_mushrooms.get_cost()}")

    # Add extra cheese
    pizza_with_cheese = CheeseDecorator(pizza_with_mushrooms)
    print(f"{pizza_with_cheese.get_description()} | Cost: ${pizza_with_cheese.get_cost()}")
