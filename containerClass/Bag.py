

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

        

    def size(self):
        return len(self.items)


#linked list implementation
class linked_list_Bag:
    def __init__(self):
        self.head = None
        self.prev_node = None
        self.next_node = None

        self.size = 0

    def __iter__(self):
        current = self.head 

        while current.next_node != None:
            yield current
            current = current.next_node

    def exists(self,item):
        for i in self:
            if i == item:
                return True
        return False
    
    def insert(self,item):
        if not self.exists(item)
            item = linked_list_Bag()
            last_item = self.head
            for node in self:
                last_item = node
            last_item.next_node = item.head #got last item now it's the new prev_node
            item.prev_node = last_item
            self.size += 1
            return True
        return False

    def delete(self,item):
        for i in self:
            if item == i:
                prevItem = i.prev_node
                nextItem = i.next_node

                prevItem.next_node =  nextItem
                nextItem.prev_node = prevItem
                self.size -= 1
                #now nothing points to the item we "deleted"
                return True
        return False

    def retrieve(self,item):
        for record in self:
            if i == record:
                return record
        return None

    def size(self):
        return self.size

