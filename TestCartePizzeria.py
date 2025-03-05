import unittest
from unittest.mock import Mock
from CartePizzeria import CartePizzeria  # Import correct de la classe
from CartePizzeriaException import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()  # Utilisation correcte de la classe
        self.pizza_mock = Mock()
        self.pizza_mock.name = "Margherita"
        self.pizza_mock.ingredients = ["Tomate", "Mozzarella", "Basilic"]
        self.pizza_mock.price = 8.5
    
    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())
    
    def test_add_pizza(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)
    
    def test_add_pizza_already_exists(self):
        self.carte.add_pizza(self.pizza_mock)
        with self.assertRaises(CartePizzeriaException):
            self.carte.add_pizza(self.pizza_mock)
    
    def test_remove_pizza(self):
        self.carte.add_pizza(self.pizza_mock)
        self.carte.remove_pizza("Margherita")
        self.assertTrue(self.carte.is_empty())
    
    def test_remove_pizza_not_found(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Inexistante")
    
    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

if __name__ == "__main__":
    unittest.main()
