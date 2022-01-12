def part1():
    with open("Day13.txt", "r") as file:
        lines = []
        line = ""
        while line != "\n":
            line = file.readline()
            lines.append(line[:-1])
        lines.pop()

        folds = []
        for line in file.readlines():
            folds.append(line[:-1])

        print(folds)
        points_set = set(lines)
        new_points = set(lines)
        print(points_set)

        for fold in folds:
            points_set = new_points
            new_points = set()
            n_fold = int(fold.split("=")[1])
            fold_type = fold.split("=")[0][-1:]
            for point in points_set:
                if fold_type == "y":
                    firs_part = point.split(",")[0]
                    y_coord = int(point.split(",")[1])
                    if y_coord < n_fold:
                        new_points.add(point)
                    elif y_coord > n_fold:
                        new_coord = n_fold - abs(y_coord-n_fold)
                        new_pos = firs_part + "," + str(new_coord)
                        print("New", new_pos)
                        new_points.add(new_pos)
                else:
                    second_part = point.split(",")[1]
                    x_coord = int(point.split(",")[0])
                    if x_coord < n_fold:
                        new_points.add(point)
                    elif x_coord > n_fold:
                        new_coord = n_fold - abs(x_coord-n_fold)
                        new_pos = str(new_coord) + "," + second_part
                        print("New", new_pos)
                        new_points.add(new_pos)
        print(new_points)
        for i in range(50):
            cadena = ""
            for j in range(50):
                point = str(j) + "," + str(i)
                if point in new_points:
                    cadena += "#"
                else:
                    cadena += "."
            print(cadena)


if __name__ == "__main__":
    part1()
