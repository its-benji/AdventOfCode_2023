def isValid(s: str) -> bool:
        arr = []
        open = '([{'
        close = '}])'
        print(len(s))
        for i in range(len(s)):
            if len(arr) == 0:
                arr.append(s[i])
            else: 
                print(len(arr))
                if arr[len(arr)-1] == '(':
                    if s[i] == ')':
                        arr.pop()
                    else:
                        arr.append(s[i])
                elif arr[len(arr)-1] == '[':
                    if s[i] == ']':
                        arr.pop()
                    else:
                        arr.append(s[i])
                elif arr[len(arr)-1] == '{':
                    if s[i] == '}':
                        arr.pop()
                    else:
                        arr.append(s[i])
        if len(arr) == 0:
            return True
        else: 
            return False
            

print(isValid('({[]})'))