# pip install matplotlib
# import matplotlib.pyplot as plt
import math
import numpy
import copy
# pip install texttable
from texttable import Texttable

def a0a1_linear(data):
    t_sum = y_sum = t2_sum = y2_sum = ty_sum = 0
    data_list_result = [[] for i in range(len(data))]
    for i,d in enumerate(data):
        t = d[0]
        data_list_result[i].append(t)
        t_sum += t

        y = d[1]
        data_list_result[i].append(y)
        y_sum += y

        t2 = t*t
        data_list_result[i].append(t2)
        t2_sum += t2

        y2 = y*y
        data_list_result[i].append(y2)
        y2_sum += y2

        ty = t*y
        data_list_result[i].append(ty)
        ty_sum += ty

    t = Texttable()
    t.add_rows([["t", "y", "t2", "y2", "ty"], *data_list_result])
    print(t.draw())

    t = Texttable()
    t.add_rows([["t_sum", "y_sum", "t2_sum", "y2_sum", "ty_sum"],
                [t_sum, y_sum, t2_sum, y2_sum, ty_sum]])
    print(t.draw())

    n = len(data_list_result)
    m4 = numpy.array([
        [n,t_sum],
        [t_sum,t2_sum]
        ])
    v4 = numpy.array([y_sum, ty_sum])
    r = numpy.linalg.solve(m4, v4)
    return r

def a0a1_hyperbola(data):
    t_sum = y_sum = one_div_t_sum = y_div_t_sum = one_div_t2_sum = 0
    data_list_result = [[] for i in range(len(data))]
    for i,d in enumerate(data):
        t = d[0]
        data_list_result[i].append(t)
        t_sum += t

        y = d[1]
        data_list_result[i].append(y)
        y_sum += y

        one_div_t = 1 / t
        data_list_result[i].append(one_div_t)
        one_div_t_sum += one_div_t

        y_div_t = y / t
        data_list_result[i].append(y_div_t)
        y_div_t_sum += y_div_t

        one_div_t2 = ((1 / t) * (1 / t))
        data_list_result[i].append(one_div_t2)
        one_div_t2_sum += one_div_t2

    t = Texttable()
    t.set_cols_dtype(["f", "f", "f", "f", "f",])
    t.set_cols_width([15, 15, 15, 15, 15,])
    t.set_precision(10)
    t.add_rows([["t", "y", "one_div_t", "y_div_t", "one_div_t2"], *data_list_result])
    print(t.draw())

    t = Texttable()
    t.set_cols_dtype(["f", "f", "f", "f", "f",])
    t.set_cols_width([15, 15, 15, 15, 15,])
    t.set_precision(10)
    t.add_rows([["t_sum", "y_sum", "one_div_t_sum", "y_div_t_sum", "one_div_t2_sum"],
                [t_sum, y_sum, one_div_t_sum, y_div_t_sum, one_div_t2_sum]])
    print(t.draw())

    n = len(data_list_result)
    m4 = numpy.array([
        [n,one_div_t_sum],
        [one_div_t_sum,one_div_t2_sum]
        ])
    v4 = numpy.array([y_sum,y_div_t_sum])
    r = numpy.linalg.solve(m4,v4)
    return r

def a0a1a3_parabola(data):
    t_sum = y_sum = t2_sum = t3_sum = t4_sum = ty_sum = t2y_sum = 0
    data_list_result = [[] for i in range(len(data))]
    for i,d in enumerate(data):
        t = d[0]
        data_list_result[i].append(t)
        t_sum += t

        y = d[1]
        data_list_result[i].append(y)
        y_sum += y

        t2 = t * t
        data_list_result[i].append(t2)
        t2_sum += t2

        t3 = t * t * t
        data_list_result[i].append(t3)
        t3_sum += t3

        t4 = t * t * t * t
        data_list_result[i].append(t4)
        t4_sum += t4

        ty = t * y
        data_list_result[i].append(ty)
        ty_sum += ty

        t2y = (t * t) * y
        data_list_result[i].append(t2y)
        t2y_sum += t2y

    t = Texttable()
    t.set_cols_dtype(["f", "f", "f", "f", "f", "f", "f"])
    t.set_cols_width([15, 15, 15, 15, 15, 15, 15,])
    t.add_rows([["t", "y", "t2", "t3", "t4", "ty", "t2y"], *data_list_result])
    print(t.draw())

    t = Texttable()
    t.set_cols_dtype(["f", "f", "f", "f", "f", "f", "f"])
    t.set_cols_width([15, 15, 15, 15, 15, 15, 15,])
    t.add_rows([["t_sum", "y_sum", "t2_sum", "t3_sum", "t4_sum", "ty_sum", "t2y_sum"],
                [t_sum, y_sum, t2_sum, t3_sum, t4_sum, ty_sum, t2y_sum]])
    print(t.draw())

    n = len(data_list_result)
    m4 = numpy.array([
        [n,t_sum,t2_sum],
        [t_sum,t2_sum,t3_sum],
        [t2_sum,t3_sum,t4_sum]
        ])
    v4 = numpy.array([y_sum,ty_sum,t2y_sum])
    r = numpy.linalg.solve(m4,v4)
    return r

def standard_deviation_y_theory(y_list):
    s = 0
    for y,y_theory in y_list:
        s += math.pow(y - y_theory, 2)
    d_dispersion = s / (len(y_list))
    return math.sqrt(d_dispersion)

def trend_equation_linear(a0, a1):
    print("a0:", a0, "a1:", a1)
    print(trend_equation_linear.__name__, ": Yx = ", round(a0, 4), "+", round(a1, 4), "* x")

def trend_equation_hyperbola(a0, a1):
    print("a0:", a0, "a1:", a1)
    print(trend_equation_hyperbola.__name__, ": Yx = ", round(a0, 4), "+", round(a1, 4), "/ x")

def trend_equation_parabola(a0, a1, a2):
    print("a0:", a0, "a1:", a1, "a2", a2)
    print(trend_equation_parabola.__name__, ": Yx = ", round(a0, 4), "+", round(a1, 4), "* x +", round(a2, 4), "* x2")

def correlation_coefficient(sum_list):
    t_sum = sum_list[0]
    y_sum = sum_list[1]
    t2_sum = sum_list[2]
    y2_sum = sum_list[3]
    ty_sum = sum_list[4]
    r = (5 * ty_sum - t_sum * y_sum) / math.pow((5*t2_sum - math.pow(t_sum, 2)) * (5*y2_sum - math.pow(y_sum, 2)), 0.5)
    return correlation_coefficient.__name__, r

def retrospection_period(t_list, a0, a1):
    result_list = []
    for t in t_list:
        result_list.append([t, a0 + a1*t])
    return result_list

def do_main(data_list, title):
    print(10*"=",title, 10*"=")

    a0a1 = a0a1_linear(copy.deepcopy(data_list))
    trend_equation_linear(*a0a1)
    # deviation ###############################################
    y_list = []
    for i,xy in enumerate(data_list):
        x,y = xy
        y_theory = a0a1[0] + a0a1[1] * x
        y_list.append([y,y_theory])
    print("standard_deviation_y_theory:", standard_deviation_y_theory(y_list))

    a0a1 = a0a1_hyperbola(copy.deepcopy(data_list))
    trend_equation_hyperbola(*a0a1)
    # deviation ###############################################
    y_list = []
    for i,xy in enumerate(data_list):
        x,y = xy
        y_theory = a0a1[0] + a0a1[1] / x
        y_list.append([y,y_theory])
    print("standard_deviation_y_theory:", standard_deviation_y_theory(y_list))

    a0a1a2 = a0a1a3_parabola(copy.deepcopy(data_list))
    trend_equation_parabola(*a0a1a2)
    # deviation ###############################################
    y_list = []
    for i,xy in enumerate(data_list):
        x,y = xy
        y_theory = a0a1a2[0] + (a0a1a2[1] * x) + (a0a1a2[2] * (x * x))
        y_list.append([y,y_theory])
    print("standard_deviation_y_theory:", standard_deviation_y_theory(y_list))

    # y_list = [y for t,y,*x in data_list[:len(data_list) - 1]]
    # print(standard_deviation(y_list))

    # print(correlation_coefficient(data_list[len(data_list) - 1 :][0]))

    # t_list = [t for t,*x in data_list[:len(data_list) - 1]]
    # linear_regression = retrospection_period(t_list, *a0a1)
    # t = Texttable()
    # t.add_rows([["t", "linear_regression"], *linear_regression])
    # print(t.draw())

    # forecast_linear_regression = retrospection_period([6, 7, 8, 9, 10], *a0a1)
    # t = Texttable()
    # t.add_rows([["t", "forecast_linear_regression"], *forecast_linear_regression])
    # print(t.draw())

    # growth_rate = math.pow(y_list[len(y_list) - 1]/y_list[0],0.25)
    # print("growth_rate:", growth_rate)

    # forecast_rates_of_growth = []
    # y_last = y_list[0]
    # forecast_rates_of_growth.append([1, y_last])
    # for i in range(2,11):
    #     y_last = y_last * growth_rate
    #     forecast_rates_of_growth.append([i, y_last])
    # t = Texttable()
    # t.add_rows([["t", "forecast_rates_of_growth"], *forecast_rates_of_growth])
    # print(t.draw())

    # print(10*"=","chart data",10*"=")
    # linear_result = linear_regression + forecast_linear_regression
    # rates_of_growth_result = forecast_rates_of_growth

    # t = Texttable()
    # t.add_rows([["t", "chart data linear_regression"], *linear_result])
    # print(t.draw())

    # t = Texttable()
    # t.add_rows([["t", "chart data rates_of_growth"], *rates_of_growth_result])
    # print(t.draw())

    # fig, ax = plt.subplots()
    # ax.set_xlabel("t")
    # ax.set_ylabel("y")
    # ax.set_title(title)

    # ax.plot([t for t,y in rates_of_growth_result],
    #         [y for t,y in rates_of_growth_result], label="за темпами зростяння")

    # ax.plot([t for t,y in linear_result],
    #         [y for t,y in linear_result], label="лінійний")

    # ax.legend()
    # plt.show()

def main():
    # ==== P(Z) ====
    # profit_list_14 = [[1,2354], [2,2390], [3,2420], [4,2500], [5,2560]]
    # profit_list_5 = [[0.81,1955],[0.74,2170],[0.86,2210],[0.80,2280],[0.82,2400]]

    profit_list_p_ot_z_lb = [[337.2, 428.2],[356.3, 451],[367.1, 456.8],[390.7, 495.8],[409.4, 515.3]]
    profit_list = profit_list_p_ot_z_lb

    # costs_list_14 = [[1,0.65], [2,0.60], [3,0.76], [4,0.68], [5,0.70]]
    # costs_list_5 = [[1,0.81], [2,0.74], [3,0.86], [4,0.80], [5,0.82]]
    # costs_list = costs_list_14

    # capital_list_14 = [[1,22870], [2,24200], [3,26100], [4,28200], [5,29800]]
    # capital_list_5 = [[1,34052], [2,34800], [3,35600], [4,36200], [5,38100]]
    # capital_list = capital_list_14

    do_main(profit_list, "прибуток P(Z)")
    # do_main(costs_list, "витрати")
    # do_main(capital_list, "капітал")

    # ==== P(K) ====
    profit_list_p_ot_k_lb = [[79.7, 428.2], [87.3, 451], [95.4, 456.8], [97.2, 495.8], [100.6, 515.3]]
    profit_list = profit_list_p_ot_k_lb
    do_main(profit_list, "прибуток P(K)")

if __name__ == "__main__":
    main()