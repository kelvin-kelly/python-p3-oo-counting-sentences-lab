#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value
    @property
    def value(self):
        self._value
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")           

    pass
    def is_sentence(self):
        if(self._value[-1] == "."):
            return True
        else:
            return False

    def is_question(self):
        if(self._value[-1] == "?"):
            return True 
        else:
            return False

    def is_exclamation(self):
        if(self._value[-1] == "!"):
            return True
        else:
            return False 

    def count_sentences(self):
        value = self.value
        for mark in ["!","?"]:
            value = value.replace(mark, ".")
        words = [i for i in value.split(".") if i]
        return len(words)   