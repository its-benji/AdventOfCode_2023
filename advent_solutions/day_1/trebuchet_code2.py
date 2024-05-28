from helper_func import strCheck
f = open("trebuchet_data.txt", "r")

sum = 0

for x in range(1000):
    line = f.readline()
    var1=''
    var2=''
    str1=''
    str2=''

    for i in range(len(line)):
        if(line[i].isnumeric()):
            var1=line[i]
            print(var1)
            break
        str1+=line[i]
        res = strCheck(str1)
        if int(res) >= 0:
            var1 = res
            print(var1)
            break
    
    rline = list(reversed(line))
    for i in range(len(rline)):
        if(rline[i].isnumeric()):
            var2=rline[i]
            print(var2)
            break
        str2 = rline[i]+str2
        res = strCheck(str2)
        if int(res) >=0:
            var2 = res
            print(var2)
            break
    var3 = var1+var2
    sum+=int(var3)

print(sum)
f.close()
