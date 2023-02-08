def bubble_sort(l):
    ordered = False
    while not ordered:
        ordered = True
        for idx, value in enumerate(l):
            if idx == 0:
                continue

            if value < l[idx - 1]:
                ordered = False
                temp = value
                l[idx] = l[idx - 1]
                l[idx - 1] = temp
    return l


if __name__ == "__main__":
    import time

    lis = list(range(100, 0, -1))
    start = time.time()
    print(bubble_sort(lis))
    end = time.time()
    print(f"{round(end - start, 8)} seconds, length: {len(lis)}")
