class Sorting:
    def __init__(self):
        print("Sorting")

    def bubbleSort(self,array):
        for i in range(len(array)-1):
            for j in range(0,len(array)-i-1):
                if(array[j+1]<array[j]):
                    array[j],array[j+1]=array[j+1],array[j]

    def selectionSort(self,array):
        for i in range(1,len(array)-1):
            min=i
            for j in range(i+1,len(array)):
                if array[j]<array[i]:
                    min=j
            if min!=i:
                array[i],array[min]=array[min],array[i]

    def insertionSort(self,array):


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
s.selectionSort(l1)
print(l1)