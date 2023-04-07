cases = int(input())
for i in range(cases):
    counter = 0
    avg = 0
    scores = list(map(int, input().split()))
    num_students = scores[0]
    del scores[0]
    for score in scores:
        avg += score
    avg /= len(scores)
    for score in scores:
        if score > avg:
            counter += 1
    print(f"{(100 * (counter / len(scores))):.3f}%")