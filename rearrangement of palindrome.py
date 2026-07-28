def st(s):
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1   
        left = ""

        for ch in sorted(freq):
            half = freq[ch] // 2
            left += ch * half
        middle = ""
        for ch in sorted(freq):
            if freq[ch] % 2 == 1:
                middle = ch

        return left+middle+left[::-1]

s="aabbb"
print(st(s))