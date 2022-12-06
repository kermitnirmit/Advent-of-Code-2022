f = open("input.txt").read().strip()
for q in range(2):
    gap = 14 if q == 1 else 4
    for i in range(len(f) - gap):
        if len(set(f[i:i+gap])) == gap:
            print(i + gap)
            break
