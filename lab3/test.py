class Node:
  def __init__(self):
    self.length = 0
    self.array = []
    self.next = None
  
class UnrolledLinkedList:
  def __init__(self, capacity):
    self.capacity = capacity #maximum capacity of an array in node
    self.head = None
    self.tail = None
  
  #this method inserts the given value in the list
  def insert(self, value):
    if self.head == None: #unrolled linked is empty
      self.head = Node()
      self.head.array.append(value) #add the value
      self.head.length += 1
      self.tail = self.head
    elif self.tail.length + 1 <= self.capacity: #current node's capacity is not full
      self.tail.array.append(value) #add the given value
      self.tail.length += 1 
    else: #current node's capacity is full
      new_node = Node() #create a new node
      #move final half of elements from the current node to the new node
      half_length = self.tail.length//2
      new_node.array.extend(self.tail.array[half_length:])
      new_node.array.append(value) #add the given value to the new node
      new_node.length = len(new_node.array) #set the length of the new node's array
      self.tail.length = half_length #update the length of the current node's array
      self.tail.next = new_node #make current node next pointer refer to the new node
      self.tail = new_node #update the tail
  
  #prints all the elements of the unrolled linked list
  def traversal(self):
    temp = self.head
    while temp:
      for i in range(0, temp.length):
        print(temp.array[i], end="\t")
      print()
      temp = temp.next
  #This method removes the first appearance of the given value
  def delete(self, value):
    #find the given value and delete it 
    temp = self.head
    while temp:
      for i in range(0, temp.length):
        if temp.array[i] == value:
          temp.array.pop(i) #remove the given value from the array
          temp.array.append(None)
          temp.length -= 1 #decrease the length
          #if the current node's length is less than 50% then move elements from next node's array to the current one
          while temp.length < (self.capacity//2) and temp.next:
            temp.array[temp.length] = temp.next.array.pop(0) 
            temp.length +=1
            temp.next.length -= 1
          
          #if the next node's length is less than 50%  then merge the two halves
          if temp.next and temp.next.length < (self.capacity//2) : 
            temp.array[temp.length:temp.length+temp.next.length] = temp.next.array[:temp.next.length]
            temp.length += temp.next.length
            deleted_node = temp.next
            temp.next = temp.next.next
            del deleted_node
          return 
      temp = temp.next
    
    raise ValueError(f'Value {value} does not exist in the list')
ull = UnrolledLinkedList(4) #maximum capacity is 4
#insert values 
ull.insert(1)
ull.insert(2)
ull.insert(3)
ull.insert(4)
ull.insert(5)
ull.insert(6)
ull.insert(7)
ull.insert(8)
print("Display all items")
ull.traversal()
ull.delete(3) 
print("Display all items after deleting value 3")
ull.traversal()
ull.delete(5) 
print("Display all items after deleting value 5")
ull.traversal()
ull.delete(6) 
print("Display all items after deleting value 6")
ull.traversal()