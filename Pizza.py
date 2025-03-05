class Pizza:
    def __init__(self, nom: str, prix: float, description: str, ingredients: list, base: str):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.ingredients = ingredients
        self.base = base  # "tomate" ou "crème"

    def __repr__(self):
        return f"Pizza(nom={self.nom}, prix={self.prix}€, base={self.base}, ingredients={', '.join(self.ingredients)})"
