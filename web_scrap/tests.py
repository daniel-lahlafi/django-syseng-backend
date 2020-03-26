from django.test import TestCase
from .models import Toolkit
from .web_scrapper import getToolkit

class WebScrapTestCase(TestCase):
    def setUp(self):
        Toolkit.objects.create(name = "testing", url="https://www.rcgp.org.uk/clinical-and-research/resources/toolkits/acute-kidney-injury-toolkit.aspx")
    def test_setting_webscrap(self):
        """Able to scrape the data for the toolkit"""
        testing = Toolkit.objects.get(name="testing")
        self.assertEqual(testing.url, 'https://www.rcgp.org.uk/clinical-and-research/resources/toolkits/acute-kidney-injury-toolkit.aspx')
        
        content = getToolkit(testing.url)
        testing.content = content
        self.assertNotEqual(testing.content, '')
