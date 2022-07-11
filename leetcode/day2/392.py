def isSubsequence(s: str, t: str) -> bool:
    sub = 0
    for i in range(len(t)):
        if sub <= len(s) - 1:
            if s[sub] == t[i]:
                sub += 1
    return sub == len(s)

print(isSubsequence("ab", "baab"))