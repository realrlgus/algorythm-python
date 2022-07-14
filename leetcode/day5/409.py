def longestPalindrome(s: str) -> int:
    s_dict = {}
    
    for t in s:
        if t not in s_dict:
            s_dict[t] = 1
        else:
            s_dict[t] = s_dict[t] + 1
    L = s_dict.values()
    E = len([i for i in L if i % 2 == 1])
    lens = sum(L) - E + (E > 0)
     
    return lens