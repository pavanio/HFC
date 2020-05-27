from django.test import TestCase

# Create your tests here.
from django.test import TestCase,Client
from django.urls import reverse

# Create your tests here.
class BlogTest(TestCase):
    def test_should_respond_only_for_TFC_prod(self):
        client = Client(HTTP_HOST="www.forchange.in")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)
    def test_should_respond_only_for_TFC_staging(self):
        client = Client(HTTP_HOST="www.forchange.in")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)
    def test_should_not_respond_for_HFC_prod(self):
        client = Client(HTTP_HOST="www.hack-for-change.org")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)

    def test_should_not_respond_for_HFC_staging(self):
        client = Client(HTTP_HOST="www.staging.hack-for-change.org")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)
