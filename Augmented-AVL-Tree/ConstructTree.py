# A function that takes in a node object and adds it to the AVL Tree
# This function should have two sub-functions. One to find a location to add the current node and the other to correct for the imbalance within the tree, after the addition of the most recent node.
# The nodes are pointed to using the addresses returned when a new node is instantiated from within the module
def AddNode2Tree(tree,node):
    # If the size of the tree is zero, add the current node to the tree without the requirement to sort

