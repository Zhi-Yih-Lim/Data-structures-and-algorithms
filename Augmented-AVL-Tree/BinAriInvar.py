def binArithCheck(baseLst):
    for bitNum, bit in enumerate(baseLst):
        # Start from the LSB of the list
        bitIdx = len(baseLst)-1-bitNum
        # If the digit pointed to by the current bitIdx is larger than one
        #, increment the bit to the left of the current bit
        if baseLst[bitIdx] == 2:
            baseLst[bitIdx-1] += 1
            baseLst[bitIdx] = 0

