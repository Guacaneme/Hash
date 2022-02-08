class Node(object):
    def __init__(self, data = None, next = None , prev = None):
        self.data = data                          # fd + fa
        self.next = next                          # fd + fa
        self.prev = prev                          # fd + fa
                                                  # 3(fd + fa) = O(1)
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None                          #fd + fa
        self.tail = None                          #fd + fa
        self.count = 0                            #fd + fa
                                                  #3fd + fa = O(1)
    def add_last(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.count += 1
            return self
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.count += 1
            return self
        
    def is_empty(self):
        return self.head is None
    
    def lenght(self):
        return self.count

    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.count += 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.count += 1
            
    def iterar(self):
        actual = self.head
        while actual:
            dato = actual.data
            actual = actual.next
            yield dato
   
    def MakeEmpty(self):
        self.head = None
        self.tail = None
        self.count = None
    
    def FindElement(self,data):
        count = 0
        for d in self.iterar():
            count += 1
            if data == d:
                return count
        return False

    def RemoveElement(self, dato):
        if self.head is None:
            print("Lista vacia")
            return
        elif self.head.next is None:
            if self.head.data == dato:
                self.head = None
                self.count -= 1
                return
            else:
                print("Item no encontrado")
                return
        elif self.head.data == dato:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return
        n = self.head
        while n.next is not None:
            if n.data == dato:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
            self.count -= 1
        else:
            if n.data == dato:
                n.prev.next = None
                self.count -= 1
            else:
                print("Item no encontrado")
                
    def FindKth(self,ind):   
        if ind >= 0 and ind < self.lenght():
            act = self.head
            for i in range (ind):
                act = act.next
            return act.data
        else:
            raise Exception("Out of range")
     
    def PrintList (self):  
        self = self.head
        if self != None:
            if self.data != None:
                if type(self.data) == str or type(self.data) == int:
                    print("[",(self.data),end=' ')
                else:
                    print("[",end=' ')
                    self.data.PrintList()
    
                while self.next != None:
                    self = self.next
                    if type(self.data) == str or type(self.data) == int:
                        print(", "+ self.data, end = ' ')
                    else:
                        print(",",end='')
                        self.data.PrintList()
                
                print(']')
            else:
                print("Lista enlazada vacía")
        else:
            print("Lista enlazada vacía")
                      
    def insert_node(self, index, data):

        if index < 0 or index > self.lenght():
            print ("¡La posición del nodo está mal!")
            return False
        elif index == 0:
            self.add_first(data)
        elif index == self.lenght():
            self.add_last(data)
        else:
            node = Node(data)
            act = self.head
            prev = None
            count = 0

            while count < index:
                prev = act
                act = prev.next
                count += 1

            prev.next = node
            node.prev = prev

            node.next = act
            act.prev = node


