
def average_volume(dic):
    i = 0
    j = 0
    for k,v in dic.items():
        i = i + int(v['5. volume'])
        j+=1
    print(j)
    return i/j

