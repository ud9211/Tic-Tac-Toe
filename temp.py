#hackerrank python list problem..

for t in range(int(input())):
    a=input()
    arr=[]
    if a[0]=='i':
        i=int(a[7])
        e=int(a[9])
        arr.insert(i,e)
    elif a[0]=='p':
        arr=arr[:-1]
    elif a[1]=='r':
        print(arr)
    elif a[0]=='r':
        e1=int(a[7])
        arr.remove(e1)
    elif a[0]=='a':
        e2=int(a[7])
        arr.append(e2)
    elif a[0]=='s':
        arr.sort()
    elif a[2]=='v':
        arr.reverse()

#if __name__ == '__main__':
   # N = int(input())