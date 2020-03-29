
def add_vectors(a, b):
    return [ a_i + b_i  for a_i, b_i in zip(a, b)]


a = [2, 3]
b = [4, -5]

c = add_vectors(a, b)

def vector_sum(vectors):

    resultant = vectors[0]

    for vector in vectors[1:]:
        resultant = add_vectors(resultant, vector)

    return resultant

d = vector_sum([a,b,c])

print(d)


