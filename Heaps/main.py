class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up()

    def _bubble_up(self):
        #bubble up is a support method for insert. 
        curr = self.get_size()-1
        while curr > 1:
            parent = curr // 2
            if self.heap[curr] > self.heap[parent]:
                self._swap(curr, parent)
                curr = parent
            else:
                return 

    def _swap(self, id1, id2):
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]

    def get_size(self):
        return len(self.heap)    

    def balance_heap(self):
        size = self.get_size()
        for i in range(size-1, 1, -1):
            parent = i // 2
            if self.heap[i] > self.heap[parent]:
                self._swap(i, parent)

            
    def is_balanced(self):
        balanced = True
        size = self.get_size()
        try:
            for i in range(1, size // 2):
                if self.heap[i] < self.heap[i*2]:
                    balanced = False
                elif self.heap[i] < self.heap[i*2+1]:
                    balanced = False
        except IndexError:
            pass 
        return balanced
    
    def print_heap(self):
        print("*"*65)
        print(self.heap)
        print("*"*65)

    def remove(self):
        if self.get_size() == 1:
            return None 
        if self.get_size() == 2:
            return self.heap.pop()
        max_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._slide_down()
        return max_val
    
    def _slide_down(self):
        curr = 1 
        max = 1
        while True:
            left_idx = curr * 2
            right_idx = curr * 2 + 1
            if (left_idx < len(self.heap) and 
                self.heap[max] < self.heap[left_idx]):
                max = left_idx
            if (right_idx < len(self.heap) and 
                self.heap[max] < self.heap[right_idx]):
                max = right_idx
            if curr != max:
                self._swap(curr, max)
                curr = max 
            else:
                return 


class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, idx):
        
        min_idx = idx 
        size = len(self.heap)
        while True:
            left_child = self._left_child(idx)
            right_child = self._right_child(idx)
            if left_child < size and self.heap[left_child] < self.heap[min_idx]:
                min_idx = left_child
            if right_child < size and self.heap[right_child] < self.heap[min_idx]:
                min_idx = right_child
            if min_idx != idx :
                self._swap(idx, min_idx)
                idx = min_idx
            else:
                return 
    

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value
    

def find_kth_smallest(nums, k):
    size = len(nums)
    max_heap = MaxHeap() 
    for i in range(size):
        max_heap.insert(nums[i])
    itr = size - k 
    while itr > 0:
        min_val = max_heap.remove()
        itr -=1 
    return max_heap.remove()


def stream_max(nums):
    max_heap = MaxHeap()
    size = len(nums)
    ret_arr = []
    
    for i in range(size):
        max_heap.insert(nums[i])
        max_val = max_heap.remove()
        ret_arr.append(max_val)
        max_heap.insert(max_val)
    
    return ret_arr


