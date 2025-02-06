def is_palim(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True
if __name__ == "__main__":
    print(is_palim(input()))