class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, n, p):
        p +=1 
        for i in range(n):
            a = arr[i]%p
            if a <= n:
                
                arr[a-1]+= p
        for i in range(n):
            arr[i] = arr[i]//p
        return arr
