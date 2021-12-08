# Refactor the code without changing the script's behavior.
# Attach any code you used to solve the task.
# Copyright 2021 Continental AG

# The code filters and separates box labels with x0, y0, x1, y1 coordinates and a class type
def main(labels):
    # parse
    for i in range(len(labels)):
        obj = labels[i].split(",")
        obj2 = []
        for o in obj[:-1]:
            obj2.append(float(o))
        obj2.append(int(obj[4]))
        labels[i] = obj2
    #print("OBJ2", obj2)
    res = labels
    # filter small labels
    res2 = []
    for i in range(len(res)):
        if not abs(res[i][0]-res[i][2]) < 2 and not abs(res[i][1]-res[i][3]) < 12:
            res2.append(res[i])
    # filter pedestrians
    res3 = []
    for i in range(len(res)):
        if res[i][4] == 5:
            res3.append(res[i])
    return res2, res3
res = main(["0,1,2.2,3,5", "0, 0, 21, 42, 5"])
print(res)
