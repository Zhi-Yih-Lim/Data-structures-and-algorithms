import numpy as np
from BinAriInvar import binArithCheck
# A module that generates the graphical representation of the AVL Tree.
def ShowTree(treeObj):
    # Only plot the tree if it is not empyt
    if treeObj.root.height == 0:
        print("There are no nodes to plot")
    else:
        # Identify the height of the tree
        treeHeight = int(treeObj.root.height)+1
        # We would like to create a square array to plot the tree. First, will have to identify the maximum number of 
        # leaves present at the bottom most layer of the tree to determine the size of the display array.
        ttlLeaves = int(np.power(2,treeHeight-1))
        # We want a space between each leaves in the bottom layer. This means that the total number of spaces to be 
        # added to the bottom layer will be one less than the total number of leaves available at the bottom layer
        ttlSpaces = ttlLeaves - 1
        # Calculate the total number of columns from the total leaves and the total spaces required
        ttlColumns = ttlLeaves + ttlSpaces
        # Instantiate the display array
        displayArr = np.zeros((treeHeight,ttlColumns))
        # Starting from the bottom row of the tree, I want to individually access the leaves of the 
        # Original tree to see if there are any leaves present
        for row in list(reversed(range(treeHeight))):
            # Calculate the total number of leaves expected in the current row
            leaves = int(np.power(2,row))
            print("A total of {} leaves in this layer".format(leaves))
            # Instantiate a list that will store lists containing directions (in char) that will 
            # sequentially point to each of the individual nodes of the current layer, from the root
            # of the tree
            pat2EachNodeLst = []
            # To access each of the nodes in the current layer of "treeObj" sequentailly, binary arithmetic 
            # can be used
            # There should the exactly the same number of digits as there are number of nodes in the current 
            # layer of interest. Say that there are four nodes in the current layer, the instantiated list should be 
            # [0 0 0 0] initially.
            baseLst = []
            for count in range(row):
                baseLst.append(0)
            # Access each of the nodes in "treeObj" for the current layer
            for nodes in range(leaves):
                # If there is only one node in the current layer, traversal of the tree is not required
                if len(baseLst) > 0:
                    # Start from the root of the tree
                    currentNode = treeObj.root
                    # Instantaite variable to see if the next node exists
                    nextNode = None
                    # Traverse downs the tree, starting from the root, using the directions defined by the digits
                    # of "baseLst", to the node of interest
                    # Instantiate a traversal counter that keeps track of the currently referenced bit in "baseLst"
                    traverseCount = -1 
                    for digitNum, digit in enumerate(baseLst):
                        if digit == 0:
                            nextNode = currentNode.leftC
                        elif digit == 1:
                            nextNode = currentNode.rightC
                        # Check if the next node exists
                        if nextNode != None:
                            if digit == 0:
                                currentNode = currentNode.leftC
                            elif digit == 1:
                                currentNode = currentNode.rightC
                            traverseCount += 1
                            
                    # By the end of the loop check if "traverseCount" is of similar value to "digitNum". If they are the same
                    # that means that the search has followed the direction specified by each digit in "baseLst" and all the
                    # parent and grandparent nodes of the current node of interest exists. The current node of interest can be 
                    # plotted in the diagram.
                    if traverseCount == digitNum:
                        # Construct a direction list of characters "L" or "R" to describe where the search should diverge to 
                        #, starting from the root of the tree
                        dirList = []
                        for digit in baseLst:
                            if digit == 0:
                                dirList.append("L")
                            elif digit == 1:
                                dirList.append("R")
                        # Append "dirList" to "pat2EachNodeLst"
                        pat2EachNodeLst.append(dirList)
                    elif traverseCount < digitNum:
                        # Append and empty list to "pat2EachNodeLst" to indicate that the current node of interest does 
                        # not exist in the "treeObj"
                        pat2EachNodeLst.append([])
                    # With each passing node, increase binary base value by one
                    baseLst[-1] += 1
                    # Check to see if "baseLst" follows the invariant for binary addition
                    binArithCheck(baseLst)
                

             
            print(pat2EachNodeLst)
        


                        

        # Using the array as reference, constuct stings to plot the tree
        # in a better view
        # Calculate  the total number of rows, including the rows that will
        # store the direction pointers, labelled as forward or backward slashes
        ttlRows = treeHeight + (treeHeight-1)
        # A boolean variable to keep track of which rows to plot nodes and 
        # which rows to plot arrows
        arrowRow = False
        # A counter to store the total "arrow rows" that have been added to the 
        # tree figure
        ttlarrowRow = 0
        for rows in range(ttlRows):
            if arrowRow == False:
                # Instantiate an empty string to store the characters
                treeString = " "
                # Cycle through the columns
                for columns in range(ttlColumns):
                    if columns == 0:
                        if displayArr[rows-ttlarrowRow,columns] == 0:
                            treeString = " "
                        elif displayArr[rows-ttlarrowRow,columns] == 2:
                            treeString = "O"
                    else:
                        if displayArr[rows-ttlarrowRow,columns] == 0:
                            treeString += " "
                        elif displayArr[rows-ttlarrowRow,columns] == 2:
                            treeString += "O"
                arrowRow = not(arrowRow)
                print(treeString)
            else:
                # If the current row is an arrow row, look at the avalable nodes 
                # in the previous and subsequent non-arrow rows to determine the 
                # suitable location to place the arrows
                ttlarrowRow+=1
                nonArrowRowNum = rows-ttlarrowRow
                nxtNonArrowRowNum = (rows-ttlarrowRow) + 1 
                # Identify the node coordinate(s) in the firs row
                # Instantiate a list to store the coordinates for the first row
                firstRowCoord = []
                for colums in range(ttlColumns):
                    if displayArr[nonArrowRowNum,colums]==2:
                        firstRowCoord.append([nonArrowRowNum,colums])
                # Instantiate a list to store the coordinates for the subsequent row
                secondRowCoord = []
                for colums in range(ttlColumns):
                    if displayArr[nonArrowRowNum,colums]==2:
                        secondRowCoord.append([nxtNonArrowRowNum,colums])
                arrowRow = not(arrowRow)
                
                # A string variable to store the items to be displayed
                arrowRowStr = " "
                # Instantiate a vector to store the arrow location and directions
                # 4 = right, 7 = left
                arrowCoord = np.zeros((1,ttlColumns))
                # For every node in the parent layer, compute the euclidean distance 
                # with respect to all of the children nodes
                for pNodeCoord in firstRowCoord:
                    # Instantiate a list to store the eucl. distance values 
                    lstOfEuclDist = []
                    for cNodeCoord in secondRowCoord:
                        lstOfEuclDist.append(np.sqrt(np.square(pNodeCoord[1]-cNodeCoord[1])+np.square(pNodeCoord[0]-cNodeCoord[0])))
                    # Find the minimum distance from the list of euclidean distances
                    minDist = min(lstOfEuclDist)
                    # Instatntiate a list to store the coordiates of the children 
                    # node(s) with the least distance
                    childLst = []
                    for count, euclDist in enumerate(lstOfEuclDist):
                        if euclDist <= minDist:
                            childLst.append(secondRowCoord[count])
                    # With the for the children nodes compliled, calculate the columnd
                    # number to plot the arrows
                    for childCoordinates in childLst:
                        # Calculate the x-coordinate midpoint
                        XDist = (childCoordinates[1]-pNodeCoord[1])/2
                        if np.abs(XDist) < 1:
                            # If the distance is less than 1, plot the arrows 
                            # directly above the children nodes
                            if XDist < 0:
                                # Use the column values of the children
                                arrowCoord[0,childCoordinates[1]] = 7
                            else:
                                arrowCoord[0,childCoordinates[1]] = 4
                                
                        else:
                            # Compute the midpoint between the current child and 
                            # parent node (on the x-axis) to plot the slashes
                            slashXCoord = int(pNodeCoord[1] + XDist)
                            if XDist < 0:
                                arrowCoord[0,slashXCoord] = 7
                            else:
                                arrowCoord[0,slashXCoord] = 4
                # Convert the numbers into strings and print 
                for columns in range(ttlColumns):
                    if columns == 0:
                        if arrowCoord[0,columns] == 4:
                            arrowRowStr = '\\'
                        elif arrowCoord[0,columns] == 7:
                            arrowRowStr = '/'
                        else:
                            arrowRowStr = ' '
                    else:
                        if arrowCoord[0,columns] == 4:
                            arrowRowStr += "\\"
                        elif arrowCoord[0,columns] == 7:
                            arrowRowStr += "/"
                        else:
                            arrowRowStr += ' '
                print(arrowRowStr)

