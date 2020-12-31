
def merge_sort(arr):
    if len(arr) > 1:
        res = []
        mid = len(arr) // 2
        L = arr[:mid] # [1, 2, 3, 4] => [1, 2]
        R = arr[mid:] # [1, 2, 3, 4] => [3, 4]

        print('-'*50)
        print(f'arr:{arr}')
        print(f'L:{L}')
        print(f'R:{R}')

        L = merge_sort(L)
        R = merge_sort(R)

        i = j = 0 # iはLを探索するインデックス、jはRを探索するインデックス
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                res.append(L[i])
                i += 1
            else: # L[i] > R[j]
                res.append(R[j])
                j += 1
        
        while i < len(L):
            res.append(L[i])
            i += 1
        
        while j < len(R):
            res.append(R[j])
            j += 1
        
        print(f'arr:{arr}')
        print(f'L:{L}')
        print(f'R:{R}')
        print(f'res:{res}')
        print('-'*50)
        
        return res
    else:
        return arr

list_a = [5, 7, 6, 4, 5, 1, 2, 3, 2, 2, 9, 1, 4]
print(merge_sort(list_a))
