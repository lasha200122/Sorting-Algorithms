def Selection_Sort(ls):
    for i in range(len(ls)- 1):
        min_value = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[min_value]:
                min_value = j

        if min_value != i:
            ls[min_value] , ls[i] = ls[i], ls[min_value]
    return ls





def Insertion_Sort(ls):
    for i in range(1,len(ls)):
        value_to_sort = ls[i]

        while ls[i-1] > value_to_sort and i > 0 :
            ls[i], ls[i-1] = ls[i-1], ls[i]
            i-=1
    return ls





def Quick_Sort(ls):
    if len(ls) <= 1:
        return ls
    else:
        pivot = ls.pop()
    greater = []
    lower =[]
    for i in ls:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return Quick_Sort(lower) + [pivot] + Quick_Sort(greater)





def Merge_Sort(ls):
    if len(ls)<=1:
        return ls
    else:
        left_ls = ls[:len(ls)//2]
        right_ls = ls[len(ls)//2:]
        Merge_Sort(left_ls)
        Merge_Sort(right_ls)
        i = 0
        j = 0
        k =0
        while i < len(left_ls) and j < len(right_ls):
            if left_ls[i] < right_ls[j]:
                ls[k] = left_ls[i]
                i+=1
            else:
                ls[k] = right_ls[j]
                j+=1
            k += 1

        while i < len(left_ls):
            ls[k] = left_ls[i]
            i +=1
            k+=1

        while j < len(right_ls):
            ls[k] = right_ls[j]
            j+=1
            k+=1
        return ls




def Heap_Sort(ls):
    def swap(ls,i,j):
        ls[i], ls[j] = ls[j], ls[i]

    def siftDown(ls,i,upper):
        while True:
            l, r = i*2+1 , i*2+2
            if max(l,r)<upper:
                if ls[i] >= max(ls[l],ls[r]): break
                elif ls[l]> ls[r]:
                    swap(ls,i,l)
                    i=l
                else:
                    swap(ls,i,r)
                    i = r
            elif l<upper:
                if ls[l]> ls[i]:
                    swap(ls,i,l)
                    i=l
                else: break
            elif r < upper:
                if ls[r] > ls[i]:
                    swap(ls,i,r)
                else:break
            else:break
    for j in range((len(ls)-2)//2,-1,-1):
        siftDown(ls,j,len(ls))
    for end in range(len(ls)-1,0,-1):
        swap(ls,0,end)
        siftDown(ls,0,end)
    return ls





def Radix_Sort(ls):
    def Get_num_digits(ls):
        m=0
        for i in ls:
            m = max(i,m)
        return len(str(m))

    def radix(ls,num_digits):
        for d in range(num_digits):
            B= [[] for i in range(10)]
            for i in ls:
                num = i//10 ** (d) %10
                B[num].append(i)
            ls = flatten(B)
        return ls

    from functools import reduce
    def flatten(ls):
        return reduce(lambda x,y:x+y,ls)

    num_digits = Get_num_digits(ls)
    ls = radix(ls,num_digits)
    return ls

