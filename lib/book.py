#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title
    
    title = property(get_title, set_title)
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if (type(page_count) is int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


# class Book:
#     def __init__(self, title, page_count):
#         self.title = title
#         self.page_count = page_count

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#         self._title = value

#     @property
#     def page_count(self):
#         return self._page_count

#     @page_count.setter
#     def page_count(self, value):
#         if isinstance(value, int):
#             self._page_count = value
#         else:
#             print("page_count must be an integer")

#     def turn_page(self):
#         print("Flipping the page...wow, you read fast!")


    
        