#! python3
# Choose a random winner from a list of names

import random, json, csv

def get_names_from_csv(filepath):
    name_list = []
    with open(filepath) as data_file:
        data = list(csv.reader(data_file))

    for row in data:
        if row != None:
            name_list.append(row[0])

    data_file.close()
    return name_list

def get_names_from_json(filepath):
    name_list = []

    with open(filepath) as data_file:
        data = json.load(data_file)

    for person in data["people"]:
        name_list.append(person["name"])
    
    data_file.close()
    return name_list

def choose_name(name_list):
    return random.choice(name_list)

if __name__ == "__main__":
    csv_list = get_names_from_csv('data/people.csv')
    print("Lucky CSV winner:", choose_name(csv_list))

    json_list = get_names_from_json('data/people.json')
    print("Lucky JSON winner:", choose_name(json_list))
