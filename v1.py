__author__ = 'sam'
__version__ = 1.0

# written in python 2.7

class Container():

    'Create a container initialized from two iterables of equal length.'

    def __init__(self,list0,list1):
        self.list0=list0
        self.list1=list1
        self.items=dict(zip(list0,list1))

    def add(self,key,value):
        'add an item to the container'
        self.items[key]=value

    def remove(self,item):
        'remove item from the container'
        for k in dictionary.keys():
            if dictionary[k]==value:
                return k
        return None

    def __add__(self,other):
        'allow another container or dict object to be added to self.'
        dictionary=self.items
        other=other if type(other) == dict else other.items
        for k in other.keys():
            dictionary[k]=other[k]
        return dictionary

    def __radd__(self,other):
        'allow self to be added to another container'
        dictionary=self.items
        other=other if type(other) == dict else other.items
        for k in other.keys():
            dictionary[k]=other[k]
        return dictionary

    def __iadd__(self,other):
        'allows the += operator to be used.'
        self.items=self+other

    def __getitem__(self,key):
        'gets the item at specified index in self.items... allows for the key to be either the value or actual key'
        return self.items[key] if key in self.items.keys() else self.getKey(self.items,key)

    def __str__(self):
        'when print is used on self, the contents of self.items will print.'
        return str(self.items)

    def __repr__(self):
        'string form of self is the contents of self.items'
        return str(self.items)

    def __len__(self):
        'get the length of self.items'
        return len(self.items)
