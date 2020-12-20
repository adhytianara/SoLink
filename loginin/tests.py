from django.test import TestCase,Client,LiveServerTestCase
from django.urls import resolve
from .views import *
from django.contrib.auth.models import User

# # Create your tests here.
# class Story9Test(TestCase):
#     def test_url_bisa_diakses(self):
#         response = Client().get('/story9/')
#         self.assertEqual(response.status_code,200)

#     def test_fungsi_view(self):
#         fungsi = resolve('/story9/')
#         self.assertEqual(fungsi.func,story9view)

#     def test_template(self):
#         response = self.client.get("/story9/")
#         self.assertTemplateUsed(response,"story9.html")

#     def test_isi_template(self):
#         response = self.client.get("/story9/")
#         isi_html = response.content.decode("utf8")
#         self.assertIn("Sign in",isi_html)
    
#     def test_url_login_ada(self):
#         response = self.client.get('/accounts/login/')
#         self.assertEqual(response.status_code,200)

#     def test_url_logout_ada(self):
#         response = self.client.get('/accounts/logout/')
#         self.assertEqual(response.status_code,302)

#     def test_using_signup_view(self):
#         response = resolve('/story9/signup/')
#         self.assertEqual(response.func,signup)

#     def test_using_login_template(self):
#         response = self.client.get('/accounts/login/')
#         self.assertTemplateUsed(response,'registration/login.html')

#     def test_using_signup_template(self):
#         response = self.client.get('/story9/signup/')
#         self.assertTemplateUsed(response,'registration/signup.html')
    
#     def test_signup(self):
#         data = {'username':'ajiinisti', 'password1':'wijaya123', 'password2':'wijaya123'}
#         response = self.client.post('/story9/signup/', data)
#         count = User.objects.all().count()

#         self.assertEqual(count,1)
#         self.assertEqual(response.status_code,302)
#         self.assertRedirects(expected_url='/accounts/login/',response=response)

#     def test_user_authenticated(self):
#         data = {'username':'ajiinisti', 'password1':'wijaya123', 'password2':'wijaya123'}
#         response = self.client.post('/story9/signup/', data)

#         data = {'username':'ajiinisti', 'password':'wijaya123'}
#         response = self.client.post('/accounts/login/',data)
#         self.assertIn('_auth_user_id', self.client.session)



