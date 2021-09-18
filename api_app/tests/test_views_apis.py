from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api_app.models import CartItem


class TestShoppingCartAPI(APITestCase):

    def setUp(self):
        self.cart_items = reverse('cart-items')

    def test_add_item_success(self):
        url = self.cart_items
        payload = {
            "product_name": "Heba's product",
            "product_price": "1000",
            "product_quantity": 7
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content, b'{"message": "New item added to Cart with id: 1"}')
        self.assertEqual(CartItem.objects.get().product_price, float(1000))
        self.assertEqual(CartItem.objects.get().product_name, "Heba's product")
        self.assertEqual(CartItem.objects.get().product_quantity, int(7))
        

    def test_get_items_success(self):
        url = self.cart_items

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'{"items": [], "count": 0}')


    def test_delete_method(self):
        url = self.cart_items
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
