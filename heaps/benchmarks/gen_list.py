import random
import json


def random_list():
    random_list = []
    for _ in range(150000):
        random_list.append(random.randint(1, 30000))
    with open("list.json", 'w') as file:
        json.dump(random_list, file)

if __name__ == "__main__":
    random_list()