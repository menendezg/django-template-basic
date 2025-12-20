from django.test import TestCase
from django.contrib.auth import get_user_model


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
