from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class WikipediaTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        # Navigate to the Wikipedia homepage
        self.driver.get('https://www.wikipedia.org')

    #create 20 test cases for wikipedia.org
    def test_search(self):
        # Find the search box
        search = self.driver.find_element(By.ID, 'searchInput')
        # Enter the search query
        search.send_keys('Selenium')
        # Submit the query
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verify the search results
        assert "Selenium" in self.driver.title

    def test_search1(self):
        # Find the search box
        search = self.driver.find_element(By.ID, 'searchInput')
        # Enter the search query
        search.send_keys('Python')
        # Submit the query
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verify the search results
        assert "Python" in self.driver.title
    
    def test_search2(self):
        # Find the search box
        search = self.driver.find_element(By.ID, 'searchInput')
        # Enter the search query
        search.send_keys('Java')
        # Submit the query
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verify the search results
        assert "Java" in self.driver.title
    
    def test_search3(self):
        # Find the search box
        search = self.driver.find_element(By.ID, 'searchInput')
        # Enter the search query
        search.send_keys('C++')
        # Submit the query
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verify the search results
        assert "C++" in self.driver.title

    def test_search4(self):
        # Find the search box
        search = self.driver.find_element(By.ID, 'searchInput')
        # Enter the search query
        search.send_keys('C#')
        # Submit the query
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        # Verify the search results
        assert "C#" in self.driver.title
    
    #another test but not search
    def test_language(self):
        # Find the language button
        lang = self.driver.find_element(By.XPATH, '//*[@id="js-link-box-en"]')
        # Click the language button
        lang.click()
        time.sleep(5)
        # Verify the language change
        assert "English" in self.driver.title

    def test_language1(self):
        # Find the language button
        lang = self.driver.find_element(By.XPATH, '//*[@id="js-link-box-ru"]')
        # Click the language button
        lang.click()
        time.sleep(5)
        # Verify the language change
        assert "Russian" in self.driver.title

    def test_language2(self):
        # Find the language button
        lang = self.driver.find_element(By.XPATH, '//*[@id="js-link-box-es"]')
        # Click the language button
        lang.click()
        time.sleep(5)
        # Verify the language change
        assert "Spanish" in self.driver.title

    #another test but not search and langauge, create 12 test cases but different from above
    def test_random(self):
        # Find the random button
        random = self.driver.find_element(By.XPATH, '//*[@id="n-randompage"]')
        # Click the random button
        random.click()
        time.sleep(5)
        # Verify the random page
        assert "Random" in self.driver.title

    def test_random1(self):
        # Find the random button
        random = self.driver.find_element(By.XPATH, '//*[@id="n-portal"]')
        # Click the random button
        random.click()
        time.sleep(5)
        # Verify the random page
        assert "Portal" in self.driver.title

    def test_random2(self):
        # Find the random button
        random = self.driver.find_element(By.XPATH, '//*[@id="n-help"]')
        # Click the random button
        random.click()
        time.sleep(5)
        # Verify the random page
        assert "Help" in self.driver.title

    #something diffrent exmple test title of the page
    def test_title(self):
        # Verify the title of the page
        assert "Wikipedia" in self.driver.title

    #footer test
    def test_footer(self):
        # Find the footer
        footer = self.driver.find_element(By.XPATH, '//*[@id="footer"]')
        # Verify the footer
        assert "Privacy policy" in footer.text
    
    #another test not footer
    def test_header(self):
        # Find the header
        header = self.driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[3]/div[1]/div[1]')
        # Verify the header
        assert "The Free Encyclopedia" in header.text

    #another test not header

    def test_main(self):
        # Find the main content
        main = self.driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[3]/div[1]')
        # Verify the main content
        assert "The Free Encyclopedia" in main.text

    #another test not main

    def test_side(self):
        # Find the side content
        side = self.driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[3]/div[2]')
        # Verify the side content
        assert "The Free Encyclopedia" in side.text
    
    #another test not side

    def test_bottom(self):
        # Find the bottom content
        bottom = self.driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[3]/div[3]')
        # Verify the bottom content
        assert "The Free Encyclopedia" in bottom.text

    #test category menu
    def test_category(self):
        # Find the category menu
        category = self.driver.find_element(By.XPATH, '//*[@id="searchLanguage"]')
        # Verify the category menu
        assert "English" in category.text

    #another test not category

    def test_category1(self):
        # Find the category menu
        category = self.driver.find_element(By.XPATH, '//*[@id="searchLanguage"]')
        # Verify the category menu
        assert "Deutsch" in category.text

    #another test not category

    def test_category2(self):
        # Find the category menu
        category = self.driver.find_element(By.XPATH, '//*[@id="searchLanguage"]')
        # Verify the category menu
        assert "Español" in category.text

        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()