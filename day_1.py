digits_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
digits_name = tuple(digits_map.keys())
digits = []


def first_digit(s: str, d: list[int]):
    first = d[0]
    i = s.index(first)
    for j in range(3, i + 1):
        substring = s[0:j]
        if substring.endswith(digits_name):
            first = next((digits_map.get(name)
                         for name in digits_name if substring.endswith(name)), first)
            break

    return str(first)


def last_digit(s: str, d: list[int]):
    last = d[-1]
    i = s.rindex(last)
    for j in range(i, len(s)).__reversed__():
        substring = s[i:j]
        if substring.endswith(digits_name):
            last = next((digits_map.get(name)
                         for name in digits_name if substring.endswith(name)), last)
            break

    return str(last)

# Open the file in read mode ('r')
with open('day_1.txt', 'r') as file:
    i = 1
    for line in file:
        line_ds = [d for d in line if d.isdigit()]
        first_digit(line, line_ds)
        digits.append(int(first_digit(line, line_ds)+last_digit(line, line_ds)))
        i += 1

print(sum(digits))
