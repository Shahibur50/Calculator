"""
Copyright (c) Shahibur Rahaman.
Licensed under the MIT License.
"""


class Operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        add = self.x + self.y
        return add
    
    def subtraction(self):
        sub = self.x - self.y
        return sub

    def multiplication(self):
        mul = self.x * self.y
        return mul

    def division(self):
        div = self.x / self.y
        return div
