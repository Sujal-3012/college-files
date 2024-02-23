def factorial(n):
    fact = 1
    for i in range(2,n + 1) :
        fact = fact * i
    return fact

n = int(input("Enter the number to calculate factorial : "))
print(factorial(n))


def bubble(arr):
    L = arr
    for a in range(0 , len(L)):
        for j in range(0 , len(L)-a-1):
            if (L[j] > L[j+1]):
                L[j] , L[j+1] = L[j+1] , L[j]
    return L;

def merging(arr , l ,m ,h):
    n1 = m - l + 1
    n2 = h - l + 1
    temp = [arr[l+i] for i in range(n2)]
    i = 0
    j = n1
    k = l
    while (i < n1 and j < n2):
        if (temp[i]<=temp[j]):
            arr[k] = temp[i]
            i+=1
        else:
            arr[k] = temp[j]
            j+=1
        k+=1
    while i<n1:
        arr[k] = temp[i]
        k+=1
        i+=1
    while j<n2:
        arr[k] = temp[j]
        k+=1
        j+=1
    
def merge(arr , s , e):
    if (s<e):
        mid = int((s+e)/2)
        merge(arr , s , mid)
        merge(arr , mid + 1 , e)
        merging(arr, s, mid, e)

L = []
k = int(input("Enter the number of elements in List : "))
for j in range(0 , k):
    a = int(input("enter the element : "))
    L.append(a)
print(L)

print("Sorted list is : " , bubble(L))
merge(L,0,len(k)-1)
print("Sorted list is : " , L)
