with open("input.txt", "r") as f:
    instructions = f.read().splitlines()


def run_instruction(i, instruction, acc):
    if instruction[:3] == "nop":
        i += 1
    elif instruction[:3] == "acc":
        acc += int(instruction[4:])
        i += 1
    elif instructions[i][:3] == "jmp":
        i += int(instruction[4:])

    return i, acc


j = 0
for _ in instructions:
    acc = 0
    i = 0
    instructions_run = set()
    mod_instructions = instructions.copy()
    if mod_instructions[j][:3] == "nop":
        mod_instructions[j] = "jmp " + mod_instructions[j][4:]
    elif mod_instructions[j][:3] == "jmp":
        mod_instructions[j] = "nop " + mod_instructions[j][4:]
    j += 1

    while i not in instructions_run and i < len(instructions):
        instructions_run.add(i)
        i, acc = run_instruction(i, mod_instructions[i], acc)

    if i >= len(instructions):
        print(acc)
        break
