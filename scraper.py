from core.selper import Selper
from core.waiter import Waiter
from core.app import App


class Scraper():
    
    def init(self):
        selper = Selper()
        driver = selper.driver()
        driver.get('https://google.com/')
        
        print("this is b4 5 seconds...")
        
        # wait for 5 seconds
        wtr = Waiter()
        wtr.wait(driver=driver, timeout=5)
        
        print("this is after 5 seconds...")
        
        # do your other stuffs here
        
# simple usage example
sc = Scraper()
sc.init()