string1 = 'matching words'
string2 = 'different words matched'

def unmatched(stringA, stringB):
    list1=[]
    for x in stringA:
            if x not in stringB:
                list1.append(x)
                
    print(list1)       
    
unmatched(string1,string2)
