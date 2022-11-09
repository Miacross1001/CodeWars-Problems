def sum_pairs(ints, s):
    res_index = set()
    for elem in ints:
        if s - elem in res_index:
            return [s-elem, elem]
        res_index.add(elem)


#print(sum_pairs([4, -2, 3, 3, 4], 8))
#print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

#l9 = [1] * 10000000
#l9[len(l9) // 2 - 1] = 6
#l9[len(l9) // 2] = 7
#l9[len(l9) - 2] = 8
#l9[len(l9) - 1] = -3
#l9[0] = 13
#l9[1] = 3
#print(sum_pairs(l9, 16))