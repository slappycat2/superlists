from django.http import HttpRequest
from django.test import TestCase

from lists.views import home_page

# Create your tests here.

# class SmokeTest(TestCase):
# 
#     def test_maths(self):
#         self.assertEqual(1+1, 3)
#
class HomePageTest(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()

        response = home_page(request)

# Once the with open works, you can delete the previous tests...but BE CAREFUL!
#         self.assertTrue(response.content.startswith(b'<html>'))
#         self.assertIn(b'<title>To-Do Lists</title>', response.content)
# #        self.assertTrue(response.content.endswith(b'</html>'))
#         self.assertTrue(response.content.strip().endswith(b'</html>'))

        with open('lists/templates/home.html') as f:
            expected_content = f.read()

        # decode() so newlines are understood 2with the byte (b) read
        self.assertEqual(response.content.decode(), expected_content)

