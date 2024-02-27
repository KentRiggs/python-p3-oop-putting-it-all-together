#!/usr/bin/env python3

class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, pages):
        if isinstance(pages, int):
            self._page_count = pages
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        