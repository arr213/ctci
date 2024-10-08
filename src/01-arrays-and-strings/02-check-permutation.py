def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


# Example usage:
if __name__ == "__main__":
    s1 = "abc"
    s2 = "bca"
    print(check_permutation(s1, s2))  # Output: True

    s1 = "abc"
    s2 = "bcd"
    print(check_permutation(s1, s2))  # Output: False