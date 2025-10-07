from core.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, repo=None):
        self.repo = repo or ProductRepository()

    def list_products(self):
        return self.repo.get_all()

    def get_product(self, product_id):
        return self.repo.get_by_id(product_id)

    def create_product(self, name, price, stock):
        return self.repo.create(name=name, price=price, stock=stock)

    def update_product(self, product_id, name, price, stock):
        return self.repo.update(product_id, name=name, price=price, stock=stock)

    def delete_product(self, product_id):
        return self.repo.delete(product_id)
