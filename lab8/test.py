def solution(N):
    candidate = [1] * (N+1) 
    result = []
    for i in range(2,N+1):
        if candidate[i] != 0:
            result.append(i)
            for j in range(2*i,N+1,i):
                candidate[j] = 0
    return result






print(solution(10))

import random

def solution2(S):
    S = list(S)
    for i in range(len(S) // 2):
        if S[i] != S[-i-1]:
            if S[i] == '?':
                S[i] = S[-i-1]
            elif S[-i-1] == '?':
                S[-i-1] = S[i]
        else:
            if S[-i-1] == '?' and S[i] =='?':
                S[i] = S[-i-1] = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z'])
    check = True
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            check = False
    if check == True:
        return ''.join(S)
    else:
        return 'NO'



print(solution2('?ab??a'))
print(solution2('bab??a'))
print(solution2('?a?'))
    


