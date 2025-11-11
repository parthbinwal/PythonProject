class Sorting:
    def __init__(self):
        print("Sorting")

    def bubbleSort(self,array):
        for i in range(len(array)-1):
            for j in range(0,len(array)-i-1):
                if(array[j+1]<array[j]):
                    array[j],array[j+1]=array[j+1],array[j]

    def selectionSort(self,array):
        pass

    def insertionSort(self,array):
        pass

    def mergeSort(self,array):
        pass

    def quickSort(self,array):
        pass

    def heapSort(self,array):
        pass

    def radixSort(self,array):
        pass

    def bucketSort(self,array):
        pass



s= Sorting()
l1=[1,5,3,2,9]
s.bubbleSort(l1)
print(l1)