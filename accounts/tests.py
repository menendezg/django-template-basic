from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import SignupPageView
from .forms import CustomUserCreationForm


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="gabe@gmail.com", password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "gabe@gmail.com")
        self.assertTrue(user.check_password("testpass123"))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="superuser",
            email="superadmin@gmail.com",
            password="superpass123",
        )
        self.assertEqual(superuser.username, "superuser")
        self.assertEqual(superuser.email, "superadmin@gmail.com")
        self.assertTrue(superuser.check_password("superpass123"))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)


class CustomUserTests(TestCase): ...


class SignUpPageTests(TestCase):  # new
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):  # new
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):  # new
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
