class SortWithoutMethod:

    def sort_method(lst):
        lst2 = []
        lst3 = []
        while lst:
            minC = lst[0]
    
            for i in lst:
                if i < minC:
                    minC = i
            lst2.append(minC)
            lst.remove(minC)
            if len(lst)== 0:
                break
            else:
                maxC = lst[0]
                for j in lst:
                    if j > maxC:
                        maxC = j
                lst3.insert(0, maxC)
                lst.remove(maxC)
        
        lst = lst2 + lst3
        return lst

    print('before sorting:')
    nums = [3, 2, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 2, 1, 43, 5, 3, 7, 8, 8, 5, 9, 3]
    print(nums)
    print('after sorting:')
    print(sort_method(nums))
