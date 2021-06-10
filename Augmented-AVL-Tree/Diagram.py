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
                print("The current column number is {}".format(columnCount))
                print("The current content in the subsequent row is {}".format(displayArr[invertHeight+1,columnCount]))
                print("risingEdge is {}".format(risingEdge))
                print("fallingEdge is {}".format(fallingEdge))
                if int(displayArr[invertHeight+1,columnCount])==1 and risingEdge == False and fallingEdge == False:
                    risingEdge = not(risingEdge)
                    startCoord = columnCount
                    print("Rising edge at {}".format(columnCount))
                elif int(displayArr[invertHeight+1,columnCount])==1 and fallingEdge == False and risingEdge == True:
                    fallingEdge = not(fallingEdge)
                    endCoord = columnCount
                    print("Falling edge at {}".format(columnCount))
                                        

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
    for rows in range(treeHeight):
        # Instantiate an empty string to store the characters
        treeString = " "
        # Cycle through the columns
        for columns in range(ttlColumns):
            if columns == 0:
                if displayArr[rows,columns] == 0:
                    treeString = " "
                else:
                    treeString = "O"
            else:
                if displayArr[rows,columns] == 0:
                    treeString += " "
                else:
                    treeString += "O"
        print(treeString) 
        
