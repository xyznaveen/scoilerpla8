class App():
    
    """
    This is just a regular class that has all the related configurations.
    """
    
    __configuration = {
        # the driver path for the chrome
        'driver_path': '/usr/local/bin/chromedriver',
        # can be either [ dev or prod ]
        'env': 'dev',
        # user agent is chrome on MacOS
        'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    
    @staticmethod
    def get(name):
        return App.__configuration[name]
    
    @staticmethod
    def is_prod():
        return App.__configuration['env'] == "prod"
    
    @staticmethod
    def is_dev():
        return not App.is_prod()
    
    @staticmethod
    def user_agent():
        return App.get('ua')
    
    @staticmethod
    def driver_path():
        return App.get('driver_path')
    
    @staticmethod
    def environment():
        return App.get('env')
    
    