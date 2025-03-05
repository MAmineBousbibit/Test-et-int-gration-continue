import pytest
from unittest.mock import Mock
from CartePizzeria import CartePizzeria
from CartePizzeriaException import CartePizzeriaException

@pytest.fixture
def carte():
    return CartePizzeria()

@pytest.fixture
def pizza_mock():
    mock = Mock()
    mock.nom = "Margherita"  # Changer `name` en `nom`
    mock.ingredients = ["Tomate", "Mozzarella", "Basilic"]
    mock.prix = 8.5  # Changer `price` en `prix`
    return mock


def test_is_empty(carte):
    assert carte.is_empty() == True

def test_add_pizza(carte, pizza_mock):
    carte.add_pizza(pizza_mock)
    assert carte.is_empty() == False
    assert carte.nb_pizzas() == 1

def test_add_pizza_already_exists(carte, pizza_mock):
    carte.add_pizza(pizza_mock)
    with pytest.raises(CartePizzeriaException):
        carte.add_pizza(pizza_mock)

def test_remove_pizza(carte, pizza_mock):
    carte.add_pizza(pizza_mock)
    carte.remove_pizza(pizza_mock.nom)  # Utiliser `nom` au lieu de "Margherita"
    assert carte.is_empty() == True


def test_remove_pizza_not_found(carte):
    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("Inexistante")

def test_nb_pizzas(carte, pizza_mock):
    assert carte.nb_pizzas() == 0
    carte.add_pizza(pizza_mock)
    assert carte.nb_pizzas() == 1
