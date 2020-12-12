import math

def average_value(data_list):
    return round(sum(data_list) / len(data_list), 2)

def dispersion_pow2(data_list, average):
    s = 0
    for i in data_list:
        s += math.pow(i - average, 2)
    return round(s / (len(data_list) - 1), 2)

def fisher_criterion(dispersion1, dispersion2):
    f = dispersion1 / dispersion2 if dispersion1 > dispersion2 else dispersion2 / dispersion1
    return round(f, 3)


def student_t_criterion(average1, average2, dispersion1_pow2, dispersion2_pow2, n1, n2):
    t1 = abs(average1 - average2)
    t2 = math.sqrt((n1 - 1) * dispersion1_pow2 + (n2 - 1) * dispersion2_pow2)
    t3 = math.sqrt((n1*n2 * (n1 + n2 - 2)) / (n1 + n2))
    t = (t1 / t2) * t3
    return t

def main():

    data = [14.1, 9.3, 19.4, 19.7, 5.4, 24.2, 13.8, 24.5, 14.7, 16.6, 5.6, 16.2, 25.3, 11.9, 18.5]
    # data = [799, 864, 990, 1163, 1140, 1173, 1290, 1302, 1295, 1355, 1464, 1559, 1581, 1931, 2032, 2260, 2093, 2123, 2210, 2130]
    data1 = data[:len(data) // 2]
    print("data1", data1)
    data2 = data[len(data) // 2:]
    print("data2", data2)

    average1 = average_value(data1)
    print("average1", average1)
    average2 = average_value(data2)
    print("average2", average2)

    dispersion1_pow2 = dispersion_pow2(data1, average1)
    print("dispersion1_pow2", dispersion1_pow2)
    dispersion2_pow2 = dispersion_pow2(data2, average2)
    print("dispersion2_pow2", dispersion2_pow2)

    f = fisher_criterion(dispersion1_pow2, dispersion2_pow2)
    print("fisher criterion", f)

    t = student_t_criterion(average1, average2, dispersion1_pow2, dispersion2_pow2, len(data1), len(data2))
    print("student t criterion", t)
    
if __name__ == "__main__":
    main()