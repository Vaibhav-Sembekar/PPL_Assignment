#Memory Allocation Simulator
#Problem Statement:
#Create a memory allocation simulator using linked lists to manage free and allocated
#memory blocks and demonstrate basic concepts of memory management.

#Linked List Implementation
class Node:
    def __init__(self, data=None, is_allocated=False, next=None):
        self.data = data
        self.is_allocated=False
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,False,None)
        else:
            cur = self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=Node(data,False,None)
    
    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        i=1
        while itr is not None:
            print('Block',i,':',itr.data,'KB')
            i+=1
            itr = itr.next

#Input Memory Partitions
par = int(input('Enter the number of memory partitions : '))
mem = LinkedList()
total_mem=0
print('Enter the blocks of memory (in KB):-')
for i in range(0,par):
    data = int(input('Block '+str(i+1)+': '))
    mem.insert_at_end(data)
    total_mem+=data

mem.print_list()
print('Total memory:',total_mem,'KB')

#Input Process List
process_list = []
no_of_processes = int(input('Enter the number of processes: '))
total_memory_requirement = 0
print('Enter the memory requirement of each process (in KB):-')
for i in range(0,no_of_processes):
    temp = int(input('Process '+str(i+1)+': '))
    process_list.append(temp)
    total_memory_requirement += temp

#Display Process List
count=0
for i in process_list:
    print('Process',count+1,':',i,'KB')
    count+=1
print('Total amount of memory required:',total_memory_requirement,'KB')

#First Fit Algorithm
print('First Fit: ')
for i in range(no_of_processes):
    current = mem.head
    is_allocated=False
    for j in range(par):
        if process_list[i]<=(current.data) and not current.is_allocated:
            print('Process',i+1,'allocated to','Block',j+1)
            current.is_allocated=True
            current=current.next
            is_allocated=True
            break
        else:
            current=current.next
    if not is_allocated:
        print('Process',i+1,'is not allocated')