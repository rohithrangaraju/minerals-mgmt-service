from mongoengine import Document, IntField, StringField, SequenceField, EmbeddedDocumentListField, FileField, \
    EmbeddedDocument, DictField, DateTimeField
import datetime


class ProductImage(EmbeddedDocument):
    image_name = StringField()
    image_description = StringField()
    image = FileField()


class Product(Document):
    product_id = SequenceField(primary_key=True)
    product_name = StringField()
    product_description = StringField()
    product_category = StringField(default="Minerals")
    product_image_gallery = EmbeddedDocumentListField(ProductImage)
    product_size_metrics = DictField(default={'min_size': 10, 'max_size': 100, 'metrics': 'mm'})
    product_created_timestamp = DateTimeField(default=datetime.datetime.utcnow())
