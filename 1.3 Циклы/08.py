prev=int(input())
post=int(input())
ASCENDING=True #стр возрастающая
DESCENDING=True #стр убывающая
CONSTANT=True #стр постоянная
WEAKLY_ASCENDING=True #неубывающая
WEAKLY_DESCENDING=True #невозрастающая

while (post!=-2000000000):
    if prev>=post:
        ASCENDING=False #точно не стр возр
    if prev<=post:
        DESCENDING=False #точно не стр уб
    if prev!=post:
        CONSTANT=False # не пост

    if prev>post:
        WEAKLY_ASCENDING=False #неуб
    if prev<post:
        WEAKLY_DESCENDING=False #невозр

    prev=post
    post=int(input())

if CONSTANT and ASCENDING:
    WEAKLY_ASCENDING = False
if CONSTANT and DESCENDING:
    is_WEAKLY_DESCENDING = False

if CONSTANT:
    print("CONSTANT")
elif ASCENDING:
    print("ASCENDING")
elif DESCENDING:
    print("DESCENDING")
elif WEAKLY_ASCENDING: #неуб
    print("WEAKLY ASCENDING")
elif WEAKLY_DESCENDING: #невозр
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")
