class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
            
    #insert a list of values
    def insert_values(self,dlist): 
            for data in dlist:
                self.insert_at_end(data)
            return
        
    
    def show_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return(count)

    #inserting a given value at a given index  
    def insert_at_index(self, index, data):
        if(index < 0 or index >= self.show_length()):
            raise Exception("Invalid index")
            
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if (count == index-1):
                temp = itr.next
                itr.next = Node(data, temp)
                break
            
            itr=itr.next
            count += 1
    
    # replace value at a given index       
    def replace(self, index, data):
        if(index < 0 or index >= self.show_length()):
            raise Exception("Invalid index")
            
        if index == 0:
            self.head.data = data
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if (count==index):
                itr.data = data
                break
            
            itr=itr.next
            count += 1
            
        
        
    #delete a node at given index
    def delete_at(self, index):
        if(index < 0 or index >= self.show_length()):
            raise Exception("Invalid index")
            
        if index == 0:
            self.head= self.head.next 
            return
        
        count = 0 
        itr = self.head
        while itr:
            if (count == index-1):
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if(itr.data == data_after):
                old = itr.next
                temp = Node(data_to_insert,old)
                itr.next = temp
                break
            
            itr = itr.next
            
                  

    def remove_by_value(self, data):
        itr = self.head
        index = 0
        while itr:
                if (itr.data == data):
                    self.delete_at(index)
                    return
            
                itr = itr.next
                index += 1
        raise Exception("Data not found in the list")
        
                
            
        
                
    def show(self):
        if self.head is None:
            print("linked list is empty")
            return
            
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'--->'
            itr = itr.next
        print(llstr)
              
        

if __name__ == '__main__':
    a=LinkedList()
