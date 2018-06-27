''' configaration file for various environments such as production or testing'''


class BaseConfig():
    '''parent class subclassed by all other environment objects'''
    DEBUG = False


class Development(BaseConfig):
    ''' development based configarations class'''
    DEBUG = True


class Test(BaseConfig):
    '''the class is used to run tests'''
    TESTING = True


class Production(BaseConfig):
    '''production based configarations class'''
    pass


CONFIGS = {
    'development': Development,
    'testing': Test,
    'production': Production
}
