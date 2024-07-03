from util import compare_objects
from constants import PI
import custom_module

class MyClass:
    def __init__(self, value):
        self.value = value

    def equals(self, other):
        return self.value == other.value


obj1 = MyClass(10)
obj2 = MyClass(10)
if obj1 == obj2:
    print("Objects are equal")


if obj1.equals(obj2):
    print("Objects are equal using equals method")