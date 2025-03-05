
import CartePizzeriaException
import Pizza


class CartePizzeria:
  
    def __init__(self):
        self.pizzas = {}

    def is_empty(self) -> bool:
        
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
       
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
       
        if pizza.name in self.pizzas:
            raise CartePizzeriaException(f"La pizza '{pizza.name}' existe déjà sur la carte.")
        self.pizzas[pizza.name] = pizza

    def remove_pizza(self, name: str):
       
        if name not in self.pizzas:
            raise CartePizzeriaException(f"La pizza '{name}' n'existe pas sur la carte.")
        del self.pizzas[name]

    def __repr__(self):
        if self.is_empty():
            return "La carte de la pizzeria est vide."
        return "\n".join(str(pizza) for pizza in self.pizzas.values())
