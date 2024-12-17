from collections import deque

path = "day_17.txt"
# path = "test.txt"

def parse_register(s: str):
    return int(s.split(":")[1].strip())

def parse_instructions(s: str):
    
    return [int(i) for i in s.split(":")[1].strip().split(',')]

with open(path) as f:
    inpt = f.read()
    A, B, C = [parse_register(i) for i in inpt.split('\n\n')[0].splitlines()]
    instructions = parse_instructions(inpt.split('\n\n')[1])
    
print(A, B, C)
print(instructions)

class Computer:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.output = []
        self.op_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        
    def __str__(self):
        return f'Register A: {self.a}\nRegister B: {self.b}\nRegister C: {self.c}'
        
    def combo_op_value(self, combo_op):
        
        values = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
            7: None
        }
        
        return values[combo_op]
            
        
    def adv(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = self.a//(2**value)
        
        self.a = result
        return -1
    
    def bxl(self, literal_op):
        result = self.b ^ literal_op

        self.b = result
        return -1
    
    def bst(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = value%8
        
        self.b = result
        
        return -1
    
    def jnz(self, literal_op):
        if self.a == 0:
            return -1
        
        return literal_op
    
    def bxc(self, _):
        result = self.b^self.c
        
        self.b = result
        
        return -1
    
    def out(self, combo_op):
        value = self.combo_op_value(combo_op)
        
        self.output.append(value%8)
        
        return -1
        
    def bdv(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = self.a//(2**value)
        
        self.b = result
        
        return -1
    
    def cdv(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = self.a//(2**value)
        
        self.c = result
        
        return -1
    
    def perform_operation(self, op_code, operand):
        
        return self.op_map[op_code](operand)


computer = Computer(A,B,C)

i = 0

while 0 <= i < len(instructions) - 1:
    
    op_code, op = instructions[i], instructions[i+1]
    
    result = computer.perform_operation(op_code, op)
    i = result if result >= 0 else i + 2
    # print(i)
    
print('p1: ', ','.join(str(i) for i in computer.output))