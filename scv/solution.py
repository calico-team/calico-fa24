string =  "..............\n..............\n..............\n..####........\n..####........\n..####........\n..####........"
list_of_lengths = []

filtered = string.splitlines()
print(filtered)
for i in filtered:
    hashtag = i.count("#")
    list_of_lengths.append(hashtag)
unique_set = set(list_of_lengths)
if len(unique_set) > 2:
    print("Built like Phineas head")
if len(unique_set) == 2:
    print("wow, its a square")