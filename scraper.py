from core.selper import Selper
from core.waiter import Waiter
from core.app import App


class Scraper():
    
    def init(self):
        selper = Selper()
        driver = selper.driver()
        driver.get('https://google.com/')

        # this is how JS is executed
        selper.exec_javascript("""
        // you can execute JS this way
        function test() {
                console.log("tested");
        }
        test();
        """)
        
        print("this is before 5 seconds...")
        
        # wait for 5 seconds
        wtr = Waiter()
        wtr.wait(driver=driver, timeout=5)
        
        print("this is after 5 seconds...")
        
        # do your other stuffs here
        
# simple usage example
sc = Scraper()
sc.init()