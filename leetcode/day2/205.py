def isIsomorphic(s: str, t: str) -> bool:
    s_words = list(dict.fromkeys([word for word in s]))
    t_words = list(dict.fromkeys([word for word in t]))
    num = 1

    if len(s_words) != len(t_words):
        return False

    for i in range(len(s_words)):
        s = s.replace(s_words[i] , str(num))
        t = t.replace(t_words[i] , str(num))
        num += 1

    
    return s == t

print(isIsomorphic("abbbababab", "baaababaab"))



