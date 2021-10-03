import time


class Waiter():
    """
    This class is named really stupidly. But all in all this class keeps the runtime busy.
    Will keep looping for specified time. But the operation isn't costly because it uses sleep
    to save CPU cycles.

    But this class does more than just wait for certain time. It takes in the XPath 
    and checks if the element is available in DOM. Will exit faster if the element is available ( as soon as it is available ).
    Or else it will just timeout.

    This is really handy while waiting for some dynamic elements to load. Just create something similar if this class
    is whack. :D 
    """

    def __init__(self):
        pass

    def wait(self, driver, xpath=None, timeout=10):
        """
        Checks whether a page element is loaded in the browser.
        """

        if xpath == '' or xpath == None:
            print("waiting for %s seconds before continuing ..." %
                  (timeout), flush=True)

        is_loaded = False

        stop_at = time.time() + timeout

        while True:

            if time.time() > stop_at:
                print(
                    "waiting for the page to load has exceeded %s seconds ..." % (timeout), flush=True)
                break

            time.sleep(.1)
            # print("time is %s" % (time.time()), flush=True)

            # check if the timeout has exceeded

            try:
                driver.find_element_by_xpath(xpath=xpath)
                is_loaded = True
            except:
                is_loaded = False

            # break loop if the element has loaded
            if is_loaded:
                break

        # check again
        try:
            driver.find_element_by_xpath(xpath=xpath)
            is_loaded = True
            print("the element { %s } is ## FOUND ## in the dom ..." % (
                xpath), flush=True)
        except:
            is_loaded = False

            if xpath != '' and xpath != None:
                print(
                    "the element { %s } is ## NOT FOUND ## in the dom ..." % (xpath), flush=True)

        return is_loaded
