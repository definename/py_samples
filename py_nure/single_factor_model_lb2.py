# pip install matplotlib
import matplotlib.pyplot as plt
import math
import numpy
import copy
# pip install texttable
from texttable import Texttable

def a0a1_linear_func(data):
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

def a0a1_hyperbola_func(data):
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

def a0a1a3_parabola_func(data):
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

def trend_equation_linear(a0,a1,x=None):
    ret = None
    if x == None:
        print("a0: %.10f a1: %.10f"%(a0,a1))
        print("trend_equation_linear: Yx = %.6f + %.6f * x"%(a0,a1))
    else:
        ret = a0+a1*x
    return ret

def trend_equation_hyperbola(a0,a1,x=None):
    ret = None
    if x == None:
        print("a0: %.10f a1: %.10f"%(a0,a1))
        print("trend_equation_hyperbola: Yx = %.6f + %.6f / x"%(a0,a1))
    else:
        ret = a0+a1/x
    return ret

def trend_equation_parabola(a0,a1,a2,x=None):
    ret = None
    if x == None:
        print("a0: %.10f a1: %.10f a2: %.10f"%(a0,a1,a2))
        print("trend_equation_parabola: Yx = %.6f + %.6f * x + %.6f * x2"%(a0,a1,a2))
    else:
        ret = a0+a1*x+(a2*(x*x))
    return ret

def correlation_coefficient(data_list):
    t_sum = y_sum = t2_sum = y2_sum = ty_sum = 0
    for d in data_list:
        t = d[0]
        t_sum += t
        y = d[1]
        y_sum += y
        t2_sum += (t*t)
        y2_sum += (y*y)
        ty_sum += (t*y)
    r = (5 * ty_sum - t_sum * y_sum) / math.pow((5*t2_sum - math.pow(t_sum, 2)) * (5*y2_sum - math.pow(y_sum, 2)), 0.5)
    return r

def do_main(data_list, title):
    print(10*"=",title,"лінійна",10*"=")
    a0a1_linear = a0a1_linear_func(copy.deepcopy(data_list))
    trend_equation_linear(*a0a1_linear)
    # deviation ###############################################
    y_list_linear = []
    for xy in data_list:
        x,y = xy
        y_theory = trend_equation_linear(*a0a1_linear,x)
        y_list_linear.append([y,y_theory])
    standard_deviation_linear = standard_deviation_y_theory(y_list_linear)
    print("standard_deviation_y_theory linear: %.6f"%(standard_deviation_linear))

    print(10*"=",title,"гіпербола", 10*"=")
    a0a1_hyperbola = a0a1_hyperbola_func(copy.deepcopy(data_list))
    trend_equation_hyperbola(*a0a1_hyperbola)
    # deviation ###############################################
    y_list_hyperbola = []
    for xy in data_list:
        x,y = xy
        y_theory = trend_equation_hyperbola(*a0a1_hyperbola,x)
        y_list_hyperbola.append([y,y_theory])
    standard_deviation_hyperbola = standard_deviation_y_theory(y_list_hyperbola)
    print("standard_deviation_y_theory hyperbola: %.6f"%(standard_deviation_hyperbola))

    print(10*"=",title,"парабола", 10*"=")
    a0a1a2_parabola = a0a1a3_parabola_func(copy.deepcopy(data_list))
    trend_equation_parabola(*a0a1a2_parabola)
    # deviation ###############################################
    y_list_parabola = []
    for xy in data_list:
        x,y = xy
        y_theory = trend_equation_parabola(*a0a1a2_parabola,x)
        y_list_parabola.append([y,y_theory])
    standard_deviation_parabola = standard_deviation_y_theory(y_list_parabola)
    print("standard_deviation_y_theory parabla: %.6f"%(standard_deviation_parabola))

    # correlation_coefficient ##################################
    print(title, "correlation_coefficient: %.6f"%(correlation_coefficient(data_list)))

    # y_theory #################################################
    y_theory_list = []
    for i in range(len(y_list_linear)):
        y_theory_list.append([
            i+1,
            data_list[i][1],
            data_list[i][0],
            y_list_linear[i][1],
            y_list_hyperbola[i][1],
            y_list_parabola[i][1]
            ])
    t = Texttable()
    t.add_rows([["index","Y","X "+title,"y теор. лінійна","y теор. гіпербола","y теор. парабола"], *y_theory_list])
    print(t.draw())

    # chart theory ###############################################
    fig, ax = plt.subplots()
    ax.set_xlabel("t")
    ax.set_ylabel("прибуток")
    ax.set_title("теоретичні однофакторні регресії "+title)

    # t_list_chart = [t for i,y,t,y_linear,y_hyperbola,y_parabola in y_theory_list]
    t_list_chart = [1, 2, 3, 4, 5]
    ax.plot(t_list_chart, [y for i,y,x,y_linear,y_hyperbola,y_parabola in y_theory_list], label="вихідні дані "+title)
    ax.plot(t_list_chart, [y_linear for i,y,x,y_linear,y_hyperbola,y_parabola in y_theory_list], label="лінійний "+title)
    ax.plot(t_list_chart, [y_hyperbola for i,y,x,y_linear,y_hyperbola,y_parabola in y_theory_list], label="гіпербола "+title)
    ax.plot(t_list_chart, [y_parabola for i,y,x,y_linear,y_hyperbola,y_parabola in y_theory_list], label="парабола "+title)

    ax.legend()
    plt.show()

    # forecast ##################################################
    print(10*"=",title,"прогнозування", 10*"=")
    list_factor_forecast = [[i+1,ty[0]] for i,ty in enumerate(data_list)]
    a0a1_factor_forecast = a0a1_linear_func(list_factor_forecast)
    list_profit_forecast = [[i+1,ty[1]] for i,ty in enumerate(data_list)]
    a0a1_profit_forecast = a0a1_linear_func(list_profit_forecast)
    forecast_list = []
    for i in range(6,11):
        factor_forecast = trend_equation_linear(*a0a1_factor_forecast, i)
        profit_forecast = trend_equation_linear(*a0a1_profit_forecast, i)
        profit_forecast_linear = trend_equation_linear(*a0a1_linear, factor_forecast)
        profit_forecast_hyperbola = trend_equation_hyperbola(*a0a1_hyperbola, factor_forecast)
        profit_forecast_parabola = trend_equation_parabola(*a0a1a2_parabola, factor_forecast)
        forecast_list.append([i,
                              factor_forecast,
                              profit_forecast,
                              profit_forecast_linear,
                              profit_forecast_hyperbola,
                              profit_forecast_parabola])

    t = Texttable()
    t.add_rows([["index",
                "factor_forecast "+title,
                "profit_forecast",
                "profit_forecast_linear",
                "profit_forecast_hyperbola",
                "profit_forecast_parabola"], *forecast_list])
    print(t.draw())

    # chart forecast #############################################
    fig, ax = plt.subplots()
    ax.set_xlabel("t")
    ax.set_ylabel("прибуток")
    ax.set_title("прогноз "+title)

    f_list_chart = [f for i,f,p,p_linear,p_hyperbola,p_parabola in forecast_list]
    ax.plot(f_list_chart, [p for i,f,p,p_linear,p_hyperbola,p_parabola in forecast_list], label="прогноз вихідні дані "+title)
    ax.plot(f_list_chart, [p_linear for i,f,p,p_linear,p_hyperbola,p_parabola in forecast_list], label="прозноз лінійний "+title)
    ax.plot(f_list_chart, [p_hyperbola for i,f,p,p_linear,p_hyperbola,p_parabola in forecast_list], label="прогноз гіпербола "+title)
    ax.plot(f_list_chart, [p_parabola for i,f,p,p_linear,p_hyperbola,p_parabola in forecast_list], label="прогноз парабола "+title)

    ax.legend()
    plt.show()

def main():
    # ==== P(Costs) ====
    # costs_profit_lb = [[337.2, 428.2],[356.3, 451],[367.1, 456.8],[390.7, 495.8],[409.4, 515.3]]
    costs_profit_14 = [[0.65*2354,2354],[0.6*2390,2390],[0.76*2420,2420],[0.68*2500,2500],[0.7*2560,2560]]
    # costs_profit_5 = [[0.81*1955,1955],[0.74*2170,2170],[0.86*2210,2210],[0.808*2280,2280],[0.828*2400,2400]]
    costs_profit = costs_profit_14
    do_main(costs_profit, "прибуток від витрат")

    # # ==== P(Capital) ====
    # capital_profit_lb = [[79.7,428.2], [87.3,451], [95.4,456.8], [97.2,495.8], [100.6,515.3]]
    capital_profit_14 = [[22870,2354],[24200,2390],[26100,2420],[28200,2500],[29800,2560]]
    # costs_profit_5 = [[34052,1955],[34800,2170],[35600,2210],[36200,2280],[38100,2400]]
    capital_profit = capital_profit_14
    do_main(capital_profit, "прибуток від капіталу")

if __name__ == "__main__":
    main()