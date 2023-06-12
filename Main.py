from Config import create_linked_list
from src.Aggregate import Aggregate
from src.LinkedList import LinkedList

if __name__ == "__main__":
    
    task_list = create_linked_list()
    task_print_list = LinkedList()

    task_print_list.print_linked_list()

    # task_print_list.print_list_reverse(task_print_list.list_head())

    agg_obj = Aggregate(task_list)
    
    #minimum execution time 
    min_task, min_task_time = agg_obj.minimum_time_task()
    print(f"Min Time is {min_task_time} and ID is {min_task}")
    
    #maximum time
    max_task, max_task_time = agg_obj.maximun_time_task()
    print(f"Max Time is {max_task_time} and ID is {max_task}")
    
    # avg time
    average, sum_task_times, no_of_nodes = agg_obj.average_time_task()
    print(f"Sum is : {sum_task_times} and Total is : {no_of_nodes}. and Average is : {average}")