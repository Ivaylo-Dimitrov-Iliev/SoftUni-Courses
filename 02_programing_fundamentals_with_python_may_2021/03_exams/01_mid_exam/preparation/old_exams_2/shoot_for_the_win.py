targets = [int(el) for el in input().split()]

command = input()

count_of_shot_targets = 0

while not command == "End":
    index = int(command)
    if index in range(len(targets)):
        old_value = targets[index]
        for i in range(len(targets)):
            if targets[i] != -1 and targets[i] > old_value:
                targets[i] -= old_value
            elif targets[i] != -1 and targets[i] <= old_value:
                targets[i] += old_value
        targets[index] = -1
        count_of_shot_targets += 1
    command = input()

targets_as_str = [str(el) for el in targets]

print(f"Shot targets: {count_of_shot_targets} -> {' '.join(targets_as_str)}")
