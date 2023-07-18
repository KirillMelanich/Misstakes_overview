from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import LiteraryFormat

LITERARY_FORMATS_URLS = reverse("catalog:literary-format-list")


class PublicLiteraryFormatTests(TestCase):
    def test_login_required(self):
        res = self.client.get(LITERARY_FORMATS_URLS)

        self.assertNotEquals(res.status_code, 200)


class PrivateLiteraryFormatTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password"
        )
        self.client.force_login(self.user)

    def test_retrieve_literary_formats(self):
        LiteraryFormat.objects.create(name="poetry")
        LiteraryFormat.objects.create(name="drama")

        response = self.client.get(LITERARY_FORMATS_URLS)
        literary_formats = LiteraryFormat.objects.all()

        self.assertEqual(
            list(response.context["literary_format_list"]),
            list(literary_formats)
        )
        self.assertTemplateUsed(response, "catalog/literary_format_list.html")


# class PrivateAuthorTests(TestCase):
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create_user(
#             "test",
#             "password123"
#         )
#         self.client.force_login(self.user)
#
#     def test_create_author(self):
#         form_data = {
#             "username": "new_user",
#             "password1": "user123test",
#             "password2": "user123test",
#             "first_name": "Test first",
#             "last_name": "Test last",
#             "pseudonym": "Test Pseudonym"
#         }
#         self.client.post(reverse("catalog:author-create"), data=form_data)
#         new_user = get_user_model().objects.get(username=form_data["username"])
#
#         self.assertEqual(new_user.first_name, form_data['first_name'])
#         self.assertEqual(new_user.last_name, form_data['last_name'])
#         self.assertEqual(new_user.pseudonym, form_data['pseudonym'])