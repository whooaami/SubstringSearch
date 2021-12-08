def read_data(file):
    with open(file, 'r') as input_file:
        data = input_file.readlines()
    return data


def longest_proper_prefix(pattern, pattern_length, lps):
    length = 0
    i = 1

    while i < pattern_length:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def kmp_search(pattern, string):
    pattern_length = len(pattern)
    string_length = len(string)
    lps = [0] * pattern_length
    j = 0
    result_list = []
    longest_proper_prefix(pattern, pattern_length, lps)
    i = 0

    while i < string_length:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == pattern_length:
            result_list.append(str(i - j) + "-" + str(i - j + pattern_length - 1))
            j = lps[j - 1]
        elif pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result_list


if __name__ == '__main__':
    result = read_data("test1.in")
    pattern = result[1]
    string = result[0]

    print('Result =>', kmp_search(pattern, string))
