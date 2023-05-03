import os
import random
import sys

import numpy

base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
id_container = [0, 0]
group_id_container = [0, 0]
group = numpy.zeros((50050, 50050))
message_id_container = [0, 0]


def add_person():
    id = random.randint(1, 10001)
    id_container.append(id)
    name = base_str[random.randint(0, len(base_str) - 1)]
    age = random.randint(1, 100)
    print(f"ap {id} {name} {age}")


def add_relation():
    if random.random() > 0.5:
        id1 = id_container[random.randint(0, len(id_container) - 1)]
        id2 = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    value = random.randint(1, 100)
    print(f"ar {int(id1)} {int(id2)} {value}")


def query_value():
    if random.random() > 0.8:
        id1 = id_container[random.randint(0, len(id_container) - 1)]
        id2 = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    print(f"qv {int(id1)} {int(id2)}")


def query_circle():
    if random.random() > 0.9:
        id1 = id_container[random.randint(0, len(id_container) - 1)]
        id2 = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    print(f"qci {int(id1)} {int(id2)}")


def query_block_sum():
    print("qbs")


def query_triple_sum():
    print("qts")


def add_group():
    id = random.randint(1, 10001)
    group_id_container.append(id)
    print(f"ag {id}")


def add_to_group():
    if random.random() > 0.8:
        id1 = id_container[random.randint(0, len(id_container) - 1)]
        id2 = int(group_id_container[random.randint(0, len(group_id_container) - 1)])
        group[id2][len(group[id2]) - 1] = id1
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    print(f"atg {int(id1)} {id2}")


def del_from_group():
    if random.random() > 0.9:
        id2 = int(group_id_container[random.randint(0, len(group_id_container) - 1)])
        tmp = random.randint(0, len(group[id2]) - 1)
        id1 = group[id2][tmp]
        for i in range(tmp, len(group[id2]) - 1):
            group[id2][i] = group[id2][i + 1]
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    print(f"dfg {int(id1)} {id2}")


def query_group_value_sum():
    if random.random() > 0.8:
        id2 = int(group_id_container[random.randint(0, len(group_id_container) - 1)])
    else:
        id2 = random.randint(1, 20000)
    print(f"qgvs {id2}")


def query_group_age_var():
    if random.random() > 0.8:
        id2 = int(group_id_container[random.randint(0, len(group_id_container) - 1)])
    else:
        id2 = random.randint(1, 20000)
    print(f"qgav {id2}")


def modify_relation():
    if random.random() > 0.8:
        id1 = id_container[random.randint(0, len(id_container) - 1)]
        id2 = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id1 = random.randint(1, 20000)
        id2 = random.randint(1, 20000)
    value = random.randint(-100, 100)
    print(f"mr {int(id1)} {int(id2)} {value}")


# def modify_relation_ok_test():
#
#
def query_best_acquaintance():
    if random.random() > 0.8:
        id = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id = random.randint(1, 20000)
    print(f"qba {id}")


def query_couple_sum():
    print("qcs")


def add_message():
    type = random.randint(0, 2)
    if type == 0:
        mess_id = random.randint(1, 10001)
        message_id_container.append(mess_id)
        social_value = random.randint(1, 100)
        if random.random() > 0.8:
            id1 = id_container[random.randint(0, len(id_container) - 1)]
            id2 = id_container[random.randint(0, len(id_container) - 1)]
        else:
            id1 = random.randint(1, 20000)
            id2 = random.randint(1, 20000)
        print(f"am {mess_id} {social_value} {type} {int(id1)} {int(id2)}")
    elif type == 1:
        mess_id = random.randint(1, 10001)
        message_id_container.append(mess_id)
        social_value = random.randint(1, 100)
        if random.random() > 0.8:
            id1 = id_container[random.randint(0, len(id_container) - 1)]
            id2 = int(group_id_container[random.randint(0, len(group_id_container) - 1)])
        else:
            id1 = random.randint(1, 20000)
            id2 = random.randint(1, 20000)
        print(f"am {mess_id} {social_value} {type} {int(id1)} {int(id2)}")


def send_message():
    if random.random() > 0.8:
        id = message_id_container[random.randint(0, len(message_id_container) - 1)]
    else:
        id = random.randint(1, 20000)
    print(f"sm {int(id)}")


def query_social_value():
    if random.random() > 0.8:
        id = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id = random.randint(1, 20000)
    print(f"qsv {int(id)}")


def query_received_messages():
    if random.random() > 0.8:
        id = id_container[random.randint(0, len(id_container) - 1)]
    else:
        id = random.randint(1, 20000)
    print(f"qrm {int(id)}")


if __name__ == '__main__':
    for k in range(1, 101):
        with open(f'data/random{k}.txt', 'w') as file:
            sys.stdout = file
            for i in range(5):
                for j in range(1600):
                    add_person()
                for j in range(1200):
                    if (j % 10 == 0):
                        add_relation()
                    if (j % 50 == 0):
                        add_to_group()
                        modify_relation()
                        add_message()
                        add_group()
                    if (j % 70 == 0):
                        send_message()
                    if (j % 100 == 0):
                        query_value()
                        query_circle()
                        query_block_sum()
                        query_triple_sum()
                        query_group_value_sum()
                        query_group_age_var()
                        query_best_acquaintance()
                        query_couple_sum()
                        send_message()
                        query_social_value()
                        query_received_messages()
                    if (j % 200 == 0):
                        del_from_group()
        os.system(f'java -jar code.jar<data/random{k}.txt >ans/ans{k}.txt')
