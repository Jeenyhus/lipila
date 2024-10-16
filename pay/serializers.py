from rest_framework import serializers
from .models import Product, Order, OrderItem, Payment, Customer, Transaction

class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer

    This serializer is used to serialize the Product model.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']

class OrderSerializer(serializers.ModelSerializer):
    """
    · Order Serializer

    This serializer is used to serialize the Order model.
    """
    class Meta:
        model = Order
        fields = ['id', 'customer', 'total', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Order Item Serializer

    This serializer is used to serialize the OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

class PaymentSerializer(serializers.ModelSerializer):
    """
    Payment Serializer

    This serializer is used to serialize the Payment model.
    """
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'method', 'created_at']

class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer Serializer

    This serializer is used to serialize the Customer model.
    """
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']

class TransactionSerializer(serializers.ModelSerializer):
    """
    Transaction Serializer

    This serializer is used to serialize the Transaction model.
    """
    class Meta:
        model = Transaction
        fields = ['id', 'order', 'payment', 'created_at']
