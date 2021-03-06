import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Edith has heard about a cool new to-do list app. She goes
        # to checkout its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
                         'Enter a to-do item')
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox,send.keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox,send.keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows]
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox,send.keys("Use peacock feathers to make a fly")
        inputbox,send.keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        # fetch the table again (my comment)
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows]
        )
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test')

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
