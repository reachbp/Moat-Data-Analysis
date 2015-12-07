
__author__ = 'bharathipriyaa'

class MyHashMap(object):
    def __init__(self):
        self.arr = []
        for i in range(0,100):
            self.arr.append([])
    def get(self,key):
        l=self.arr[hash(key)%100]
        for elem in l:
            if(elem.key==key):
                return elem.value
        raise Exception("Key not found")
    def remove(self,key):
        l=self.arr[hash(key)%100]
        for elem in l:
            if(elem.key==key):
                l.remove(elem)
                return
        raise Exception("Key not found")
    def put(self,key,value):
        l=self.arr[hash(key)%100]
        elem_not_present=True
        for elem in l:
            if(elem.key==key):
                elem.value=value
                elem_not_present=False
                break
        if(elem_not_present):
            l.append(MyEntry(key,value))

class MyEntry(object):
    def __init__(self,k,v):
        self.key=k
        self.value=v


