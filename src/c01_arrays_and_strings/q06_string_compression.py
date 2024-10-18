def string_compression(s: str) -> str:
    compressed = []
    count = 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i] + str(count))
            count = 0

    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s


# Example usage:
if __name__ == "__main__":
    s = "aabcccccaaa"
    print(string_compression(s))  # Output: a2b1c5a3

    s = "abc"
    print(string_compression(s))  # Output: abc
