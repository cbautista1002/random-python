# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().rstrip())

input_list = []

for _ in range(n):
    input_list.append(raw_input().rstrip())


def num_decorator(f):
    def decorated(num_list):
        new_num_list = []
        for i in num_list:
            if i[0] == '0':
                new_num_list.append(i[1:])
            elif len(i) == 12 and i[0:2] == '91':
                new_num_list.append(i[2:])
            elif len(i) == 10:
                new_num_list.append(i[:])
        f(new_num_list)
    return decorated

@num_decorator
def sort_numbers(a):
    a = sorted(a)
    print a
    return a

print sort_numbers(input_list)