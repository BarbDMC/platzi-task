from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    #detecta que la app exista

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    #detecta que la app este en modo testing

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('dashboard'))
    #verifica que el index redirige a hello

    def test_dashboard_get(self):
        response = self.client.get(url_for('dashboard'))

        self.assert200(response)
    #verifica que hello devuelva un 200 cuando se hace un GET

    def test_dashboard_post(self):
        response = self.client.post(url_for('dashboard'))

        self.assertTrue(response.status_code,405)

#verifica que cuando se haga un POST se redirija a Index

    def test_auth_blueprint_exist(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))


