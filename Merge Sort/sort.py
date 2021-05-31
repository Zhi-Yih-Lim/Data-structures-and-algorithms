import numpy as np

def MergeSort(unsortedList,parameters):
    # Check the length of the unsorted array, if it is only one in length, return is as it is
    if len(unsortedList) == 1:
        sortedLst = unsortedList
    else:
        # Instantiate a list to store the sorted class object
        sortedLst = []
        # Identify the midpoint of the list 
        midpoint = len(unsortedList)//2
        # Separate the unsorted list into the left unsorted and right unsorted
        leftUnsort = unsortedList[0:midpoint]
        rightUnsort = unsortedList[midpoint:]
    
        # Recurese upon the respective lists
        sortedLeft = MergeSort(leftUnsort,parameters)
        sortedRight = MergeSort(rightUnsort,parameters)
        # Assign index pointers to identify the locations from the left and right sorted lists to compare
        leftLstIdx = 0
        rightLstIdx = 0
        # Merge the sorted left and right lists 
        for counter in range(len(unsortedList)):
            # If the right of left list indeces points to their final element, terminate the loop and return the sorted lists
            if leftLstIdx == len(sortedLeft):
                # Append the remaining contents of the right list to the sortedLst and return
                sortedLst = sortedLst + sortedRight[rightLstIdx:]
                break
            elif rightLstIdx == len(sortedRight):
                # Append the remaining contents of the right list to the sortedLst and return
                sortedLst = sortedLst + sortedLeft[leftLstIdx:]
                break
            else:
                # See which parameter to compare
                if parameters == "P":
                    if sortedLeft[leftLstIdx].price > sortedRight[rightLstIdx].price:
                        sortedLst.append(sortedRight[rightLstIdx]) 
                        # Increment the list counter
                        rightLstIdx += 1
                    else:
                        sortedLst.append(sortedLeft[leftLstIdx])
                        # Increment the list counter
                        leftLstIdx += 1
                elif parameters == "mpg":
                    if sortedLeft[leftLstIdx].efficiency > sortedRight[rightLstIdx].efficiency:
                        sortedLst.append(sortedRight[rightLstIdx]) 
                        # Increment the list counter
                        rightLstIdx += 1
                    else:
                        sortedLst.append(sortedLeft[leftLstIdx])
                        # Increment the list counter
                        leftLstIdx += 1

    return sortedLst
