# pip install matplotlib
import matplotlib.pyplot as plt
import math
import numpy
# pip install texttable
from texttable import Texttable

def calculate_coefficients(data):
    t_sum = 0
    y_sum = 0
    t2_sum = 0
    y2_sum = 0
    ty_sum = 0
    for i,d in enumerate(data):
        t = d[0]
        t_sum += t
        y = d[1]
        y_sum += y

        t2 = t*t
        y2 = y*y
        ty = t*y
        data[i].append(t2)
        t2_sum += t2
        data[i].append(y2)
        y2_sum += y2
        data[i].append(ty)
        ty_sum += ty

    data.append([t_sum, y_sum, t2_sum, y2_sum, ty_sum])
    t = Texttable()
    t.add_rows([["t", "y", "t2", "y2", "ty"], *data])
    print(t.draw())

    n = len(data) - 1
    m4 = numpy.array([[n,t_sum],[t_sum,t2_sum]])
    v4 = numpy.array([y_sum, ty_sum])
    r = numpy.linalg.solve(m4, v4)
    return r

def standard_deviation(data_list):
    y_average = sum(data_list) / len(data_list)
    s = 0
    for i in data_list:
        s += math.pow(i - y_average, 2)
    d_dispersion = s / (len(data_list) - 1)
    return standard_deviation.__name__, math.sqrt(d_dispersion)

def print_trend_equation(a0, a1):
    print("a0:", a0, "a1:", a1)
    print("Yx = ", round(a0, 4), "+", round(a1, 4), "* x")

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
    a0a1 = calculate_coefficients(data_list)
    print_trend_equation(*a0a1)
    y_list = [y for t,y,*x in data_list[:len(data_list) - 1]]
    print(standard_deviation(y_list))

    print(correlation_coefficient(data_list[len(data_list) - 1 :][0]))

    t_list = [t for t,*x in data_list[:len(data_list) - 1]]
    linear_regression = retrospection_period(t_list, *a0a1)
    t = Texttable()
    t.add_rows([["t", "linear_regression"], *linear_regression])
    print(t.draw())

    forecast_linear_regression = retrospection_period([6, 7, 8, 9, 10], *a0a1)
    t = Texttable()
    t.add_rows([["t", "forecast_linear_regression"], *forecast_linear_regression])
    print(t.draw())

    growth_rate = math.pow(y_list[len(y_list) - 1]/y_list[0],0.25)
    print("growth_rate:", growth_rate)

    forecast_rates_of_growth = []
    y_last = y_list[0]
    forecast_rates_of_growth.append([1, y_last])
    for i in range(2,11):
        y_last = y_last * growth_rate
        forecast_rates_of_growth.append([i, y_last])
    t = Texttable()
    t.add_rows([["t", "forecast_rates_of_growth"], *forecast_rates_of_growth])
    print(t.draw())

    print(10*"=","chart data",10*"=")
    linear_result = linear_regression + forecast_linear_regression
    rates_of_growth_result = forecast_rates_of_growth

    t = Texttable()
    t.add_rows([["t", "chart data linear_regression"], *linear_result])
    print(t.draw())

    t = Texttable()
    t.add_rows([["t", "chart data rates_of_growth"], *rates_of_growth_result])
    print(t.draw())

    fig, ax = plt.subplots()
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.set_title(title)

    ax.plot([t for t,y in rates_of_growth_result],
            [y for t,y in rates_of_growth_result], label="за темпами зростяння")

    ax.plot([t for t,y in linear_result],
            [y for t,y in linear_result], label="лінійний")

    ax.legend()
    plt.show()

def main():
    profit_list_14 = [[1,2354], [2,2390], [3,2420], [4,2500], [5,2560]]
    # profit_list_1 = [[1,3093], [2,3150], [3,3170], [4,3210], [5,3220]]
    profit_list = profit_list_14

    costs_list_14 = [[1,0.65], [2,0.60], [3,0.76], [4,0.68], [5,0.70]]
    # costs_list_1 = [[1,0.76], [2,0.78], [3,0.64], [4,0.71], [5,0.68]]
    costs_list = costs_list_14

    capital_list_14 = [[1,22870], [2,24200], [3,26100], [4,28200], [5,29800]]
    # capital_list_1 = [[1,26300], [2,26500], [3,28200], [4,29600], [5,31100]]
    capital_list = capital_list_14

    do_main(profit_list, "прибуток")
    do_main(costs_list, "витрати")
    do_main(capital_list, "капітал")

if __name__ == "__main__":
    main()