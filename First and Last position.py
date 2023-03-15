def first(arr, low, high, key, length):
  return arr.index(x)
 
def last(arr, low, high, key, length): 
  return length - 1 - arr[::-1].index(x)
 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
 
x = 0
print('First Occurrence = ',
      first(arr, 0, n - 1, x, n))
print('Last Occurrence = ',
      last(arr, 0, n - 1, x, n))