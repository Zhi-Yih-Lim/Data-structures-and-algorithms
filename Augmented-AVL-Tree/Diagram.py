import numpy as np
# A module that generates the graphical representation of the AVL Tree.
def ShowTree(treeObj):
    # Identify the height of the tree
    treeHeight = treeObj.root.height
    # Calculte the total number of leaves expected at the lowest layer
    maxLeaves = np.power(2,treeHeight)
    # Identify the total number of columns required at the lowest level. Each node at the lowest level should have a spacing column between 
    ttlSpace = maxLeaves - 1 
    # Instantaite a square array with the total number of columns including the number of max leaves together with the required spacing between the columns
    ttlColumns = maxLeaves + ttlSpace
    arr = np.zeros((maxLeaves+ttlSpace,maxLeaves+ttlSpace))
