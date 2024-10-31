"""
LCT implementation.
All the operations are O(log n) in amortized time.
Based on https://courses.csail.mit.edu/6.851/spring12/scribe/L19.pdf.
"""


class LinkCutTree:
    def __init__(self, n):
        pass

    def make_tree(self):
        """
        Returns a new vertex in a singleton tree.
        This operation allows us to add elements and later manipulate them.
        """
        pass

    def link(self, v, w):
        """
        Makes vertex v a new child of vertex w, i.e. adds an edge (v, w).
        In order for the representation to remain valid this operation assumes that v is the root of its tree and that v and w are nodes of distinct trees.
        """
        pass

    def cut(self, v):
        """
        Deletes the edge between vertex v and its parent, parent(v), where v is not the root.
        """
        pass

    def find_root(self, v):
        """
        Returns the root of the tree that vertex v is a node of.
        This operation is interesting because path to root can be very long.
        The operation can be used to determine if two nodes u and v are connected.
        """
        pass

    def path_aggregate(self, v):
        """
        Returns an aggregate, such as max/min/sum, of the weights of the edges on the path from the root of the tree to node v.
        It is also possible to augment the data structure to return many kind of statistics about the path.
        """
        pass
