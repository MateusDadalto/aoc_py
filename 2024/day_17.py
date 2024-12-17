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
    
# print(A, B, C)
# print(instructions)

class Computer:
    def __init__(self, a, b, c, log_ops):
        self.a = a
        self.b = b
        self.c = c
        self.output = []
        self.log = log_ops
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
        
        if self.log:
            print(f'VARIABLE INPUT {combo_op} adv -> A // 2^{value} -> SET A {result}')
        
        self.a = result
        return -1
    
    def bxl(self, literal_op):
        result = self.b ^ literal_op
        
        if self.log:
            print(f'CONSTANT INPUT bxl -> B XOR {literal_op} -> SET B {result}')

        self.b = result
        return -1
    
    def bst(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = value%8
        
        self.b = result
        
        if self.log:
            print(f'VARIABLE INPUT {combo_op} bst -> {value} % 8 -> SET B {result}')
        
        return -1
    
    def jnz(self, literal_op):
        if self.a == 0:
            if self.log:
                print(f'CONSTANT INPUT jnz -> A is 0, do nothing')
            return -1
        
            
        if self.log:
            print(f'CONSTANT INPUT jnz -> A is {self.a} jump to {literal_op}')
        
        return literal_op
    
    def bxc(self, _):
        result = self.b^self.c
        
        if self.log:
            print(f'CONSTANT INPUT bxc -> B xor C {self.b} ^ {self.c} -> SET B {result}')
        self.b = result
        
        return -1
    
    def out(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = value%8
        if self.log:
            print(f'APPEND OUTPUT out -> Combo op {combo_op} -> value: {value} % 8-> APPEND OUT {result}')
        self.output.append(result)
        
        return -1
        
    def bdv(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = self.a//(2**value)
        
        if self.log:
            print(f'VARIABLE INPUT {combo_op} bdv -> A // 2^{value} -> SET B {result}')
        
        self.b = result
        
        return -1
    
    def cdv(self, combo_op):
        value = self.combo_op_value(combo_op)
        result = self.a//(2**value)
        
        if self.log:
            print(f'VARIABLE INPUT {combo_op} cdv -> A // 2^{value} -> SET C {result}')
        
        self.c = result
        
        return -1
    
    def perform_operation(self, op_code, operand):
        if self.log:
            print(f'perform operation {op_code} with operand {operand}')
        return self.op_map[op_code](operand)



def process(a,b,c, instructions, log):
    computer = Computer(a,b,c, log)
    i = 0
    
    while 0 <= i < len(instructions) - 1:
        
        op_code, op = instructions[i], instructions[i+1]
        
        result = computer.perform_operation(op_code, op)
        i = result if result >= 0 else i + 2
        out_len = len(computer.output)
        
    print('Halted')
            
    print('p1:', ','.join(str(i) for i in computer.output))
    
def process_single(a,b,c, instructions, log):
    computer = Computer(a,b,c, log)
    i = 0
    
    while 0 <= i < len(instructions) - 1:
        
        op_code, op = instructions[i], instructions[i+1]
        
        result = computer.perform_operation(op_code, op)
        i = result if result >= 0 else i + 2
        out_len = len(computer.output)
        
        if out_len == 1:
            return computer.output[0]
    
    return None

p1 = process(A, B, C, instructions, False)

# after manually evaluating my loop, I saw that in each iteration A = A//8
# So to find the number we do a "DFS" (don't know if it is actually a DFS) starting from the last number
# Find A where process(A,0,0) == rev(instructions)[0]. 
# Multiply that A by 8 and try to find new A where process(A,0,0) == rev(instructions)[+1] AND A//8 == previous A
# If there is no A that satisfies that condition, go back to previous A and try A+1

q = deque([(0, 0, None)])
rev = [j for j in reversed(instructions)]
p2 = 0
log = False
while len(q) > 0:
    x, i, prev_x = q.popleft()
    
    if len(rev) == i:
        p2 = prev_x
        break
    
    if prev_x and x//8 > prev_x:
        continue
    
    result = process_single(x, 0, 0, instructions, log)
    if result == rev[i]:

        q.appendleft((x*8, i+1, x))
    
    q.append((x+1, i, x))
    
print('p2:', p2)
