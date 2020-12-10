with open("input.txt", "r") as f:
    instructions = f.read().splitlines()

acc = 0
i = 0
instructions_run = set()


def run_instruction(i, instruction, acc):
    if instruction[:3] == "nop":
        i += 1
    elif instruction[:3] == "acc":
        acc += int(instruction[4:])
        i += 1
    elif instructions[i][:3] == "jmp":
        i += int(instruction[4:])

    return i, acc


while i not in instructions_run:
    instructions_run.add(i)
    i, acc = run_instruction(i, instructions[i], acc)

print(acc)
