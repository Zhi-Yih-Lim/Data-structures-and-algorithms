import numpy as np
# A module that generates the graphical representation of the AVL Tree.
def ShowTree(treeObj):
    # Only plot the tree if it is not empyt
    if treeObj.root.height == 0:
        print("There are no nodes to plot")
    else:
        # Identify the height of the tree
        treeHeight = int(treeObj.root.height) + 1
        # Calculate the maximum number of leaves expected at the bottom most
        # layer of the tree
        ttlLeaves = int(np.power(2,treeHeight-1))
        # The total number of spaces between the subsequent nodes at the 
        # bottom layer
        ttlSpaces = ttlLeaves - 1
        # Calculate the total columns expected
        ttlColumns = ttlLeaves + ttlSpaces
        # Instantiate an array that will store the locations of the 
        # nodes within the tree
        displayArr = np.zeros((treeHeight,ttlColumns))
        # Based on the inherent structure of the AVL tree, there are limited
        # number of nodes that can be fitted wihtin each layer. Cycle through 
        # each layer and calculate the total number of nodes that can fit 
        # within that layer
        for row in range(treeHeight):
            # Calculate the inverted row position
            invertedRow = (treeHeight-1)-row
            # Calculate the total number of nodes within the current 
            # layer
            ttlNodes = int(np.power(2,invertedRow))
            # Instantiate a list that will store the path to the current node 
            # of interest, from the root of the tree
            pathLst = []
            # Use binary addition to generate the path to access each node
            baseLst = []
            for node in range (ttlNodes):
                baseLst.append(0)
            # Using the values in 'baseLst' as reference, traverse down 
            # the AVL tree
            for node in range(ttlNodes):
                # Variable that points to the root node, intitally
                currentNode = treeObj.root
                # Instantiate a traversal counter
                travCount = 0
                # We want to traverse all the way down to the leaves 
                # while keeping count of the total steps taken
                while currentNode != None:
                    if baseLst[travCount] == 0:
                        currentNode = currentNode.leftC
                    elif baseLst[travCount] == 1:
                        currentNode = currentNode.rightC
                    travCount += 1
                # Upon exiting the loop, check "travCount". If "travCount"
                # is less than the total number of layers, than measn the the 
                # path from the tree root to the current leaf of interest is 
                # incomplete and the current leaf of interest does not exist
                if travCount < int(treeHeight-1):
                    pathLst.append([])
                else:
                    # Instantiate a direction list
                    dirLst = []
                    for bit in baseLst:
                        if bit == 0:
                            dirLst.append('L')
                        elif bit == 1:
                            dirLst.append('R')
                    # Append the direction list to 'pathLst'
                    pathLst.append(dirLst)    
                # With each passing node, increase binary base value by one
                baseLst[-1] += 1
                # Check to see if there are any bits that are larger than one
                # if so, carry over
                for bitNum, bit in enumerate(baseLst):
                    invertBit = len(baseLst)-1-bitNum
                    # If the subsequent bit is larger than one
                    # carry over the value to the current position
                    if baseLst[invertBit] == 2:
                        baseLst[invertBit-1] += 1
                        baseLst[invertBit] = 0
             
            # With 'pathLst' now populated for each of the nodes 
            # in the current row, access the corresponding node position
            # within 'displayArr' and assign the values to be either
            # '0' or '1' to indicate if the node in that position is 
            # present or not
            if ttlColumns - ttlNodes == (ttlNodes-1):
                # This means that we are in the bottom row of the tree
                # Here, nodes are separated by one space in between
                for nodeNum,path in enumerate(pathLst):
                    # Calculate the x-coordinate of the current Node
                    globXCoord = (nodeNum*2) 
                    if len(path) == 0:
                        # 1 indicates that there should be a node
                        # present but is absent for the current tree
                        displayArr[invertedRow,globXCoord]=1
                    else:
                        # 2 indicates that there is a node present in the 
                        # current spot
                        displayArr[invertedRow,globXCoord]=2
            else:
                # For the remaining rows, access the subsequent row to identify 
                # the node location for the current row
                for nodeNum,path in enumerate(pathLst):
                    # Instantiate a rising and falling edge detector 
                    risingEdge = False
                    fallingEdge = False
                    # Instantiate a variable to keep track of the previous
                    # X-coordinate
                    prevXCoord = 0
                    for col in range(ttlColumns):
                        if (displayArr[invertedRow+1,col] == 1 or displayArr[invertedRow+1,col] == 2) and risingEdge == False:
                               risingEdge = True
                               prevXCoord = col
                        elif (displayArr[invertedRow+1,col] == 1 or displayArr[invertedRow+1,col]) == 2 and risingEdge == True:
                                 fallingEdge = True
                        # If both the rising and falling edges have been detected
                        # calculate the midpoint between the rising and falling
                        # edges
                        if risingEdge and fallingEdge:
                            midpoint = prevXCoord + ((col - prevXCoord)//2)
                            # Plot the current node location in displayArr
                            if len(path) == 0:
                                displayArr[invertedRow,midpoint] = 1
                            else:
                                displayArr[invertedRow,midpoint] = 2
                            # Reset the rising and falling edge variables
                            risingEdge = False
                            fallingEdge = False



                        

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

