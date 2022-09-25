from audioop import add
from cgitb import text
from gc import callbacks
from turtle import back
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import themes_callback

from loader import dp

theme_5 = {'НОД и НОК':'nod_nok',
        'Обыкновенные дроби': 'obiknovenniye_drobi',
        'Десятичные дроби':'desyatichniye_drobi',
        'Задачи на движение':'zadachi_na_dvijeniye',
        'Признаки делимости чисел':'delimosti_chisel'}

theme_6 = {'Бесконечно периодические дроби': 'bes_per_drobi',
    'Пропорция':'proportion',
    'Масштаб':'masshtab',
    'Целые числа':'chisla',
    'Задачи на движение по воде':'dvij_po_vode'}

theme_7 = {'Степень':'stepen',
    'Одночлены':'odnochlen',
    'Многочлены':'mnogochlen',
    'Разложение на множители':'razloj_mnojiteli',
    'Формулы сокращённого умножения':'formula_umnoj',
    'Алгебраические дроби':'algebra_drobi',
    'Линейные уравнения':'lin_uravneniya',
    'Система линейных уравнений':'sistema_lin_urav',
    'Линейная функция':'lin_func'}

theme_8 = {'Квадратрые корни':'kvadrad_korni',
    'Квадратные уравнения':'kvadrad_uravneniya',
    'Неполные квадратные уравнения':'nepolniye_kvadrad_uravneniya',
    'Теорема Виета':'teorema_vieta',
    'Уравнения сводящиеся к квадратным':'urav_svod_kvadrad',
    'Линейные неравенства':'lin_neravenstva',
    'Система линейных неравенств':'sistema_lin_neravenstv',
    'Метод интервалов':'metod_intervalov'}

theme_9 = {'Модульные уравнения и неравенства':'modul_uravneniya',
    'Иррациональные уравнения и неравенства':'irrat_uravneniya_neravenstva',
    'Арифметическая прогрессия':'arif_progressiya',
    'Геометрическая прогрессия':'geometry_progressiya',
    'Текстовые задачи':'tekst_zadachi'}

theme_10 = {'Показательные уравнения и неравенства':'pokaz_urav_neravenstva',
    'Показательная функция':'pokaz_funksiya',
    'Логарифммические преобразования':'log_preobrazovaniya',
    'Логарифммические уравнения и неравенства':'log_urav_neravenstva',
    'Логарифмическая функция':'log_funskiya'}

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

geometriya_1 = {'Смежные и вертикальные углы':'smej_vert_ugli',
    'Параллельные прямые':'paralel_pramoy',
    'Треугольник':'treugolnik',
    'Виды треугольников и их свойства':'vidi_treugolnikov',
    'Синус, косинус, тангенс и котангенс угла':'sin_kos_tan_cotan',
    'Теорема синусов, теорема косинусов':'teorema_sin_cos',
    'Биссектриса, медиана, высота':'biss_mediana_visota',
    'Площадь треугольника':'ploshad_treugolnikov',
    'Подобие треугольников':'podobiye_treugolnikov'}

geometriya_2 = {'Четырёхугольник':'chetirohugolnik',
        'Параллелограмм':'parallelogram',
        'Ромб':'romb',
        'Прямоугольник':'pryamougolnik',
        'Квадрат':'kvadrat',
        'Окружность и круг':'okrujnost_krug',
        'Сектор и сегмент':'sektor_segment',
        'Уравнение окружности':'urav_okrujnosti',
        'Треугольник и окружность':'treugol_okrujnost'}

geometriya_3 = {'Четырёхугольник и окружность':'chetiryoh_okrujnost',
       'Многоугольник и окружность':'mnogougol_okrujnost',
        'Векторы':'vektori',
        'Многогранники':'mnogogranniki',
        'Призма':'prizma',
        'Трапеция':'trapetsiya',
        'Параллелепипед':'paralepiped',
        'Куб':'kub'}
    
geometriya_4 = {'Пирамида':'piramida',
        'Цилиндр':'silindr',
        'Конус':'konus',
        'Шар и сфера':'shar_sfera',
        'Призма и шар':'prizma_shar',
        'Пирамида и шар':'piramida_shar',
        'Цилиндр и шар':'silindr_shar',
        'Конус и шар':'konus_shar'}

nazad = InlineKeyboardButton(text='назад', callback_data='nazad_v_klass')

themes_5 = InlineKeyboardMarkup(row_width=1)
for key, value in theme_5.items():
    themes_5.insert(InlineKeyboardButton(text=key, callback_data = themes_callback.new(item_name=value)))
themes_5.insert(nazad)

themes_6 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_6.items():
    themes_6.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_6.insert(nazad)

themes_7 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_7.items():
    themes_7.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_7.insert(nazad)

themes_8 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_8.items():
    themes_8.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_8.insert(nazad)

themes_9 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_9.items():
    themes_9.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_9.insert(nazad)

themes_10 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_10.items():
    themes_10.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_10.insert(nazad)

themes_11 = InlineKeyboardMarkup(row_width=1)
for key,value in theme_11.items():
    themes_11.insert(InlineKeyboardButton(text=key, callback_data=themes_callback.new(item_name=value)))
themes_11.insert(nazad)


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

