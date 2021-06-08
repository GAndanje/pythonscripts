def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        middleIdx = len(array)//2
        leftArray = array[:middleIdx]
        rightArray = array[middleIdx:]
        return doMerge(mergeSort(leftArray),mergeSort(rightArray))

def doMerge(leftArray,rightArray):
    i,j,k =0,0,0
    sortedArray = [None]*(len(leftArray)+len(rightArray))
    while i <= len(leftArray)-1:
        if leftArray[i]<rightArray[j]:
            sortedArray[k] = leftArray[i]
            i+=1
        else:
            sortedArray[k]=rightArray[j]
            j+=1
        k+=1
    while j<len(rightArray)-1:
        sortedArray[k]=rightArray[j]
        j+=1
        k+=1
    return sortedArray
        
    
mergeSort([5,4,3,2,1])