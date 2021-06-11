import numpy as np
# A module that generates the graphical representation of the AVL Tree.
def ShowTree(treeObj):
    # Identify the height of the tree
    treeHeight = int(treeObj.root.height) + 1
    # The bottom layer will contain the most nodes
    # The displaying array should be set such that the leaves are only 
    # separated by one column between them
    ttlLeaves = np.power(2,treeHeight-1)
    ttlColumns = ttlLeaves + (ttlLeaves - 1)
    displayArr = np.zeros((treeHeight,ttlColumns))
    # Starting form the bottom layer, identify the locations to plot the nodes
    for row in range(treeHeight):
        invertHeight = (treeHeight-1)-row
        # Determine the number of nodes required to be included in this row
        ttlNodes = np.power(2,treeHeight-1)
        # If the current row is the last row, set the nodes in alternate slots
        if invertHeight ==  treeHeight - 1:
            # Populate the array
            # Instantiate a boolean variable to remember the location for spaces
            spaceBool = False
            for colCount in range(ttlColumns):
                if spaceBool:
                    displayArr[invertHeight,colCount] = 0
                else:
                    displayArr[invertHeight,colCount] = 1
                spaceBool = not(spaceBool)

        else:
            # Refer to the next row in the array and use the midpoints
            # between two nodes (in the subsequent array) to identify the locatiom
            # to plot the node in the current row
            # Set a boolean variable to identify when to plot the node in the 
            # current row
            risingEdge = False
            fallingEdge = False
            startCoord = 0
            endCoord = 0
            
            # Cycle through the subsequent row
            for columnCount in range(ttlColumns):

                if int(displayArr[invertHeight+1,columnCount])==1 and risingEdge == False and fallingEdge == False:
                    risingEdge = not(risingEdge)
                    startCoord = columnCount

                elif int(displayArr[invertHeight+1,columnCount])==1 and fallingEdge == False and risingEdge == True:
                    fallingEdge = not(fallingEdge)
                    endCoord = columnCount

                                        

                # If the rising and falling edge boolean variables are all true
                # that means that a computation of midpoint will have to be 
                # performed
                if risingEdge and fallingEdge:
                    midpoint = startCoord + ((endCoord-startCoord)//2)
                    # Set the variable for the current row to be true
                    displayArr[invertHeight,midpoint]=1
                    # Reset the rising and falling edge boolean variables
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
                    else:
                        treeString = "O"
                else:
                    if displayArr[rows-ttlarrowRow,columns] == 0:
                        treeString += " "
                    else:
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
                if displayArr[nonArrowRowNum,colums]==1:
                    firstRowCoord.append([nonArrowRowNum,colums])
            # Instantiate a list to store the coordinates for the subsequent row
            secondRowCoord = []
            for colums in range(ttlColumns):
                if displayArr[nxtNonArrowRowNum,colums]==1:
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

