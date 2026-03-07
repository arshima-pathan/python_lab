"""#integer array
from array import array
arr=array('i',[10,20,30,40])
print (arr)
print(type(arr))

#len()-number of elements
from array import array
arr=array('i',[10,20,30,40])
print(len (arr))

#append(x)-add element at end
from array import array
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#insert(pos,x)-insert at position
from array import array
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#remove(x)-remove first occurrence
from array import array
arr=array('i',[10,20,30,40])
arr.remove(20)
print(arr)

#pop()
from array import array
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed :",x)
print(arr)

#index(x)
from array import array
arr=array('i',[10,20,30,40])
print(arr.index(30))

#count(x)
from array import array
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#reverse()
from array import array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)

#positive indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#negative indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])"""

#modifying elements
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#index error
from array import array
arr=array('i',[10,20,30])
print(arr[5])

#basic slice
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])

#slicing with step
from array import array
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#negative slicing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#reverse array using slicing
from array import array
arr=array('i',10,20,30,40,50)
print(arr[::-1])

#modifying slices
from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)