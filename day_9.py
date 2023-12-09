path = "day_9.txt"
# path = "test.txt"

sequences = []
with open(path, 'r') as file:
    for line in file:
        sequences.append([int(x) for x in line.split()])


def diff(seq: list[int]):
    return [seq[i+1] -  seq[i] for i in range(len(seq) - 1)]

def predict(seq: list[int]):
    if any([i != 0 for i in seq]):
        return seq[-1] + predict(diff(seq))
    else:
        return 0
    
def predict_previous(seq: list[int]):
    if any([i != 0 for i in seq]):
        return seq[0] - predict_previous(diff(seq))
    else:
        return 0


print(sum([predict_previous(s) for s in sequences]))