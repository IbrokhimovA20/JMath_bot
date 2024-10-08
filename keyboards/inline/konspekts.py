from audioop import add
from cgitb import text
from gc import callbacks
from unicodedata import category
from unittest.mock import call
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import lesson_callback

nazad_5_6 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_5_6')
nazad_7_8 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_7_8')
# nazad_8 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_8')
nazad_9 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_9')
nazad_10 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_10')
nazad_11 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_11')
nazad_geometry_1 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_geometry_1')
nazad_geometry_2 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_geometry_2')
nazad_geometry_3 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_geometry_3')
nazad_geometry_4 = InlineKeyboardButton(text='назад к темам', callback_data='nazad_geometry_4')


docs = {'obiknovenniye_drobi' : {'Шпаргалка' : True, 'Примеры' : True,'видеоурок' : 'https://youtu.be/GbJfzwRQ6kQ?si=D2_MgYN-eUX0q7rb', 'back' : nazad_5_6},
        'desyatichniye_drobi' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' : 'https://youtu.be/_iJ8GeNTxJQ?si=xoLSU7JoGid5ZCPr', 'back' : nazad_5_6},
        'period_drobi' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' : 'https://youtu.be/qcnyTmXJzjs?si=9XAUNgTVpeOiE9eN', 'back' : nazad_5_6},
        'ratsion_chisla' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' : 'https://youtu.be/DqrO4G6Irg0?si=WMnxXJoQ-yJK4zf3', 'back' : nazad_5_6},
        'stepen_ratsion_chisel' : {'Шпаргалка' : True, 'Примеры' : True,'видеоурок' : 'https://youtu.be/daFHLipLYBg?si=keVSWYccjA_hrgHb', 'back' : nazad_7_8},
        'odno_mnogochlen' : {'Шпаргалка' : True, 'Примеры' : True,'видеоурок' : 'https://youtu.be/5D8Z74at47o','back' : nazad_7_8},
        'formula_umnoj' : {'Шпаргалка' : True, 'Примеры' : True,'видеоурок' : False,'back' : nazad_7_8},
        'razloj_mnojiteli' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' : False,'back' : nazad_7_8},
        'algebra_drobi' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' : False,'back' : nazad_7_8},
        'arif_koren' : {'Шпаргалка' : True, 'Примеры' : True,'видеоурок' :'https://youtu.be/6AC2Chg7j48?si=wKpSI79RkrqGcgfg','back' : nazad_7_8},
        'lin_uravneniya' : {'Шпаргалка' : False,'Примеры' : False, 'видеоурок' :False,'back' : nazad_7_8},
        'kvadrad_uravneniya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False,'back' : nazad_7_8},
        'teorema_vieta' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False,'back' : nazad_7_8},
        'urav_vish_step' :{'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False,'back' : nazad_7_8},
        'sistema_uravneniy' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/oeiIeVCnuts?si=78G0tH9wrVcnO-SK','back' : nazad_7_8},
        'sistema_lin_neravenstv' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False,'back' : nazad_7_8},
        'metod_intervalov' :  {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/eZVExkq7Qw4?si=34EppADohUYRIwoZ','back' : nazad_7_8},
        'modul_uravneniya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/xfxx849a2Xc?si=fEfPnee9NIiLl2xQ','back' : nazad_7_8},
        'irrat_uravneniya_neravenstva' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/YZYMrk_A9Js?si=2_ZElnwisoNTIX6I', 'back' : nazad_7_8},
        'arif_progressiya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/tMkawjepqZQ?si=8bivI-J0SzO33giT', 'back' : nazad_7_8},
        'geometry_progressiya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/ZDIME3uZqts?si=v55ICXH0Cfc2q1nx', 'back' : nazad_7_8},
        'liney_funksiya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/XtaLastSBWA?si=78lcsdjPMFohxXjh', 'back' : nazad_7_8},
        'kvadrat_funksiya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/LSQKcvOJBXs?si=WY6al8mI5GYHizbC', 'back' : nazad_7_8},
        'raz_zadach_funksiya' : {'Шпаргалка' : False,'Примеры' : False, 'видеоурок' :'https://youtu.be/9FMmTF0Dja8?si=5SZFzqlcEa0S_bZu', 'back' : nazad_7_8},
        'stepen_funksiya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_7_8},
        'obrat_funksiya' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_7_8},
        'pokaz_urav_neravenstva' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/Ce9HjJxDNA0?si=s8UfQzYiVesc4M_O', 'back' : nazad_7_8},
        'log_preobrazovaniya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/Bq7TuElu7-4?si=nOEdC0T8wJvMK2nB', 'back' : nazad_7_8},
        'log_urav_neravenstva' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :'https://youtu.be/EfSoPwvUrh0?si=oa_O78aZCnHKt3lC', 'back' : nazad_7_8},
        'log_funskiya' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_7_8},
        'osnov_ponyatiya' :{'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_9},
        'osnov_tokdestva' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'formuli_privedeniya' : {'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_9},
        'formuli_slojeniya' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'dvoynoy_ugol' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'form_sum_rznost' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'form_proizved' : {'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_9},
        'form_pol_ugla' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'obr_trigio_funk' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'trigo_uravneniya' : {'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_9},
        'trigo_nerav' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'trigo_funk' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_9},
        'roizvod_prost_func' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'proizvod_sloj_func' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'issled_func' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'fiz_mex_func' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'pervob_integral' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'metod_zamen_peremen' : {'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_10},
        'integ_chasti' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'opred_integral' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_10},
        'mnojestva' : {'Шпаргалка' : False,'Примеры' : True, 'видеоурок' :False, 'back' : nazad_11},
        'kombinatorika' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_11},
        'teor_veroyat' : {'Шпаргалка' : False, 'Примеры' : True,'видеоурок' :False, 'back' : nazad_11},
        'param_lin_urav' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11},
        'param_kvadrat_urav' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11},
        'sistema_param_urav' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11},
        'zadach_chisla' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11},
        'zadach_dvij' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11},
        'zadach_sovm_rabota' : {'Шпаргалка' : False,'Примеры' : False, 'видеоурок' :False, 'back' : nazad_11},
        'zadach_protsent' : {'Шпаргалка' : False,'Примеры' : False, 'видеоурок' :False, 'back' : nazad_11},
        'zadach_smes' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' :False, 'back' : nazad_11}}


docs_geot = {'ugli' :  {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'paralel_pramoy' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'treugolnik' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'vidi_treugolnikov' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'sin_kos_tan_cotan' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'biss_mediana_visota' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_1},
            'ploshad_treugolnikov' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'podobiye_treugolnikov' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'kvadrat' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'parallelogram' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'trapetsiya' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'mnogougolnik' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_2},
            'okrujnost_krug' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'ploshad' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'okrujnost_treugolnik' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'okrujnost_chugolnik' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'sistema_koordinat' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'prizma' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_3},
            'piramida' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_4},
            'silindr' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_4},
            'konus' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_4},
            'shar_sfera' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_4},
            'kombinasiya' : {'Шпаргалка' : False, 'Примеры' : False,'видеоурок' : False,'back' : nazad_geometry_4}}



async def give_documents(theme):
    # documents = InlineKeyboardMarkup(row_width=1)
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_keyboard.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name=f'teor_{theme}')))
    if docs[theme]['Примеры']:
        inline_keyboard.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name=f'prim_{theme}')))
    if docs[theme]['Шпаргалка']:
        inline_keyboard.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name=f'shpar_{theme}')))
    if docs[theme]['видеоурок']:
        inline_keyboard.insert(InlineKeyboardButton(text='видеоурок', url=docs[theme]['видеоурок']))
    inline_keyboard.insert(docs[theme]['back'])
    return inline_keyboard


async def give_geot_documents(theme):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_keyboard.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name=f'teor_geot_{theme}')))
    if docs_geot[theme]['Примеры']:
        inline_keyboard.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name=f'prim_geot_{theme}')))
    if docs_geot[theme]['Шпаргалка']:
        inline_keyboard.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name=f'shpar_geot_{theme}')))
    if docs_geot[theme]['видеоурок']:
        inline_keyboard.insert(InlineKeyboardButton(text='видеоурок', url=docs_geot[theme]['видеоурок']))
    inline_keyboard.insert(docs_geot[theme]['back'])
    return inline_keyboard





# obiknovenniye_drobi = InlineKeyboardMarkup(row_width=1)
# obiknovenniye_drobi.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_obiknovenniye_drobi')))
# obiknovenniye_drobi.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_obiknovenniye_drobi')))
# obiknovenniye_drobi.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_obiknovenniye_drobi')))
# obiknovenniye_drobi.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/GbJfzwRQ6kQ?si=D2_MgYN-eUX0q7rb'))
# obiknovenniye_drobi.insert(nazad_5_6)

# desyatichniye_drobi = InlineKeyboardMarkup(row_width=1)
# desyatichniye_drobi.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_desyatichniye_drobi')))
# desyatichniye_drobi.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_desyatichniye_drobi')))
# desyatichniye_drobi.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/_iJ8GeNTxJQ?si=xoLSU7JoGid5ZCPr'))
# desyatichniye_drobi.insert(nazad_5_6)


# per_drobi = InlineKeyboardMarkup(row_width=1)
# per_drobi.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_per_drobi')))
# per_drobi.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_per_drobi')))
# per_drobi.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/qcnyTmXJzjs?si=9XAUNgTVpeOiE9eN'))
# per_drobi.insert(nazad_5_6)

# ratsion_chisla = InlineKeyboardMarkup(row_width=1)
# ratsion_chisla.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_ratsion_chisla')))
# ratsion_chisla.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_ratsion_chisla')))
# ratsion_chisla.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/DqrO4G6Irg0?si=WMnxXJoQ-yJK4zf3'))
# ratsion_chisla.insert(nazad_5_6)


# stepen_rat_chisla = InlineKeyboardMarkup(row_width=1)
# stepen_rat_chisla.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_stepen_rat_chisla')))
# stepen_rat_chisla.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_stepen_rat_chisla')))
# stepen_rat_chisla.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_stepen_rat_chisla')))
# stepen_rat_chisla.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/daFHLipLYBg?si=keVSWYccjA_hrgHb'))
# stepen_rat_chisla.insert(nazad_5_6)

# proportion = InlineKeyboardMarkup(row_width=1)
# proportion.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_proportion')))
# proportion.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# proportion.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_proportion')))
# proportion.insert(nazad_6)

# masshtab = InlineKeyboardMarkup(row_width=1)
# masshtab.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_masshtab')))
# masshtab.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# masshtab.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_masshtab')))
# masshtab.insert(nazad_6)

# chisla = InlineKeyboardMarkup(row_width=1)
# chisla.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_chisla')))
# chisla.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# chisla.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_chisla')))
# chisla.insert(nazad_6)

# dvij_po_vode = InlineKeyboardMarkup(row_width=1)
# dvij_po_vode.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_dvij_po_vode')))
# dvij_po_vode.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# dvij_po_vode.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_dvij_po_vode')))
# dvij_po_vode.insert(nazad_6)

# stepen = InlineKeyboardMarkup(row_width=1)
# stepen.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_stepen')))
# stepen.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# stepen.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_stepen')))
# stepen.insert(nazad_7)

# odnochlen = InlineKeyboardMarkup(row_width=1)
# odnochlen.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_odnochlen')))
# odnochlen.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_odnochlen')))
# odnochlen.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_odnochlen')))
# odnochlen.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# # odnochlen.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_odnochlen')))
# odnochlen.insert(nazad_7_8)


# mnogochlen = InlineKeyboardMarkup(row_width=1)
# mnogochlen.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_mnogochlen')))
# mnogochlen.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# mnogochlen.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_mnogochlen')))
# mnogochlen.insert(nazad_7_8)

# delimosti_chisel = InlineKeyboardMarkup(row_width=1)
# delimosti_chisel.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_delimosti_chisel')))
# delimosti_chisel.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# delimosti_chisel.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_delimosti_chisel')))
# delimosti_chisel.insert(nazad_7_8)

# formula_umnoj = InlineKeyboardMarkup(row_width=1)
# formula_umnoj.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_formula_umnoj')))
# formula_umnoj.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_formula_umnoj')))
# formula_umnoj.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_formula_umnoj')))
# formula_umnoj.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# # formula_umnoj.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_formula_umnoj')))
# formula_umnoj.insert(nazad_7_8)


# razloj_mnojiteli = InlineKeyboardMarkup(row_width=1)
# razloj_mnojiteli.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_razloj_mnojiteli')))
# razloj_mnojiteli.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_razloj_mnojiteli')))
# razloj_mnojiteli.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='prim_razloj_mnojiteli')))
# razloj_mnojiteli.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# # razloj_mnojiteli.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_razloj_mnojiteli')))
# razloj_mnojiteli.insert(nazad_7_8)


# algebra_drobi = InlineKeyboardMarkup(row_width=1)
# algebra_drobi.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_algebra_drobi')))
# algebra_drobi.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_algebra_drobi')))
# algebra_drobi.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_algebra_drobi')))
# algebra_drobi.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# # algebra_drobi.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_algebra_drobi')))
# algebra_drobi.insert(nazad_7_8)

# arif_koren = InlineKeyboardMarkup(row_width=1)
# arif_koren.insert(InlineKeyboardButton(text='Теория', callback_data=lesson_callback.new(item_name='teor_arif_koren')))
# arif_koren.insert(InlineKeyboardButton(text='Примеры', callback_data=lesson_callback.new(item_name='prim_arif_koren')))
# arif_koren.insert(InlineKeyboardButton(text='Шпаргалка', callback_data=lesson_callback.new(item_name='shpar_arif_koren')))
# arif_koren.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# # algebra_drobi.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_algebra_drobi')))
# arif_koren.insert(nazad_7_8)

# lin_uravneniya = InlineKeyboardMarkup(row_width=1)
# lin_uravneniya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_lin_uravneniya')))
# lin_uravneniya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# lin_uravneniya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_lin_uravneniya')))
# lin_uravneniya.insert(nazad_7_8)

# sistema_lin_urav = InlineKeyboardMarkup(row_width=1)
# sistema_lin_urav.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_sistema_lin_urav')))
# sistema_lin_urav.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# sistema_lin_urav.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_sistema_lin_urav')))
# sistema_lin_urav.insert(nazad_7_8)

# lin_func = InlineKeyboardMarkup(row_width=1)
# lin_func.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_lin_func')))
# lin_func.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# lin_func.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_lin_func')))
# lin_func.insert(nazad_7_8)

# kvadrad_korni = InlineKeyboardMarkup(row_width=1)
# kvadrad_korni.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_kvadrad_korni')))
# kvadrad_korni.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# kvadrad_korni.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_kvadrad_korni')))
# kvadrad_korni.insert(nazad_7_8)

# kvadrad_uravneniya = InlineKeyboardMarkup(row_width=1)
# kvadrad_uravneniya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_kvadrad_uravneniya')))
# kvadrad_uravneniya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# kvadrad_uravneniya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_kvadrad_uravneniya')))
# kvadrad_uravneniya.insert(nazad_7_8)

# nepolniye_kvadrad_uravneniya = InlineKeyboardMarkup(row_width=1)
# nepolniye_kvadrad_uravneniya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_nepolniye_kvadrad_uravneniya')))
# nepolniye_kvadrad_uravneniya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# nepolniye_kvadrad_uravneniya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_nepolniye_kvadrad_uravneniya')))
# nepolniye_kvadrad_uravneniya.insert(nazad_7_8)

# teorema_vieta = InlineKeyboardMarkup(row_width=1)
# teorema_vieta.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_teorema_vieta')))
# teorema_vieta.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# teorema_vieta.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_teorema_vieta')))
# teorema_vieta.insert(nazad_7_8)

# urav_svod_kvadrad = InlineKeyboardMarkup(row_width=1)
# urav_svod_kvadrad.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_urav_svod_kvadrad')))
# urav_svod_kvadrad.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# urav_svod_kvadrad.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_urav_svod_kvadrad')))
# urav_svod_kvadrad.insert(nazad_7_8)

# lin_neravenstva = InlineKeyboardMarkup(row_width=1)
# lin_neravenstva.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_lin_neravenstva')))
# lin_neravenstva.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# lin_neravenstva.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_lin_neravenstva')))
# lin_neravenstva.insert(nazad_7_8)

# sistema_lin_neravenstv = InlineKeyboardMarkup(row_width=1)
# sistema_lin_neravenstv.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_sistema_lin_neravenstv')))
# sistema_lin_neravenstv.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# sistema_lin_neravenstv.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_sistema_lin_neravenstv')))
# sistema_lin_neravenstv.insert(nazad_7_8)

# metod_intervalov = InlineKeyboardMarkup(row_width=1)
# metod_intervalov.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_metod_intervalov')))
# metod_intervalov.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# metod_intervalov.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_metod_intervalov')))
# metod_intervalov.insert(nazad_7_8)

# modul_uravneniya = InlineKeyboardMarkup(row_width=1)
# modul_uravneniya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_modul_uravneniya')))
# modul_uravneniya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# modul_uravneniya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_modul_uravneniya')))
# modul_uravneniya.insert(nazad_9)

# irrat_uravneniya_neravenstva = InlineKeyboardMarkup(row_width=1)
# irrat_uravneniya_neravenstva.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_irrat_uravneniya_neravenstva')))
# irrat_uravneniya_neravenstva.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# irrat_uravneniya_neravenstva.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_irrat_uravneniya_neravenstva')))
# irrat_uravneniya_neravenstva.insert(nazad_9)

# arif_progressiya = InlineKeyboardMarkup(row_width=1)
# arif_progressiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_arif_progressiya')))
# arif_progressiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# arif_progressiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_arif_progressiya')))
# arif_progressiya.insert(nazad_9)

# geometry_progressiya = InlineKeyboardMarkup(row_width=1)
# geometry_progressiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_geometry_progressiya')))
# geometry_progressiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# geometry_progressiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_geometry_progressiya')))
# geometry_progressiya.insert(nazad_9)

# tekst_zadachi = InlineKeyboardMarkup(row_width=1)
# tekst_zadachi.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_tekst_zadachi')))
# tekst_zadachi.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# tekst_zadachi.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_tekst_zadachi')))
# tekst_zadachi.insert(nazad_9)

# pokaz_urav_neravenstva = InlineKeyboardMarkup(row_width=1)
# pokaz_urav_neravenstva.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_pokaz_urav_neravenstva')))
# pokaz_urav_neravenstva.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# pokaz_urav_neravenstva.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_pokaz_urav_neravenstva')))
# pokaz_urav_neravenstva.insert(nazad_10)

# pokaz_funksiya = InlineKeyboardMarkup(row_width=1)
# pokaz_funksiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_pokaz_funksiya')))
# pokaz_funksiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# pokaz_funksiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_pokaz_funksiya')))
# pokaz_funksiya.insert(nazad_10)

# log_preobrazovaniya = InlineKeyboardMarkup(row_width=1)
# log_preobrazovaniya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_log_preobrazovaniya')))
# log_preobrazovaniya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# log_preobrazovaniya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_log_preobrazovaniya')))
# log_preobrazovaniya.insert(nazad_10)

# log_urav_neravenstva = InlineKeyboardMarkup(row_width=1)
# log_urav_neravenstva.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_log_urav_neravenstva')))
# log_urav_neravenstva.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# log_urav_neravenstva.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_log_urav_neravenstva')))
# log_urav_neravenstva.insert(nazad_10)

# log_funskiya = InlineKeyboardMarkup(row_width=1)
# log_funskiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_log_funskiya')))
# log_funskiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# log_funskiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_log_funskiya')))
# log_funskiya.insert(nazad_10)

# proizvodnaya = InlineKeyboardMarkup(row_width=1)
# proizvodnaya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_proizvodnaya')))
# proizvodnaya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# proizvodnaya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_proizvodnaya')))
# proizvodnaya.insert(nazad_11)

# sloj_prozivodnaya = InlineKeyboardMarkup(row_width=1)
# sloj_prozivodnaya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_sloj_prozivodnaya')))
# sloj_prozivodnaya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# sloj_prozivodnaya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_sloj_prozivodnaya')))
# sloj_prozivodnaya.insert(nazad_11)

# promejutki_vozrast_ekstremum = InlineKeyboardMarkup(row_width=1)
# promejutki_vozrast_ekstremum.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_promejutki_vozrast_ekstremum')))
# promejutki_vozrast_ekstremum.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# promejutki_vozrast_ekstremum.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_promejutki_vozrast_ekstremum')))
# promejutki_vozrast_ekstremum.insert(nazad_11)

# geometry_smisl_proizvod = InlineKeyboardMarkup(row_width=1)
# geometry_smisl_proizvod.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_geometry_smisl_proizvod')))
# geometry_smisl_proizvod.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# geometry_smisl_proizvod.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_geometry_smisl_proizvod')))
# geometry_smisl_proizvod.insert(nazad_11)

# mehanicheskiy_smisl_proizvod = InlineKeyboardMarkup(row_width=1)
# mehanicheskiy_smisl_proizvod.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_mehanicheskiy_smisl_proizvod')))
# mehanicheskiy_smisl_proizvod.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# mehanicheskiy_smisl_proizvod.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_mehanicheskiy_smisl_proizvod')))
# mehanicheskiy_smisl_proizvod.insert(nazad_11)

# pervoobraznaya = InlineKeyboardMarkup(row_width=1)
# pervoobraznaya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_pervoobraznaya')))
# pervoobraznaya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# pervoobraznaya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_pervoobraznaya')))
# pervoobraznaya.insert(nazad_11)

# neopredelenniy_integral = InlineKeyboardMarkup(row_width=1)
# neopredelenniy_integral.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_neopredelenniy_integral')))
# neopredelenniy_integral.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# neopredelenniy_integral.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_neopredelenniy_integral')))
# neopredelenniy_integral.insert(nazad_11)

# opred_integral_trapetsiya = InlineKeyboardMarkup(row_width=1)
# opred_integral_trapetsiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_opred_integral_trapetsiya')))
# opred_integral_trapetsiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# opred_integral_trapetsiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_opred_integral_trapetsiya')))
# opred_integral_trapetsiya.insert(nazad_11)

# metod_zamena_peremenniye = InlineKeyboardMarkup(row_width=1)
# metod_zamena_peremenniye.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_metod_zamena_peremenniye')))
# metod_zamena_peremenniye.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# metod_zamena_peremenniye.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_metod_zamena_peremenniye')))
# metod_zamena_peremenniye.insert(nazad_11)

# integ_po_chastyam = InlineKeyboardMarkup(row_width=1)
# integ_po_chastyam.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_integ_po_chastyam')))
# integ_po_chastyam.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# integ_po_chastyam.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_integ_po_chastyam')))
# integ_po_chastyam.insert(nazad_11)

# smej_vert_ugli = InlineKeyboardMarkup(row_width=1)
# smej_vert_ugli.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_smej_vert_ugli')))
# smej_vert_ugli.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# smej_vert_ugli.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_smej_vert_ugli')))
# smej_vert_ugli.insert(nazad_geometry_1)

# paralel_pramoy = InlineKeyboardMarkup(row_width=1)
# paralel_pramoy.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_paralel_pramoy')))
# paralel_pramoy.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# paralel_pramoy.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_paralel_pramoy')))
# paralel_pramoy.insert(nazad_geometry_1)

# treugolnik = InlineKeyboardMarkup(row_width=1)
# treugolnik.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_treugolnik')))
# treugolnik.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# treugolnik.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_treugolnik')))
# treugolnik.insert(nazad_geometry_1)

# vidi_treugolnikov = InlineKeyboardMarkup(row_width=1)
# vidi_treugolnikov.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_vidi_treugolnikov')))
# vidi_treugolnikov.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# vidi_treugolnikov.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_vidi_treugolnikov')))
# vidi_treugolnikov.insert(nazad_geometry_1)

# sin_kos_tan_cotan = InlineKeyboardMarkup(row_width=1)
# sin_kos_tan_cotan.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_sin_kos_tan_cotan')))
# sin_kos_tan_cotan.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# sin_kos_tan_cotan.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_sin_kos_tan_cotan')))
# sin_kos_tan_cotan.insert(nazad_geometry_1)

# teorema_sin_cos = InlineKeyboardMarkup(row_width=1)
# teorema_sin_cos.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_teorema_sin_cos')))
# teorema_sin_cos.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# teorema_sin_cos.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_teorema_sin_cos')))
# teorema_sin_cos.insert(nazad_geometry_1)

# biss_mediana_visota = InlineKeyboardMarkup(row_width=1)
# biss_mediana_visota.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_biss_mediana_visota')))
# biss_mediana_visota.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# biss_mediana_visota.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_biss_mediana_visota')))
# biss_mediana_visota.insert(nazad_geometry_1)

# ploshad_treugolnikov = InlineKeyboardMarkup(row_width=1)
# ploshad_treugolnikov.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_ploshad_treugolnikov')))
# ploshad_treugolnikov.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# ploshad_treugolnikov.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_ploshad_treugolnikov')))
# ploshad_treugolnikov.insert(nazad_geometry_1)

# podobiye_treugolnikov = InlineKeyboardMarkup(row_width=1)
# podobiye_treugolnikov.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_podobiye_treugolnikov')))
# podobiye_treugolnikov.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# podobiye_treugolnikov.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_podobiye_treugolnikov')))
# podobiye_treugolnikov.insert(nazad_geometry_1)

# chetirohugolnik = InlineKeyboardMarkup(row_width=1)
# chetirohugolnik.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_chetirohugolnik')))
# chetirohugolnik.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# chetirohugolnik.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_chetirohugolnik')))
# chetirohugolnik.insert(nazad_geometry_2)

# parallelogram = InlineKeyboardMarkup(row_width=1)
# parallelogram.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_parallelogram')))
# parallelogram.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# parallelogram.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_parallelogram')))
# parallelogram.insert(nazad_geometry_2)

# mnogougolnik = InlineKeyboardMarkup(row_width=1)
# mnogougolnik.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_mnogougolnik')))
# mnogougolnik.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# mnogougolnik.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_smnogougolnik')))
# mnogougolnik.insert(nazad_geometry_2)

# romb = InlineKeyboardMarkup(row_width=1)
# romb.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_romb')))
# romb.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# romb.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_romb')))
# romb.insert(nazad_geometry_2)

# pryamougolnik = InlineKeyboardMarkup(row_width=1)
# pryamougolnik.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_pryamougolnik')))
# pryamougolnik.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# pryamougolnik.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_pryamougolnik')))
# pryamougolnik.insert(nazad_geometry_2)

# kvadrat = InlineKeyboardMarkup(row_width=1)
# kvadrat.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_kvadrat')))
# kvadrat.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# kvadrat.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_kvadrat')))
# kvadrat.insert(nazad_geometry_2)

# okrujnost_krug = InlineKeyboardMarkup(row_width=1)
# okrujnost_krug.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_okrujnost_krug')))
# okrujnost_krug.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# okrujnost_krug.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_okrujnost_krug')))
# okrujnost_krug.insert(nazad_geometry_2)

# sektor_segment = InlineKeyboardMarkup(row_width=1)
# sektor_segment.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_sektor_segment')))
# sektor_segment.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# sektor_segment.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_sektor_segment')))
# sektor_segment.insert(nazad_geometry_2)

# urav_okrujnosti = InlineKeyboardMarkup(row_width=1)
# urav_okrujnosti.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_urav_okrujnosti')))
# urav_okrujnosti.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# urav_okrujnosti.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_urav_okrujnosti')))
# urav_okrujnosti.insert(nazad_geometry_2)

# treugol_okrujnost = InlineKeyboardMarkup(row_width=1)
# treugol_okrujnost.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_treugol_okrujnost')))
# treugol_okrujnost.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# treugol_okrujnost.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_treugol_okrujnost')))
# treugol_okrujnost.insert(nazad_geometry_2)

# chetiryoh_okrujnost = InlineKeyboardMarkup(row_width=1)
# chetiryoh_okrujnost.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_chetiryoh_okrujnost')))
# chetiryoh_okrujnost.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# chetiryoh_okrujnost.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_chetiryoh_okrujnost')))
# chetiryoh_okrujnost.insert(nazad_geometry_3)

# mnogougol_okrujnost = InlineKeyboardMarkup(row_width=1)
# mnogougol_okrujnost.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_mnogougol_okrujnost')))
# mnogougol_okrujnost.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# mnogougol_okrujnost.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_mnogougol_okrujnost')))
# mnogougol_okrujnost.insert(nazad_geometry_3)

# vektori = InlineKeyboardMarkup(row_width=1)
# vektori.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_vektori')))
# vektori.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# vektori.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_vektori')))
# vektori.insert(nazad_geometry_3)

# mnogogranniki = InlineKeyboardMarkup(row_width=1)
# mnogogranniki.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_mnogogranniki')))
# mnogogranniki.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# mnogogranniki.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_mnogogranniki')))
# mnogogranniki.insert(nazad_geometry_3)

# prizma = InlineKeyboardMarkup(row_width=1)
# prizma.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_prizma')))
# prizma.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# prizma.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_prizma')))
# prizma.insert(nazad_geometry_3)

# trapetsiya = InlineKeyboardMarkup(row_width=1)
# trapetsiya.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_trapetsiya')))
# trapetsiya.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# trapetsiya.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_trapetsiya')))
# trapetsiya.insert(nazad_geometry_3)

# paralepiped = InlineKeyboardMarkup(row_width=1)
# paralepiped.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_paralepiped')))
# paralepiped.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# paralepiped.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_paralepiped')))
# paralepiped.insert(nazad_geometry_3)

# kub = InlineKeyboardMarkup(row_width=1)
# kub.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_kub')))
# kub.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# kub.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_kub')))
# kub.insert(nazad_geometry_3)

# piramida = InlineKeyboardMarkup(row_width=1)
# piramida.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_piramida')))
# piramida.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# piramida.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_piramida')))
# piramida.insert(nazad_geometry_4)

# silindr = InlineKeyboardMarkup(row_width=1)
# silindr.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_silindr')))
# silindr.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# silindr.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_silindr')))
# silindr.insert(nazad_geometry_4)

# konus = InlineKeyboardMarkup(row_width=1)
# konus.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_konus')))
# konus.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# konus.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_konus')))
# konus.insert(nazad_geometry_4)

# shar_sfera = InlineKeyboardMarkup(row_width=1)
# shar_sfera.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_shar_sfera')))
# shar_sfera.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# shar_sfera.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_shar_sfera')))
# shar_sfera.insert(nazad_geometry_4)

# prizma_shar = InlineKeyboardMarkup(row_width=1)
# prizma_shar.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_prizma_shar')))
# prizma_shar.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# prizma_shar.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_prizma_shar')))
# prizma_shar.insert(nazad_geometry_4)

# piramida_shar = InlineKeyboardMarkup(row_width=1)
# piramida_shar.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_piramida_shar')))
# piramida_shar.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# piramida_shar.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_piramida_shar')))
# piramida_shar.insert(nazad_geometry_4)

# silindr_shar = InlineKeyboardMarkup(row_width=1)
# silindr_shar.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_silindr_shar')))
# silindr_shar.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# silindr_shar.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_silindr_shar')))
# silindr_shar.insert(nazad_geometry_4)

# konus_shar = InlineKeyboardMarkup(row_width=1)
# konus_shar.insert(InlineKeyboardButton(text='конспект', callback_data=lesson_callback.new(item_name='kons_konus_shar')))
# konus_shar.insert(InlineKeyboardButton(text='видеоурок', url='https://youtu.be/5D8Z74at47o'))
# konus_shar.insert(InlineKeyboardButton(text='тесты', callback_data=lesson_callback.new(item_name='test_konus_shar')))
# konus_shar.insert(nazad_geometry_4)