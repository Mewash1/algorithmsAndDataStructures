from file_comprehension import turn_file_into_list
from bubble_sort import bubble_sort

with open("pan-tadeusz.txt", 'r', encoding='utf-8') as file:
   new_list = turn_file_into_list(file)
   print(bubble_sort(new_list[0:1000]))