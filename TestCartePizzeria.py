import unittest
from unittest.mock import Mock
from Boisson import Boisson
from CartePizzeria import CartePizzeria 
from CartePizzeriaException import CartePizzeriaException
from Dessert import Dessert
from Pizza import Pizza

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()
        
        self.pizza_mock = Mock(spec=Pizza)
        self.pizza_mock.nom = "Margherita"
        self.pizza_mock.ingredients = ["Tomate", "Mozzarella", "Basilic"]
        self.pizza_mock.prix = 8.5
        self.pizza_mock.description = "Une pizza italienne classique."
        self.pizza_mock.base = "tomate"
        
        self.boisson_mock = Mock(spec=Boisson)
        self.boisson_mock.nom = "Coca-Cola"
        self.boisson_mock.prix = 2.5
        self.boisson_mock.alcool = False
        
        self.dessert_mock = Mock(spec=Dessert)
        self.dessert_mock.nom = "Tiramisu"
        self.dessert_mock.prix = 5.0
        self.dessert_mock.ingredients = ["Café", "Mascarpone", "Biscuit"]
        self.dessert_mock.fait_maison = True
    
    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())
    
    def test_add_pizza(self):
        self.carte.add(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)
    
    def test_add_pizza_already_exists(self):
        self.carte.add(self.pizza_mock)
        with self.assertRaises(CartePizzeriaException):
            self.carte.add(self.pizza_mock)
    
    def test_remove_pizza(self):
        self.carte.add(self.pizza_mock)
        self.carte.remove("Margherita")
        self.assertTrue(self.carte.is_empty())
    
    def test_remove_pizza_not_found(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove("Inexistante")
    
    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)
        self.carte.add(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)
    
    def test_add_boisson(self):
        self.carte.add(self.boisson_mock)
        self.assertEqual(self.carte.nb_drinks(), 1)
    
    def test_add_dessert(self):
        self.carte.add(self.dessert_mock)
        self.assertEqual(self.carte.nb_desserts(), 1)
    
    def test_remove_boisson(self):
        self.carte.add(self.boisson_mock)
        self.carte.remove("Coca-Cola")
        self.assertEqual(self.carte.nb_drinks(), 0)
    
    def test_remove_dessert(self):
        self.carte.add(self.dessert_mock)
        self.carte.remove("Tiramisu")
        self.assertEqual(self.carte.nb_desserts(), 0)

if __name__ == "__main__":
    unittest.main()
