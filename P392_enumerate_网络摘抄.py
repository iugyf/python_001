seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))     


print("\n-------------------------------------")
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)
