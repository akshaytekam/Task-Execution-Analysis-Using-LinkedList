from src.LinkedList import LinkedList
from itertools import count

class Aggregate:
    
    #Initializing object
    def __init__(self, llist:LinkedList):
        self.llist = llist
    
    #Search for max. time task
    def maximun_time_task(self):
        temp=self.llist.head
        x=temp.endtime-temp.starttime
        while(temp):
            y=temp.endtime-temp.starttime
            if y>x:
                x=y
                t_id=temp.id
            temp=temp.next
        return t_id, int(x)
    
    #Search for min. time task
    def minimum_time_task(self):
        temp=self.llist.head
        x=temp.endtime-temp.starttime
        while(temp):
            y=temp.endtime-temp.starttime
            if y<x:
                x=y
                t_id=temp.id
            temp=temp.next
        return t_id, int(x)
    
    #Search for avg. time task
    def average_time_task(self):
        temp=self.llist.head
        link_list_count=0
        total=0
        while(temp):
            x=temp.endtime-temp.starttime
            total=total+x
            link_list_count=link_list_count+1
            temp=temp.next
        average_time=total/link_list_count
        return int(average_time), total, link_list_count