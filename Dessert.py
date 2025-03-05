class Dessert:
    def __init__(self, nom: str, prix: float, ingredients: list, fait_maison: bool):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.fait_maison = fait_maison

    def __repr__(self):
        fait_maison_str = "fait maison" if self.fait_maison else "industriel"
        return f"Dessert(nom={self.nom}, prix={self.prix}€, {fait_maison_str}, ingredients={', '.join(self.ingredients)})"

