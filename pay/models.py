from django.db import models

"""
  This contains all models of this POS (Point of Sale) system. and it is used to create the database schema.

  The models are:
  - Product
  - Order
  - OrderItem
  - Payment
  - Customer
  - Transaction

  Each model is a class that inherits from the django.db.models.Model class.
  Each class represents a table in the database.
  Each attribute in the class represents a column in the table.

  The class attributes are the fields of the table.
  The class methods are used to perform operations on the table.

  The class Meta is used to define the table name and other properties of the table.
"""

class Product(models.Model):
    """
    · Product model

    This model represents the product table in the database.
    It contains the following fields:
    - name: the name of the product
    - price: the price of the product
    - stock: the stock of the product

    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    · Order model

    This model represents the order table in the database.
    It contains the following fields:
    - customer: the customer who placed the order
    - total: the total amount of the order
    - created_at: the date and time the order was created

    """
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    """
    · OrderItem model

    This model represents the order_item table in the database.
    It contains the following fields:
    - order: the order to which the item belongs
    - product: the product in the order
    - quantity: the quantity of the product
    - price: the price of the product
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_items'

    def __str__(self):
        return f'OrderItem {self.id}'


class Payment(models.Model):
    """
    · Payment model

    This model represents the payment table in the database.
    It contains the following fields:
    - order: the order for which the payment is made
    - amount: the amount of the payment
    - method: the payment method used
    - created_at: the date and time the payment was made

    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return f'Payment {self.id}'


class Customer(models.Model):
    """
    · Customer model

    This model represents the customer table in the database.
    It contains the following fields:
    - name: the name of the customer
    - email: the email of the customer
    - phone: the phone number of the customer
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """
    · Transaction model

    This model represents the transaction table in the database.
    It contains the following fields:
    - order: the order for which the transaction is made
    - payment: the payment for the transaction
    - created_at: the date and time the transaction was made
    
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f'Transaction {self.id}'


