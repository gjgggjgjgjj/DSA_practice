

class Bag:
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

