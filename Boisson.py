class Boisson:
    def __init__(self, nom: str, prix: float, alcool: bool):
        self.nom = nom
        self.prix = prix
        self.alcool = alcool

    def __repr__(self):
        alcool_str = "avec alcool" if self.alcool else "sans alcool"
        return f"Boisson(nom={self.nom}, prix={self.prix}€, {alcool_str})"

