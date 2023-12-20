from collections import deque
from math import lcm


path = "day_20.txt"
# path = "test.txt"

LOW = 0
HIGH = 1
BROADCASTER = 'broadcaster'
FLIP_FLOP = '%'
CONJUNCTION = '&'
BUTTON = 'button'

class FlipFlop:
    def __init__(self, connections):
        self.state = False
        self.connections = connections

    def __str__(self) -> str:
        return f'state: {self.state}, connections: {self.connections}'

    def __output(self):
        return HIGH if self.state else LOW

    def receive(self, source, pulse):
        if pulse == LOW:
            self.state = not self.state
            return self.__output()
        
        return None

class Conjunction:
    def __init__(self, connections):
        self.state = {}
        self.connections = connections

    def __str__(self) -> str:
        return f'state: {self.state}, connections: {self.connections}'

    def __output(self):
        return LOW if all([p == HIGH for p in self.state.values()]) else HIGH
        
    def add_input(self, input):
        self.state[input] = LOW
        
    def receive(self, source, pulse):
        self.state[source] = pulse

        return self.__output()

class Broadcaster:
    def __init__(self, connections):
        self.connections = connections

    def __str__(self) -> str:
        return f'connections: {self.connections}'
    
    def receive(self, source, pulse):
        return pulse

class Button:
    def __init__(self) -> None:
        self.connections = [BROADCASTER]

    def __str__(self) -> str:
        return f'connections: {self.connections}'

    def receive(self, source, pulse):
        return LOW

class Output:
    def __init__(self) -> None:
        self.connections = []

    def __str__(self) -> str:
        return f'connections: {self.connections}'
    
    def receive(self, source, pulse):
        return None

modules = {BUTTON: Button()}
conjunctions = set()
flip_flops = set()
with open(path, 'r') as file:
    
    for line in file:
        line = line.strip()
        kind, connections = line.split(' -> ')
        kind = kind.strip()
        connections = [s.strip() for s in connections.split(',')]

        if kind.startswith(BROADCASTER):
            modules[BROADCASTER] = Broadcaster(connections)
            continue

        name = kind[1:]

        if kind.startswith(FLIP_FLOP):
            modules[name] = FlipFlop(connections)
            flip_flops.add(name)
        elif kind.startswith(CONJUNCTION):
            modules[name] = Conjunction(connections)
            conjunctions.add(name)
        else:
            assert False, f"All cases should be covered. {line}" 

for m in modules:
    for c in modules[m].connections:
        if c in conjunctions:
            modules[c].add_input(m)


low_total = 0
high_total = 0
button_pressed = 0
rx = False
last_print = 0

cycles = {k: 0 for k in modules['hp'].state}
all_cycles_detected = False
# I manually saw that 'hp' in a Conjunction module
# so all states in 'hp' will need to be HIGH for it to send low
# So... Let's detect Cycles! (and hope they start in the beginning)
while not all_cycles_detected:
    button_pressed += 1
    q = deque([(BUTTON, None, None)])
    while len(q) > 0:
        m, source, pulse = q.popleft()

        if m == 'rx' and (1 in modules['hp'].state.values()):
            state = modules['hp'].state
            for k in state:
                if(state[k] == HIGH):
                    cycles[k] = button_pressed
            
            all_cycles_detected = all([v != 0 for v in cycles.values()])

        module = modules.get(m, Output())
        output = module.receive(source, pulse)
        if output == None:
            continue

        if output == HIGH:
            high_total += len(module.connections)
        elif output == LOW:
            low_total += len(module.connections)

        for c in module.connections:
            q.append((c, m, output))

print(lcm(*cycles.values()))