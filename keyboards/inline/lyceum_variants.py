from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# (label, вариант url, решение url или None)
RU_VARIANTS = [
    ('1', 'https://t.me/J_M_ath/2309?single', 'https://t.me/J_M_ath/2801'),
    ('2', 'https://t.me/J_M_ath/2311', None),
    ('3', 'https://t.me/J_M_ath/2313', None),
    ('4', 'https://t.me/J_M_ath/2317', None),
    ('5', 'https://t.me/J_M_ath/2302', None),
    ('6', 'https://t.me/J_M_ath/2784', 'https://t.me/J_M_ath/2789?single'),
    ('7', 'https://t.me/J_M_ath/2792', 'https://t.me/J_M_ath/2797'),
    ('8', 'https://t.me/J_M_ath/2289', 'https://t.me/J_M_ath/2292'),
    ('9', 'https://t.me/J_M_ath/2282', 'https://t.me/J_M_ath/2284'),
    ('10', 'https://t.me/J_M_ath/2794', None),
    ('11', 'https://t.me/J_M_ath/2297', 'https://t.me/J_M_ath/2307'),
    ('12', 'https://t.me/J_M_ath/2318', None),
    ('Экзамен 25.07.2024', 'https://t.me/J_M_ath/2321', 'https://t.me/J_M_ath/2323'),
    ('Экзамен 26.07.2024', 'https://t.me/J_M_ath/2332', 'https://t.me/J_M_ath/2334'),
]

# (label, вариант рус url, вариант узб url, решение url или None)
UZB_VARIANTS = [
    ('118', 'https://t.me/J_M_ath/3021', 'https://t.me/J_M_ath/3023', 'https://t.me/J_M_ath/3025'),
    ('218', 'https://t.me/J_M_ath/3034', 'https://t.me/J_M_ath/3036', 'https://t.me/J_M_ath/3040'),
    ('3117', 'https://t.me/J_M_ath/3049', 'https://t.me/J_M_ath/3051', 'https://t.me/J_M_ath/3057'),
    ('4117', 'https://t.me/J_M_ath/3065', 'https://t.me/J_M_ath/3067', 'https://t.me/J_M_ath/3078'),
    ('419', 'https://t.me/J_M_ath/3084', 'https://t.me/J_M_ath/3086', 'https://t.me/J_M_ath/3093'),
    ('517', 'https://t.me/J_M_ath/3102', 'https://t.me/J_M_ath/3104', 'https://t.me/J_M_ath/3119'),
    ('717', 'https://t.me/J_M_ath/3125', 'https://t.me/J_M_ath/3127', 'https://t.me/J_M_ath/3141'),
    ('3119', 'https://t.me/J_M_ath/3148', 'https://t.me/J_M_ath/3150', 'https://t.me/J_M_ath/3160'),
    ('418', 'https://t.me/J_M_ath/3169', 'https://t.me/J_M_ath/3171', 'https://t.me/J_M_ath/3176'),
    ('5119', 'https://t.me/J_M_ath/3186', 'https://t.me/J_M_ath/3188', 'https://t.me/J_M_ath/3193'),
    ('5118', 'https://t.me/J_M_ath/3199', 'https://t.me/J_M_ath/3201', 'https://t.me/J_M_ath/3208'),
    ('6118', 'https://t.me/J_M_ath/3217', 'https://t.me/J_M_ath/3219', 'https://t.me/J_M_ath/3225'),
    ('6119', 'https://t.me/J_M_ath/3241', 'https://t.me/J_M_ath/3243', 'https://t.me/J_M_ath/3259'),
    ('7118', 'https://t.me/J_M_ath/3270', 'https://t.me/J_M_ath/3272', 'https://t.me/J_M_ath/3278'),
    ('8112', 'https://t.me/J_M_ath/3289', 'https://t.me/J_M_ath/3291', 'https://t.me/J_M_ath/3306'),
    ('9119', 'https://t.me/J_M_ath/3315', 'https://t.me/J_M_ath/3317', 'https://t.me/J_M_ath/3328'),
    ('1019', 'https://t.me/J_M_ath/3337', 'https://t.me/J_M_ath/3339', 'https://t.me/J_M_ath/3346'),
    ('1119', 'https://t.me/J_M_ath/3355', 'https://t.me/J_M_ath/3357', 'https://t.me/J_M_ath/3374'),
    ('324', 'https://t.me/J_M_ath/3365', 'https://t.me/J_M_ath/3369', 'https://t.me/J_M_ath/3383'),
    ('1219', 'https://t.me/J_M_ath/3390?single', 'https://t.me/J_M_ath/3392', None),
    ('253', 'https://t.me/J_M_ath/3394', 'https://t.me/J_M_ath/3397', None),
    # "424 вариант (узб)" из исходного списка не попал в пересланное сообщение как ссылка — добавить, когда пришлёшь её отдельно.
]


def _ru_row(label, variant, reshenie):
    row = [InlineKeyboardButton(text=f'{label} вариант', url=variant)]
    if reshenie:
        row.append(InlineKeyboardButton(text=f'{label} решение', url=reshenie))
    return row


def _uzb_row(label, variant_ru, variant_uz, reshenie):
    row = [
        InlineKeyboardButton(text=f'{label} 🇷🇺', url=variant_ru),
        InlineKeyboardButton(text=f'{label} 🇺🇿', url=variant_uz),
    ]
    if reshenie:
        row.append(InlineKeyboardButton(text=f'{label} решение', url=reshenie))
    return row


lyceum_variants = InlineKeyboardMarkup(
    inline_keyboard=[_ru_row(*item) for item in RU_VARIANTS]
    + [_uzb_row(*item) for item in UZB_VARIANTS]
    + [[InlineKeyboardButton(text='назад', callback_data='nazad_lyceum_variants')]]
)
