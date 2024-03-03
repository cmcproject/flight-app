"""
Tests for the flight API
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# from rest_framework import status
from rest_framework.test import APIClient

TEAM_URL = reverse("flight:sensor-data")


def create_user(email="user@example.com", password="pass123"):
    """Create and return user"""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicFlightApiTests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        pass


class PrivateFlightApiTests(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_get_data(self):
        pass
