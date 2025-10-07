import json
import traceback

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from core.services.product_service import ProductService

service = ProductService()

@csrf_exempt
def product_list(request):
    try:
        products = service.list_products()
        data = [
            {"id": p.id, "name": p.name, "price": float(p.price), "stock": p.stock}
            for p in products
        ]
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e), "trace": traceback.format_exc()}, status=500)

@csrf_exempt
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

@csrf_exempt
def product_update(request, product_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            product = service.update_product(
                product_id=product_id,
                name=data.get('name'),
                price=data.get('price'),
                stock=data.get('stock')
            )
            if product:
                return JsonResponse({
                    "id": product.id,
                    "name": product.name,
                    "price": float(product.price),
                    "stock": product.stock
                })
            else:
                return HttpResponseBadRequest("Product not found")
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")
    return HttpResponseNotAllowed(["PUT"])


@csrf_exempt
def product_delete(request, product_id):
    if request.method == "DELETE":
        success = service.delete_product(product_id)
        if success:
            return JsonResponse({"status": "deleted"})
        else:
            return HttpResponseBadRequest("Product not found")
    return HttpResponseNotAllowed(["DELETE"])