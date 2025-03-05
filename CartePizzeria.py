
from CartePizzeriaException import CartePizzeriaException

from Pizza import Pizza


class CartePizzeria:
  
    def __init__(self):
        self.pizzas = {}

    def is_empty(self) -> bool:
        
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
       
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        if pizza.nom in self.pizzas:  # Utiliser `nom` au lieu de `name`
            raise CartePizzeriaException(f"La pizza '{pizza.nom}' existe déjà sur la carte.")
        self.pizzas[pizza.nom] = pizza


    def remove_pizza(self, nom: str):
        if nom not in self.pizzas:
            raise CartePizzeriaException(f"La pizza '{nom}' n'existe pas sur la carte.")
        del self.pizzas[nom]


    def __repr__(self):
        if self.is_empty():
            return "La carte de la pizzeria est vide."
        return "\n".join(str(pizza) for pizza in self.pizzas.values())
