from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                # now we can park our value
                self.left = BSTNode(value)
            else:
                # no parking on this level do down one level
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):  ###### This is recursive!!
        # start at root compare target against self
        if target == self.value:
            return True
        if target < self.value:
            if not self.left: ## can't go left - there isn't a Node there
                return False ## -- means does not contain.
            return self.left.contains(target)
        else:
            if not self.right: ## can't go right - there isn't a Node there
                return False ## -- means does not contain
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self): #recursive 
        if not self.right:
            return self.value
        return self.right.get_max()

        ###### Iterative solution for get_max ##########
        '''
    def iterative_get_max(self):
        current_max = self.value

        current = self

        while current is not None:
            if current.value > current_max:
                current_max = current.value

            current = current.right
        return current_max
        '''
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on root
        fn(self.value)
        # pass to left child
        if self.left:
            self.left.for_each(fn)
        #pass to the right child
        if self.right:
            self.right.for_each(fn)    

        ###### Iterative solution for for_each ##########    
        '''
    def iterative_for_each(self, fn): # depth first
        stack = []

        stack.append(self) # add root node

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            fn(current.value)
        '''
    
        '''
    def breadth_first_for_each(self, fn): # breadth first
        queue = deque()

        queue.append(self) # add root node

        while len(queue) > 0:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            fn(current.value)
        '''

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
        
    def bft_print(self, node):
        # use breadth_first_for_each where fn = print(current.value)
        queue = deque()
        queue.append(self) # add root node
        while len(queue) > 0:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            print(current.value)
        
    def dft_print(self, node):
        # use iterative_for_each where fn = print(current.value)
        stack = []
        stack.append(self) # add root node
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node == None:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
        