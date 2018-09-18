import serpy
from serpy import Field


class ProductImage(serpy.Serializer):
    name = Field(attr="image_name")
    description = Field(attr="image_description")
    image = Field()


class Product(serpy.Serializer):
    product_id = Field()
    product_name = Field()
    product_description = Field()
    product_category = Field()
    product_image_gallery = ProductImage(many=True)
    product_size_metrics = Field()
    product_created_timestamp = Field()
