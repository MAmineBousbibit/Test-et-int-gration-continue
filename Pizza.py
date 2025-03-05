class Pizza:
    def __init__(self, nom: str, ingredients: list, prix: float, description: str, base: str):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.description = description
        self.base = base  # "tomate" ou "crème"

    def __repr__(self):
        return f"Pizza(nom={self.nom}, prix={self.prix}€, base={self.base}, ingredients={', '.join(self.ingredients)})"
