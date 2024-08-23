from sys import argv

script, path = argv
def open_file(path):
    arr = open(path)
    array = []
    for a in arr:
        try:
            array.append(int(a))
        except:
            print(f"couldn't parse : {a}")
            continue
    return array

array = open_file(path)
goal = int(sum(array) / len(array))
count = 0

for num in array:

    while num != goal:
        if num < goal:
            num += 1
            count += 1
        else:
            num -= 1
            count += 1

print(count)



