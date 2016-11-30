
from unittest import TestCase

from mercadopago import configuration

class TestConfiguration(TestCase):
    def setClientIDandSecret(self):
        configuration.client_id = "client_id"
        configuration.client_secret = "client_secret"
        self.assertEquals(configuration.client_id, "client_id")
        self.assertEquals(configuration.client_secret, "client_secret")

    def setAccessToken(self):
        configuration.access_token = "access_token"
        self.assertEquals(configuration.access_token, "access_token")

    def setAppID(self):
        configuration.app_id = "app_id"
        self.assertEquals(configuration.app_id, "app_id")