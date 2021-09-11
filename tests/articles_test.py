import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("techcrunch","TechCrunch","Connie Loizos","Tesla should say something","http://techcrunch.com/2021/09/10/tesla-should-say-something/","http://techcrunch.com/2021/09/10/tesla-should-say-something/","2021-09-11T05:37:56Z","Last weekend, a reader wrote to this editor, politely asking")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
        
        
    def test_init(self):
        self.assertEqual(self.new_article.id,"techcrunch")
        self.assertEqual(self.new_article.name,"TechCrunch")
        self.assertEqual(self.new_article.author,"Connie Loizos")
        self.assertEqual(self.new_article.title,"Tesla should say something")
        self.assertEqual(self.new_article.description,"Last weekend, a reader wrote ")
        self.assertEqual(self.new_article.url,"http://techcrunch.com/2021/09/10/tesla-should-say-something/")
        self.assertEqual(self.new_article.urlToImage,"https://techcrunch.com/wp-content/uploads/2019/03/Austin.jpg?w=600")
        self.assertEqual(self.new_article.publishedAt,"2021-09-11T05:37:56Z")
        self.assertEqual(self.new_article.content,"Last weekend, a reader wrote to this editor, politely asking")
if __name__ == '__main__':
    unittest.main()