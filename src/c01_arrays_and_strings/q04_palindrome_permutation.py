def palindrome_permutation(s: str) -> bool:
    s = s.replace(" ", "").lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1


# Example usage:

if __name__ == "__main__":
    test_string = "Tact Coa"
    print(palindrome_permutation(test_string))  # Output: True

    test_string = "Tact boa"
    print(palindrome_permutation(test_string))  # Output: False