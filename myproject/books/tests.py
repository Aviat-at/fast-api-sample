from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create sample books
        Book.objects.create(title="Book A", author="Author A")
        Book.objects.create(title="Book B", author="Author B")

    def test_list_all_books(self):
        response = self.client.get('/api/books/')  # endpoint

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # we created 2 books

        # Optional: Check content
        self.assertEqual(response.data[0]['title'], "Book A")
        self.assertEqual(response.data[1]['title'], "Book B")
