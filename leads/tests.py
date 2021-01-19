from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class LandingPageTest(TestCase):

    def test_status_code(self):
        # TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        print(response.content)

        # def test_template_name(self):
        # # TODO some sort of test
        # self.client_class
        # pass