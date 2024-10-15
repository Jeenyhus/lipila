from django.test import TestCase
from .models import Customer

# Create your tests here.

class CustomerTestCase(TestCase):
  def setUp(self):
    self.john = Customer.objects.create(name='John Doe', email='john@example.com', phone='1234567890')
    self.jane = Customer.objects.create(name='Jane Doe', email='jane@example.com', phone='0987654321')

  def test_customer_name(self):
    john = Customer.objects.get(name='John Doe')
    jane = Customer.objects.get(name='Jane Doe')
    self.assertEqual(john.name, 'John Doe')
    self.assertEqual(jane.name, 'Jane Doe')

  def test_customer_email(self):
    john = Customer.objects.get(email=self.john.email)
    jane = Customer.objects.get(email=self.jane.email)

    self.assertEqual(john.email, 'john@example.com')
    self.assertEqual(jane.email, 'jane@example.com')

  def test_customer_phone(self):
    john = Customer.objects.get(phone=self.john.phone)
    jane = Customer.objects.get(phone=self.jane.phone)

    self.assertEqual(john.phone, '1234567890')
    self.assertEqual(jane.phone, '0987654321')
