from django.test import SimpleTestCase
from django.urls import reverse, resolve


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(
            self.response, "<h1>Welcome to the Book Store. This is our homepage</h1>"
        )

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This is not on the page")

    def test_home_page_url_resolves_home_page_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, "home_page")
