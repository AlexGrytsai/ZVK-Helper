from tkinter.messagebox import showerror
from decimal import *

getcontext().prec = 2

                            # ДЛЯ ТЕСТОВ
dp = {'costraction_data': {'data': [['10', '3.89'], ['1а', '3,48'], ['2а', '237'], ['4б', '226']]},
      'main_data': {'Network': 'К-2', 'Construction': 'ДП', 'Luk': 'ДБ1'}}

kanal = {'costraction_data': dict(
    data=[['10', 380, '1,500', '1100'], ['10', '3.80', 1, 700], ['!10!', '3,49', '1. 5', 1100],
          ['2а', '237', '15', 400]]),
    'main_data': {'Network': 'К-1', 'Construction': 'Колодязі з ПЕ', 'Lotok': 'Стандартний', 'Gorlovina': 'Стандартна',
                  'Luk': 'В', 'Quantity_Luk': 1}}

voda_kameri = {'costraction_data': {'data': [['5', '1,8х 3.0', 68.0], [2, '3.0х 2.4', 48.0], [3, '3.0х 3.0', 295]]},
               'main_data': {'Network': 'В-1', 'Construction': 'Камери', 'Height': 'Стандартна',
                             'Gorlovina': 'Мінімальна', 'Luk': 'В', 'Quantity_Luk': 2}}

voda_kolodci = {
    'costraction_data': {'data': [['5', 24, '20'], ['11', '25', 2], ['!10!', '24', '1. 0'], ['12', '3,49', '1. 5']]},
    'main_data': {'Network': 'В-1', 'Construction': 'Колодязі', 'Gorlovina': 'Мінімальна', 'Luk': 'В',
                  'Quantity_Luk': 1}}
# ---------------------------------------------------------------------------------------------------------------------

other = {'Stairs': {'Драбина': {'ГОСТ': '',
                                'Завод': [],
                                'Единцы изм': 'м.п.'},
                    'Скоба ходова з ПЕ покриттям': {'ГОСТ': 'EN 13101',
                                                    'Завод': ['ТОВ «Імпекс-Груп Україна»'],
                                                    'Единцы изм': 'шт.'},
                    'Скоба ходова чавунна': {'ГОСТ': 'ДСТУ Б В.2.6-106',
                                             'Завод': ['ТОВ «Імпекс-Груп Україна»'],
                                             'Единцы изм': 'шт.'}},
         'Concrete': {'Бетонна суміш С12/15': {'ГОСТ': 'ДСТУ Б В.2.7-176:2008',
                                               'Завод': ['ТОВ «Комбінат будіндустрії»',
                                                         'ТОВ «АБЕТОН»',
                                                         'ТОВ "ПБГ КОВАЛЬСЬКА"'],
                                               'Единцы изм': 'м3'}}
         }

type_grid = {'Grid': {'Л': {'Название': 'Люк чавунний тип "Л"', 'Высота': 80, 'Вес': 50,
                           'Примечание': 'з логотипом ПрАТ "АК "Київводоканал"'},
                     'С': {'Название': 'Люк чавунний тип "С"', 'Высота': 95, 'Вес': 66,
                           'Примечание': 'з логотипом ПрАТ "АК "Київводоканал"'},
                     'В': {'Название': 'Люк чавунний тип "В"', 'Высота': 140, 'Вес': 95,
                           'Примечание': 'з логотипом ПрАТ "АК "Київводоканал"'},
                     'ВМ': {'Название': 'Люк чавунний тип "ВМ"', 'Высота': 180, 'Вес': 125,
                            'Примечание': 'з логотипом ПрАТ "АК "Київводоканал"'},
                     'General info': {'ГОСТ': 'ДСТУ Б В.2.5-26:2005',
                                      'Завод': ['ТОВ «Імпекс-Груп Україна»'],
                                      'Единцы изм': 'шт.'},
                      'ДП': {'Д(А15)': {'Высота': 120, 'Вес': 30},
                             'ДБ1': {'Высота': 90, 'Вес': 50},
                             'ДБ2': {'Высота': 120, 'Вес': 80},
                             'ДМ1': {'Высота': 128, 'Вес': 60},
                             'ДМ2': {'Высота': 120, 'Вес': 100},
                             'ДС1': {'Высота': 120, 'Вес': 80},
                             'ДС2': {'Высота': 120, 'Вес': 130},
                             'General info':
                                 {'ГОСТ': 'ДСТУ Б В.2.5-26:2005',
                                  'Завод': ['ТОВ «Імпекс-Груп Україна»'],
                                  'Единцы изм': 'шт.'}}}
             }

kamiri_nabor = {'Стандартна': {'1.8x1.8': {'КП-5': 2, 'КС-1': 8},
                               '1.8x2.4': {'КП-2': 4, 'КС-1': 4, 'КC-9': 4},
                               '1.8x3.0': {'КП-2': 2, 'КПд-1': 2, 'КС-1': 4, 'КС-4': 4},
                               '2.4x3.0': {'КП-3': 4, 'КС-2': 4, 'КС-5': 4},
                               '3.0x3.0': {'КП-3': 4, 'КПд-2': 2, 'КC-3': 4, 'КС-4': 4},
                               '3.0x3.6': {'КП-3': 4, 'КПд-2': 4, 'КС-1': 4, 'КС-5': 4},
                               '3.0x4.2': {'КП-3': 4, 'КПд-2': 6, 'КС-4': 4, 'КC-6': 4},
                               '3.6x4.2': {'КП-4': 8, 'КПд-4': 4, 'КC-6': 4, 'КC-7': 4},
                               '4.2x4.2': {'КП-4': 8, 'КПд-4': 6, 'КC-6': 4, 'КC-7': 4},
                               '4.2x4.8': {'КП-4': 8, 'КПд-4': 8, 'КC-7': 4, 'КC-8': 4}},
                'З добором': {'1.8x1.8': {'КП-5': 2, 'КС-1': 8, 'КCд-1': 8},
                              '1.8x2.4': {'КП-2': 4, 'КС-1': 4, 'КC-9': 4, 'КCд-1': 4, 'КCд-9': 4},
                              '1.8x3.0': {'КП-2': 2, 'КПд-1': 2, 'КС-1': 4, 'КС-4': 4, 'КCд-1': 4, 'КCд-4': 4},
                              '2.4x3.0': {'КП-3': 4, 'КС-2': 4, 'КС-5': 4, 'КСд-2': 4, 'КCд-5': 4},
                              '3.0x3.0': {'КП-3': 4, 'КПд-2': 2, 'КC-3': 4, 'КС-4': 4, 'КCд-3': 4, 'КCд-4': 4},
                              '3.0x3.6': {'КП-3': 4, 'КПд-2': 4, 'КС-1': 4, 'КС-5': 4, 'КCд-1': 4, 'КCд-5': 4},
                              '3.0x4.2': {'КП-3': 4, 'КПд-2': 6, 'КС-4': 4, 'КC-6': 4, 'КCд-4': 4, 'КCд-6': 4},
                              '3.6x4.2': {'КП-4': 8, 'КПд-4': 4, 'КC-6': 4, 'КC-7': 4, 'КCд-5': 4, 'КCд-7': 4},
                              '4.2x4.2': {'КП-4': 8, 'КПд-4': 6, 'КC-6': 4, 'КC-7': 4, 'КCд-6': 4, 'КCд-7': 4},
                              '4.2x4.8': {'КП-4': 8, 'КПд-4': 8, 'КC-7': 4, 'КC-8': 4, 'КCд-7': 4, 'КCд-8': 4}}}

constraction = {'Горловина': {'КО-6': {'Толщина': 70, 'Вес': 50},
                              'КС7.3': {'Толщина': 300, 'Вес': 123},
                              'ПО-10': {'Толщина': 150, 'Вес': 800},
                              'ПО-2': {'Толщина': 120, 'Вес': 550},
                              'ПО-3': {'Толщина': 160, 'Вес': 900},
                              'ПО-4': {'Толщина': 200, 'Вес': 1530},
                              'ПО-6.3': {'Толщина': 150, 'Вес': 930},
                              'ПО-7': {'Толщина': 150, 'Вес': 880},
                              'ЛЗБ-4': {'Толщина': 100, 'Вес': 100},
                              'ПД-6': {'Толщина': 220, 'Вес': 2040},
                              'КС 10.3': {'Вес': 200},
                              'КС 10.6': {'Вес': 400},
                              'КС 10.9': {'Вес': 600},
                              '1ПП 10-2': {'Толщина': 150, 'Вес': 250},
                              'General info': {'Единцы изм': 'шт.',
                                               'ГОСТ': 'ДСТУ Б В.2.6-2:2009',
                                               'Завод': ['ТОВ «Комбінат будіндустрії»', 'ТОВ «АБЕТОН»',
                                                         'ТОВ "ПБГ КОВАЛЬСЬКА"']}
                              },
                'Колодязі': {'ПН-10': {'Вес': 450},
                             'ПН-15': {'Вес': 950},
                             'ПН-20': {'Вес': 1475},
                             'КС 10.3': {'Вес': 200},
                             'КС 10.6': {'Вес': 400},
                             'КС 10.9': {'Вес': 600},
                             'КС 15.3': {'Вес': 320},
                             'КС 15.6': {'Вес': 663},
                             'КС 15.9': {'Вес': 1000},
                             'КС 20.3': {'Вес': 490},
                             'КС 20.6': {'Вес': 980},
                             'КС 20.9': {'Вес': 1468},
                             '1ПП 10-2': {'D': 1000, 'Толщина': 150, 'Вес': 250},
                             '1ПП 15-2': {'D': 1500, 'Толщина': 150, 'Вес': 675},
                             '2ПП 20-2-1': {'D': 2000, 'Вес': 1275, 'Толщина': 160},
                             '2ПП 20-2-2': {'D': 2000, 'Вес': 1380, 'Толщина': 160},
                             'General info': {'Единцы изм': 'шт.',
                                             'ГОСТ': 'ДСТУ Б В.2.6-2:2009',
                                             'Завод': ['ТОВ «Комбінат будіндустрії»', 'ТОВ «АБЕТОН»',
                                                       'ТОВ "ПБГ КОВАЛЬСЬКА"']}
                            },
                'Камери': {'КПд-1': {'Вес': 660}, 'КПд-2': {'Вес': 1000}, 'КПд-4': {'Вес': 1365},
                           'КП-2': {'Вес': 1350}, 'КП-3': {'Вес': 2025}, 'КП-4': {'Вес': 2895}, 'КП-5': {'Вес': 2325},
                           'КС-1': {'Вес': 900}, 'КС-2': {'Вес': 1175}, 'КC-3': {'Вес': 1450}, 'КС-4': {'Вес': 1450},
                           'КС-5': {'Вес': 1450},
                           'КC-6': {'Вес': 1925}, 'КC-7': {'Вес': 1925}, 'КC-8': {'Вес': 2225}, 'КC-9': {'Вес': 1175},
                           'КCд-1': {'Вес': 450}, 'КСд-2': {'Вес': 590}, 'КCд-3': {'Вес': 725}, 'КCд-4': {'Вес': 725},
                           'КCд-5': {'Вес': 725},
                           'КCд-6': {'Вес': 965}, 'КCд-7': {'Вес': 965}, 'КCд-8': {'Вес': 1115}, 'КCд-9': {'Вес': 590},
                           'General info': {'Единцы изм': 'шт.',
                                            'ГОСТ': 'ДСТУ Б В.2.6-2:2009',
                                            'Завод': ['ТОВ «Комбінат будіндустрії»', 'ТОВ «АБЕТОН»',
                                                      'ТОВ "ПБГ КОВАЛЬСЬКА"']}
                           },
                'ДП': {'ЗП1 ПН': {'Высота': 800, 'Вес': 713},
                       'ЗП1-2 ПН': {'Высота': 400, 'Вес': 412},
                       'ЗП1': {'Высота': 800, 'Вес': 312},
                       'ЗП1-2': {'Высота': 400, 'Вес': 713},
                       'General info': {'Единцы изм': 'шт.',
                                        'ГОСТ': 'ДСТУ Б В.2.6–2–95',
                                        'Завод': ['ТОВ «Комбінат будіндустрії»', 'ТОВ «АБЕТОН»',
                                                  'ТОВ "ПБГ КОВАЛЬСЬКА"']}
                       }
                }

vedomost = {}
spec = {}
error_log = {}

def calculate_min_height_gorlovina(diametr=0, grid='В', gorlovina='Стандартна', basic_data=None):
    h_pp = 0
    if diametr == 1000:
        h_pp = constraction['Колодязі']['1ПП 10-2']['Толщина']
    elif diametr == 1500:
        h_pp = constraction['Колодязі']['1ПП 15-2']['Толщина']
    elif diametr == 2000:
        h_pp = constraction['Колодязі']['2ПП 20-2-1']['Толщина']
    if basic_data is None:
        basic_data = []
    if gorlovina == 'Стандартна':
        if basic_data[1] == 'Колодязі' or basic_data[1] == 'Колодязі з ПЕ':
            height_gorlovin = 500 + h_pp
            return height_gorlovin
        else:
            height_gorlovin = 500 + 200
            return height_gorlovin
    elif gorlovina == 'Мінімальна':
        if basic_data[1] == 'Камери':
            if grid == 'ВМ':
                height_gorlovin = 200 + type_grid['Grid'][grid]['Высота'] + 1 * \
                                  constraction['Горловина']['КО-6']['Толщина'] + constraction['Горловина']['ПД-6'][
                                      'Толщина']
                return height_gorlovin
            else:
                height_gorlovin = 200 + type_grid['Grid'][grid]['Высота'] + 3 * \
                                  constraction['Горловина']['КО-6']['Толщина']
                return height_gorlovin
        elif basic_data[1] == 'Колодязі' or basic_data[1] == 'Колодязі з ПЕ':
            if grid == 'ВМ':
                height_gorlovin = h_pp + type_grid['Grid'][grid]['Высота'] + 1 * \
                                  constraction['Горловина']['КО-6']['Толщина'] + constraction['Горловина']['ПД-6'][
                                      'Толщина']
                return height_gorlovin
            else:
                height_gorlovin = h_pp + type_grid['Grid'][grid]['Высота'] + 3 * \
                                  constraction['Горловина']['КО-6']['Толщина']
                return height_gorlovin


def check_depth_consctr(depth, diametr=0, name="#", lotok=0, gorlovina='Стандартна', basic_data=None):
    if basic_data is None:
        basic_data = []
    global error_log
    if len(str(depth)) > 0:
        if str(depth).isalnum() == False or str(depth).isnumeric() == True:
            depth = str(depth).replace(',', '')
            depth = str(depth).replace('.', '')
            depth = str(depth).replace(' ', '')
            if str(depth).isdigit() != True:
                error_log['total_errors'] += 1
                error_log['errors'][error_log[
                    'total_errors']] = f'№ {name}. Недопустимий формат введених даних глибини.\nКритична помилка - розрахунок не виконаний.'
                return "ERROR"

            else:
                if len(str(depth)) == 1:
                    depth = int(depth) * 1000
                elif len(str(depth)) == 2:
                    depth = int(depth) * 100
                elif len(str(depth)) == 3:
                    depth = int(depth) * 10
                if basic_data == ['В-1', 'Колодязі']:
                    if int(depth) - calculate_min_height_gorlovina(diametr, gorlovina=gorlovina,
                                                              basic_data=basic_data) >= 1500:
                        return int(depth)
                    else:
                        error_log['total_errors'] += 1
                        error_log['errors'][error_log[
                            'total_errors']] = f'№ {name}. Відповідно до ДБН В.2.5-74:2013 п.12.65 (висота робочої частини не може бути <1.5м).\nКритична помилка - розрахунок не виконаний.'
                        return "ERROR"
                elif basic_data == ['В-1', 'Камери', 'Стандартна']:
                    if int(depth) - calculate_min_height_gorlovina(gorlovina=gorlovina, basic_data=basic_data) - 2100 >= 0:
                        return int(depth)
                    else:
                        error_log['total_errors'] += 1
                        error_log['errors'][error_log[
                            'total_errors']] = f'№ {name}. Загальна глибина камери менше необхідної.\nКритична помилка - розрахунок не виконаний.'
                        return "ERROR"
                elif basic_data == ['В-1', 'Камери', 'З добором']:
                    if int(depth) - calculate_min_height_gorlovina(gorlovina=gorlovina,
                                                              basic_data=basic_data) - 2100 - 560 >= 0:
                        return int(depth)
                    else:
                        error_log['total_errors'] += 1
                        error_log['errors'][error_log['total_errors']] = \
                            f'№ {name}. Загальна глибина камери менше необхідної.\nКритична помилка - розрахунок не виконаний.'
                        return "ERROR"
                elif basic_data == ['К-1', 'Колодязі'] or basic_data == ['К-2', 'Колодязі'] or basic_data == ['К-1',
                                                                                                              'Колодязі з ПЕ']:
                    if int(depth) - calculate_min_height_gorlovina(diametr, gorlovina=gorlovina,
                                                              basic_data=basic_data) - int(lotok) >= 300:
                        return int(depth)
                    else:
                        error_log['total_errors'] += 1
                        error_log['errors'][error_log['total_errors']] = \
                            f'№ {name}. Загальна глибина колодязя менше необхідної.\nКритична помилка - розрахунок не виконаний.'
                        return "ERROR"
                elif basic_data == ['К-2', 'ДП']:
                    if int(depth) >= 530:
                        return int(depth)
                    else:
                        error_log['total_errors'] += 1
                        error_log['errors'][error_log['total_errors']] = \
                            f'№ {name}. Загальна глибина ДП менше необхідної.\nКритична помилка - розрахунок не виконаний.'
                        return "ERROR"
        else:
            error_log['total_errors'] += 1
            error_log['errors'][error_log['total_errors']] = \
                f'№ {name}. Невірний формат введених даних глибини.\nКритична помилка - розрахунок не виконаний.'
            return "ERROR"
    else:
        error_log['total_errors'] += 1
        error_log['errors'][error_log['total_errors']] = \
            f'№ {name}. Не задана глибина.\nКритична помилка - розрахунок не виконаний.'
        return "ERROR"


def check_name_constr_not_empty(name: str):
    if len(str(name)) > 0:
        return name
    else:
        error_log['total_errors'] += 1
        error_log['errors'][error_log['total_errors']] = \
            f"№ {name}. Не вказаний номер конструкції за планом.\nПрисвоєний номер - ERROR"
        return "ERROR"


def check_diametr_constr(diametr, name):
    if len(str(diametr)) > 0:
        if str(diametr).isalnum() == False or str(diametr).isnumeric() == True:
            diametr = str(diametr).replace(',', '')
            diametr = str(diametr).replace('.', '')
            diametr = str(diametr).replace(' ', '')
            diametr = int(diametr)
            if str(diametr).isdigit() == True:
                if len(str(diametr)) == 1:
                    diametr = diametr * 1000
                elif len(str(diametr)) == 2:
                    diametr = diametr * 100
                elif len(str(diametr)) == 3:
                    diametr = diametr * 10
                if diametr == 1000 or diametr == 1500 or diametr == 2000:
                    return int(diametr)
                else:
                    error_log['total_errors'] += 1
                    error_log['errors'][error_log['total_errors']] = \
                        (
                            f'№ {name}. Вказаний невірний діаметр колодязя.\nДоступні для розрахунку діамтри: 1000мм, 1500мм, 2000мм.'
                            f'\nКритична помилка - розрахунок не виконаний.')
                    return "ERROR"
            else:
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = \
                    f'№ {name}. Невірний формат введених даних діаметру.\nКритична помилка - розрахунок не виконаний.'
                return "ERROR"
        else:
            error_log['total_errors'] += 1
            error_log['errors'][error_log['total_errors']] = \
                f'№ {name}. Невірний формат введених даних діаметру.\nКритична помилка - розрахунок не виконаний.'
            return "ERROR"
    else:
        error_log['total_errors'] += 1
        error_log['errors'][
            error_log['total_errors']] = f'№ {name}. Не задан діаметр.\nКритична помилка - розрахунок не виконаний.'
        return "ERROR"


def check_input_data(input_constr_data: dict):
    '''Обрабатываются входные данные'''
    global vedomost, name
    global error_log
    error_log.update({'errors': {}, 'total_errors': 0})
    input_data = input_constr_data['main_data']
    data_to_dict = input_constr_data['costraction_data']
    basic_data = [input_data['Network'], input_data['Construction']]
    if basic_data == ['В-1', 'Колодязі']:
        for j in range(len(data_to_dict['data'])):
            depth = data_to_dict['data'][j][1]
            diametr = data_to_dict['data'][j][2]
            name = data_to_dict['data'][j][0]
            gorlovina = input_data['Gorlovina']
            if check_name_constr_not_empty(name) != 'ERROR':
                name = check_name_constr_not_empty(name)
            else:
                name = 'ERROR'

            if check_diametr_constr(diametr, name) != "ERROR":
                diametr = check_diametr_constr(diametr, name)
            else:
                continue

            if check_depth_consctr(depth, diametr, name, gorlovina=gorlovina, basic_data=basic_data) != "ERROR":
                depth = check_depth_consctr(depth, diametr, name, gorlovina=gorlovina, basic_data=basic_data)
            else:
                continue

            # Check same name construction В-1
            if data_to_dict['data'][j][0] not in vedomost:
                vedomost[name] = {'Г-на кол': depth,
                                  'Д_кол': diametr,
                                  'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                  'Basic Data': {'Network': input_data['Network'],
                                                 'Construction': input_data['Construction'],
                                                 'Горловина': input_data['Gorlovina']}}
            else:
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = \
                    f"Співпадіння номерів за планом.\nНомеру {name} присвоєно номер !{name}!"
                vedomost[f"!{name}!"] = {'Г-на кол': depth,
                                         'Д_кол': diametr,
                                         'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                         'Basic Data': {'Network': input_data['Network'],
                                                        'Construction': input_data['Construction'],
                                                        'Горловина': input_data['Gorlovina']}}
    #
    if basic_data == ['К-2', 'ДП']:
        for j in range(len(data_to_dict['data'])):
            if check_name_constr_not_empty(data_to_dict['data'][j][0]) != 'ERROR':
                data_to_dict['data'][j][0] = check_name_constr_not_empty(data_to_dict['data'][j][0])
            else:
                data_to_dict['data'][j][0] = 'ERROR'

            if check_depth_consctr(depth=data_to_dict['data'][j][1], name=data_to_dict['data'][j][0]) != "ERROR":
                data_to_dict['data'][j][1] = check_depth_consctr(depth=data_to_dict['data'][j][1],
                                                                 name=data_to_dict['data'][j][0], basic_data=basic_data)
            else:
                continue

                # Check same name construction ДП
            if data_to_dict['data'][j][0] not in vedomost:
                vedomost[data_to_dict['data'][j][0]] = {'Г-на кол': data_to_dict['data'][j][1],
                                                        'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                                        'Basic Data': {'Network': input_data['Network'],
                                                                       'Construction': input_data['Construction']}}
            else:
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = \
                    f"Співпадіння номерів за планом.\nНомеру {name} присвоєно номер !{name}!"
                vedomost[f"!{data_to_dict['data'][j][0]}!"] = {'Г-на кол': data_to_dict['data'][j][1],
                                                               'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                                               'Basic Data': {'Network': input_data['Network'],
                                                                              'Construction': input_data[
                                                                                  'Construction']}}

    if basic_data == ['К-1', 'Колодязі'] or basic_data == ['К-1', 'Колодязі з ПЕ'] or basic_data == ['К-2', 'Колодязі']:
        for j in range(len(data_to_dict['data'])):
            name = data_to_dict['data'][j][0]
            diametr = data_to_dict['data'][j][2]
            depth = data_to_dict['data'][j][1]
            lotok = data_to_dict['data'][j][3]
            gorlovina = input_data['Gorlovina']
            if check_name_constr_not_empty(name) != 'ERROR':
                name = check_name_constr_not_empty(name)
            else:
                name = 'ERROR'

            if check_diametr_constr(diametr=diametr, name=name) != "ERROR":
                diametr = check_diametr_constr(diametr=diametr, name=name)
            else:
                continue

            if str(lotok).isdigit() != True:
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = \
                    f'№ {name}. Невірний формат введених даних лотка.\nКритична помилка - розрахунок не виконаний.'
                continue

            if check_depth_consctr(depth=depth, diametr=diametr, name=name, lotok=lotok, gorlovina=gorlovina,
                                   basic_data=basic_data) != "ERROR":
                depth = check_depth_consctr(depth=depth, diametr=diametr, name=name, lotok=lotok, gorlovina=gorlovina,
                                            basic_data=basic_data)
            else:
                continue

            # Check same name construction К
            if name not in vedomost:
                vedomost[name] = {'Г-на кол': depth,
                                  'Д_кол': diametr,
                                  'Лоток': int(lotok),
                                  'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                  'Basic Data': {'Network': input_data['Network'],
                                                 'Construction': input_data['Construction'],
                                                 'Горловина': input_data['Gorlovina'],
                                                 'Type lotok': input_data['Lotok']}}
            else:
                error_log['total_errors'] += 1
                error_log['errors'][error_log[
                    'total_errors']] = f"Співпадіння номерів за планом.\nНомеру {name} присвоєно номер !{name}!"
                vedomost[f"!{name}!"] = {'Г-на кол': int(depth),
                                         'Д_кол': diametr,
                                         'Лоток': int(lotok),
                                         'Elements': {'Other': {'Grid': [input_data['Luk'], 1]}},
                                         'Basic Data': {'Network': input_data['Network'],
                                                        'Construction': input_data['Construction'],
                                                        'Горловина': input_data['Gorlovina'],
                                                        'Type lotok': input_data['Lotok']}}
    if basic_data == ['В-1', 'Камери']:
        for j in range(len(data_to_dict['data'])):
            basic_data_kamer = [input_data['Network'], input_data['Construction'], input_data['Height']]
            name = data_to_dict['data'][j][0]
            gorlovina = input_data['Gorlovina']
            if check_name_constr_not_empty(name) != 'ERROR':
                name = check_name_constr_not_empty(name)
            else:
                name = 'ERROR'

            if check_depth_consctr(depth=data_to_dict['data'][j][2], diametr=0, name=name, lotok=0, gorlovina=gorlovina,
                                   basic_data=basic_data_kamer) != "ERROR":
                data_to_dict['data'][j][2] = check_depth_consctr(depth=data_to_dict['data'][j][2], diametr=0, name=name,
                                                                 lotok=0, gorlovina=gorlovina,
                                                                 basic_data=basic_data_kamer)
            else:
                continue

            if len(data_to_dict['data'][j][1]) > 0:
                data_to_dict['data'][j][1] = str(data_to_dict['data'][j][1]).replace(',', '.')
                data_to_dict['data'][j][1] = str(data_to_dict['data'][j][1]).replace(' ', '')
                if len(data_to_dict['data'][j][1]) == 7:
                    if float(data_to_dict['data'][j][1][:3]) < float(data_to_dict['data'][j][1][-3:]):
                        long_side = str(data_to_dict['data'][j][1][-3:])
                        short_side = str(data_to_dict['data'][j][1][:3])
                        data_to_dict['data'][j][1] = f"{short_side}x{long_side}"
                    else:
                        long_side = str(data_to_dict['data'][j][1][:3])
                        short_side = str(data_to_dict['data'][j][1][-3:])
                        data_to_dict['data'][j][1] = f"{short_side}x{long_side}"
                else:
                    error_log['other'][name] = 'Невірний формат введених даних розміру камери.'
                    continue

                # Check same name construction B kameri
            if name not in vedomost:
                vedomost[name] = {'Г-на кол': data_to_dict['data'][j][2],
                                  'Д_кол': data_to_dict['data'][j][1],
                                  'Elements': {'Other': {'Grid': [input_data['Luk'], 2]}},
                                  'Basic Data': {'Network': input_data['Network'],
                                                 'Construction': input_data['Construction'],
                                                 'Горловина': input_data['Gorlovina'],
                                                 'Height': input_data['Height']}}
            else:
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = \
                    f"Співпадіння номерів за планом.\nНомеру {name} присвоєно номер !{name}!"
                vedomost[f"!{name}!"] = {'Г-на кол': data_to_dict['data'][j][2],
                                         'Д_кол': data_to_dict['data'][j][1],
                                         'Elements': {'Other': {'Grid': [input_data['Luk'], 2]}},
                                         'Basic Data': {'Network': input_data['Network'],
                                                        'Construction': input_data['Construction'],
                                                        'Горловина': input_data['Gorlovina'],
                                                        'Height': input_data['Height']}}
    return vedomost

def calculation_spec(ready_vedomost, basic_data=None):
    global spec
    global constraction
    global type_grid
    global other

    notice = ''
    type_constraction = ''
    if basic_data == ['В-1', 'Камери']:
        type_constraction = 'Елементи теплових камер'
        spec.update({'Constraction': {type_constraction: {}, 'Елементи горловини': {}}, 'Other': {'Різне': {}}})
    elif basic_data[1] == 'Колодязі' or basic_data[1] == 'Колодязі з ПЕ':
        type_constraction = 'Елементи колодязів'
        spec.update({'Constraction': {type_constraction: {}, 'Елементи горловини': {}}, 'Other': {'Різне': {}}})
    elif basic_data == ['К-2', 'ДП']:
        type_constraction = 'Елементи дощоприймачів'
        spec.update({'Constraction': {type_constraction: {}}, 'Other': {'Різне': {}}})
    for i in ready_vedomost:
        for const, qt in ready_vedomost[i]['Elements']['Constraction'].items():
            if basic_data[1] == 'Колодязі з ПЕ':
                type_const = 'Колодязі'
            else:
                type_const = basic_data[1]
            GOST = constraction[type_const]['General info']['ГОСТ']
            code_product = ''
            factory = constraction[type_const]['General info']['Завод'][0]
            units = constraction[type_const]['General info']['Единцы изм']
            weight = constraction[type_const][const]['Вес']
            if basic_data[1] == 'Колодязі з ПЕ':
                if const == 'ПН-10' or const == 'ПН-15' or const == 'ПН-20':
                    if const not in spec['Constraction'][type_constraction]:
                        spec['Constraction'][type_constraction][const] = [GOST, code_product, factory, units, qt,
                                                                                weight]
                    else:
                        spec['Constraction'][type_constraction][const][4] += qt
                else:
                    if f"{const}П" not in spec['Constraction'][type_constraction]:
                        spec['Constraction'][type_constraction][f"{const}П"] = [GOST, code_product, factory, units, qt, weight]
                    else:
                        spec['Constraction'][type_constraction][f"{const}П"][4] += qt
            else:
                if const not in spec['Constraction'][type_constraction]:
                    spec['Constraction'][type_constraction][const] = [GOST, code_product, factory, units, qt,
                                                                            weight]
                else:
                    spec['Constraction'][type_constraction][const][4] += qt

        if basic_data != ['К-2', 'ДП']:
            for const, qt in ready_vedomost[i]['Elements']['Gorlovina Elements'].items():
                GOST = constraction['Горловина']['General info']['ГОСТ']
                code_product = ''
                factory = constraction['Горловина']['General info']['Завод'][0]
                units = constraction['Горловина']['General info']['Единцы изм']
                weight = constraction['Горловина'][const]['Вес']
                if const not in spec['Constraction']['Елементи горловини']:
                    spec['Constraction']['Елементи горловини'][const] = [GOST, code_product, factory, units, qt,
                                                                              weight]
                else:
                    spec['Constraction']['Елементи горловини'][const][4] += qt

        for const, qt in ready_vedomost[i]['Elements']['Other'].items():
            if const in type_grid:
                if basic_data[1] == 'ДП':
                    grid = qt[0]
                    GOST = type_grid[const]['ДП']['General info']['ГОСТ']
                    factory = type_grid[const]['ДП']['General info']['Завод'][0]
                    weight = type_grid[const]['ДП'][qt[0]]['Вес']
                    notice = ''
                else:
                    grid = type_grid[const][qt[0]]['Название']
                    GOST = type_grid[const]['General info']['ГОСТ']
                    factory = type_grid[const]['General info']['Завод'][0]
                    weight = type_grid[const][qt[0]]['Вес']
                    if basic_data[0] == 'К-1' or basic_data[0] == 'В-1':
                        notice = type_grid[const][qt[0]]['Примечание']
                code_product = ''
                qt_1 = qt[1]
                units = type_grid[const]['General info']['Единцы изм']
                if grid not in spec['Other']['Різне']:
                    if basic_data[0] == 'К-2':
                        spec['Other']['Різне'][grid] = [GOST, code_product, factory, units, qt_1, weight]
                    elif basic_data[0] == 'К-1' or basic_data[0] == 'В-1':
                        spec['Other']['Різне'][grid] = [GOST, code_product, factory, units, qt_1,
                                                        weight, notice]

                else:
                    spec['Other']['Різне'][grid][4] += qt_1
            if const in other:
                if basic_data[0] == 'В-1':
                    GOST = other[const]['Драбина']['ГОСТ']
                    code_product = ''
                    factory = other[const]['Драбина']['Завод']
                    units = other[const]['Драбина']['Единцы изм']
                    if 'Драбина' not in spec['Other']['Різне']:
                        spec['Other']['Різне']['Драбина'] = [GOST, code_product, factory, units, Decimal(qt)]
                    else:
                        spec['Other']['Різне']['Драбина'][4] += Decimal(qt)

                elif basic_data[0] == 'К-2' and const == 'Stairs' or basic_data == ['К-1', 'Колодязі'] and const == 'Stairs':
                    GOST = other[const]['Скоба ходова чавунна']['ГОСТ']
                    code_product = ''
                    factory = other[const]['Скоба ходова чавунна']['Завод'][0]
                    units = other[const]['Скоба ходова чавунна']['Единцы изм']
                    if 'Скоба ходова чавунна' not in spec['Other']['Різне']:
                        spec['Other']['Різне']['Скоба ходова чавунна'] = [GOST, code_product, factory, units, qt]
                    else:
                        spec['Other']['Різне']['Скоба ходова чавунна'][4] += qt
                elif basic_data == ['К-1', 'Колодязі з ПЕ'] and const == 'Stairs':
                    GOST = other[const]['Скоба ходова з ПЕ покриттям']['ГОСТ']
                    code_product = ''
                    factory = other[const]['Скоба ходова з ПЕ покриттям']['Завод'][0]
                    units = other[const]['Скоба ходова з ПЕ покриттям']['Единцы изм']
                    if 'Скоба ходова з ПЕ покриттям' not in spec['Other']['Різне']:
                        spec['Other']['Різне']['Скоба ходова з ПЕ покриттям'] = [GOST, code_product, factory, units, qt]
                    else:
                        spec['Other']['Різне']['Скоба ходова з ПЕ покриттям'][4] += qt
                elif const == 'Concrete':
                    GOST = other[const]['Бетонна суміш С12/15']['ГОСТ']
                    code_product = ''
                    factory = other[const]['Бетонна суміш С12/15']['Завод'][0]
                    units = other[const]['Бетонна суміш С12/15']['Единцы изм']
                    if 'Бетонна суміш С12/15' not in spec['Other']['Різне']:
                        spec['Other']['Різне']['Бетонна суміш С12/15'] = [GOST, code_product, factory, units, qt]
                    else:
                        spec['Other']['Різне']['Бетонна суміш С12/15'][4] += qt

def calculation_elmets_dp(ready_data: dict):
    global vedomost
    global type_grid
    for dp in ready_data:
        grid = ready_data[dp]['Elements']['Other']['Grid'][0]
        work_part = ready_data[dp]['Г-на кол'] - type_grid['Grid']['ДП'][grid]['Высота']
        vedomost[dp].update({'Work part': work_part})
        if work_part >= 400:
            zp1_pn = 0
            zp1_2_pn = 0
            zp_1 = 0
            zp_1_2 = 0
            vedomost[dp]['Elements'].update({'Constraction': {}})
            if work_part <= 800:
                zp1_2_pn += 1
                vedomost[dp]['Elements']['Constraction'].update({'ЗП1-2 ПН': zp1_2_pn})
                work_part -= 400
                if work_part >= 200:
                    vedomost[dp]['Elements']['Constraction'].update({'ЗП1-2': 1})
                    vedomost[dp].update({'Note': f'Підрізати ЗП1-2 до висоти {work_part}мм'})
            elif work_part >= 800:
                zp1_pn += 1
                vedomost[dp]['Elements']['Constraction'].update({'ЗП1 ПН': zp1_pn})
                work_part -= 800
                zp_1 += work_part // 800
                if zp_1 > 0:
                    vedomost[dp]['Elements']['Constraction'].update({'ЗП1': zp_1})
                work_part -= zp_1 * 800
                zp_1_2 += work_part // 400
                work_part -= zp_1_2 * 400
                if zp_1_2 > 0:
                    vedomost[dp]['Elements']['Constraction'].update({'ЗП1-2': zp_1_2})
                if work_part >= 200:
                    zp_1_2 += 1
                    vedomost[dp]['Elements']['Constraction'].update({'ЗП1-2': zp_1_2})
                    vedomost[dp].update({'Note': f'Підрізати ЗП1-2 до висоти {work_part}мм'})
                else:
                    vedomost[dp].update({'Note': f'Добрати {work_part}мм робочої висоти цеглою або ФЕМ'})
        else:
            showerror(title="Помилка!",
                      message="Висота робочої частини менше 400мм.\nПеревірте дані і повторіть розрахунок.")
            break


def calculate_elemeta_gorlovina(date: list):
    global type_grid
    global constraction
    vedomost_gorlovina = {'Constraction': {}, 'Other': {'Grid': [date[0][0], date[0][1]]}}
    name = date[4]
    grid = date[0][0]
    grid_qt = date[0][1]
    gorlovina_height = date[3]
    size_constraction = date[2]
    basic_data = date[1]
    h_pp = 0
    gorlovina_clean_height = 0
    if basic_data == ['В-1', 'Камери']:
        if size_constraction == '1.8x1.8' or size_constraction == '1.8x2.4' or size_constraction == '1.8x3.0':
            if 1 <= grid_qt <= 2:
                if 2 - grid_qt > 0: vedomost_gorlovina['Constraction'].update({'ЛЗБ-4': (2 - grid_qt)})
                vedomost_gorlovina['Other']['Grid'][1] = grid_qt
            else:
                grid_qt == 2
                if 2 - grid_qt > 0: vedomost_gorlovina['Constraction'].update({'ЛЗБ-4': (2 - grid_qt)})
                vedomost_gorlovina['Other']['Grid'][1] = grid_qt
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = (f'№ {name}. '
                                                                  f'Недопустима кількість люків (можлива кількість - 1шт. або 2шт.)')
        else:
            if 1 <= grid_qt <= 4:
                if 4 - grid_qt > 0: vedomost_gorlovina['Constraction'].update({'ЛЗБ-4': (4 - grid_qt)})
                vedomost_gorlovina['Other']['Grid'][1] = grid_qt
            else:
                grid_qt == 4
                if 4 - grid_qt > 0: vedomost_gorlovina['Constraction'].update({'ЛЗБ-4': (4 - grid_qt)})
                vedomost_gorlovina['Other']['Grid'][1] = grid_qt
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = (f'№ {name}. '
                                                                  f'Недопустима кількість люків (можлива кількість - 1-4шт.)')
        if grid == 'ВМ':
            vedomost_gorlovina['Constraction'].update({'ПД-6': grid_qt, 'КО-6': 1 * grid_qt})
            gorlovina_clean_height = gorlovina_height - 200 - 290 - 70
        else:
            gorlovina_clean_height = gorlovina_height - 200 - type_grid['Grid'][grid]['Высота']

    elif basic_data[1] == 'Колодязі' or basic_data[1] == 'Колодязі з ПЕ':
        if size_constraction == 1000:
            h_pp = constraction['Колодязі']['1ПП 10-2']['Толщина']
        elif size_constraction == 1500:
            h_pp = constraction['Колодязі']['1ПП 15-2']['Толщина']
        elif size_constraction == 2000:
            h_pp = constraction['Колодязі']['2ПП 20-2-1']['Толщина']
        if size_constraction == 2000:
            if 1 > grid_qt > 2:
                grid_qt == 1
                vedomost_gorlovina['Other']['Grid'][1] = grid_qt
                error_log['total_errors'] += 1
                error_log['errors'][error_log['total_errors']] = (f'№ {name}. '
                                                                  f'Недопустима кількість люків (можлива кількість - 1шт. або 2шт.)')
            if size_constraction == 1000 or size_constraction == 1500:
                if grid_qt != 1:
                    grid_qt == 1
                    vedomost_gorlovina['Other']['Grid'][1] = grid_qt
                    error_log['total_errors'] += 1
                    error_log['errors'][error_log['total_errors']] = (f'№ {name}. '
                                                                      f'Недопустима кількість люків (можлива кількість - 1шт. або 2шт.)')

        if grid == 'ВМ':
            vedomost_gorlovina['Constraction'].update({'ПД-6': grid_qt, 'КО-6': 1 * grid_qt})
            gorlovina_clean_height = gorlovina_height - h_pp - 290 - 70
        else:
            gorlovina_clean_height = gorlovina_height - h_pp - type_grid['Grid'][grid]['Высота']


    if gorlovina_clean_height > 450:
        gorlovina_clean_height -= 150  # Высота перекрытия КС 10
        vedomost_gorlovina['Constraction'].update({'1ПП 10-2': grid_qt})
        vedomost_gorlovina['Other'].update({'Stairs': 0})

        if gorlovina_clean_height < 600:
            ks_3 = gorlovina_clean_height // 300
            if ks_3 > 0:
                vedomost_gorlovina['Constraction'].update({'КС 10.3': ks_3 * grid_qt})
                vedomost_gorlovina['Other']['Stairs'] += Decimal(0.3) * Decimal(grid_qt)
                gorlovina_clean_height -= 300 * ks_3

        # Для правильного распределения КС.9 и КС.6, и что бы не использовать КС.3
        elif 300 <= gorlovina_clean_height - (900 * (gorlovina_clean_height // 900)) <= 600:
            ks_9 = (gorlovina_clean_height - 600) // 900
            if ks_9 > 0:
                vedomost_gorlovina['Constraction'].update({'КС 10.9': ks_9 * grid_qt})
                vedomost_gorlovina['Other']['Stairs'] += Decimal(0.9) * Decimal(grid_qt)
                gorlovina_clean_height -= 900 * ks_9
            ks_6 = gorlovina_clean_height // 600
            if ks_6 > 0:
                vedomost_gorlovina['Constraction'].update({'КС 10.6': ks_6 * grid_qt})
                vedomost_gorlovina['Other']['Stairs'] += Decimal(0.6) * Decimal(grid_qt)
                gorlovina_clean_height -= 600 * ks_6
        else:
            ks_9 = gorlovina_clean_height // 900
            if ks_9 > 0:
                vedomost_gorlovina['Constraction'].update({'КС 10.9': ks_9 * grid_qt})
                vedomost_gorlovina['Other']['Stairs'] += Decimal(0.9) * Decimal(grid_qt)
                gorlovina_clean_height -= 900 * ks_9
            ks_6 = gorlovina_clean_height // 600
            if ks_6 > 0:
                vedomost_gorlovina['Constraction'].update({'КС 10.6': ks_6 * grid_qt})
                vedomost_gorlovina['Other']['Stairs'] += Decimal(0.6) * Decimal(grid_qt)
                gorlovina_clean_height -= 600 * ks_6

    if gorlovina_clean_height <= 450:
        ks7 = gorlovina_clean_height // 300
        if ks7 > 0:
            vedomost_gorlovina['Constraction'].update({'КС7.3': ks7 * grid_qt})
            gorlovina_clean_height -= ks7 * 300

        ko6 = gorlovina_clean_height // 70
        if ko6 > 0:
            if 'КО-6' not in vedomost_gorlovina['Constraction']:
                vedomost_gorlovina['Constraction'].update({'КО-6': ko6 * grid_qt})
            else:
                vedomost_gorlovina['Constraction']['КО-6'] += (ko6 * grid_qt)
            gorlovina_clean_height -= ko6 * 70
    return vedomost_gorlovina


def calculation_elements_kameri(ready_data: dict):
    global vedomost
    global type_grid
    global kamiri_nabor
    for kameri in ready_data:
        height = ready_data[kameri]['Basic Data']['Height']
        size = ready_data[kameri]['Д_кол']
        vedomost[kameri]['Elements'].update({'Constraction': kamiri_nabor[height][size]})
        if height == 'Стандартна':
            work_part = 2100
            vedomost[kameri].update({'Work part': work_part})
            vedomost[kameri]['Elements']['Other']['Stairs'] = Decimal(1.90) * Decimal(vedomost[kameri]['Elements']['Other']['Grid'][1])
        else:
            work_part = 2100 + 560
            vedomost[kameri].update({'Work part': work_part})
            vedomost[kameri]['Elements']['Other']['Stairs'] = Decimal(2.50) * Decimal(vedomost[kameri]['Elements']['Other']['Grid'][1])
        gorlovina_height = ready_data[kameri]['Г-на кол'] - work_part
        vedomost[kameri].update({'Gorlovina height': gorlovina_height})
        for_gorlovina = [vedomost[kameri]['Elements']['Other']['Grid'],
                         [vedomost[kameri]['Basic Data']['Network'],
                          vedomost[kameri]['Basic Data']['Construction']],
                         vedomost[kameri]['Д_кол'],
                         gorlovina_height,
                         kameri]
        vedomost_gorlovina = calculate_elemeta_gorlovina(for_gorlovina)
        vedomost[kameri]['Elements'].update({'Gorlovina Elements': vedomost_gorlovina['Constraction']})
        vedomost[kameri]['Elements']['Other']['Grid'] = vedomost_gorlovina['Other']['Grid']
        if 'Stairs' in vedomost_gorlovina['Other']:
            vedomost[kameri]['Elements']['Other']['Stairs'] += vedomost_gorlovina['Other']['Stairs']

def calculation_concrete_lotok(diametr=0, lotok=0, type_lotok=''):
    diametr = Decimal(diametr) / Decimal(1000)
    lotok = Decimal(lotok) / Decimal(1000)
    r = (lotok - Decimal(0.1)) / 2
    v_concrete = 0
    if type_lotok == 'Стандартний':
        # Согласно ТПР: к диметру колодца нужно прибавить 400мм (0.4м)
        v_full_lotka = Decimal(3.14) * (((diametr + Decimal(0.4)) / 2) ** 2) * lotok
        # Принял толщину слоя под трубой 50мм (0.05м)
        v_concrete_under_pipe = Decimal(3.14) * (((diametr + Decimal(0.4)) / 2) ** 2) * Decimal(0.05)
        v_empty = (Decimal(3.14) * (r ** 2) * (diametr + Decimal(0.4))) / 2 + r * 2 * (lotok - r) * (diametr + Decimal(0.4))
        v_concrete = v_full_lotka - v_empty + v_concrete_under_pipe
    elif type_lotok == 'В колодязі':
        v_full_lotka = Decimal(3.14) * ((diametr/2)**2) * lotok
        # Принял толщину слоя под трубой 50мм (0.05м)
        v_concrete_under_pipe = Decimal(3.14) * ((diametr/2)**2) * Decimal(0.05)
        v_empty = (Decimal(3.14) * (r ** 2) * diametr) / 2 + r * 2 * (lotok - r) * diametr
        v_concrete = v_full_lotka - v_empty + v_concrete_under_pipe
    return v_concrete

def calculation_elements_kolodci(ready_data: dict, basic_data: list):
    global vedomost
    global type_grid
    lotok = 0
    type_lotka = ''
    for num in ready_data:
        vedomost[num]['Elements'].update({'Constraction': {}})
        diametr = ready_data[num]['Д_кол']
        if basic_data[0] == 'К-1' or basic_data[0] == 'К-2':
            lotok = ready_data[num]['Лоток']
            type_lotka = ready_data[num]['Basic Data']['Type lotok']
            # type_lotka = ''
        d_vedomost = int(diametr/100)
        grid = ready_data[num]['Elements']['Other']['Grid'][0]
        grid_qt = ready_data[num]['Elements']['Other']['Grid'][1]
        type_golovina = ready_data[num]['Basic Data']['Горловина']
        height_gorlovina = calculate_min_height_gorlovina(diametr=diametr, grid=grid, gorlovina=type_golovina, basic_data=basic_data)
        work_part = ready_data[num]['Г-на кол'] - height_gorlovina
        if basic_data[0] == 'К-1' and type_lotka == 'Стандартний' or basic_data[0] == 'К-2' and type_lotka == 'Стандартний':
            work_part -= lotok
            v_concrete = float(calculation_concrete_lotok(diametr=diametr, lotok=lotok,type_lotok=type_lotka))
            vedomost[num]['Elements']['Other'].update({'Concrete': v_concrete})
        elif basic_data[0] == 'К-1' and type_lotka != 'Стандартний' or basic_data[0] == 'К-2' and type_lotka != 'Стандартний':
            v_concrete = float(calculation_concrete_lotok(diametr=diametr, lotok=lotok,type_lotok=type_lotka))
            vedomost[num]['Elements']['Other'].update({'Concrete': v_concrete})

        vedomost[num]['Elements']['Constraction'].update({f'ПН-{d_vedomost}': 1})

        if d_vedomost == 20 and grid_qt == 1:
            vedomost[num]['Elements']['Constraction'].update({f'2ПП 20-2-1': 1})
        elif d_vedomost == 20 and grid_qt == 2:
            vedomost[num]['Elements']['Constraction'].update({f'2ПП 20-2-2': 1})
        else:
            vedomost[num]['Elements']['Constraction'].update({f'1ПП {d_vedomost}-2': 1})

        if work_part < 600:
            ks_3 = work_part // 300
            if ks_3 > 0:
                vedomost[num]['Elements']['Constraction'].update({f'КС {d_vedomost}.3': ks_3 * grid_qt})
                work_part -= 300 * ks_3

        # Для правильного распределения КС.9 и КС.6, и что бы не использовать КС.3
        if 300 <= work_part - (900 * (work_part // 900)) <= 600:
            ks_9 = (work_part - 600) // 900
            if ks_9 > 0:
                vedomost[num]['Elements']['Constraction'].update({f'КС {d_vedomost}.9': ks_9 * grid_qt})
                work_part -= 900 * ks_9
            ks_6 = work_part // 600
            if ks_6 > 0:
                vedomost[num]['Elements']['Constraction'].update({f'КС {d_vedomost}.6': ks_6 * grid_qt})
                work_part -= 600 * ks_6
        else:
            ks_9 = work_part // 900
            if ks_9 > 0:
                vedomost[num]['Elements']['Constraction'].update({f'КС {d_vedomost}.9': ks_9 * grid_qt})
                work_part -= 900 * ks_9
            ks_6 = work_part // 600
            if ks_6 > 0:
                vedomost[num]['Elements']['Constraction'].update({f'КС {d_vedomost}.6': ks_6 * grid_qt})
                work_part -= 600 * ks_6

        gorlovina_height = work_part + height_gorlovina
        vedomost[num]['Basic Data'].update({f'Gorlovina height': gorlovina_height})
        vedomost[num]['Basic Data'].update({f'Work part': ready_data[num]['Г-на кол'] - gorlovina_height})
        for_gorlovina = [vedomost[num]['Elements']['Other']['Grid'],
                         [vedomost[num]['Basic Data']['Network'], vedomost[num]['Basic Data']['Construction']],
                         vedomost[num]['Д_кол'],
                         gorlovina_height,
                         num]
        vedomost_gorlovina = calculate_elemeta_gorlovina(for_gorlovina)
        vedomost[num]['Elements'].update({'Gorlovina Elements': vedomost_gorlovina['Constraction']})

        if basic_data[0] == 'В-1':
            stairs = float(Decimal((ready_data[num]['Г-на кол'] - gorlovina_height)) / Decimal(1000))
            vedomost[num]['Elements']['Other'].update({'Stairs': stairs})
        else:
            skobi = (ready_data[num]['Г-на кол'] - gorlovina_height) // 300
            vedomost[num]['Elements']['Other'].update({'Stairs': skobi})

# if __name__ == '__main__':
def recieve_input_data(data):
    print(data)
    vedomost.clear()
    spec.clear()
    error_log.clear()
    check_input_data(data)
    basic_data = [data['main_data']['Network'], data['main_data']['Construction']]
    if basic_data == ['К-2', 'ДП']:
        calculation_elmets_dp(vedomost)
    elif basic_data == ['В-1', 'Камери']:
        calculation_elements_kameri(vedomost)
    elif basic_data[1] == 'Колодязі' or basic_data[1] == 'Колодязі з ПЕ':
        calculation_elements_kolodci(vedomost, basic_data)
    calculation_spec(vedomost, basic_data)

    print(vedomost)
    print(spec)
    print(error_log)
    return vedomost, spec, error_log

        # vedomost.clear()
        # spec.clear()
        # error_log.clear()


# recieve_input_data(kanal)
