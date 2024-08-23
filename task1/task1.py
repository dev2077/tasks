from sys import argv

script, n, m = argv
n = int(n)
m = int(m)

def generate_arr(n):
    array = []
    for i in range(1, n + 1):
        array.append(i)
    return array

def get_loop(i, n):
    return i % n

def find_path(array, m, n):
    result_array = []
    temp_array = []
    i = 0
    result = ''
    while True:
        temp_array.append(array[get_loop(i, n)])
        if len(temp_array) == m:
            result_array.append(temp_array)
            if temp_array[m - 1] == array[0]:
                break
            temp_array = []
            i -= 1
        i += 1
    if result_array:
        for r in result_array:
            result += str(r[0])
        return result

array = generate_arr(n)

count = 0
if len(array) > 0:
    result_array = find_path(array, m, n)
    print(result_array)
