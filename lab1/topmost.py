import wordfreq
import sys
import urllib.request

stopWordsFilvag = sys.argv[1]
inputFilvagEllerUrl = sys.argv[2]
topmostCount = int(sys.argv[3])

with open(stopWordsFilvag) as stopWordsFil:
    stopWords = []
    for line in stopWordsFil:
        stopWords.append(line.strip())

    inputLines = []
    if inputFilvagEllerUrl.startswith("http://") or inputFilvagEllerUrl.startswith("https://"):
        response = urllib.request.urlopen(inputFilvagEllerUrl)
        inputLines = response.read().decode("utf8").splitlines()
    else:
        with open(inputFilvagEllerUrl) as inputFil:
            inputLines = inputFil.readlines()

    tokens = wordfreq.tokenize(inputLines)
    count = wordfreq.countWords(tokens, stopWords)
    wordfreq.printTopMost(count, topmostCount)
