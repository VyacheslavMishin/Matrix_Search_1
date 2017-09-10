import time

# 37344, ~ 1,83 sec. -> ..., 1,78 sec. -> ..., 1,73 -> ..., 1,70 sec. -> ..., 1,67 sec. -> ..., 1,61 sec. -> ..., 1,57 sec.
amount = 0

control_lst = range(7)
control_lst_dom = []

A = []
for i in range(7):
    A.append(i)

for i in A:
    for j in A:
        buff = [i, j]
        control_lst_dom.append(buff)
        buff = []


B = A[::-1]
B.pop(0)

print("\n")
for i in A:
    for j in B:
        buff = [j, i]
        control_lst_dom.append(buff)
        buff = []

for item in control_lst_dom:
    if control_lst_dom.count(item) > 1:
        control_lst_dom.remove(item)
for item in control_lst_dom:
    if control_lst_dom.count(item) > 1:
        control_lst_dom.remove(item)

lst_0 = range(7)

# Алгоритм функции основан на решении системы линейных уравнений, составленных по условию задачи.
# Система линейных уравнений имеет в своём решении 7 свободных параметров.
# Поэтому программа с помощью 7 вложенных циклов перебирает 7^7 = 823 543 возможных набора (Вместо десятка триллиарда вариантов при переборе всех домино или всех возможных наборов чисел).
# Сумма элементов получаемых матриц удовлетворяет условию задачи, поэтому достаточно проверить, что матрица составлена из домино.

def matrix_searcher(amount_var):
    for x_8 in lst_0:
        for x_10 in lst_0:
            for x_11 in lst_0:

                r = x_10 + x_11
                x_5 = -x_8 + r

                if (x_5 >= 0) and (x_5 <= 6):
                    for x_12 in lst_0:

                        x_9 = 13 - r - x_12

                        if (x_9 >= 0) and (x_9 <= 6):
                            for x_16 in lst_0:

                                X_1 = x_8 + x_12 + x_16
                                x_4 = 13 - X_1

                                if (x_4 >= 0) and (x_4 <= 6):
                                    for x_15 in lst_0:

                                        X_2 = x_15 + x_16
                                        x_2 = - 13 - x_10 + x_11 + X_2 + X_1
                                        b = x_11 + x_15

                                        if (x_2 >= 0) and (x_2 <= 6):
                                            for x_14 in lst_0:

                                                a = 13 - x_14
                                                l = a - X_1
                                                m = l - X_2

                                                x_7 = - x_10 - m

                                                if (x_7 >= 0) and (x_7 < 7):
                                                    x_1 = x_15 - l

                                                    if (x_1 >= 0) and (x_1 < 7):
                                                        x_13 = a - X_2

                                                        if (x_13 >= 0) and (x_13 < 7):
                                                            x_3 = 13 - x_7 - b

                                                            if (x_3 >= 0) and (x_3 < 7):
                                                                x_6 = 13 + m - x_11

                                                                if (x_6 < 0) or (x_6 > 6):
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                                else:
                                                    continue

                                                cont = 0

                                                temp_lst = [[x_1, x_5], [x_2, x_6], [x_3, x_7], [x_4, x_8],
                                                            [x_9, x_13],
                                                            [x_10, x_14], [x_11, x_15], [x_12, x_16]]

                                                for item_c in control_lst_dom:
                                                    if temp_lst.count(item_c) > 1:
                                                        cont += 1
                                                        break

                                                if cont:
                                                    continue
                                                else:
                                                    print(str(x_1) + " " + str(x_2) + " " + str(x_3) + " " + str(x_4) + "\n" + str(x_5) + " " + str(x_6) + " " + str(x_7) + " " + str(x_8) + "\n" + str(x_9) + " " + str(x_10) + " " + str(x_11) + " " + str(x_12) + "\n" + str(x_13) + " " + str(x_14) + " " + str(x_15) + " " + str(x_16))
                                                    print("\n")
                                                    amount_var += 1
    return amount_var


def timed(f, *args, n_iter=10):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


amount = 0

print("matrix_searcher run time: ")
# print(timed(matrix_searcher, amount))
print("matrix_searcher result: ")
print(matrix_searcher(amount))
