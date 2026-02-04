from django.test import TestCase, Client
from django.contrib.auth.models import User
from catalogue.models import Artist
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status

class ArtistAPITestCase(TestCase):
    def setUp(self):
        """Initialisation des tests"""
        self.client = APIClient()
        
        # Création d'un utilisateur pour l'authentification
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Création de quelques artistes pour les tests
        self.artist1 = Artist.objects.create(
            firstname='John',
            lastname='Doe'
        )
        self.artist2 = Artist.objects.create(
            firstname='Jane',
            lastname='Smith'
        )
        
        # Authentification du client
        self.client.force_authenticate(user=self.user)

    def test_get_all_artists(self):
        """Test de la récupération de tous les artistes"""
        response = self.client.get(reverse('catalogue:artist-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_artist(self):
        """Test de la récupération d'un seul artiste"""
        response = self.client.get(
            reverse('catalogue:artist-detail', kwargs={'pk': self.artist1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['firstname'], 'John')

    def test_create_artist(self):
        """Test de la création d'un nouvel artiste"""
        data = {
            'firstname': 'Bob',
            'lastname': 'Johnson'
        }
        response = self.client.post(reverse('catalogue:artist-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 3)

    def test_update_artist(self):
        """Test de la mise à jour d'un artiste"""
        data = {
            'firstname': 'John',
            'lastname': 'Updated Doe'
        }
        response = self.client.put(
            reverse('catalogue:artist-detail', kwargs={'pk': self.artist1.pk}),
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist1.refresh_from_db()
        self.assertEqual(self.artist1.lastname, 'Updated Doe')

    def test_delete_artist(self):
        """Test de la suppression d'un artiste"""
        response = self.client.delete(
            reverse('catalogue:artist-detail', kwargs={'pk': self.artist1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 1)