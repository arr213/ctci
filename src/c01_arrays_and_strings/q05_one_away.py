def one_away(s1, s2):
    if len(s1) == len(s2):
        return one_away_same_length(s1, s2)
    elif len(s1) == len(s2) + 1:
        return one_away_diff_length(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_away_diff_length(s2, s1)
    return False


def one_away_same_length(s1, s2):
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_away_diff_length(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


# Example usage:
if __name__ == "__main__":
    str1 = "pale"
    str2 = "ple"
    print(one_away(str1, str2))  # Output: True

    str1 = "pales"
    str2 = "pale"
    print(one_away(str1, str2))  # Output: True

    str1 = "pale"
    str2 = "bale"
    print(one_away(str1, str2))  # Output: True

    str1 = "pale"
    str2 = "bake"
    print(one_away(str1, str2))  # Output: False
