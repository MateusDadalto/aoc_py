from itertools import cycle
from collections import deque
# from copy import deepcopy

path = "day_09.txt"
# path = "test.txt"
UNICODE_MAX = int('0x110000', 0)
empty_char = chr(UNICODE_MAX - 1)
with open(path) as f:
    line = f.readline()


loop = cycle(['F', '.'])
blocks = []
blocks_p2 = []
id = 0
# p2 [(size, id), (size, -1)]
for c in line:
    f_or_dot = next(loop)
    blocks += [id]*int(c) if f_or_dot == 'F' else [-1]*int(c)
    blocks_p2.append(chr(int(id))*int(c) if f_or_dot == 'F' else empty_char*int(c))
    
    id += 1 if f_or_dot == 'F' else 0

blocks_str = ''.join(blocks_p2)
SIZE = len(blocks)
q = deque(blocks)

# compress
compressed = []
fill_empty = False
while len(q) > 0:
    if fill_empty:
        digit = q.pop()
    else:
        digit = q.popleft()
    
    if digit < 0:
        fill_empty = True
    else:
        compressed.append(digit)
        fill_empty = False
    

# print(compressed)
p1 = sum([i*compressed[i] for i in range(len(compressed))])

print(p1)
# print(blocks_p2)
# p2

# def swap(list, i, j): 
#     tmp = list[i]
#     list[i] = list[j]
#     list[j] = tmp
    
#     return list

# def find_first_empty(blocks, size, max_i):
#     for index in range(len(blocks)):
        
#         if index > max_i:
#             return None
        
#         empty_size, id = blocks[index]
#         if id == -1 and empty_size >= size:
#             return index
    
#     return None
        
    
# def change_block(blocks, file_index, empty_index):
#     f_size, f_id = blocks[file_index]
#     e_size, e_id = blocks[empty_index]
    
#     remaining_space = e_size - f_size
    
#     new_b = swap(blocks, file_index, empty_index)
    
#     if remaining_space > 0:
#         return new_b[:empty_index + 1] + [(remaining_space, -1)] + new_b[empty_index+1:]
    
#     return new_b
        
# # compress
# compressed_p2 = []
# fill_empty = False
# while len(q) > 0:
#     if fill_empty:
#         block = q.pop()
#     else:
#         block = q.popleft()
    
#     if block[1] == -1:
#         fill_empty = True
#     else:
#         compressed.append(digit)
#         fill_empty = False
    
        
        

true_index = len(blocks_str)
for i in reversed(range(len(blocks_p2))):
    block = blocks_p2[i]
    true_index -= len(block)
    
    rep = empty_char*len(block)
    
    if rep in blocks_str and blocks_str.index(rep) < true_index:
        blocks_str = blocks_str.replace(rep, block, 1)
        blocks_str = blocks_str[0:true_index] + rep + blocks_str[true_index + len(block):]
    
# print(blocks_str)

p2 = sum([i*int(ord(blocks_str[i])) for i in range(len(blocks_str)) if blocks_str[i] != empty_char])
print(p2)