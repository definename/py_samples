# pip install matplotlib
import matplotlib.pyplot as plt
import math
import numpy
# pip install texttable
from texttable import Texttable

def a0a1_linear_func(data):
    y_sum = x1_sum = x2_sum = x1_2_sum = x1x2_sum = x1y_sum = x2_2_sum = x2y_sum = 0
    data_list_result = [[] for i in range(len(data))]
    for i,d in enumerate(data):
        y = d[0]
        data_list_result[i].append(y)
        y_sum += y

        x1 = d[1]
        data_list_result[i].append(x1)
        x1_sum += x1

        x2 = d[2]
        data_list_result[i].append(x2)
        x2_sum += x2

        x1_2 = x1 * x1
        data_list_result[i].append(x1_2)
        x1_2_sum += x1_2

        x1x2 = x1 * x2
        data_list_result[i].append(x1x2)
        x1x2_sum += x1x2

        x1y = x1 * y
        data_list_result[i].append(x1y)
        x1y_sum += x1y

        x2_2 = x2 * x2
        data_list_result[i].append(x2_2)
        x2_2_sum += x2_2

        x2y = x2 * y
        data_list_result[i].append(x2y)
        x2y_sum += x2y

    t = Texttable()
    t.set_cols_dtype(["f" for i in range(8)])
    t.set_cols_width([15 for i in range(8)])
    t.add_rows([["y","x1","x2","x1_2","x1x2","x1y","x2_2","x2y"], *data_list_result])
    print(t.draw())

    t = Texttable()
    t.add_rows([["y_sum","x1_sum","x2_sum","x1_2_sum","x1x2_sum","x1y_sum","x2_2_sum","x2y_sum"],
                [y_sum,x1_sum,x2_sum,x1_2_sum,x1x2_sum,x1y_sum,x2_2_sum,x2y_sum]])
    print(t.draw())

    n = len(data_list_result)
    m = numpy.array([
        [n,x1_sum,x2_sum],
        [x1_sum,x1_2_sum,x1x2_sum],
        [x2_sum,x1x2_sum,x2_2_sum]
        ])
    v = numpy.array([y_sum,x1y_sum,x2y_sum])
    r = numpy.linalg.solve(m, v)
    return r

def trend_equation_linear(a0,a1,a2,x1=None,x2=None):
    ret = None
    if x1 == None and x2 == None:
        print("a0: %.6f a1: %.6f a2: %.6f"%(a0,a1,a2))
        print("trend_equation_linear: Yx = %.6f + %.6f * x1 + %.6f * x2"%(a0,a1,a2))
    else:
        ret = a0+a1*x1+a2*x2
    return ret

def pair_correlation_coefficient(data_list):
    t_sum = y_sum = t2_sum = y2_sum = ty_sum = 0
    for d in data_list:
        t = d[0]
        t_sum += t
        y = d[1]
        y_sum += y
        t2_sum += (t*t)
        y2_sum += (y*y)
        ty_sum += (t*y)
    n = len(data_list)
    r = (n * ty_sum - t_sum * y_sum) / math.pow((n*t2_sum - math.pow(t_sum, 2)) * (n*y2_sum - math.pow(y_sum, 2)), 0.5)
    return r

def multi_correlation_coefficient(r_x1x2, r_yx1, r_yx2):
    r = math.sqrt((math.pow(r_yx1,2)+math.pow(r_yx2,2)-2*r_x1x2*r_yx1*r_yx2)/(1-math.pow(r_x1x2,2)))
    return r

def do_main(data_list,costs_capital_forecast_lb1):
    # a0a1a2 ###################################################
    a0a1a2_linear = a0a1_linear_func(data_list)
    trend_equation_linear(*a0a1a2_linear)

    # y_theory #################################################
    y_theory_list = [[] for i in range(len(data_list))]
    for i,d in enumerate(data_list):
        y=d[0];x1=d[1];x2=d[2]
        y_theory_list[i].append(trend_equation_linear(*a0a1a2_linear,x1,x2))
    t = Texttable()
    t.add_rows([["y_theory"], *y_theory_list])
    print(t.draw())

    # y_theory chart ############################################
    fig, ax = plt.subplots()
    ax.set_xlabel("t")
    ax.set_ylabel("прибуток")
    ax.set_title("теоретичні однофакторні регресії ")
    t_list_chart = [i for i in range(len(y_theory_list))]
    ax.plot(t_list_chart,y_theory_list,label="теоретичні значення прибутку")
    ax.legend()
    plt.show()

    r_x1x2 = pair_correlation_coefficient([[x1,x2] for y,x1,x2 in data_list])
    print("correlation_coefficient x1x2: %.6f"%(r_x1x2))

    r_yx1 = pair_correlation_coefficient([[y,x1] for y,x1,x2 in data_list])
    print("pair_correlation_coefficient yx1: %.6f"%(r_yx1))
    
    r_yx2 = pair_correlation_coefficient([[y,x2] for y,x1,x2 in data_list])
    print("pair_correlation_coefficient yx2: %.6f"%(r_yx2))

    Ry_x1x2 = multi_correlation_coefficient(r_x1x2,r_yx1,r_yx2)
    print("multi_correlation_coefficient Ry_x1x2: %.10f"%Ry_x1x2)

    Rx2_yx1 = multi_correlation_coefficient(r_yx1,r_yx2,r_x1x2)
    print("multi_correlation_coefficient Ry_x1x2: %.10f"%Rx2_yx1)

    Rx1_yx2 = multi_correlation_coefficient(r_yx2,r_yx1,r_x1x2)
    print("multi_correlation_coefficient Rx1_yx2: %.10f"%Rx1_yx2)

    # forecast ####################################################
    for i,d in enumerate(costs_capital_forecast_lb1):
        costs_capital_forecast_lb1[i].append(data_list[i][0])
        costs_capital_forecast_lb1[i].append(trend_equation_linear(*a0a1a2_linear,d[0],d[1]))
    t = Texttable()
    t.add_rows([["витрати(прогноз лб1)","капітал(прогноз лб1)","прибуток факт","прибуток прогноз"], *costs_capital_forecast_lb1])
    print(t.draw())

def main():
    # # variant methoda
    # do_main([
    #     [3093,0.76,26300],
    #     [3150,0.78,26500],
    #     [3170,0.64,28200],
    #     [3210,0.71,29600],
    #     [3220,0.68,31100],
    #     [3093,0.76,26400],
    #     [3250,0.68,26690],
    #     [3170,0.54,28200],
    #     [3310,0.81,29900],
    #     [4220,0.98,31100]
    #     ],
    #     [
    #     [0.760,25800],
    #     [0.737,27070],
    #     [0.714,28340],
    #     [0.691,29610],
    #     [0.668,30880]
    #     ])

    # # variant 1
    # do_main([
    #         [3093,0.76,26300],
    #         [3150,0.78,26500],
    #         [3170,0.64,28200],
    #         [3210,0.71,29600],
    #         [3220,0.68,31100],
    #         [3193,0.74,26400],
    #         [3050,0.76,26500],
    #         [3180,0.54,28300],
    #         [3110,0.81,29400],
    #         [3320,0.87,31200]
    #         ],
    #         [
    #         [0.760,25800],
    #         [0.737,27070],
    #         [0.714,28340],
    #         [0.691,29610],
    #         [0.668,30880]
    #         ])

    # variant 14
    do_main([
            [2354,0.65,22870],
            [2390,0.60,24200],
            [2420,0.76,26100],
            [2500,0.68,28200],
            [2560,0.70,29800],
            [2354,0.65,22870],
            [2390,0.60,24200],
            [2420,0.76,26100],
            [2500,0.68,28200],
            [2560,0.70,29800]
            ],
            [
            [0.642,22662],
            [0.660,24448],
            [0.678,26234],
            [0.696,28020],
            [0.714,29806]
            ])

if __name__ == "__main__":
    main()