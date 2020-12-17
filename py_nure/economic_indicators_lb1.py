import math
import numpy
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
    print("Yx = ", round(a0, 4), "+", round(a1, 4), "* x")

def correlation_coefficient(sum_list):
    t_sum = sum_list[0]
    y_sum = sum_list[1]
    t2_sum = sum_list[2]
    y2_sum = sum_list[3]
    ty_sum = sum_list[4]
    r = (5 * ty_sum - t_sum * y_sum) / math.pow((5*t2_sum - math.pow(t_sum, 2)) * (5*y2_sum - math.pow(y_sum, 2)), 0.5)
    return correlation_coefficient.__name__, r

def main():
    print(5*"=", "profit", 5*"=")
    profit_list = [[1,3093], [2,3150], [3,3170], [4,3210], [5,3220]]
    print(standard_deviation([y for t,y in profit_list]))
    a0a1 = calculate_coefficients(profit_list)
    print_trend_equation(*a0a1)
    print(correlation_coefficient(profit_list[len(profit_list) -1 :][0]))

    print(5*"=", "costs", 5*"=")
    costs_list = [[1,0.76], [2,0.78], [3,0.64], [4,0.71], [5,0.68]]
    print(standard_deviation([y for t,y in costs_list]))
    a0a1 = calculate_coefficients(costs_list)
    print_trend_equation(*a0a1)
    print(correlation_coefficient(costs_list[len(costs_list) -1 :][0]))

    print(5*"=", "capital", 5*"=")
    capital_list = [[1,26300], [2,26500], [3,28200], [4,29600], [5,31100]]
    print(standard_deviation([y for t,y in capital_list]))
    a0a1 = calculate_coefficients(capital_list)
    print_trend_equation(*a0a1)
    print(correlation_coefficient(capital_list[len(capital_list) -1 :][0]))

if __name__ == "__main__":
    main()