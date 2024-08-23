from sys import argv
import json

script, path1, path2, path3 = argv

def get_values(values):
    result = {}
    for i in values['values']:
        result[i["id"]] = i["value"]
    return result

def form_report(values, tests, key):
    for test in tests[key]:
        id1 = test.get('id')
        if id1 in values.keys():
            test['value'] = values[test.get('id')]
        if 'values' in test.keys():
            form_report(values, test, 'values')

    return tests

def open_file(file):
    with open(file) as json_file:
        json_data = json.load(json_file)
    return json_data

def save_file(file, result):
    with open(file, 'w') as json_file:
        json.dump(result, json_file)

values = open_file(path1)
tests = open_file(path2)
result = form_report(get_values(values), tests, 'tests')
save_file(path3, result)