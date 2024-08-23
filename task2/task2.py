from sys import argv

script, circle_points_path, points_path = argv
def open_file(path):
    arr = open(path)
    array = []
    start_range = float(10**(-38))
    end_range = float(10**(38))

    for a in arr:
        a = a.split()
        for i in range(len(a)):

            a[i] = float(a[i])
            if len(a) > 2 or ((a[i] < start_range or a[i] > end_range) and a[i] != 0.0):
                exit()
        try:
            array.append(a)
        except:
            print(f"couldn't parse : {a}")
            continue
    return array

def calculate(center_points, radius, points):
    for dots in points:
        if len(dots) == 2:
            x = (dots[0] - center_points[0]) ** 2
            y = (dots[1] - center_points[1]) ** 2
            xy = x + y

            if xy == radius:
                print('0')
            elif xy < radius:
                print('1')
            else:
                print('2')

coord_data = open_file(circle_points_path)

if coord_data:
    try:
        center_points = coord_data[0]
        radius = coord_data[1][0] ** 2
    except:
        exit(0)

points = open_file(points_path)

if points and len(points) <= 100:
    calculate(center_points, radius, points)