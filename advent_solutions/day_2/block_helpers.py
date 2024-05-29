def checkgreen(line, ind):
    sub = ''
    for i in range(ind, len(line)):
        if(line[i]==';'):
            break
        if(line[i]==','):
            break
        sub+=line[i]
    if 'green' in sub:
        return True
    if 'blue' in sub:
        return True
    return False
        
def checkblue(line, ind):
    sub = ''
    for i in range(ind, len(line)):
        if(line[i]==';'):
            break
        if(line[i]==','):
            break
        sub+=line[i]
    if 'blue' in sub:
        print('trips blue', sub)
        return True
    return False

# add comment to push