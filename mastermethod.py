import operator
from inspect import signature


def sort_merge(lst, lst1, lst2, comp):
    i=0
    j=0
    k=0

    while i < len(lst1) and j < len(lst2):
        if comp(lst1[i], lst2[j]):
            lst[k]=lst1[i]
            i=i+1
        else:
            lst[k]=lst2[j]
            j=j+1
        k=k+1

    while i < len(lst1):
        lst[k]=lst1[i]
        i=i+1
        k=k+1

    while j < len(lst2):
        lst[k]=lst2[j]
        j=j+1
        k=k+1
    return lst

def greatest_num_merge(lst, lst1, lst2, comp):
    i=0
    j=0
    k=0
    import pdb; pdb.set_trace()
    lst = lst1[i]
    while i < len(lst1) and j < len(lst2):
        if comp(lst1[i], lst2[j]):
            if not comp(lst,lst1[i]):
                lst=lst1[i]
            i=i+1
        else:
            #lst=lst2[j]
            j=j+1
        k=k+1
    yield lst


def masterMethod(lst, comp=operator.gt, mergeFunc=sort_merge):
    #todo: add assert that cmp is a binary operator
    #todo: add assert for lst contains orderable types
    length = int(len(lst))
    if length > 1:
        lst1, lst2 = lst[:int(length/2)], lst[int(length/2):]
        masterMethod(lst1, comp=comp)
        masterMethod(lst2, comp=comp)
        return mergeFunc(lst, lst1, lst2,comp=comp)
    return False

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print("Original inptu")
    print(alist)
    print("Sorted descending")
    print(masterMethod(alist))
    print("Sorted ascending")
    print(masterMethod(alist,comp=operator.lt))

    print(list(masterMethod(alist, comp=operator.gt, mergeFunc=greatest_num_merge)))
