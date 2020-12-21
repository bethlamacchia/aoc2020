
"""

    acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
    jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
    nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

part 1 - there's a loop somewhere in the code, - Immediately before any instruction is executed a second time, what value is in the accumulator?

part 2
Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). 
What is the value of the accumulator after the program terminates?
"""

# use a bool to indicate if p1 or not so we don't get a bunch of printouts
# each time we run the tmp code from part 2
def run(instructions: [], p1: bool=True):
    seen = set()
    cur = 0
    acc = 0
    terminated = False
    while not terminated:
        if cur in seen:
            if p1:
                print("part 1: " + str(acc))
            break
        cmd, arg = instructions[cur]
        seen.add(cur)
        if cmd == "nop":
            cur += 1
        if cmd == "jmp":
            cur += int(arg)
        if cmd == "acc":
            acc += int(arg)
            cur += 1
        # Terminate if at end at program
        terminated = cur == len(instructions)
        if terminated:
            print("part 2: " + str(acc))


if __name__ == "__main__":

    instructions=[]

    with open("input.txt") as file:
        for line in file:
            # separate command and argument
            instructions.append(line.split(' '))

    run(instructions)

    for i in range(len(instructions)):
        # Copy lines so that changes don't persist each swap
        tmp = [x for x in instructions]

        # Switch statement jmp/nop
        if 'jmp' in tmp[i][0]:
            tmp[i] = ('nop', tmp[i][1])
        elif 'nop' in tmp[i][0]:
            tmp[i] = ('jmp', tmp[i][1])

        run(tmp, p1=False)