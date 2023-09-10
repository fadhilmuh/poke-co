from django.test import TestCase
from django.test import Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        client = Client()
        response = client.get('/main/') 
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        client = Client()
        response = client.get('/main/') 
        self.assertTemplateUsed(response, 'main.html')

    def test_template_rendering(self):
        client = Client()
        response = client.get('/main/')
        self.assertEqual(response.status_code, 200)

        # Cek konten template
        self.assertContains(response, "Welcome to Poké.co")
        self.assertContains(response, "Player Information")
        self.assertContains(response, "Featured Character")
        self.assertContains(response, "Name:")
        self.assertContains(response, "Class:")

        # Cek gambar
        self.assertInHTML("<img alt=\"Pikachu\" src=\"/static/main/assets/Angry-Pikachu-Transparent.png\">", response.content.decode())

        # Cek konten footer
        self.assertContains(response, "Fadhil Muhammad (2206083464). Pemrograman Berbasis Platform Gasal 23/24.")