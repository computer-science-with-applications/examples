from tree import Tree


class BST(Tree):
    """
    A class that represent a Binary Search Tree.
    
    It is implemented in terms of the Tree class in
    the tree module.
    """
    
    def __init__(self):
        """Creates an empty BST"""
        Tree.__init__(self)
        
    @property
    def __left(self):
        """Returns the left sub-tree"""
        return self._children[0]

    @property
    def __right(self):
        """Returns the right sub-tree"""
        return self._children[1]

    def insert(self, k, v):
        """
        Inserts a key/value pair into the BST
        
        If the key does not already exist in the tree,
        it inserts a new node with that key and returns True.
        If the key already exists in the tree, it does nothing
        and returns False.
        """
        
        if self.is_null():
            # Set the key and value. This turns
            # the tree from a null tree to a tree
            # with a single node and no children.
            self.key = k
            self.value = v
            
            # Add the left and right subtrees (both
            # are initially null)
            self.add_child(BST())
            self.add_child(BST())

            return True
    
        if k < self.key:
            return self.__left.insert(k, v)
        elif k > self.key:
            return self.__right.insert(k, v)
        elif k == self.key:
            return False
    
    def find(self, k):
        """
        Finds a node with a given key in the tree.
        
        If such a key exists, it returns a tuple with
        True and the value associated with that key.
        
        Otherwise, it returns (False, None)
        """
        if self.is_null():
            return (False, None)
    
        if k < self.key:
            return self.__left.find(k)
        elif k > self.key:
            return self.__right.find(k)
        elif k == self.key:
            return (True, self.value)



    def __inorder_r(self, l):
        if not self.is_null():
            self.__left.__inorder_r(l)
            l.append(self.value)
            self.__right.__inorder_r(l)
    
    def values(self):
        """
        Returns the values in the tree in order
        (by doing an in-order traversal)
        """
        
        l = []
        self.__inorder_r(l)
        return l

def gen_example():
    t1 = BST()

    rv = t1.insert(50, "fifty")
    assert rv == True 

    rv = t1.insert(30, "thirty")
    assert rv == True 
    rv = t1.insert(5, "five")
    assert rv == True 
    rv = t1.insert(20, "twenty")
    assert rv == True 

    rv = t1.insert(90, "ninety")
    assert rv == True 
    rv = t1.insert(70, "seventy")
    assert rv == True 
    rv = t1.insert(110, "one hundred and ten")
    assert rv == True 

    rv = t1.insert(50, "fifty")
    assert rv == False
    rv = t1.insert(30, "thirty")
    assert rv == False
    rv = t1.insert(70, "seventy")
    assert rv == False
    return t1


if __name__ == "__main__":
    t1 = gen_example()

    print(t1.values())

    t1.print()

    assert t1.find(50) == (True, "fifty")
    assert t1.find(30) == (True, "thirty")
    assert t1.find(5) == (True, "five")
    assert t1.find(20) == (True, "twenty")
    assert t1.find(90) == (True, "ninety")
    assert t1.find(70) == (True, "seventy")
    assert t1.find(110) == (True, "one hundred and ten")

    assert t1.find(49) == (False, None)
    assert t1.find(51) == (False, None)

    assert t1.find(4) == (False, None)
    assert t1.find(6) == (False, None)





