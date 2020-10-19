from Commands_Box.urls import Enter_the_categories

class Search:
    def __init__(self):
        self.categories = Enter_the_categories()
        self.list_category = []
    def lista(self):
        for category in self.categories:
            self.list_category.append(category)
        print(self.list_category)
        return self.list_category
    def seach(self, input):
        while True:
            index = self.list_category.index(input)
            print(input)