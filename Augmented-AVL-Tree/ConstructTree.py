# A function that takes in a node object and adds it to the AVL Tree
# This function should have two sub-functions. One to find a location to add the current node and the other to correct for the imbalance within the tree, after the addition of the most recent node.
# The nodes are pointed to using the addresses returned when a new node is instantiated from within the module
import numpy as np

class Tree(object):
   
    def __init__(self,node):
        self.root = node
        self.height = 1
        self.leftMost = None
        self.rightMost = None

    def add_node(self,node):
        # Start from the root node
        currentNode = self.root
        # While the search has not reached the leaves, keep searching
        while True:
            # If the node to be added is larger than the current node
            if node > currentNode:
                # If the right-subtree of the current node is heavier than the left subtree
                if currentNode.rightC != None: 
                    # If the currentNode's right subtree is heavier than the left subtree, increment the height of the current node by one.
                    if currentNode.leftC == None:
                        currentNode.height += 1
                        currentNode = currentNode.rightC
                    elif currentNode.leftC.height <= currentNode.rightC.height:
                        currentNode.height += 1
                        currentNode = currentNode.rightC
                    else:
                        currentNode = currentNode.rightC

                else:
                    if currentNode.leftC == None:
                        currentNode.height += 1
                        currentNode.rightC = node
                        break
                    else:
                        currentNode.rightC = node
                        break
            else:
                if currentNode.leftC != None:
                    if currentNode.rightC == None:
                        currentNode.height += 1
                        currentNode = currentNode.leftC
                    elif currentNode.rightC.height <= currentNode.leftC.height:
                        currentNode.height += 1
                        currentNode = currentNode.leftC
                    else:
                        currentNode = currentNode.leftC
                else:
                    if currentNode.rightC == None:
                        currentNode.height += 1
                        currentNode.leftC = node
                        break
                    else:
                        currentNode.leftC = node
                        break

