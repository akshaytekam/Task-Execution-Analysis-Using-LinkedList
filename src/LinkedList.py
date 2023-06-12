class Node:
    #Node class constructor
    def __init__(self,id,starttime,endtime):
        self.next=None
        self.id=id
        self.starttime=starttime
        self.endtime=endtime
    
    @property
    def task_id(self):
        return self.id
    @property
    def start_time(self):
        return self.starttime
    @property
    def end_time(self):
        return self.endtime    
    

class LinkedList:
    #LinkedList class constructor
    def __init__(self):
        self.head = None

    def list_head(self):
        return self.head

    def insert_node(self, node:Node, insert_at_start=0):
        count=1
        current = self.head
        if insert_at_start == 1:
            node.next = self.head
            self.head = node
        while current:
            if count+1 == insert_at_start:
                node.next =current.next
                current.next = node
                return
            else:
                count+=1
                current = current.next

    #printing list nodes
    def print_linked_list(self):
        temp=self.head
        while(temp):
            print(temp.id, temp.starttime, temp.endtime)
            temp=temp.next
    
    #nodes in reverse order
    def print_list_reverse(self,head):
        temp=head
        if temp==None:
            return
        self.print_list_reverse(temp.next)
        print(temp.id, temp.starttime, temp.endtime)