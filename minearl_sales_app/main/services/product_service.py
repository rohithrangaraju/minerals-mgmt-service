from ..models.product import Product, ProductImage
from collections import defaultdict

PRODUCT_ATTRIBUTES = ('product_name', 'product_description', 'product_category', 'product_size_metrics')


def create_product(json_dict=defaultdict()):
    product = Product()
    # product.product_id = json_dict.get('product_id')
    for key in json_dict:
        if key in PRODUCT_ATTRIBUTES:
            setattr(product, key, json_dict.get(key))
    product.save()


def get_product():
    query_data = Product.objects.all()
    return ""
