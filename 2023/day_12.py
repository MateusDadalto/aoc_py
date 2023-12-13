from functools import cache


path = "day_12.txt"
path = "test.txt"

def f(springs, broken_groups):
    """ f is a wrapper function to cache the relevant dp part """
    
    @cache
    def dp(i, group_i):
        valid_possibilities = 0
        # when we get to the end of the string
        if i >= len(springs):
            # return 1 if the group index is the last one of the groups
            # meaning that we are in the end of the string and every group was counted
            return 1 if group_i == len(broken_groups) else 0
        
        # if the character is a dot or ? lets check the next character for the same group
        if springs[i] in ['.', '?']:
            valid_possibilities = dp(i+1, group_i)
        
        # Check if current group fits in this configuration
        # if it fits, move to next index after the group and next group
        # fit conditions:
        # if character is # or ? and we have a valid group index 
        # AND
        # is a valid group range
        #   (current index + group_size is smaller than springs string and there are no '.' in this group space)
        # AND
        # group ends after the group range (either end of string or ./?)
        if springs[i] in ['#', '?'] and group_i < len(broken_groups) and \
            (i+broken_groups[group_i] <= len(springs) and '.' not in springs[i: i+broken_groups[group_i]]) and \
            (i+broken_groups[group_i] == len(springs) or springs[i+broken_groups[group_i]] != '#'):

            valid_possibilities += dp(i+broken_groups[group_i] + 1, group_i + 1)

        return valid_possibilities
    
    return dp(0,0)

answer = 0

with open(path, 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        springs, dist = line.split()
        springs = '?'.join([springs]*5)
        # print(springs)
        broken_groups = [int(d) for d in dist.split(',')] * 5
        # print(broken_groups)
        a = f(springs, broken_groups)
        # print(springs, broken_groups, a, sep='   ')
        answer += a

print(answer)