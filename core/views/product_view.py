import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from core.services.product_service import ProductService

service = ProductService()

def product_list(request):
    products = service.list_products()
    data = [{"id": p.id, "name": p.name, "price": float(p.price)} for p in products]
    return JsonResponse(data, safe=False)

@csrf_exempt  # nodig om POST via Postman te testen zonder CSRF token
def product_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = service.create_product(
                name=data['name'],
                price=data['price'],
                stock=data['stock']
            )
            return JsonResponse({"id": product.id, "name": product.name, "price": float(product.price)})
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")
    return None