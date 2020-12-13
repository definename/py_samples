import math

def dispersion(data_list, average):
    s = 0
    for i in data_list:
        s += math.pow(i - average, 2)
    return round(s / (len(data_list) - 1), 2)

def student_t_criterion(average1, average2, dispersion1_pow2, dispersion2_pow2, n1, n2):
    t1 = abs(average1 - average2)
    t2 = math.sqrt((n1 - 1) * dispersion1_pow2 + (n2 - 1) * dispersion2_pow2)
    t3 = math.sqrt((n1*n2 * (n1 + n2 - 2)) / (n1 + n2))
    t = (t1 / t2) * t3
    return t

def main():

    # Метод проверки разностей средних уровней
    print(5*"=", "average difference", 5*"=")

    # USD 2014
    # https://net.dn.ua/money/stat.php?valute=12&year=2014&mon=0
    usd = [7.99, 8.65, 9.91, 11.63, 11.40, 11.74, 12.90, 13.02, 12.95, 14.64]

    # GBP 2014
    # https://net.dn.ua/money/stat.php?valute=8&year=2014&mon=0
    gbp = [13.16, 14.31, 16.48, 19.46, 19.17, 20.03, 21.58, 21.27, 20.84, 23.15]
    data = gbp

    arr1 = data[:len(data) // 2]
    print("arr1", arr1)
    arr2 = data[len(data) // 2:]
    print("arr2", arr2)

    average1 = round(sum(arr1) / len(arr1), 2)
    print("average1", average1)
    average2 = round(sum(arr2) / len(arr2), 2)
    print("average2", average2)

    dispersion1 = dispersion(arr1, average1)
    print("dispersion1", dispersion1)
    dispersion2 = dispersion(arr2, average2)
    print("dispersion2", dispersion2)

    f_calc = round(dispersion1 / dispersion2 if dispersion1 > dispersion2 else dispersion2 / dispersion1, 2)
    assert(len(arr1) - 1 == 4)
    assert(len(arr2) - 1 == 4)
    f_tabl = 6.39 # because P <= 0.05 and len(arr1) - 1 == 4 and len(arr2) - 1 = 4

    print("f_calc", f_calc)
    print("f_tabl", f_tabl)
    is_accepted = f_calc < f_tabl
    print("the hypothesis of homogeneity of dispersion is accepted:", is_accepted)
    if is_accepted:
        t_criterion_calc = round(student_t_criterion(average1, average2, dispersion1, dispersion2, len(arr1), len(arr2)), 2)
        print("t_criterion_calc:", t_criterion_calc)
        assert(len(arr1) + len(arr2) - 2 == 8)
        t_criterion_tabl = 2.31 # because P <= 0.05 and len(arr1) + len(arr2) - 2 == 8
        print("t_criterion_tabl:", t_criterion_tabl)
        print("trend exist:", t_criterion_calc > t_criterion_tabl)

    # Метод Фостера-Стьюарта
    print(5*"=", "foster–stuart", 5*"=")
    result_list = []
    for i, val in enumerate(data):
        if i == 0:
            result_list.append((None, None, None, None))
        else:
            # calculate k
            j = 0
            while j < i:
                if val < data[j]:
                    j = -1
                    break
                j += 1
            k_val = 0 if j == -1 else 1
            # calculate l
            j = 0
            while j < i:
                if val > data[j]:
                    j = -1
                    break
                j += 1
            l_val = 0 if j == -1 else 1
            # calculate s
            s_val = k_val + l_val
            # calculate d
            d_val = k_val - l_val
            result_list.append((k_val, l_val, s_val, d_val))

    print(*result_list, sep="\n")
    
    s_sum = 0
    d_sum = 0
    for k,l,s,d in result_list[1:]:
        s_sum += s
        d_sum += d
    print("s_sum:", s_sum)
    print("d_sum:", d_sum)

    assert(len(data) == 10)
    m = 3.858 # because len(data) == 10
    t_s = abs(d_sum - 0) / 1.964
    print("t_s", round(t_s, 2))

    t_d = round((s_sum - m) / 1.288, 2)
    print("t_d", t_d)

    assert(len(data) - 1 == 9)
    t_tabl = 2.26 # because len(data) - 1 == 9
    print("t_tabl", t_tabl)
    print("row trend exist:", t_s > t_tabl)
    print("dispersion trend exist:", t_d > t_tabl)

if __name__ == "__main__":
    main()