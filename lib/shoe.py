#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = None
        self.size = size

    def get_brand(self):
        return self._brand
    def set_brand(self, new_brand):
        self._brand = new_brand

    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")

    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    