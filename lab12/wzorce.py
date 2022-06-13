import time



def naive(S, W):
    with open(S, encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    

    n_s = len(S)
    n_w = len(W)
    m = 0
    found = 0
    comp = 0
    rng = n_s - n_w + 1 
    
    
    while m < rng:
        i = 0
        check = True
        while i < n_w:
            comp += 1 
            if S[m+i] != W[i]:
                check = False
                break
            i += 1
        if check ==  True:
            found += 1
        m += 1

    return found, comp
                     

def Rabin_Karp(S,W):
    with open(S, encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    
    M = len(S)
    N = len(W)
    hW = hash(W)
    found = 0
    comp = 0

    for m in range(0,M-N+1):
        hS = hash(S[m:m+N])
        comp+=1
        if hS == hW:
            
            if S[m:m+N] == W:
                found += 1
    return found,comp


def hash(word):
    hw = 0
    d = 256
    q = 101
    N = len(word)
    for i in range(N):
        hw = (hw*d + ord(word[i]))% q
    return hw  
def rolling_hash(S,W):
    with open(S, encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    
    M = len(S)
    N = len(W)
    hW = hash(W)
    found = 0
    comp = 0
    h = 1
    d = 256
    q = 101
    N = len(W)
    col = 0
    hS = hash(S[0:N])
    for i in range(N-1):
        h = (h*d) % q

    for m in range(0,M-N+1):
        if m < M-N:  
            hp = (d*(hS - ord(S[m]) * h) + ord(S[m + N])) % q
        
            if hp < 0:
                hp += q 
            comp+=1
        if hS == hW:
            
            if S[m:m+N] == W:
                found += 1
            else:
                col += 1
        hS = hp
    return found,comp,col


def Knuth(S,W):
    with open(S, encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    
    n_s = len(S)
    n_w = len(W)
    m = 0
    found = 0
    comp = 0
     
    T = kmp_table(W)
    P = [0] * n_s
    i = 0
    nP= 0 
    
    while m < n_s:
        comp += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == n_w:
                found += 1
                P[nP] = m - i
                nP += 1
                i = T[i-1]
        else:
            i = T[i]
            if i < 0:
                m+=1
                i+=1


    return found, comp
    
def kmp_table(W):
    T = [0] * len(W)
    pos = 1
    cnd = 0
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    
    return T


def main():
    

    

    

    t_start = time.perf_counter()
    it = naive("lotr.txt", 'time.')  
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(it[0],';',it[1], sep='')


    

    
    t_start = time.perf_counter()
    m = Rabin_Karp("lotr.txt", 'time.')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(m[0],';',m[1], sep='')


    t_start = time.perf_counter()
    z = rolling_hash("lotr.txt", 'time.')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(z[0],';',z[1],';',z[2], sep='')


    t_start = time.perf_counter()
    g = Knuth("lotr.txt", 'time.')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print(g[0],';',g[1],sep='')
if __name__ == "__main__":      
    main()  