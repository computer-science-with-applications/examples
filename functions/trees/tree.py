#!/usr/bin/python


import textwrap
import sys


# This will try to import the necessary libraries
# to plot trees. These can be complicated to install
# so, if they are not available, we simply prevent
# the plotting function from working.
try:
    import matplotlib
    import matplotlib.pylab as plt
    import networkx as nx
    import pygraphviz
    import matplotlib
    import warnings
    warnings.simplefilter(action = "ignore", category = FutureWarning)
    warnings.simplefilter(action = "ignore", category = matplotlib.MatplotlibDeprecationWarning)
    CAN_PLOT=True
except ImportError as ie:
    CAN_PLOT=False    

class Tree(object):
    """
    A class representing a tree. More specifically,
    an instance of this class will represent either
    a null tree or a tree with a root node and some
    number of subtrees (which will, themselves,
    be instances of Tree)
    """
    
    def __init__(self, k=None, v=None):
        """
        Constructor.
        
        Creates either a null tree or a tree with
        a root node and no subtrees. The root node
        will have a key and value associated with it.
        
        Parameters
        - k, v: Key and value for the root node. If both
                of these are None, then a null tree is
                created.
        """
        
        assert (k is None and v is None) or (k is not None), \
               "Tree must either be null (key and value both None) " \
               "or it must have a key"
        
        self._k = k
        self._v = v 
        
        if k is None and v is None:
            self._children = None
        else:
            self._children = []
    
    
    def is_null(self):
        """
        Returns True if the tree is the null tree, False otherwise.
        """
        return (self._k is None and self._v is None and self._children is None)


    @property
    def key(self):
        """ Getter for key attribute"""
        return self._k
    
    
    @key.setter
    def key(self, k):
        """ Setter for key attribute"""
        
        if k is None:
            raise ValueError("Cannot set a key to None")
        self._k = k
        
        # If this was a null tree, then setting a key
        # means we're turning it into a tree with a root
        # node, so we have to set the children to be an
        # empty list
        if self._children is None:
            self._children = []


    @property
    def value(self):
        """ Getter for value attribute"""
        return self._v
    
    
    @value.setter
    def value(self, v):
        """ Setter for key attribute"""
                
        if self.is_null():
            raise ValueError("Cannot set a value on a null tree. Set its key first.")
                
        self._v = v


    def add_child(self, other_tree):
        """
        Adds an existing tree as a child of the tree.
        
        Parameter:
        - other_tree: Tree to add as a subtree
        """
        if not isinstance(other_tree, Tree):
            raise ValueError("Parameter to add_child must be a Tree object")
        
        self._children.append(other_tree)

    
    @property
    def children(self):
        """
        Generator property to iterate over the children,
        but preventing direct access to the list of children
        """
        
        for st in self._children:
            yield st

            
    @property
    def num_children(self):
        """Property that returns the number of children"""
        return len(self._children)


    def search(self, k):
        """
        Recursively searches the tree for a subtree with a root
        node with a given key. Note: if there are multiple
        such subtrees, it will return the first subtree it finds.
        
        Parameters:
        - k: The key to search for.
        
        Returns: The subtree with the given key or None if no such
        subtree exists.        
        """
        
        if self.is_null():
            return None
        elif self._k == k:
            return self
        else:
            for st in self._children:
                rv = st.search(k)
                
                if rv is not None:
                    return rv

        return None


    def __print_r(self, prefix, last, kformat, vformat, maxdepth):
        """
        Recursive method to print out the tree. Should not be
        called directly. See print() method for more details
        """
        if maxdepth is not None:
            if maxdepth == 0:
                return
            else:
                maxdepth -= 1    
    
        if len(prefix) > 0:
            if last:
                lprefix1 = prefix[:-3] + u"  └──"
            else:
                lprefix1 = prefix[:-3] + u"  ├──"
        else:
            lprefix1 = u""
    
        if len(prefix) > 0:
            lprefix2 = prefix[:-3] + u"  │"
        else:
            lprefix2 = u""
    
        if last:
            lprefix3 = lprefix2[:-1] + "   "
        else:
            lprefix3 = lprefix2 + "  "
    
        if not self.is_null():
            ltext = (kformat + ": " + vformat).format(self._k, self._v)
        else:
            ltext = "NULL"
    
        ltextlines = textwrap.wrap(ltext, 80, initial_indent=lprefix1, subsequent_indent=lprefix3)
    
        print(lprefix2)
        print(u"\n".join(ltextlines))
    
        if self.is_null():
            return
        else:
            for i, st in enumerate(self.children):
                if i == self.num_children - 1:
                    newprefix = prefix + u"   "
                    newlast = True
                else:
                    newprefix = prefix + u"  │"
                    newlast = False

                st.__print_r(newprefix, newlast, kformat, vformat, maxdepth)
    
    
    def print(self, kformat="{}", vformat="{}", maxdepth=None):
        """
        Prints out the tree.
        
        Parameters:
        - kformat, vformat: Format strings for the key and value
        - maxdepth: Maximum depth to print
        """
        
        self.__print_r(u"", False, kformat, vformat, maxdepth)


    def __plot_r(self, g, labels, parent_id):
        if self.is_null():
            return
    
        tree_id = id(self)
    
        g.add_node(tree_id)
        labels[tree_id] = self.key
    
        if parent_id is not None:
            g.add_edge(parent_id, tree_id)
    
        for st in self.children:
            st.__plot_r(g, labels, tree_id)    
    
    def plot(self):
        if not CAN_PLOT:
            print("Error: Cannot plot the tree. networkx and/or pypgraphviz are not installed")
            return
    
        G = nx.DiGraph()
        labels = {}
    
        self.__plot_r(G, labels, None)
    
        node_pos = nx.nx_pydot.pydot_layout(G, prog='dot')
    
        nx.draw(G, node_pos, arrows=False, with_labels=False)
        nx.draw_networkx_labels(G, node_pos, labels)
        plt.show()    




if __name__ == "__main__":
    t = Tree("ROOT", "foo")

    for i in range(5):
        st = Tree("CHILD %i" % (i+1), "foo")
        t.add_child(st)

    for st in t.children:
        for i in range(2):
            sst = Tree("GRANDCHILD %i" % (i+1), "foo")
            st.add_child(sst)

    t.print()
    


