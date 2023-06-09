from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    # this is an instance generated manually from the my_discount serializer
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

# use countless serializers to import into the views.py
class SecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
        ]

