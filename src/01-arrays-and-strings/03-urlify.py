def urlify(s):
    return s.strip().replace(' ', '%20')

# Example usage:
if __name__ == "__main__":
    urlify("Mr John Smith")  # Output: "Mr%20John%20Smith"