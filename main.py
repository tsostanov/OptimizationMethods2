def function(x):
    return 5 * x ** 2 - 8 * x ** (5 / 4) - 20 * x


def derivative_function(x):
    return 10 * x - 10 * x ** (1 / 4) - 20


def dderivative_function(x):
    return 10 - (5 / (2 * x ** (3 / 4)))


def bisection_method(func, a, b, epsilon):
    print("Метод половинного деления")
    iteration = 1
    print(f"Шаг номер {iteration}")
    print(f"a = {a}, b = {b}")
    x1 = (a + b - epsilon) / 2
    x2 = (a + b + epsilon) / 2
    print(f"x1 = {x1}, x2 = {x2}")
    y1 = func(x1)
    y2 = func(x2)
    print(f"y1 = {y1}, y2 = {y2}")
    if y1 > y2:
        print("y1 > y2, поэтому a = x1")
        a = x1
    else:
        print("y1 <= y2, поэтому b = x2")
        b = x2
    while abs(b - a) >= 2 * epsilon:
        iteration += 1
        print(f"Шаг номер {iteration}")
        print(f"a = {a}, b = {b}")
        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2
        print(f"x1 = {x1}, x2 = {x2}")
        y1 = func(x1)
        y2 = func(x2)
        print(f"y1 = {y1}, y2 = {y2}")
        if y1 > y2:
            print("y1 > y2, поэтому a = x1")
            a = x1
        else:
            print("y1 <= y2, поэтому b = x2")
            b = x2
    xm = (a + b) / 2
    ym = func(xm)
    print(f"Xm = {xm}, Ym = {ym}")


def golden_section_method(func, a, b, epsilon):
    print("\nМетод золотого сечения")
    phi = (1 + 5 ** 0.5) / 2  # Золотое сечение
    iteration = 1
    print(f"Шаг номер {iteration}")
    print(f"a = {a}, b = {b}")
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    print(f"x1 = {x1}, x2 = {x2}")
    y1 = func(x1)
    y2 = func(x2)
    print(f"y1 = {y1}, y2 = {y2}")
    if y1 >= y2:
        print("y1 >= y2, поэтому a = x1")
        a = x1
    else:
        print("y1 < y2, поэтому b = x2")
        b = x2
    while abs(b - a) >= epsilon:
        iteration += 1
        print(f"Шаг номер {iteration}")
        print(f"a = {a}, b = {b}")
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi
        print(f"x1 = {x1}, x2 = {x2}")
        y1 = func(x1)
        y2 = func(x2)
        print(f"y1 = {y1}, y2 = {y2}")
        if y1 >= y2:
            print("y1 >= y2, поэтому a = x1")
            a = x1
        else:
            print("y1 < y2, поэтому b = x2")
            b = x2
    xm = (a + b) / 2
    ym = func(xm)
    print(f"Xm = {xm}, Ym = {ym}")


def chord_method(func, der_func, a, b, epsilon):
    print("\nМетод хорд")
    iteration = 1
    print(f"Шаг номер {iteration}")
    print(f"a = {a}, b = {b}")
    x = a - (a - b) * (der_func(a) / (der_func(a) - der_func(b)))
    print(f"x = {x}")
    if der_func(x) > 0:
        print("f'(x) > 0, поэтому b = x")
        b = x
    else:
        print("f'(x) <= 0, поэтому a = x")
        a = x
    while abs(der_func(x)) > epsilon:
        iteration += 1
        print(f"Шаг {iteration}:")
        print(f"a = {a}, b = {b}")
        x = a - (a - b) * (der_func(a) / (der_func(a) - der_func(b)))
        print(f"x = {x}")
        if der_func(x) > 0:
            print("f'(x) > 0, поэтому b = x")
            b = x
        else:
            print("f'(x) <= 0, поэтому a = x")
            a = x

    print(f"Xm = {x}, Ym = {func(x)}")


def newton_method(func, derivative_func, dderivative_func, a, b, epsilon):
    print("\nМетод Ньютона")
    iteration = 1
    print(f"Шаг номер {iteration}")
    print(f"a = {a}, b = {b}")
    if func(a) * dderivative_func(a) > 0:
        x0 = a
        print("Начальное приближение x0 = a")
    elif func(b) * dderivative_func(b) > 0:
        x0 = b
        print("Начальное приближение x0 = b")
    else:
        x0 = (a + b) / 2
        print("Начальное приближение x0 = (a + b) / 2")
    print(f"x0 = {x0}")
    xi = x0 - func(x0) / derivative_func(x0)
    print(f"xi = {xi}")
    while abs(derivative_func(xi)) > epsilon:
        iteration += 1
        print(f"Шаг {iteration}:")
        print(f"a = {a}, b = {b}")
        x0 = xi
        xi = x0 - derivative_func(x0).real / dderivative_func(x0).real
        print(f"xi = {xi}")
    print(f"Xm = {xi}, Ym = {func(xi).real}")




a, b = 3, 3.5
e = 0.02
bisection_method(function, a, b, e)
golden_section_method(function, a, b, e)
chord_method(function, derivative_function, a, b, e)
newton_method(function, derivative_function, dderivative_function, a, b, e)

