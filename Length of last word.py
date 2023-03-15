def length(str):
    lis = list(str.split(" "))
    return len(lis[-1])
 
 
# Driver code
str = "Geeks for Geeks"
print("The length of last word is",
      length(str))