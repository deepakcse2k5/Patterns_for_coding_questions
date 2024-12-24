contact_dict = {"1":["abc@gmail.com","abc@hotmail.com"],
"2": ["abc@yahoo.com"],
"3": ["abc@hotmail.com","abc@yahoo.com"],
"4":["xyz@gmail.com","ghi@yahoo.in"],
"5":["xyz@gmail.com"],
"6":["ghi@hotmail.com"]}
from collections import defaultdict

def merge_contact_list(contact_dict):
    parent = {}
    result = defaultdict(list)

    # union find disjoin sets
    def find(x):
        if parent[x]!=x:
            parent[x] = find(parent[x]
   

