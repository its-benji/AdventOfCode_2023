f = open("trebuchet_data.txt", "r")

# 1. read line-by-line through file
# 2. take each individual line and go through
# with two 'for' loops, extracting first 'number'
sum = 0

for x in range(1000):
    line = f.readline()
    var1 = ''
    var2 = ''
    for i in range(len(line)):
        if(line[i].isnumeric()):
            var1 = line[i]
            break
    rline = list(reversed(line))
    for i in range(len(rline)):
        if(rline[i].isnumeric()):
            var2 = rline[i]
            break
    var3=var1+var2
    var3=int(var3)
    sum+=var3
f.close()

print(sum)
