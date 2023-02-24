l=[5,1,35,21,'salom',5,'A','z','Hayr',12]
ls=[]
lch=[]
for i in range(len(l)-1,-1,-1):
    s=str(l[i])
    if s.isalpha() and len(s)==1:
        lch.append(s)
        l.pop(i)
    elif s.isalpha():
        ls.append(s)
        l.pop(i)
def SelectionSort(arr:list):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ind]:
                 min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
SelectionSort(l)
SelectionSort(ls)
SelectionSort(lch)
l.extend(lch)
l.extend(ls)
print(l)
