class SelectionSort: # two parts sorted and unsorted select minmum
       def __init__(self, arr):
              self.arr = arr
              self.l=len(arr)
       def sort(self):
              for i in range(self.l):
                     min = i
                     for j in range(i+1, self.l):
                            if self.arr[min] > self.arr[j]:
                                   min = j

                     self.arr[i], self.arr[min]= self.arr[min], self.arr[i]
              return self.arr

class BubbleSort:# compare with adjacent element and send the bigger value to the last of the list
       def __init__(self, arr):
              self.arr = arr
              self.l=len(arr)

       def sort(self):
              for i in range(self.l): # for increasing the i the index
                     for j in range(i+1, self.l-i-1):
                            if self.arr[i]>self.arr[j]:
                                   self.arr[i], self.arr[j]=self.arr[j],self.arr[i]
              return self.arr

class InsertionSort: #select the number which is small and put it before greater numbers
       def __init__(self, arr):
              self.arr = arr
              self.l=len(arr)
       def sort(self):
              for i in range(self.l):
                     key=self.arr[i]
                     j=i-1
                     while j>=0 and key< self.arr[j]:
                            self.arr[j+1]=self.arr[j]
                            j-=1
                     self.arr[j+1]= key

              return self.arr

class MergeSort:
       def sort(self,arr):
              l=len(arr)
              if l>1:
                     mid=l//2
                     left=arr[:mid]
                     right=arr[mid:]
                     self.sort(left)
                     self.sort(right)

                     i=0
                     j=0
                     k=0

                     while i< len(left) and j<len(right):
                            if left[i]<right[j]:
                                   arr[k]=left[i]
                                   i+=1

                            else:
                                   arr[k]=right[j]
                                   j+=1

                            k+=1
                     while i<len(left):
                            arr[k]=left[i]
                            i+=1
                            k+=1

                     while i<len(left):
                            arr[k]=left[i]
                            i+=1
                            k+=1

              return arr



if __name__=='__main__':
       l=[7,5,3,2,2,1]
       s= SelectionSort(l)
       print('selection sort\n',s.sort())
       b=BubbleSort(l)
       print('bubble sort\n',b.sort())
       i=InsertionSort(l)
       print('insertion sort\n',i.sort())
       m=MergeSort()
       print('merge sort\n',m.sort(l))
       print(l.sort())
       print(l)