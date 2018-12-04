#Jesus Hurtado, Lab 5 - option A, CS 2302 Data Structures, Fall 2018
#Program to implement a min-heap and then Heap sort by reading content from a file

class Heap:     #Class for constructing the min-heap
    def __init__(self):     #Initializing an empty array
        self.heap_array=[]
    
    #Inserts an element into heap and instantly makes it a min-heap implementation    
    def insert(self,k):
        
        self.heap_array.append(k)
        
        #Uses a percolate up implementation for the min-heap
        index = len(self.heap_array)-1
        
        while index > 0:
            parent = (index-1)//2
            
            #if parent is less than zero means that it has reached the top element(the smallest element)
            if parent < 0:
                return
            #If parent is smaller than child, then do nothing
            if self.heap_array[parent] <= self.heap_array[index]:
                return
            #If parent is bigger than child,then proceed to swap
            else: 
                if self.heap_array[parent] > self.heap_array[index]:
                    temp = self.heap_array[parent]
                    self.heap_array[parent] = self.heap_array[index]
                    self.heap_array[index]= temp
                    index = parent   #index now is set equal to parent, meaning is going up
           
    def min_heap_list(self):    #Returns min-heap list
        return self.heap_array
            
    def print_minheap(self):    #Prints min-heap list (and current modifications)
        #for i in self.heap_array:
        print(self.heap_array)
        
    def extract_min(self):  #Extracts the smallest element
        
        if self.is_empty(): #If empty means there is nothing
            return None
        
        min_element = self.heap_array[0]   #Smallest element is the first element in list (min-heap)
        #new_heap=[]
        
        #for i in range(1,len(self.heap_array),1):
         #   new_heap.append(self.heap_array[i])
        #self.heap_array = new_heap
        
        #print(self.heap_array)
        
        return min_element 
    
    def is_empty(self):     #Checks if heap is empty
        return len(self.heap_array) == 0
    
    def min_heap_percolate_down(self,node_index, heap_list, list_size):
        child_index = 2 * node_index + 1
        value = heap_list[node_index]

        while child_index < list_size:
            # Find the minimum among the node and all the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < list_size:
                if heap_list[i + child_index] < min_value:
                    min_value = heap_list[i + child_index]
                    min_index = i + child_index
                i = i + 1
                                    
            if min_value == value:
                return

            # Swap heap_list[node_index] and heap_list[min_index]
            temp = heap_list[node_index]
            heap_list[node_index] = heap_list[min_index]
            heap_list[min_index] = temp
        
            node_index = min_index
            child_index = 2 * node_index + 1


    # Sorts the list of numbers using the heap sort algorithm
    def heap_sort(self,numbers):
        # Heapify numbers list
        i = len(numbers) // 2 - 1
        while i >= 0:
            self.min_heap_percolate_down(i, numbers, len(numbers))
            i = i - 1
        #print("This is the min-heapfied list:")
        #print(numbers)
        i = len(numbers) - 1
        while i > 0:
            # Swap numbers[0] and numbers[i]
            temp = numbers[0]
            numbers[0] = numbers[i]
            numbers[i] = temp

            self.min_heap_percolate_down(0, numbers, i)
            i = i - 1
        
            
def get_numbers(mh):    #Method is used to retrieve content and insert it into min-heap
    f = open('numbers.txt')
    numbers = f.read()
    list1 = numbers.split(',')
    print("This is the original list retrieved from the file:")
    #print(list1)
    nums = [int(i) for i in list1]   
    print(nums)     #Prints the original list
    print()
    for i in nums:
        mh.insert(i)    #Inserts each of the elements of original list into min-heap
    return nums
        
def main():   #Main method
    print()
    minheap = Heap()    #Creates a reference to the Heap class
    get_numbers(minheap)    #Calls the method used to retrieve content
    print("This is the min-heaped list:")
    minheap.print_minheap()   #Prints last update to the min-heap implementation
    print()
    num_list = minheap.min_heap_list()   #Gets the list to do heap sort
    
    minheap.heap_sort(num_list) #Method to heap sort the min-heap list
    print("This is the sorted min-heap list:")
    minheap.print_minheap()    #Prints the sorted list
        
main()