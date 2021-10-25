def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while (i < len(lefthalf) and
            j < len(righthalf)):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            else:
                alist[k] = righthalf[j]
                j += 1
                k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

with open('input.txt', 'r') as f:
    data = {}
    n = f.readline()

    for i in range(int(n)):
        x = f.readline().split()
        data[x[0]] = data[x[0]] + [x[1]] if data.__contains__(x[0]) else [x[1]]

keys = list(data.keys())
mergeSort(keys)
lst = []

with open('output.txt', 'w') as f:
    for key in keys:
        for val in data[key]:
            lst.append(key + ' ' + val)
    f.writelines('\n'.join(lst))