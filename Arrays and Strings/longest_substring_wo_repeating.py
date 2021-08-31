# strategy: two pointers

def longest_substring_without_repeating_characters(s: str) -> int:
    max_c = 0
    l = r = 0
    window = set()
    while r < len(s):
        if s[r] not in window:
            window.add(s[r])
            r += 1
        else:
            window.remove(s[l])
            l += 1
        max_c = max(max_c, r-l)

    return max_c

s = 'aaaab'
longest_substring_without_repeating_characters(s)