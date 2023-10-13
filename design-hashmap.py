class MyHashMap:

    def __init__(self):
        self.lst = [Linked() for _ in range(1007)] 

    def put(self, key: int, value: int) -> None:
        val = key % 1007
        prev = temp = self.lst[val]
        while temp:
            if temp.key == key:
                temp.val = value
            prev = temp
            temp = temp.next
        prev.next = Linked(key, value)    

    def get(self, key: int) -> int:
        temp = self.lst[key % 1007]
        while temp:
            if temp.key == key:
                return temp.val
            temp = temp.next

        return -1        

        

    def remove(self, key: int) -> None:
        prev = temp = self.lst[key % 1007]
        temp = temp.next
        
        while temp:
            if temp.key == key:
                print(temp.next)
                temp.val = -1
                return
            prev = temp    
            temp = temp.next
        


class Linked:
    def __init__(self, key = -1, val = 0, next = None):
        self.key = key
        self.val = val
        self.next = next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)