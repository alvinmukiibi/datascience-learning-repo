# for i in [1,2,3,4,5]:
#     print i
#     for j in [1,2,3,4,5]:
#         print j
#         print i + j
#
# print "Done looping"

from __future__ import  division

print 5 / 2

check = 2 in [3,2,4] # True
x = [1,2,3,4]
y = [5,6,7,8]
x.extend(y) # modifies x to concatenate y onto it

print x

# for no modification of x

z = x + y

# print z

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3 # my_list is now [1, 3]
try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"

def sum_and_product(x, y):
    return (x + y),(x * y)

sp = sum_and_product(2, 3) # equals (5, 6)
s, p = sum_and_product(5, 10) # s is 15, p is 50

print p

x, y = 1, 2 # now x is 1, y is 2
x, y = y, x # Pythonic way to swap variables; now x is 2, y is 1

grades = { "Joel" : 80, "Tim" : 95 } # dictionary literal

# You can check for the existence of a key using in:

joel_has_grade = "Joel" in grades # True
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0
grades["Tim"] = 99 # replaces the old value
grades["Kate"] = 100 # adds a third entry
num_students = len(grades) # equals 3

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print tweet_values
