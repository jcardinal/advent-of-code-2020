with open("input.txt", "r") as f:
    collected_answers = f.read().split("\n\n")

for i in range(len(collected_answers)):
    collected_answers[i] = set(collected_answers[i].replace("\n", ""))

sum_of_counts = 0
for i in range(len(collected_answers)):
    sum_of_counts += len(collected_answers[i])

print(sum_of_counts)