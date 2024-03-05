import random

def generate_list(length):
    bottom_bound = 5
    upper_bound = 2 * 100
    random_list = []
    for _ in range(0, length):
        new_el = random.randint(bottom_bound, upper_bound)
        random_list.append(new_el)
    return random_list

print(generate_list(5))
