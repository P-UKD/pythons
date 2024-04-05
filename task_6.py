seq = input()

length = None
count = 0

i = 0
while i < len(seq):
    prev = seq[i - 1] if i > 0 else None
    curr = seq[i]

    if prev and curr != prev:
        if not length:
            length = count
        elif count != length:
            print(False)
            exit()
        count = 1
    else:
        count += 1

    i += 1

print(not length or count == length)
