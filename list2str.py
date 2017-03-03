lst = ['tomato', 'potato', 'banana', 'apple']
lst = ['tomato']
lst = ['tomato', 'potato']

def list2str(lst):
    if len(lst) == 0:
        return ''

    if len(lst) == 1:
        return str(lst[0])

    new_lst = [lst[i] + ', ' for i in range(len(lst) - 2)]

    new_lst.append(lst[-2] + ' and ')
    new_lst.append(lst[-1])    
    return ''.join(new_lst)

print(list2str(lst))
