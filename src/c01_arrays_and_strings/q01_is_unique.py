def is_unique(string: str) -> bool:
    # Using a set to track characters we've seen
    char_set = set()

    for char in string:
        if char in char_set:
            return False
        char_set.add(char)

    return True


# Example usage:
if __name__ == "__main__":
    test_string = "abcdef"
    print(is_unique(test_string))  # Output: True

    test_string = "abcdeaf"
    print(is_unique(test_string))  # Output: False