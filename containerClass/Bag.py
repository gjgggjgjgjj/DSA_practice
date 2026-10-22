

class first_Bag:
    def __init__(self):
        self.items = []

    #must override the equal sign for this to work

    def __iter__(self):
        for item in self.items:
            yield item

    def insert(self,item):
        if not self.exists(item):    #only when equal to 
            self.items.append(item)
            return True
        #so they are duplicate/ is detected
        return False

    #if the objects are the same it'll delete one
    def delete(self,item):
        for i in range(len(self.items)):
            if self.items[i] == item: 
                self.items.pop(i)
                return True
        return False

    def exists(self,item):
        for i in self.items:
            if i == item:
                return True
        return False

    #needs to be an entire object
    def retrieve(self,item):
        for record in self.items:
            if record == item:
                return record
        return None

        

    def getSize(self):
        return len(self.items)


#linked list implementation
# class linked_list_Bag:
#     def __init__(self):
#         self.head = None
#         self.prev_node = None
#         self.next_node = None
#
#         self.size = int(0)
#
#     def __iter__(self):
#         if not self.head:
#             return
#         current = self.head
#         while current != None:
#             yield current
#             current = current.next_node
#
#     def exists(self,item):
#         for i in self:
#             if i == item:
#                 return True
#         return False
#
#     def insert(self,item):
#         if not self.exists(item):
#             #for first item
#             if self.size == 0:
#                 self.setHead(item)
#                 self.size += 1
#                 return True
#
#             bagObject = linked_list_Bag()
#             bagObject.setHead(item)
#
#             last_item = self.head
#             # print("TEST: here is self.head", last_item)
#             for node in self:
#                 if node != None:
#                     last_item = node
#             last_item.next_node = bagObject #got last item now it's the new prev_node
#             item.prev_node = last_item
#             self.size += 1
#             return True
#         return False
#
#     def delete(self,item):
#         for i in self:
#             if item == i:
#                 prevItem = i.prev_node
#                 nextItem = i.next_node
#
#                 prevItem.next_node =  nextItem
#                 nextItem.prev_node = prevItem
#                 self.size -= 1
#                 #now nothing points to the item we "deleted"
#                 return True
#         return False
#
#     def retrieve(self,item):
#         for record in self:
#             if item == record.head:
#                 # input("found one! press enter",record.head,item)
#                 return record
#         # print("couldn't find :", item)
#         # input("found one! press enter",record.head,item)
#         return None
#
#     #helper to set head of another class object put into it
#     def setHead(self,item):
#         self.head = item
#
#     def getSize(self):
#         return int(self.size)

class Node:
    """Node helper class for doubly linked list."""
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None


class linked_list_Bag:
    """Doubly Linked List Implementation of Bag ADT."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.item
            current = current.next

    def exists(self, item):
        for record in self:
            if record == item:
                return True
        return False

    def insert(self, item):
        if self.exists(item):
            return False

        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
        return True

    def delete(self, item):
        current = self.head

        while current is not None:
            if current.item == item:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def retrieve(self, item):
        for record in self:
            if record == item:
                return record
        return None

    def getSize(self):
        return self.size

