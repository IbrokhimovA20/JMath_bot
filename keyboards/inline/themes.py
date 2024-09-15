from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import themes_callback

from loader import dp

# theme_5 = {'НОД и НОК':'nod_nok',
#         'Обыкновенные дроби': 'obiknovenniye_drobi',
#         'Десятичные дроби':'desyatichniye_drobi',
#         'Задачи на движение':'zadachi_na_dvijeniye',
#         'Признаки делимости чисел':'delimosti_chisel'}

theme_5_6 = {'Обыкновенные дроби': 'theme_obiknovenniye_drobi',
        'Десятичные дроби':'theme_desyatichniye_drobi',
        'Периодические дроби' : 'theme_period_drobi',
        'Действия над рациональными числами':'theme_ratsion_chisla',
        'Степень с рациональным показателем':'theme_stepen_ratsion_chisel'}

# theme_6 = {'Бесконечно периодические дроби': 'bes_per_drobi',
#     'Пропорция':'proportion',
#     'Масштаб':'masshtab',
#     'Целые числа':'chisla',
#     'Задачи на движение по воде':'dvij_po_vode'}


theme_7_8 = {'Одночлены  и многочлены' : 'theme_odno_mnogochlen',
            'Формулы сокращенного умножения' : 'theme_formula_umnoj',
            'Разложение на множители' : 'theme_razloj_mnojiteli',
            'Алгебраические дроби' : 'theme_algebra_drobi',
            'Арифметический корень' : 'theme_arif_koren',
            'Линейные уравнения' : 'theme_lin_uravneniya',
            'Квадратные уравнения' : 'theme_kvadrad_uravneniya',
            'Теорема Виета' : 'theme_teorema_vieta',
            'Уравнения высших степеней' : 'theme_urav_vish_step',
            'Система уравнений' : 'theme_sistema_uravneniy',
            'Неравенства + Система неравенств' : 'theme_sistema_lin_neravenstv',
            'Метод интервалов' : 'theme_metod_intervalov'}

# theme_7 = {'Степень':'stepen',
#     'Одночлены':'odnochlen',
#     'Многочлены':'mnogochlen',
#     'Разложение на множители':'razloj_mnojiteli',
#     'Формулы сокращённого умножения':'formula_umnoj',
#     'Алгебраические дроби':'algebra_drobi',
#     'Линейные уравнения':'lin_uravneniya',
#     'Система линейных уравнений':'sistema_lin_urav',
#     'Линейная функция':'lin_func'}

# theme_8 = {'Квадратрые корни':'kvadrad_korni',
#     'Квадратные уравнения':'kvadrad_uravneniya',
#     'Неполные квадратные уравнения':'nepolniye_kvadrad_uravneniya',
#     'Теорема Виета':'teorema_vieta',
#     'Уравнения сводящиеся к квадратным':'urav_svod_kvadrad',
#     'Линейные неравенства':'lin_neravenstva',
#     'Система линейных неравенств':'sistema_lin_neravenstv',
#     'Метод интервалов':'metod_intervalov'}




theme_9_10 = {'Модульные уравнения и неравенства':'modul_uravneniya',
    'Иррациональные уравнения и неравенства':'irrat_uravneniya_neravenstva',
    'Арифметическая прогрессия':'arif_progressiya',
    'Геометрическая прогрессия':'geometry_progressiya',
    'Линейная функция' : 'liney_funksiya',
    'Квадратичная функция' : 'kvadrat_funksiya',
    'Разные задачи на функцию' : 'raz_zadach_funksiya',
    'Степенные функции' : 'stepen_funksiya',
    'Обратная функция' : 'obrat_funksiya',
    'Показательные уравнения и неравенства':'pokaz_urav_neravenstva',
    'Логарифммические преобразования':'log_preobrazovaniya',
    'Логарифммические уравнения и неравенства':'log_urav_neravenstva',
    'Показательная и Логарифмическая функции':'log_funskiya'}

# theme_10 = {'Показательные уравнения и неравенства':'pokaz_urav_neravenstva',
#     'Показательная функция':'pokaz_funksiya',
#     'Логарифммические преобразования':'log_preobrazovaniya',
#     'Логарифммические уравнения и неравенства':'log_urav_neravenstva',
#     'Логарифмическая функция':'log_funskiya'}

theme_11 = {'Производная':'proizvodnaya',
    'Сложная производная':'sloj_prozivodnaya',
    'Промежутки возрастания функции, точки экстремума':'promejutki_vozrast_ekstremum',
    'Геометрический смысл производной':'geometry_smisl_proizvod',
    'Механический смысл производной':'mehanicheskiy_smisl_proizvod',
    'Первообразная':'pervoobraznaya',
    'Неопределенный интеграл':'neopredelenniy_integral',
    'Определенный интеграл, площадь криволинейной трапеции':'opred_integral_trapetsiya',
    'Метод замены переменных':'metod_zamena_peremenniye',
    'Интегрирование по частям':'integ_po_chastyam'}

geometriya_1 = {'Углы и основные понятия геометрии':'ugli',
    'Параллельные прямые':'paralel_pramoy',
    'Треугольники общие понятия':'treugolnik',
    'Виды треугольников,прямоугольный' : 'vidi_treugolnikov',
    'Треугольники Теорема синусов,косинусов Р б и Р н треугольники':'sin_kos_tan_cotan',
    'Высота, биссектрисы и медиана треугольника':'biss_mediana_visota'}

geometriya_2 = {'Площадь треугольника':'ploshad_treugolnikov',
    'Подобие треугольников и средняя линия':'podobiye_treugolnikov',
    '4_угольники,квадрат,прямоугольник':'kvadrat',
    'Ромб и параллелограмм':'parallelogram',
    'Трапеция':'trapetsiya',
    'Многоугольники':'mnogougolnik'}

geometriya_3 = {'Окружность и круг':'okrujnost_krug',
        'Площадь, длина и уравнение окружности':'ploshad',
        'Окружность + треугольник':'okrujnost_treugolnik',
        'Окружность + 4-угольник':'okrujnost_chugolnik',
        'Система координат и векторы':'sistema_koordinat',
        'Призма':'prizma'}
    
geometriya_4 = {'Пирамида':'piramida',
    'Цилиндр':'silindr',
       'Конус':'konus',
        'Шар и Сфера':'shar_sfera',
        'Комбинация тел':'kombinasiya'}


all_classes = {'5_6_class' : theme_5_6, '7_8_class' : theme_7_8, '9_10_class' : theme_9, '11_class' : theme_11}

nazad = InlineKeyboardButton(text='назад', callback_data='nazad_v_klass')




async def give_class_themes(class_theme):
    themes = InlineKeyboardMarkup(row_width=1)
    for key, value in all_classes[class_theme].items():
        themes.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=value)))
    themes.insert(nazad)
    return themes






# themes_5_6 = InlineKeyboardMarkup(row_width=1)
# for key, value in theme_5_6.items():
#     themes_5_6.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=value)))
# themes_5_6.insert(nazad)

# themes_7_8 = InlineKeyboardMarkup(row_width=1)
# for key,value in themes_7_8.items():
#     themes_7_8.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
# themes_7_8.insert(nazad)

# themes_8 = InlineKeyboardMarkup(row_width=1)
# for key,value in theme_8.items():
#     themes_8.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
# themes_8.insert(nazad)

# themes_9 = InlineKeyboardMarkup(row_width=1)
# for key,value in theme_9.items():
#     themes_9.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
# themes_9.insert(nazad)

# themes_10 = InlineKeyboardMarkup(row_width=1)
# for key,value in theme_10.items():
#     themes_10.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
# themes_10.insert(nazad)

# themes_11 = InlineKeyboardMarkup(row_width=1)
# for key,value in theme_11.items():
#     themes_11.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
# themes_11.insert(nazad)


page_1 = InlineKeyboardButton(text='1/4', callback_data=themes_callback.new('page_1'))
next_1 = InlineKeyboardButton(text='⏭', callback_data=themes_callback.new('next_1'))
geometriya_themes_1 = InlineKeyboardMarkup(row_width=1)
for key,value in geometriya_1.items():
    geometriya_themes_1.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
geometriya_themes_1.row(page_1, next_1)

prev_1 = InlineKeyboardButton(text='⏮', callback_data=themes_callback.new('prev_1'))
page_2 = InlineKeyboardButton(text='2/4', callback_data=themes_callback.new('page_2'))
next_2 = InlineKeyboardButton(text='⏭', callback_data=themes_callback.new('next_2'))
geometriya_themes_2 = InlineKeyboardMarkup(row_width=1)
for key,value in geometriya_2.items():
    geometriya_themes_2.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
geometriya_themes_2.row(prev_1, page_2, next_2)

prev_2 = InlineKeyboardButton(text='⏮', callback_data=themes_callback.new('prev_2'))
page_3 = InlineKeyboardButton(text='3/4', callback_data=themes_callback.new('page_3'))
next_3 = InlineKeyboardButton(text='⏭', callback_data=themes_callback.new('next_3'))
geometriya_themes_3 = InlineKeyboardMarkup(row_width=1)
for key,value in geometriya_3.items():
    geometriya_themes_3.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
geometriya_themes_3.row(prev_2, page_3, next_3)

prev_3 = InlineKeyboardButton(text='⏮', callback_data=themes_callback.new('prev_3'))
page_4 = InlineKeyboardButton(text='4/4', callback_data=themes_callback.new('page_4'))
geometriya_themes_4 = InlineKeyboardMarkup(row_width=1)
for key,value in geometriya_4.items():
    geometriya_themes_4.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
geometriya_themes_4.row(prev_3,page_4)

