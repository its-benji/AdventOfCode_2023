with open("parts.txt", 'r') as file:
    grid = file.read().splitlines()
res = set()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col.isdigit() or col=='.':  
            continue
        for rr in [r-1, r, r+1]:
            if rr<0 or rr>len(grid):
                continue
            for cc in [c-1, c, c+1]:
                if c<0 or c>len(row) or not grid[rr][cc].isdigit():
                    # if row[c] == '&':
                    #     print('&:', r, c, col, row[cc], len(grid))
                    continue
                # i = cc
                while cc > 0 and row[cc-1].isdigit():
                    cc-=1
                # print('First:', r, rr, cc, grid[rr][i+1], row[i])
                if grid[rr][cc].isdigit():
                    # print('add:', grid[rr][i+1], rr, i+1)
                    res.add((rr,cc))
                    # print('rc:', rr+1,cc+1)
# print(res)

sum = 0
for tp in res:
    r=int(tp[0])
    c=int(tp[1])
    n=''

    while c<len(grid[r]) and grid[r][c].isdigit():
        n+=grid[r][c]
        c+=1
    # print(n)
    sum+=int(n)
print(sum)