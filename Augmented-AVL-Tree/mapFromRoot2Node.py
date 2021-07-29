# This function shoud receive "treeObj" and the row number of interest.
# The function should then return a list of lists, containing either "O",
# a series of "L" and "R"s, indicating the path to take to access the current
# node of interest, within the current layer of interest from the root of
# "treeObj", or an empty list, indicating that the current node of interest
# does not exist
# The function will also receive a list of zeros called "baseLst" that contains 
# the bits required for binary addition in order to access each node sequentially.
# An empty list called "pat2EachNodeLst" is also passed to this function and is expected
# to be returned, contain the direction of travel, from the root of the tree to the node 
# of interest using either "L" or "R" to indicate the direction of travel, staring from
# the root of the tree.
from BinAriInvar import binArithCheck
import numpy as np
def stringToNode(treeObj,baseLst,pat2EachNodeLst,layer=-1):
    # Check if the layer of interest has been specified
    if layer == -1:
        print("Layer number not defined, exiting \"stringToNode\" function")
        return None
    else:
        # First, based on the row index (zero indexed), calculate the total number of leaves expected
        # for this layer
        leaves = int(np.power(2,layer))
        # Cycle through each individual node
        for node in range(leaves):
            # If the number of leaves for the current layer only one, that means that this node is the 
            # root of the tree. This means that no traversion through the layers of the tree is required.
            # Append "O" to "pat2EachNodeLst" to indicate that the only node in this layer is the root 
            # of the tree and return
            if leaves == 1:
                pat2EachNodeLst.append(["O"])
                return pat2EachNodeLst
            else:
                # Start frin the root of the tree
                currentNode = treeObj.root
