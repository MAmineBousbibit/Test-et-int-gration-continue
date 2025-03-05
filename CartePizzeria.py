from CartePizzeriaException import CartePizzeriaException

from Dessert import Dessert
from Pizza import Pizza
from Boisson import Boisson
class CartePizzeria:
    def __init__(self):
        self.elements = {}

    def is_empty(self) -> bool:
        return len(self.elements) == 0

    def nb_pizzas(self) -> int:
        return sum(isinstance(e, Pizza) for e in self.elements.values())
    
    def nb_drinks(self) -> int:
        return sum(isinstance(e, Boisson) for e in self.elements.values())
    
    def nb_desserts(self) -> int:
        return sum(isinstance(e, Dessert) for e in self.elements.values())

    def add(self, element):
        if element.nom in self.elements:
            raise CartePizzeriaException(f"L'élément '{element.nom}' existe déjà sur la carte.")
        if isinstance(element, Pizza):
            if any(isinstance(e, Pizza) and e.ingredients == element.ingredients and e.base == element.base for e in self.elements.values()):
                raise CartePizzeriaException("Une pizza avec les mêmes ingrédients et la même base existe déjà.")
        self.elements[element.nom] = element

    def remove(self, name: str):
        if name not in self.elements:
            raise CartePizzeriaException(f"L'élément '{name}' n'existe pas sur la carte.")
        del self.elements[name]


    def __repr__(self):
        if self.is_empty():
            return "La carte de la pizzeria est vide."
        return "\n".join(str(e) for e in self.elements.values())
