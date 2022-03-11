sample_string = "A New version of python is ready to download on desktops"

def repetitions(ex_string, character):
    count = 0
    for x in ex_string:
        if character == x:
            count += 1
    print(count)
    
repetitions(sample_string, 't')
