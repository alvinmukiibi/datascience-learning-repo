document = ["we", "can", "be", "good", "if","we", "want","come", "on","good", "we","be"]

word_counts = {}

# THE FIRST WAY
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


print word_counts

# THE 2ND WAY
word_counts_2 = {}

for word in document:
    try:
        word_counts_2[word] += 1
    except KeyError:
        word_counts_2[word] = 1

print word_counts_2

# THE 3RD WAY

word_counts_3 = {}

for word in document:
    previous_count = word_counts_3.get(word, 0)
    word_counts_3[word] = previous_count + 1

print word_counts_3

# THE 4TH WAY using defaultdict
# A defaultdict is like a regular dictionary, except that when you try to look up a key it doesnt contain
# it first adds a value for it using a zero-argument function you provided when you created it.

from collections import  defaultdict

word_counts_4 = defaultdict(int)

for word in document:
    word_counts_4[word] += 1

print  word_counts_4


# THE 5TH WAY, using Counter

from collections import Counter

word_counts_5 = Counter(document)

print word_counts_5

for word, count in word_counts_5.most_common(3):
    print word, count


# SETS a collection of distinct elements

s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is still { 1, 2 }
x = len(s) # equals 2

# helps in searching

document_set = set(document)

print "can" in document_set
print document_set
print len(document_set)