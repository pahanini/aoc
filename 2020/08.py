from utils import read_re


class Instruction:

    def __init__(self, line):
        self.operation = line[0]
        self.operand = int(line[1])
        self.executed = 0


class Console:

    def __init__(self, program):
        self.program = program
        self.instructions = []
        self.acc = 0
        self.mutator = 0
        self.pointer = 0
        self.load()

    def load(self):
        self.instructions = []
        self.acc = 0
        self.pointer = 0
        for line in self.program:
            self.instructions.append(Instruction(line))

    def next(self):
        while 0 <= self.pointer < len(self.instructions):
            yield self.instructions[self.pointer]

    def mutate(self):
        self.load()
        while self.instructions[self.mutator].operation == 'acc':
            self.mutator += 1
        instruction = self.instructions[self.mutator]
        self.instructions[self.mutator].operation = 'jmp' if instruction.operation == 'nop' else 'nop'
        self.mutator += 1

    def exec(self, instruction):
        if instruction.operation == 'acc':
            self.acc += instruction.operand
            self.pointer += 1
        elif instruction.operation == 'nop':
            self.pointer += 1
        elif instruction.operation == 'jmp':
            self.pointer += instruction.operand
        instruction.executed += 1

    def find_inf(self):
        for instruction in self.next():
            if instruction.executed == 1:
                return self.acc
            self.exec(instruction)

    def fix(self):
        while self.find_inf() is not None:
            self.mutate()
        return self.acc


ptn = r'^(nop|acc|jmp) ([\+\-0-9]+)$'
tst = read_re('08.tst', ptn)
cons = Console(tst)

assert cons.find_inf() == 5
assert cons.fix() == 8

dat = read_re('08.dat', ptn)
cons = Console(dat)

print("day 8 puzzle 1 =", cons.find_inf())
print("day 8 puzzle 2 =", cons.fix())
