import random


def gen_roll(min_num, max_num, num_die):
    roll_value = round(min_num + (random.random() * (max_num - min_num)))
    roll_value = roll_value * num_die
    return roll_value
    