# https://en.wikipedia.org/wiki/Heapsort

def heapsort(arr):
# change the inputted array to a heap
# create a storage array for sorted data
# use the insert method from Heap class to insert each element in the array
# we will need to then reverse the order of the array to make elements in ascending order

  heap = Heap() # creates an empty heap tree
  sorted = [0 for _ in range(len(arr))] #??
  # sorted = [0] * len(arr)  # creates an array that is an array of 0's

  for item in arr:
    heap.insert(item)

  for i in range(len(arr)):
    sorted[len(arr)-i-1] = heap.delete() 
  # we can do this because the delete method returns the deleted value
  # we are setting the sorted array items with the removed items from the heap

  return sorted

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2