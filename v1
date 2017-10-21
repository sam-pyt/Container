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
        self.items[key]=value

    def remove(self,item):
        'remove item from the container'
        for k in dictionary.keys():
            if dictionary[k]==value:
                return k
        return None

    def __add__(self,other):
        dictionary=self.items
        for k,v in other.keys(),other.values():
            dictionary[k]=v
        return dictionary

    def __radd__(self,other):
        dictionary=self.items
        for k,v in other.keys(),other.values():
            dictionary[k]=v
        return dictionary

    def __iadd__(self,other):
        self.items=self+other

    def __getitem__(self,key):
        return self.items[key] if key in self.items.keys() else self.getKey(self.items,key)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)
