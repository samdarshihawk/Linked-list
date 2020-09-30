#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Doublelinked:
    def __init__(self):
        self.head = None

    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        
        node = Node(data, self.head, None)
        self.head.prev=node
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        
        pos = self.get_lastnode()
        node = Node(data, None, pos)
        pos.next = node
        
    
    def insert_values(self, values):
        self.head = None
        for data in values:
            self.insert_at_end(data)
            
            
     #inserting a given value at a given index  
    def insert_at_index(self, index, data):
        if(index < 0 or index >= self.get_length()):
            raise Exception("Invalid index")
            
        if index == 0:
            self.insert_at_begining(data)
            return
       
        count = 0
        itr = self.head
        while itr:
            if (count == index-1):
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
    
    #delete a node at given index
    def delete_at(self, index):
        if(index < 0 or index >= self.get_length()):
            raise Exception("Invalid index")
            
        if index == 0:
            self.head= self.head.next 
            self.head.prev = None
            return
        
        count = 0 
        itr = self.head
        while itr:
            if (count == index):
                itr.prev.next = itr.next
                break
                
            itr = itr.next
            count += 1
            
        
        
    # returns the memory location of last element in a list
    def get_lastnode(self):
        if self.head is None:
            raise Exception("Empty list")
        
        itr = self.head
        while itr:
            if itr.next is None:
                last = itr
                break
            itr = itr.next
        return(last)
    
    # return the length of the list 
    def get_length(self):
        count = 0
        if self.head is None:
            return(0)
        
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return(count)
    
        
    # to print the list in forward or backward depending upon the order
    def show(self, order = 'f'):
        if self.head is None:
            return("double linked list is empty")
        
        if (order == 'f'):
            itr = self.head
            dlstr = ''
            while itr:
                dlstr += str(itr.data)+'--->'
                itr = itr.next
            print(dlstr)
        
        elif(order == 'r'):
            itr = self.get_lastnode()
            dlstr = ''
            while itr:
                dlstr += str(itr.data)+'--->'
                itr = itr.prev
            print(dlstr)
        
        else:
            raise Exception('Wrong Input!')
            
    
            
        
    
       


# In[21]:


ll = Doublelinked()
ll.insert_values(["banana","mango","grapes","orange"])


# In[22]:


ll.show('r')


# In[15]:


ll.delete_at(3)


# In[16]:


ll.show()


# In[17]:


ll.delete_at(1)


# In[18]:


ll.show()


# In[19]:


ll.delete_at(0)


# In[20]:


ll.show()


# In[ ]:




