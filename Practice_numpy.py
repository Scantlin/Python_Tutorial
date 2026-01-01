import numpy as np

x = np.arange(1, 8, 2)
#print(x)

#changing the memory bits of array
x = np.array([1,2,3], dtype=np.int8)
#print(type(x[0]))
#print(x.shape)

#Shaping two Dimensional Array
twoD = np.array((np.arange(0,8,2), np.arange(1,8,2)), dtype=np.int8)
twoD = twoD.reshape(4,2)
#print(twoD)

#empty Array
y = np.zeros((2,5)) #1st method returns all 0
z = np.ones((5,3)) #2nd method returns all 1
n = np.empty((2,2)) #3rd method returns random value
#print(n)

#numpy eye function
eye = np.eye(4)
eye[eye == 1] = 4 
eye[eye == 0] = 5
eye[0] = 10
eye[:, 0] = 5
#print(eye)

#Sorting Array
sorted = np.sort(eye, axis=0, kind="quicksort")
#print(sorted)

#copy and view
y = sorted.view()
q = sorted.copy()

#y[:] = 4
#print(y)
#print(sorted)