from collections import Counter

with open("input.txt", "r") as f:
    collected_answers = f.read().split("\n\n")


def count_all_yes(group):
    num_all_yes = 0
    num_group_members = len(group.split("\n"))
    frequency_counts = Counter(group)
    for answer in frequency_counts:
        if frequency_counts[answer] == num_group_members:
            num_all_yes += 1
    return num_all_yes


sum_of_counts = 0
for group in collected_answers:
    sum_of_counts += count_all_yes(group)

print(sum_of_counts)