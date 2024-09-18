def tokenize(lines: list[str]):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1
            if start < len(line):
                if line[start].isalpha():
                    end = start+1
                    while end < len(line) and line[end].isalpha():
                        end += 1
                    words.append(line[start:end].lower())
                    start = end-1
                elif line[start].isdigit():
                    end = start+1
                    while end < len(line) and line[end].isdigit():
                        end += 1
                    words.append(line[start:end])
                    start = end-1
                else:
                    words.append(line[start])

            start = start + 1

    return words


# Ett alternativt sätt:
# import re
# def tokenize(lines: List[str]):
#     words = []
#     for line in lines:
#         line = line.lower()
#         m = re.findall(r'([a-zåäö]+|[0-9]+|[^\s])', line)
#         words.extend(m)
#     return words


def countWords(words: list[str], stopWords: list[str]):
    a = {}
    for word in words:
        if word in stopWords:
            continue

        if word not in a:
            a[word] = 0
        a[word] += 1
    return a


def printTopMost(frequencies: dict[str, int], n: int):
    for (word, freq) in sorted(frequencies.items(), key=lambda x: -x[1])[0:n]:
        print(word.ljust(20) + str(freq).rjust(5))
