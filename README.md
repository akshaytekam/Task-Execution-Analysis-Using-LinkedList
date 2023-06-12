# Task-Execution-Analysis-Using-LinkedList

project title: Task execution analysis

Task are schedule for execution and relavant data needs to be stored and analyse further.
we have data for each task that includes a task ID, start time, and end time.

once the data is available and stored in linked list, we will perform analysis based on the data points
that are stored in linked list.

project structure:-

(src)
  - linkedList.py
  - aggregate.py

likedlist.py file will consist of implementation related to the jobs that are stored in a linked list format.  this will have a class name linkedList that will contain insert, update , and delete operation in linked list.

this file will also include the structure of the node that needs to be created in order to store details of each task or node.

In the aggregate file  we will have implementation related to various analysis that will be perform on the saved task. This will have the implementation related to finding the min, max, and avg of the stored value.


config.py:
	This file contains pre-define data points that can be used directly to create the nodes and setup the linked list.

Main.py:
  This file will call all the methods  that will initiate the linked list creation process.
and also call the methods related to the task.

The linkedlist.py should contain 3 function inside class, 
  1. insert_node()
      - this method supposed to insert the node in linked list.
	you can design this function to insert the data either at end or beginning of linked list.
  2. print_link_list()
	- this method will print the linked list by traversing each node in the linked list.
	this should print the task ID atlest for each node. 
  3. print_list_reverse()
	- implement this method to print the node information in reverse order.
	not reversing linked list just print the data in revered order.
 

aggregate.py:

   This contains functions
   1. minimum_time_task()
 	- this aims at fetching the minimum time task from the given linked list.
	if we have two or more nodes satifying this condition then return the task ID of the node that 	is inserted towards the end of linked list.
    2. maximun_time_task()
	- same as above.
   3. average_time_task()
	- this method aims at fetching the average time of the task from the given liked list.


