from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        wanted_product = [p for p in self.products if p.name == product_name]
        if wanted_product:
            return wanted_product[0]

    def remove(self, product_name):
        removed_product = self.find(product_name)
        if removed_product:
            self.products.remove(removed_product)

    def __repr__(self):
        result = '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
        return result

