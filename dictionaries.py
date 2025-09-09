from typing import TypedDict


class Product(TypedDict):
    name: str
    price: float
    quantity: int


product_catalog: dict[str, Product] = {
    "SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50},
    "SKU456": {"name": "Gadget B", "price": 34.95, "quantity": 25},
    "SKU789": {"name": "Gizmo C", "price": 9.99, "quantity": 100},
}

sku_to_find = "SKU123"

searched_product: Product | None = product_catalog[sku_to_find]
print(f"The price of {searched_product['name']} is ${searched_product['price']}")
