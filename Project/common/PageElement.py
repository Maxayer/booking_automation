class PageElement:

    def __init__(self, name, locator_type, locator, is_checked):
        self.name = name
        self.locator_type = locator_type
        self.locator = locator
        self.is_checked = is_checked

    def get_locator_type(self):
        return self.locator_type

    def get_locator(self):
        return self.locator
