import csv
with open('tracking.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    next(reader, None)
    count = 0
    summa = 0
    delay_count = 0
    for i in reader:
        summa += int(i[14])
        count += 1
        if int (i[14]) >= 400:
            delay_count += 1

    avg = summa / count
    print("Average latency = {}".format(avg))
    print("Number of times latency reached over 400 ms = {}".format(delay_count))
