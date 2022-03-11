sameple_dict = { 'key1': 5, 'key2': 49, 'key3': 12, 'key4': 39, 'key5': 26 }

def high_value_key(ex_dict, n):
    if n>len(ex_dict):
        print('dictionary has less values than the number you provided')
    else:
        # form a list of tuples
        list_new = list(ex_dict.items())
        # sort tuple with second item, lambda function
        list_new.sort(reverse=True, key=lambda x:x[1])
        print({k:v for (k,v) in list_new})
        print(list_new[n-1][0])

high_value_key(sameple_dict,9)
