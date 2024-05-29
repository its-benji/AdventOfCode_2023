from block_helpers import checkblue
from block_helpers import checkgreen
f = open("blocks.txt", "r")
sum=0
for x in range(100):
    line = list(f.readline())
    n = True
    gnum = ''
    cnum = ''
    for i in range(len(line)):
        while line[i].isnumeric():
            if n:
                gnum+=line[i]
            else: 
                cnum+=line[i]
                if int(cnum)>=15:
                    gnum='0'
                    break
                elif int(cnum)==14:
                    b1 = checkblue(line, i)
                    if b1==False:
                        gnum='0'
                        break
                elif int(cnum)==13:
                    b2 = checkgreen(line, i)
                    if b2==False:
                        gnum='0'
                        break
            
            i=i+1
        cnum=''
        if gnum=='0':
            break
        if line[i]==':':
            n=False
    sum+=int(gnum)
    print('Game: ', x+1, gnum, sum)
print(sum)

f.close()