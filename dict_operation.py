sameple_dict = { 'key1': 5, 'key2': 49, 'key3': 12, 'key4': 39, 'key5': 66 }

def high_value_key(ex_dict): # should return key for highest value
    max_value = 0
    for u,(x,y) in enumerate(ex_dict.items()):
        for i in list(ex_dict.values())[u:]:
            while y >= i and y > max_value:
                max_value = y
                high_key = x
                break
                
    return high_key        
        
    
print(high_value_key(sameple_dict))

