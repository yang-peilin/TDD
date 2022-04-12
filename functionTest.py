from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
    # edith has heard about a cool new online to-do app. she goes to check out its homepage
        self.browser.get('http://localhost:8000')
    # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title), "Browser title was: " + self.browser.title
        self.fail('Finish the test!')


# she is invited to enter a to-do item straight away

# she types "buy peacock feaathers" into a text book (Edith's hobby is tying fly-fishing lures)


# when sha hits enter, the page updates, and now the page lists
# 1. buy peacock feathers as an item in a to-do list

# there is still a text box inviting her to add another item, she enters "Use peacock feathers to make a fly" (edith is very methodical)

# the page updates again, and now shows both items on her list

# edith wonders whether the site will remember her list. then she sees that the site has generated a unique url her -- there is some
# explanatory text to that effect

# she visites that url - her to-do list is still there

# satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()




