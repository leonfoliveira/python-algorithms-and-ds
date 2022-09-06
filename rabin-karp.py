def rabin_karp(pattern, string):
    n = len(string)
    m = len(pattern)
    
    if m > n:
        return False
    
    def encode(char):
        return ord(char) - ord('a')
    
    BASE = 26 # a-z
    MOD = 10**9+7
    
    def get_hash(substr):
        value = 0
        for char in substr:
            value = (value*BASE + encode(char)) % MOD
        return value
    
    pattern_hash = get_hash(pattern)
    target_hash = get_hash(string[:m])
    
    for start in range(-1, n - m):
        end = start + m
        if start > -1:
            target_hash = (target_hash - encode(string[start])*BASE**(m-1)) % MOD                    
            target_hash = (target_hash*BASE + encode(string[end])) % MOD
        if target_hash == pattern_hash and string[start+1:end+1] == pattern:
            return True
    return False

print(rabin_karp('abc', 'cacadhsdabc'))
