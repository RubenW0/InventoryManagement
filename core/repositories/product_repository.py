from core.models import Product

class ProductRepository:
    def get_all(self):
        return Product.objects.all()

    def get_by_id(self, product_id):
        return Product.objects.get(id=product_id)

    def create(self, name, price, stock):
        product = {"name": name, "price": price, "stock": stock}
        self.data.append(product)
        return product
