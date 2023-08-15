from typing import List

from project.client import Client
from project.meals.meal import Meal
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_TYPE_MEAL = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.VALID_TYPE_MEAL:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        except IndexError:
            client = Client(client_phone_number)

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        available_meal_names = [m.name for m in self.menu]
        for meal_name in meal_names_and_quantities.keys():
            if meal_name not in available_meal_names:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name][0]
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if m.name == meal_name][0]
            ordered_meal = FoodOrdersApp.VALID_TYPE_MEAL[meal.__class__.__name__](meal.name, meal.price, quantity)
            client.shopping_cart.append(ordered_meal)
            client.bill += ordered_meal.price * ordered_meal.quantity
            meal.quantity -= quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for client_meal in client.shopping_cart:
            app_meal = [m for m in self.menu if m.name == client_meal.name][0]
            app_meal.quantity += client_meal.quantity

        client.shopping_cart.clear()
        client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        client.shopping_cart.clear()
        total_paid_money = client.bill
        client.bill = 0.0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
