#!/usr/bin/env python

class foo():
    def __init__(self, bar=None):
        self.text = "Hello from foo!"
        self.bar = bar

    def speak(self):
        try:
            print(self.text)
            print(self.bar.text)
        except AttributeError as att:
            print("Printing failed due to {}".format(att))

class bar():
    def __init__(self):
        self.text = "Hello from bar!"

def main():
    object_bar = bar()
    object_foo = foo(object_bar)
    object_foo.speak()

if __name__ == "__main__":
    main()