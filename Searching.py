class Searching:
    def __init__(self):
        print("searching...")
    def binarySearch(self,array,value):
        i=0
        j=len(array)-1
        while(i<j):
            if(array[i]==value):
                return i
            elif(array[i]>value):
                j=j-1
            else:
                i=i+1

        return -1

    def linearSearch(self,array,value):
        for i in range(len(array)):
            if(array[i]==value):
                return i
        return -1


s=Searching()
array=[1,2,3,4,5,6]
print(s.linearSearch(array,4))
print(s.binarySearch(array,7))