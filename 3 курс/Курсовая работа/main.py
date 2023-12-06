# CORRELATION
# чтение данных из csv файла
def get_data(file_name):
    data_list = []
    with open(f"data_files/{file_name}.csv") as file:
        array = [row.strip() for row in file]
    for el in array:
        data_list.append(el.split(';'))
    return data_list

# суммирование значений
def sum_value(my_double_list):
    sum_list = [0 for x in range(len(my_double_list[0]))]
    for i in range(1, len(my_double_list)):
        for j in range(len(my_double_list[0])):
            sum_list[j] = float(sum_list[j]) + float(my_double_list[i][j])
    return sum_list

# нахождение средних
def averge_value(my_list, n):
    av_list = []
    for el in my_list:
        av_list.append(round((el / n), 3))
    return av_list

#ранжирование
def ranks(avg_val, keys):
    my_dict_el_val = {}
    my_dict_el_val_rank = {}
    my_dict_el_rank = {}

    i = 0
    for key in keys:
        my_dict_el_val[key]=avg_val[i]
        i+=1
    
    sorted_avg_val = sorted(avg_val)
    i = 1
    for val in sorted_avg_val:
        my_dict_el_val_rank[val] = i
        i+=1
    
    for key in keys:
        value = my_dict_el_val[key]
        my_dict_el_rank[key] = my_dict_el_val_rank[value]
    
    return my_dict_el_rank

# получение массивов для корреляционного поля
def get_X_Y(dict, keys):
    my_list = []
    for key in keys:
        my_list.append(dict[key])
    return my_list

# квадраты разностей между соответствующими значениями
def get_mass_d2(mass_x, mass_y):
    d2_list = []
    for i in range(len(mass_x)):
        d = mass_x[i] - mass_y[i]
        d2_list.append(d**2)
    return d2_list

# ранговая корреляция Спирмена
def rank_cor_Spir(deltas_list):
    l = len(deltas_list)
    sum_d2 = 0
    for el in deltas_list:
        sum_d2 += el
    Rs = 1 - (6 * sum_d2) / (l * (l**2 -1))
    return Rs

# T-критерий
def T_kof(Rs, n):
    from math import sqrt
    t = abs(Rs)*sqrt((n-2)/(1-Rs*Rs))
    return t

# загрузка критических значений из файла
def get_T_crit_values():
    data_list = []
    with open("data_files/T_crit_values.csv") as file:
        array = [row.strip() for row in file]
    for el in array:
        data_list.append(el.split(';'))
    return data_list

# получение критического значения
def find_crit(n, alpha, crit_list = get_T_crit_values()):
    if alpha == 0.05:
        var = 1
    elif alpha == 0.01:
        var = 2
    elif alpha == 0.001:
        var = 3
    else:
        print("Выбран недоступный уровень значимости!")
    for i in range(1, len(crit_list)):
        if int(crit_list[i][0]) == n - 2:
            return crit_list[i][var]

# csv таблица с данными
def create_csv_table(KEYS, name_1, name_2, X, Y, D2, n, rs, t, t_crit):
    import csv
    with open('cor_field/cor_field_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
                                
        spamwriter.writerow(['Измерения'] + KEYS)
        spamwriter.writerow([f'Ранг {name_1}'] + X)
        spamwriter.writerow([f'Ранг {name_2}'] + Y)
        spamwriter.writerow(['d^2'] + D2)
        spamwriter.writerow(['n', n])
        spamwriter.writerow(['rs', str(round(float(rs), 3))])
        spamwriter.writerow(['t', str(round(float(t), 3))])
        spamwriter.writerow(['t_crit', str(round(float(t_crit), 3))]) 


# GRAPHICS
# корреляционное поле
def correlation_field(x_mass, y_mass):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.figure("Корреляция")
    plt.title('Корреляционное поле')
    plt.xlabel("IT")
    plt.ylabel("Med")
    plt.grid( axis = 'y')
    #plt.grid(True)
    x = np.array(x_mass)
    y = np.array(y_mass)
    plt.scatter(x, y)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), color = 'r')
    #plt.show()
    plt.savefig('graphics/cor_field.png')

# получение данных для полигона распределение
def get_Xi_mi(data_list, selected):
    selection = []
    for el in selected:
        for i in range(len(data_list[0])):
            if data_list[0][i] == el:
                selection.append(i+1)
    vals = [int(i) for i in range(1,len(data_list[0])+1)]
    counter = {}
    for el in vals:
        counter[el] = 0
    for i in range(1, len(data_list)):
        for el in selection:
            counter[int(data_list[i][el-1])]+=1
    return counter

# полигон распределения
def distribution_polygon(my_data_dict:dict, name):
    import matplotlib.pyplot as plt
    import numpy as np
    Xi = list(my_data_dict.keys())
    Mi = []
    for el in Xi:
        Mi.append(my_data_dict[el])

    plt.figure()
    plt.title(f'Полигон распределения {name}')
    plt.xlabel("Xi")
    plt.ylabel("mi")
    plt.grid(True)
    x = np.array(Xi)
    y = np.array(Mi)
    plt.plot(x, y, 'o-')
    #plt.show()
    plt.savefig(f'graphics/poligon_{name}.png')

# получение данных для кумулянты
def get_Xi_mxi(dict_xi:dict):
    n = len(list(dict_xi.keys()))
    keys = [i for i in range(1, n+2)]
    value = 0
    dict_Xi_mxi = {}
    dict_Xi_mxi[keys[0]] = value
    for key in keys:
        if key != keys[0]:
            value += dict_xi[key-1]
            dict_Xi_mxi[key] = value
    return dict_Xi_mxi
    
# кумулянта
def cumulant(my_data_dict:dict, name):
    import matplotlib.pyplot as plt
    import numpy as np
    Xi = list(my_data_dict.keys())
    Mxi = []
    for el in Xi:
        Mxi.append(my_data_dict[el])
    
    plt.figure()
    plt.title(f'Кумулянта {name}')
    plt.xlabel("Xi")
    plt.ylabel("Mxi")
    plt.grid(True)
    x = np.array(Xi)
    y = np.array(Mxi)
    plt.plot(x, y, 'o-')
    #plt.show()
    plt.savefig(f'graphics/cumulant_{name}.png')

# получение данных для эмпирической функции распределения
def get_Xi_Wxi(dict_xi_mxi:dict):
    x_keys = list(dict_xi_mxi.keys())
    values = []
    for key in x_keys:
        values.append(dict_xi_mxi[key])
    x_keys.pop(-1)
    sum = values[len(values)-1]
    values.pop(0)
    wxi = []
    for val in values:
        wxi.append(round(val / sum, 3))
    return x_keys, wxi

# эмпирическая функция распределения
def empirical_distribution(list_Xi, list_Wxi, name):
    import matplotlib.pyplot as plt
    import numpy as np
    pairs_Xi_list = []
    pairs_Wxi_list = []
    for el in list_Xi:
        pairs_Xi_list.append([el, el+1])
    for el in list_Wxi:
        pairs_Wxi_list.append([el, el])
    
    plt.figure()
    plt.title(f'Эмпирическая функция распределения ({name})')
    plt.xlabel("Xi")
    plt.ylabel("Wxi")
    plt.grid(True)
    for i in range(len(pairs_Xi_list)):
        x = np.array(pairs_Xi_list[i])
        y = np.array(pairs_Wxi_list[i])
        plt.plot(x, y, 'blue')
    #plt.show()
    plt.savefig(f'graphics/emp_dist_{name}.png')


def main():
    name1 = str(input('Введите название первой выборки: '))
    name2 = str(input('Введите название второй выборки: '))
    
    # получение данных
    data_it = get_data('data_1')
    data_med = get_data('data_2')

    # получение оцениваемых атрибутов
    keys = data_it[0]

    # количество результатов
    n = len(data_it) - 1

    # суммирование
    summa_IT = sum_value(data_it)
    summa_med = sum_value(data_med)

    # средние значения
    avg_list_IT = averge_value(summa_IT, n)
    avg_list_med = averge_value(summa_med, n)

    # ранжирование результатов
    dict_rank_IT = ranks(avg_list_IT, keys)
    dict_rank_med = ranks(avg_list_med, keys)

    # данные для корреляционного анализа и построения корреляционного поля
    Xi = get_X_Y(dict_rank_IT, keys)
    Yi = get_X_Y(dict_rank_med, keys)

    # квадраты разностей X-Y
    D2i = get_mass_d2(Xi, Yi)

    # коэффициент ранговой корреляции
    Rs = rank_cor_Spir(D2i)
    print(f'Коэффициент ранговой корреляции Пирсона: {round(Rs, 3)}')

    # T-критерий
    N = len(keys)
    T = T_kof(Rs, N)
    print(f'T-критерий: {round(T, 3)}')

    # T-критическое
    level = float(input('Выберите уровень значимости (0.05, 0.01 или 0.001): '))
    T_crit = find_crit(N, level)
    print(f'T критическое: {T_crit}')

    # корреляционное поле (график)
    correlation_field(Xi, Yi)

    # данные для корреляции
    create_csv_table(keys, name1, name2, Xi, Yi, D2i, N, Rs, T, T_crit)

    #Анализ выборки
    #Выборка
    print(f'Выберите по каким атрибутам будем строить вариационные ряды (введите через запятую) \n {keys}')
    inp_data = str(input('Атрибуты: '))
    viborka = inp_data.split(',')
    print(viborka)

    # Полигон распределения (графики)
    dict_x_m = get_Xi_mi(data_it, viborka)
    dict_y_m = get_Xi_mi(data_med, viborka)
    distribution_polygon(dict_x_m, name1)
    distribution_polygon(dict_y_m, name2)

    # кумулянта (графики)
    dict_Xi_mxi = get_Xi_mxi(dict_x_m)
    dict_Yi_myi = get_Xi_mxi(dict_y_m)
    cumulant(dict_Xi_mxi, name1)
    cumulant(dict_Yi_myi, name2)

    # эмпирическая функция распределения (графики)
    mass_Xi, mass_Wxi = get_Xi_Wxi(dict_Xi_mxi)
    mass_Yi, mass_Wyi = get_Xi_Wxi(dict_Yi_myi)
    empirical_distribution(mass_Xi, mass_Wxi, name1)
    empirical_distribution(mass_Yi, mass_Wyi, name2)
    
    print('Graphics saved to /graphics!')

    
if __name__ == '__main__':
    main()