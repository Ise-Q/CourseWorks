import sys
print(sys.executable)
import numpy as np
import pandas as pd

# init rng
rng = np.random.default_rng(42)

# Define method to build balanced BST from sorted list

class Node:
    def __init__(self, val, index):
        self.value = val
        self.index = index # index from sorted list
        self.LeftChild = None
        self.RightChild = None
    
    @classmethod
    def build_balanced_bst(cls, sorted_list : list, low: int , high: int):
        """
        Set midpoint m as root. Recursively buld tree by applying the method to the left and right of the root node.
        Define it as a classmethod, since you don't need a specific instance (so you don't need to use self).

        Parameters:
            low : index of the lowest value of the sorted list 
            high : index of highest value of the sorted list
        """
        if low > high: 
            return None
        m = (low + high) // 2
        root = cls(sorted_list[m], index = m)
        root.LeftChild = root.build_balanced_bst(sorted_list, low, m - 1)
        root.RightChild = root.build_balanced_bst(sorted_list, m+1, high)
        
        return root

    # Return index (recursive)
    def search_for_index(self, target):
        if self.value == target:
            return self.index
        elif self.value < target:
            return self.RightChild.search_for_index( target)
        else: 
            return self.LeftChild.search_for_index( target)
    
    # iterative (while loop)
    def search_for_index_iterative(self, target):
        current_node = self
        
        while current_node.value is not None:
            if current_node.value == target:
                return current_node.index
            elif current_node.value < target:
                current_node = current_node.RightChild
            elif current_node.value > target:
                current_node = current_node.LeftChild
        

## Check
A = [-10.0, -0.2, 0, 1,2,3,4,5.0,20,23,200,2000]
low = 0
high = len(A) - 1
bst = Node.build_balanced_bst(A, low, high)
print(bst)
print(bst.LeftChild.LeftChild.value) # Get minimum

# how to find specific val (return index)
target = rng.choice(A) # choose one from list
print(target)

print(A[bst.search_for_index(target)])

print(A[bst.search_for_index_iterative(target)])