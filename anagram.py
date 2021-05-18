def check_anagram(s1, s2):
    if sorted(s1) != sorted(s2):
        return False
    else:
        return True

print(check_anagram("abcda","ebcda"))