from src.LinkedList import Node, LinkedList
import csv

data_file="data.csv"
def create_linked_list():

    list_task = LinkedList()

    with open(data_file, newline='') as file:
        reader = csv.DictReader(file)
        for item in reader:
            # if 'Task ID' not in item or 'Start Time' not in item or 'End Time' not in item:
            #     print("Missing required columns in the CSV file.")
            #     return None
            start_time = (item['Start Time'])
            end_time  = (item['End Time'])
            node  = Node(item['Task ID'], start_time, end_time)
            list_task.insert_node(node, 1)
            
    return list_task