from cgitb import text
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.callback_data import lesson_callback
from keyboards.inline.konspekts import *
from keyboards.inline.themes import give_class_themes
from keyboards.inline.themes import geometriya_themes_1,geometriya_themes_2,geometriya_themes_3,geometriya_themes_4


from aiogram.types import CallbackQuery

from loader import dp,bot
all_teors = {"teor_obiknovenniye_drobi" : ["BQACAgIAAxkBAAL5qWboHJAw62AmNf1X54ThELD1c6yEAALTTwACvG5BS3JLZqS90aGmNgQ", 
                                           "BQACAgIAAxkBAAL5q2boHMd9HVJ_fSVPhJknYduywcn3AALYTwACvG5BSzMdfpMrugSxNgQ",
                                           "BQACAgIAAxkBAAL5rWboHMlftjkAAWcc4xzKTdUjdYOFQQAC2U8AArxuQUuXnPo-NXV-9jYE",
                                           "BQACAgIAAxkBAAL5r2boHMsnDXpKX4XC8MPskXl2n9y5AALaTwACvG5BS1-OiGE-6QVDNgQ"],
            "shpar_obiknovenniye_drobi" : ["BQACAgIAAxkBAAL57WbpHjbsIR8SKF02TDS-RoeSt0O1AAIrXAACvG5JS7DcFvwVkQK_NgQ"],
            "prim_obiknovenniye_drobi" : ["BQACAgIAAxkBAAL59GbpH52B6RHhNsNt37tkoO0u3ycnAAJIXAACvG5JSwqd6hFQf95NNgQ",
                                          "BQACAgIAAxkBAAL59mbpH55JDr2PYbMntMEwMYCcLhRPAAJJXAACvG5JS2Hg3N4bmMMxNgQ",
                                          "BQACAgIAAxkBAAL5-GbpH6F6xMpULmGhJdHbFY-6sN4GAAJKXAACvG5JS1aN9CA2WWGfNgQ",
                                          "BQACAgIAAxkBAAL5-mbpH6M21o2y57OgDylNNEJevwjqAAJLXAACvG5JS8EP6mZa_1enNgQ"],
            "teor_period_drobi" : ["BQACAgIAAxkBAAL5_GbpIE5n7xbirVKCZO_CYEbX9oO0AAJQXAACvG5JS3lI757TbE_XNgQ",
                                   "BQACAgIAAxkBAAL5_mbpIFFC0KHHNvuItU9mEX3wuyFPAAJRXAACvG5JSwABvV3raTvvQDYE",
                                   "BQACAgIAAxkBAAL6AAFm6SBTbAr-j4EJE9N8wq-RfeMvRQACUlwAArxuSUudHbW7pCW4STYE"],
            "prim_period_drobi" : ["BQACAgIAAxkBAAL6AmbpIKaRlom1JtbJ5xPRjrsvuxBuAAJUXAACvG5JSwjs2KP2VyeYNgQ",
                                   "BQACAgIAAxkBAAL6BGbpIKf22nQNBnGji1GBXLVn7S-gAAJVXAACvG5JS1qWqmj5qLGlNgQ"],
            "teor_ratsion_chisla" : ["BQACAgIAAxkBAAL6EGbpIauOFNVfxDVZmr-wMv3CwNPfAAJgXAACvG5JSzlcqIf6et_QNgQ",
                                     "BQACAgIAAxkBAAL6EmbpIa0Cv7RTwl5xEhvp6xOD4nmnAAJhXAACvG5JS3Not9shgo_oNgQ"],
            "prim_ratsion_chisla" : ["BQACAgIAAxkBAAL6FGbpIclv68wLqOyUn5VvsovMjtJ5AAJjXAACvG5JS5MosRKfCH5TNgQ",
                                     "BQACAgIAAxkBAAL6FmbpIczNO-ZVaY2P4lKiKyXrZ53NAAJkXAACvG5JS6cwkEeyDOj1NgQ"],
            "teor_stepen_ratsion_chisel" : ["BQACAgIAAxkBAAL6GGbpIhBdVp-vOKhDmAjlL6u3H6rSAAJmXAACvG5JS8Ojw_u0WA0zNgQ",
                                            "BQACAgIAAxkBAAL6GmbpIhKEcscdtb80dO9fnqGA94jQAAJnXAACvG5JSzVFPQUEFnCqNgQ",
                                            "BQACAgIAAxkBAAL6HGbpIhT6WemBpLWQKnn_fWF6lWc3AAJoXAACvG5JS3KbTvda481uNgQ"],
            "prim_stepen_ratsion_chisel" : ["BQACAgIAAxkBAAL6HmbpImMJ8EEN3bFR1Sx3_iqjfPe4AAJrXAACvG5JS4n5mFM254AaNgQ",
                                             "BQACAgIAAxkBAAL6IGbpImVuGKJ4ylon6gMNZBsz8YGoAAJtXAACvG5JS1hgkQ4tTXLeNgQ",
                                             "BQACAgIAAxkBAAL6ImbpImgbxuat60fSECIIl0Hn-WclAAJuXAACvG5JS2_5XUVrefGoNgQ",
                                             "BQACAgIAAxkBAAL6JGbpImt75WCEaVPmoCkHrRiee2NBAAJvXAACvG5JS2PgFQk7B93SNgQ",
                                             "BQACAgIAAxkBAAL6JmbpIm2xYVlTC-PgPmQbAcPcsiVVAAJwXAACvG5JS5ofZOR5rJVjNgQ",
                                             "BQACAgIAAxkBAAL6KGbpIm-jh4godZsx5CqyI6O7prGWAAJxXAACvG5JSz30J1XO5PmjNgQ",
                                             "BQACAgIAAxkBAAL6KmbpInEL4Hh5pavalrZrKmqaLpU-AAJyXAACvG5JS457qhRytWkoNgQ"],
            "shpar_stepen_ratsion_chisel" : ["BQACAgIAAxkBAAL6LGbpItD2KSCjStO79xEM2asdEjxYAAJ4XAACvG5JS4CypnEliys4NgQ"],
            "teor_odno_mnogochlen" : ["BQACAgIAAxkBAAL6LmbpI1Kbm2-3eBYsk-hY0ATDzusaAAJ-XAACvG5JSxXf83pbsVJFNgQ",
                                      "BQACAgIAAxkBAAL6MGbpI1XHR62z0rlhkhf_2nbrFjJuAAKAXAACvG5JS-ZfeenkFCMNNgQ",
                                      "BQACAgIAAxkBAAL6MmbpI1c4rvX83KINXvv86TKrqy04AAKBXAACvG5JSwpqXXHTzGmMNgQ"],
            "prim_odno_mnogochlen" : ["BQACAgIAAxkBAAL6NGbpI5P2gjSFYB_N5_Svc7kQLY5oAAKEXAACvG5JSxwDrtnH95CiNgQ",
                                      "BQACAgIAAxkBAAL6NmbpI5UlkyAXWNcCBG9Ykp8LfMIHAAKFXAACvG5JS1ctIphB7hqVNgQ",
                                      "BQACAgIAAxkBAAL6OGbpI5cXgSFUTf9KV1AYvQeMVJ9IAAKGXAACvG5JS-ON_0rZY4IpNgQ"],
            "teor_formula_umnoj" : ["BQACAgIAAxkBAAL6OmbpI_r4HnMWYcSL5-2jr256iaoiAAKJXAACvG5JS5AfNM9KuTYINgQ"],
            "prim_formula_umnoj" : ["BQACAgIAAxkBAAL6PGbpJAUy8dAgmPVjf4xDuwhCaBrkAAKMXAACvG5JS3wqgn09WCriNgQ",
                                    "BQACAgIAAxkBAAL6PmbpJAiyVDu4xwPAAWamdqOOpRh8AAKNXAACvG5JS-i-lhDGWCE_NgQ"],
            "shpar_formula_umnoj" : ["BQACAgIAAxkBAAL6QGbpJBb5KoBvaWj62C7tGfn9q8-cAAKOXAACvG5JS72_YG89uRsmNgQ"],
            "teor_razloj_mnojiteli" : ["BQACAgIAAxkBAAL6QmbpJItCekk0I9whjn8yI1wa1AdSAAKSXAACvG5JSyFGcT30fxzxNgQ",
                                       "BQACAgIAAxkBAAL6RGbpJI4k03zEPi-g2bu0qJ-xuaRmAAKTXAACvG5JSw-i-0tiiRLmNgQ"],
            "prim_razloj_mnojiteli" : ["BQACAgIAAxkBAAL6RmbpJJ4i2ccqZCRimziC1oWZbD-QAAKUXAACvG5JS7J7clvFxd_sNgQ",
                                       "BQACAgIAAxkBAAL6SGbpJKigajAVJICj4s925HzHYYP5AAKVXAACvG5JS2M09bn_7_pQNgQ"],
            "teor_algebra_drobi" : ["BQACAgIAAxkBAAL6SmbpJPjb6EFmleZp0VdDKvkwRJbvAAKXXAACvG5JS_KGuXVCkFjRNgQ",
                                    "BQACAgIAAxkBAAL6TGbpJPr1I-RcwTmxsmHNpbXoHU7PAAKYXAACvG5JS6jbuvl5bbZANgQ"],
            "prim_algebra_drobi" : ["BQACAgIAAxkBAAL6TmbpJSbu7CbCZFmyPgcOw7MRooXuAAKbXAACvG5JS-Axz3BYmLjeNgQ",
                                    "BQACAgIAAxkBAAL6UGbpJSgwctFxE4fhLuVs0ue0cjdCAAKcXAACvG5JSzkQV04D8lwtNgQ",
                                    "BQACAgIAAxkBAAL6UmbpJStRoNgTrwJsP07De6fMyVVTAAKdXAACvG5JS0Q25mrSEDiJNgQ",
                                    "BQACAgIAAxkBAAL6VGbpJS25olCixLS4BZiLjM6Ns-eWAAKeXAACvG5JSw6Q5fvzdbbcNgQ",
                                    "BQACAgIAAxkBAAL6VmbpJS9wDt0dqruISwjXaKbQOTn4AAKfXAACvG5JS2HiIGQh3ModNgQ",
                                    "BQACAgIAAxkBAAL6WGbpJTIgbFuhmjvGISSN2bXTdB2qAAKgXAACvG5JS6hvsZTHBBn6NgQ"],
            "teor_arif_koren" : ["BQACAgIAAxkBAAL6WmbpKKWzreZxvPbUVseXlltWYSOfAALLXAACvG5JSwX_K_0ETi3rNgQ",
                                 "BQACAgIAAxkBAAL6XGbpKKe0B8Neb8-ImBV2JCH6NYUPAALMXAACvG5JS9iIxpoByDjpNgQ",
                                 "BQACAgIAAxkBAAL6XmbpKKmVHMY_RJjOCj_iHSEu0rSwAALNXAACvG5JS-xmze76pVd7NgQ"],
            "prim_arif_koren" : ["BQACAgIAAxkBAAL6YGbpKMOox9Rwbk1jVdSVMSfbZk7JAALPXAACvG5JS77Zw91ye0AAATYE",
                                 "BQACAgIAAxkBAAL6YmbpKMVVRPs3KKdhoCpVclpMjX54AALQXAACvG5JS9gWWvuyOmBoNgQ",
                                 "BQACAgIAAxkBAAL6ZGbpKMf6wBBUyAQ7Ch_PB_59UR-IAALRXAACvG5JS2QHy1IF98o9NgQ"],
            "shpar_arif_koren" : ["BQACAgIAAxkBAAL6ZmbpKODYaMkCH_OfCFgooWcPwFceAALSXAACvG5JSxw3eDmZDpxINgQ"],

            "teor_lin_uravneniya" : ["BQACAgIAAxkBAAL6aGbpKTKg_FZnkmL95B1A31Q1uba_AALVXAACvG5JSwIEIz2ksljANgQ",
                                     "BQACAgIAAxkBAAL6ambpKTTuFpDmTpaXimDsilzbVHRiAALWXAACvG5JSxlqyha4WZBSNgQ"],
            "teor_kvadrad_uravneniya" : ["BQACAgIAAxkBAAL6bGbpKX6pJVJbTM-N1ntMpkkKVcgfAALZXAACvG5JSx_l74Djc4vrNgQ",
                                         "BQACAgIAAxkBAAL6bmbpKYDyxfgSIb_CEnhu93QUtY-UAALaXAACvG5JS1OI8kAC8NepNgQ"],
            "prim_kvadrad_uravneniya" : ["BQACAgIAAxkBAAL6cGbpKao5g66XI67LkN-HTXbx6bIIAALgXAACvG5JS2J_v11O5iTcNgQ",
                                         "BQACAgIAAxkBAAL6cmbpKazgl3UaAixsrqmTHp7snP8_AALhXAACvG5JS1acVjZHxlqlNgQ",
                                         "BQACAgIAAxkBAAL6dGbpKa7DHVrrC5BH7PWSV0ECHIuOAALiXAACvG5JS-xmOdZK7mNaNgQ",
                                         "BQACAgIAAxkBAAL6dmbpKbDfo8xk5m9aZKbFyANv0CIHAALjXAACvG5JS0WaZaWP3ajBNgQ",
                                         "BQACAgIAAxkBAAL6eGbpKbLqLqs0jm_bHA2Bcbg5AAGMHQAC5FwAArxuSUuUWfXBXdPqnjYE",
                                         "BQACAgIAAxkBAAL6embpKbQ6b8nWfnaeZOQt725Qd4amAALlXAACvG5JS_y6cfu2kgkHNgQ"],
            "teor_teorema_vieta" : ["BQACAgIAAxkBAAL6fGbpKh16YuA0Vrja4K5x68D9UHC0AALrXAACvG5JS1X-Wthr6KqhNgQ",
                                    "BQACAgIAAxkBAAL6fmbpKh8pF_KrZAUCYG0rq5-b2LbpAALsXAACvG5JS-C0GNGacacuNgQ"],
            "prim_teorema_vieta" : ["BQACAgIAAxkBAAL6gGbpKkFgBrTN6Eje8r86oORM2DANAALuXAACvG5JS1tmddPoVc5kNgQ",
                                    "BQACAgIAAxkBAAL6gmbpKkM5jGO8MFysOJKrhL5hIg-TAALvXAACvG5JS3jATT0AAb9hOjYE",
                                    "BQACAgIAAxkBAAL6hGbpKkU0v-nZtq2k5s8asywAAal61gAC8FwAArxuSUu3P3hcODNTHjYE",
                                    "BQACAgIAAxkBAAL6hmbpKkd2bc0yJbCcefx2FsGjA4T5AALyXAACvG5JS2Fn15aiCPMONgQ",
                                    "BQACAgIAAxkBAAL6iGbpKklCm5-l0KMcu-ZtkemLO0HbAAL0XAACvG5JS4pTWZE4n0DRNgQ"],
            "teor_urav_vish_step" : ["BQACAgIAAxkBAAL6imbpKsRGMwqwsW_9Bm8OEaoxovIFAAL3XAACvG5JS_ERhxdNoMMJNgQ",
                                     "BQACAgIAAxkBAAL6jGbpKsbUyH_l_vpMii-PnlSV6PJ1AAL5XAACvG5JSxvTIShoZoonNgQ",
                                     "BQACAgIAAxkBAAL6jmbpKstnhImHx60Wb_8doAHIwlzFAAL6XAACvG5JS9POiLxCDmjWNgQ",
                                     "BQACAgIAAxkBAAL6kGbpKs4D20UQTkX8Ydpdll1CMB_uAAL7XAACvG5JS2X_tsHd9BBFNgQ",
                                     "BQACAgIAAxkBAAL6kmbpKtAdbCVBm9sp9tUOfeOKNwInAAL8XAACvG5JS4TmlOEKV4hgNgQ"],
            "prim_urav_vish_step" : ["BQACAgIAAxkBAAL6lGbpKz4aJsiM8SIa4Sm1DM6UT_XsAAL9XAACvG5JS-4vI3RLDCpJNgQ",
                                     "BQACAgIAAxkBAAL6lmbpK0CbOzP17QeVImXDG-9ySRcXAAL-XAACvG5JS1fRbzp0eP6PNgQ",
                                     "BQACAgIAAxkBAAL6mGbpK0LUEcEkQ3IFX7ogc0PvqI17AAL_XAACvG5JS5hL9UWg0xcAATYE",
                                     "BQACAgIAAxkBAAL6mmbpK0TlECQHI3RXY9k7WvVKV5mbAANdAAK8bklLBcXMTKb1tVY2BA",
                                     "BQACAgIAAxkBAAL6nGbpK0Zawt9YWclx1L3Mo3d_qee4AAIBXQACvG5JS7bhApao7JcINgQ",
                                     "BQACAgIAAxkBAAL6nmbpK0jBS6Z10Nf9ZnYHxNwDTi8TAAICXQACvG5JS3Y289w5n7rTNgQ",
                                     "BQACAgIAAxkBAAL6oGbpK0rD0amsviV1_e8B5LHRJMEEAAIDXQACvG5JS1ZO7wpDiw7ENgQ"],
            "teor_sistema_uravneniy" : ["BQACAgIAAxkBAAL6ombpLA1axTp57jpultSAMUuZnEHDAAIKXQACvG5JSw5PpYBD2qk8NgQ",
                                        "BQACAgIAAxkBAAL6pGbpLA-u67Y6OJ-0DvSmm_vj39qKAAILXQACvG5JS9P5Y8cC4dDzNgQ",
                                        "BQACAgIAAxkBAAL6pmbpLBJpnV6Hb2hJTtKUxM_vJp7OAAIMXQACvG5JS_vBF75xt6ZINgQ",
                                        "BQACAgIAAxkBAAL6qGbpLBVZf4sy3WYwLWolz2ou39lIAAINXQACvG5JS--K-_aExEQaNgQ",
                                        "BQACAgIAAxkBAAL6qmbpLBfSIaN_sUuQhVC8mb0FVDwsAAIOXQACvG5JS67d-gMSUHA6NgQ"],
            "prim_sistema_uravneniy" : ["BQACAgIAAxkBAAL6rGbpN5J5IxzW5h8Jw_roVznPj7g9AAKLXQACvG5JS7Dz-pG5qZFmNgQ",
                                        "BQACAgIAAxkBAAL6rmbpN5dKN7ftCPnk6SbzpS5RhgYkAAKMXQACvG5JS5v7DlvS5UklNgQ",
                                        "BQACAgIAAxkBAAL6sGbpN5n8_ATqdoSJcCL2DMgvuGxnAAKNXQACvG5JS6W2jWlqITIgNgQ",
                                        "BQACAgIAAxkBAAL6smbpN5tQ7xWLK1eh_l36OWiDOFIXAAKOXQACvG5JSxEt323htfy9NgQ",
                                        "BQACAgIAAxkBAAL6tGbpN50yUkLVkVMF6LCsYgSwttHkAAKPXQACvG5JS9Md-KCY_RuENgQ",
                                        "BQACAgIAAxkBAAL6tmbpN5-52yQfVeMFz5uJO_IsGkH_AAKQXQACvG5JS579IxAmHF0NNgQ",
                                        "BQACAgIAAxkBAAL6uGbpN6HF2-kZdH4emQkOxrE2BojZAAKRXQACvG5JS0c_d8xqckpcNgQ",
                                        "BQACAgIAAxkBAAL6umbpN6OpQfWWrFfMT_mxXwWP9VdsAAKSXQACvG5JS3G1A5HlnN9pNgQ",
                                        "BQACAgIAAxkBAAL6vGbpN6XHdofmM_TAagIdDx-l9vAVAAKTXQACvG5JS66UPgaQzx3oNgQ",
                                        "BQACAgIAAxkBAAL6vmbpN6hzMoqE7rguu8H0oGHD-bPfAAKUXQACvG5JS-v2f1EdF5VfNgQ",
                                        "BQACAgIAAxkBAAL6wGbpN6tMP9jC2N8NVAxlM4-9eZq4AAKWXQACvG5JS33m5kA0QVhdNgQ"],
            "teor_sistema_lin_neravenstv" : ["BQACAgIAAxkBAAL6wmbpOHNzjqlwxlZiJwjVjUCSbtbcAAI4UAACitrISnDcBnyU3lV9NgQ",
                                             "BQACAgIAAxkBAAL6xGbpOHkfa2ibwzGfYMZ8nVgLJbj8AAI5UAACitrISnpJJXW0igTgNgQ"],
            "prim_sistema_lin_neravenstv" : ["BQACAgIAAxkBAAL6xmbpOKMpYdxjKtVSzIlX3RaXhQxNAAI8UAACitrISqMbEUDjCh1MNgQ",
                                             "BQACAgIAAxkBAAL6yGbpOKjpjC7EEX7st38aYmAR9G2xAAI9UAACitrISvR3I6DvMXdINgQ",
                                             "BQACAgIAAxkBAAL6ymbpOK-7X64gLnIVhQ1qsd44hNjKAAI-UAACitrISh0i4-bXSovSNgQ"],
            "teor_metod_intervalov" : ["BQACAgIAAxkBAAL6zGbpOQABAWRL_Pq5lPq2bANMwyrZ1AACwFAAAorayEqWUJncgDXghzYE",
                                       "BQACAgIAAxkBAAL6zWbpOQABu3cwWPTTvEG-IqoUSLIgSAACwVAAAorayEqC-m8XNHYS5jYE"],
            "prim_metod_intervalov" : ["BQACAgIAAxkBAAL61GbpOTRjJfpZMMeMm6uKg-GGskBfAAIyUgACitrISv7NHvKBLRMFNgQ",
                                       "BQACAgIAAxkBAAL61mbpOTt2yG9rrTTJ6L-fZ0M__4XEAAIzUgACitrISj0G2PMuAUdSNgQ",
                                       "BQACAgIAAxkBAAL62GbpOUHYrcmCRcbYEm1tODh3N6rPAAI2UgACitrISp_iS4Sb8WqJNgQ",
                                       "BQACAgIAAxkBAAL62mbpOUf6D5P7tpu9ODGgPu_Xok_8AAI1UgACitrISl5PlxGucxmUNgQ",
                                       "BQACAgIAAxkBAAL63GbpOU0s7z7qfyKimHQkjfQVuSgvAAJcUgACitrISoP8ctv-zD2xNgQ"],
            "teor_modul_uravneniya" : ["BQACAgIAAxkBAAL63mbpOaxo8C3MfM0YqIvijxKrt1eGAAJkUgACitrISgPoKDsHhTusNgQ",
                                       "BQACAgIAAxkBAAL64GbpObCgdEqlwOuHXAABssFzgOD-RAACZVIAAorayEpyPjCI1ePJVjYE",
                                       "BQACAgIAAxkBAAL64mbpObV22W94sOvqHQSoBDKq5nafAAJmUgACitrISlvlNmz5bX4ZNgQ",
                                       "BQACAgIAAxkBAAL65GbpOboMt3DysZO91LC3FCWD6hygAAJnUgACitrISoizTtrdnKOkNgQ"],
            "prim_modul_uravneniya" : ["BQACAgIAAxkBAAL65mbpOfLyAAGn1Sj_vS-mY6S64HQxaAACalIAAorayEoRGDCLT7gpszYE",
                                       "BQACAgIAAxkBAAL66GbpOfa47z9fA8Bbbza7DY4yMf7RAAJrUgACitrISruhWPNyIVsNNgQ",
                                       "BQACAgIAAxkBAAL66mbpOfoyW0-BJjSU1okyPpO2u2UlAAJtUgACitrISp60RfQoh9ZwNgQ"],
            "teor_irrat_uravneniya_neravenstva" : ["BQACAgIAAxkBAAL67GbpOkcdP_2Mha5jCXoSOLbYpj-uAAKEUgACitrISnqMG1bUODEmNgQ",
                                                   "BQACAgIAAxkBAAL67mbpOkzKUSo5oPbL4LCw8bdBbqtcAAKFUgACitrISsEPS8Xe46JyNgQ",
                                                   "BQACAgIAAxkBAAL68GbpOlH0X4oK8DbbNkxKay4XMTb4AAKGUgACitrISsuUmoNBuYEqNgQ",
                                                   "BQACAgIAAxkBAAL68mbpOljKtNr3UexuI6oXB3J5csUeAAKRUgACitrISkAZ5DTsLauLNgQ",
                                                   "BQACAgIAAxkBAAL69GbpOlxslT7SMfJTgxDIYN0Tj8blAAKSUgACitrISkVlIJlBYE2aNgQ"],
            "prim_irrat_uravneniya_neravenstva" : ["BQACAgIAAxkBAAL69mbpOpXgDMq34M7CD0WJCHFiLdcWAAKdUgACitrISuoVY2ACCaypNgQ",
                                                   "BQACAgIAAxkBAAL6-GbpOplHAvTf4NQU-IuM-WO4sw85AAKgUgACitrIShG6nppYbfyONgQ",
                                                   "BQACAgIAAxkBAAL6-mbpOp4pInN7L-pZSscMwOKw8yj7AAKhUgACitrISqcrYWWYfFUPNgQ",
                                                   "BQACAgIAAxkBAAL6_GbpOqTiyN8-HYLW_KwsQufaWFTXAAKiUgACitrISo1W8Fl4mPZyNgQ",
                                                   "BQACAgIAAxkBAAL6_mbpOqi-ozoMjUE1EPPMczmx2Si7AAKjUgACitrISmRFj3MY3xmBNgQ",
                                                   "BQACAgIAAxkBAAL7AAFm6Tqt_3b-1w6bij8VisDddSOZwwACpFIAAorayEqcDeHQpRwIWDYE",
                                                   "BQACAgIAAxkBAAL7AmbpOrKXGQi3Nm82lc3lao7r0lBsAAKlUgACitrISl-VILV6JYFKNgQ"],
            "teor_arif_progressiya" : ["BQACAgIAAxkBAAL7BGbpOzdsa8O93VNkt001OFpkGppsAAKmUgACitrISjszAu-gu5EaNgQ",
                                       "BQACAgIAAxkBAAL7BmbpOzpSI9RzWuzFPnQy5-bwFd9ZAAKnUgACitrISqwH3R2jsqzsNgQ"],
            "prim_arif_progressiya" : ["BQACAgIAAxkBAAL7CGbpO0_zMfjEWfrGh-bWfdx4peCLAAKrUgACitrISmWxOMBii1NYNgQ",
                                       "BQACAgIAAxkBAAL7CmbpO1OgWqpiMr8ZTUYaI64ImMMJAAKsUgACitrISuIbHtl94qarNgQ"],
            "teor_geometry_progressiya" : ["BQACAgIAAxkBAAL7DGbpO4IPzDAfBFhuJL9HAjFN-o9oAAK4UgACitrISnsoVVoyhuWANgQ",
                                           "BQACAgIAAxkBAAL7DmbpO4ZZtN4kUghgapU-hoUoAvmbAAK5UgACitrISu8drSoo3PqbNgQ"],
            "prim_geometry_progressiya" : ["BQACAgIAAxkBAAL7EGbpO7IfNpuuX_WsusE1uFL5Jd8xAAK9UgACitrISh6Vtgjea9R-NgQ",
                                           "BQACAgIAAxkBAAL7EmbpO7dtFTB9_xFeXVlRsQGhD-DDAAK-UgACitrISm-9XkTvZDyTNgQ",
                                           "BQACAgIAAxkBAAL7FGbpO7xrb1-3_SY25KckGd5npL7ZAAK_UgACitrISpXWoivzl8R0NgQ",
                                           "BQACAgIAAxkBAAL7FmbpO8BuIpl9Hqb_0HVcO0bk1agrAALAUgACitrISr4OzS47ZoxANgQ",
                                           "BQACAgIAAxkBAAL7GGbpO8TVjbNjAV6St4AYvkzYblQXAALBUgACitrISg5x_pWtR1yQNgQ",
                                           "BQACAgIAAxkBAAL7GmbpO8hZpu0Dmqt958UsPtGRHXjFAALCUgACitrISm0u6Qpl7XCqNgQ",
                                           "BQACAgIAAxkBAAL7HGbpO8zjwUl8rAI6IP9nwHf8JQ93AALDUgACitrISpiNiWRHD1bDNgQ",
                                           "BQACAgIAAxkBAAL7HmbpO9ALBOFV-xREnNAcMm1J6stuAALEUgACitrISsN-4bKzM3mwNgQ",
                                           "BQACAgIAAxkBAAL7IGbpO9RihjDfXDLrkORV9wOI5q_mAALFUgACitrISmpNFNQ26E8xNgQ"],
            "teor_liney_funksiya" : ["BQACAgIAAxkBAAL7ImbpRrxgtDmzeTdDI1fCiLgKe_EPAALNUgACitrISrEbIp3KFDhXNgQ",
                                     "BQACAgIAAxkBAAL7JGbpRsF68Qn0RxN1V8YvQENuLYHnAALOUgACitrISsxfsYfPHvSeNgQ"],
            "prim_liney_funksiya" : ["BQACAgIAAxkBAAL7JmbpRuVuiBrcI9q424yitpy3NAt1AALPUgACitrIShwmF0W66i-MNgQ",
                                     "BQACAgIAAxkBAAL7KGbpRuj_dyv91HT-B-jO-VoHrRncAALQUgACitrISk9pcOKuGmxRNgQ",
                                     "BQACAgIAAxkBAAL7KmbpRu3IRRLaur9MghDL93wwK1ukAALRUgACitrISqHEPBONrZMaNgQ"],
            "teor_kvadrat_funksiya" : ["BQACAgIAAxkBAAL7LGbpRyIO_DJJ5YxzjpEflY_rZFm7AALdUgACitrISrAh8T7FiX0wNgQ",
                                       "BQACAgIAAxkBAAL7LmbpRybb0djtVJBZT2irkpkgUbTUAALeUgACitrISlxV-xSXBFJ0NgQ"],
            "prim_kvadrat_funksiya" : ["BQACAgIAAxkBAAL7MGbpRz7RPFdQn30BBFwlSM6sZ4GoAALjUgACitrIShozW14xYxp3NgQ",
                                       "BQACAgIAAxkBAAL7MmbpR0KJFj_AFfj9Q4RJhgZexfK3AALkUgACitrISp1WnEvtR8AVNgQ",
                                       "BQACAgIAAxkBAAL7NGbpR0Yxrp19lNTdPBSjXhoMaUh1AALlUgACitrISnddVylWrV2WNgQ",
                                       "BQACAgIAAxkBAAL7NmbpR0uLQE7z4TWv_PT-cj8vkSqeAALmUgACitrISsNLw7qNlkc9NgQ"],
            "teor_raz_zadach_funksiya" : ["BQACAgIAAxkBAAL7OGbpR4oKI5FmNKD6o3gB8U_-blahAALoUgACitrISuy8kEkULAUYNgQ",
                                          "BQACAgIAAxkBAAL7OmbpR43an3IIGrAatBkCvJSc8crMAALpUgACitrISrC7CVK2hlqCNgQ"],
            "teor_stepen_funksiya" : ["BQACAgIAAxkBAAL7PGbpR8k4pQjPjFlZdzz4N0KQp8ZUAAJZWgACxQnRStWj3fsvHhNoNgQ",
                                      "BQACAgIAAxkBAAL7PmbpR8zzOCX5mYArhG7qoE19xzW4AAJaWgACxQnRSq6nd4meHMyCNgQ"],
            "prim_stepen_funksiya" : ["BQACAgIAAxkBAAL7QGbpR-HDcfPDXZdTYK5kdIVgdkOjAAKNWgACxQnRSjRS89THkbQeNgQ",
                                      "BQACAgIAAxkBAAL7QmbpR-WH2Rjeb7n1gG7n0HssEyHJAAKOWgACxQnRSpjEHyBaehjwNgQ",
                                      "BQACAgIAAxkBAAL7RGbpR-l18OkL1NDu28ZI6sd7gFheAAKLWgACxQnRSilZmqQENdw_NgQ",
                                      "BQACAgIAAxkBAAL7RmbpR-5CDARwnmjZARX-CkYEd-zEAAKMWgACxQnRSpV5F7FWShhjNgQ",
                                      "BQACAgIAAxkBAAL7SGbpR_MqfQABZjzIgGxD0KGVbslLWwACiloAAsUJ0UrmB4ieGvhjUDYE",
                                      "BQACAgIAAxkBAAL7SmbpR_ez_OtxDSsVU6PCxdhrWRGGAAKJWgACxQnRSlTD8g9bOls2NgQ",
                                      "BQACAgIAAxkBAAL7TGbpR_toFnFXGVRwS4YkohmvkWM_AAKPWgACxQnRSsYVZrqnu1ekNgQ",
                                      "BQACAgIAAxkBAAL7TmbpR__SnWvFWERBhp6XA28fB8CfAAKQWgACxQnRSm8ncnFbZaLZNgQ",
                                      "BQACAgIAAxkBAAL7UGbpSAOX3o1MKPB92rahWdJqBt2JAAKRWgACxQnRSt9wxB8RFQbwNgQ",
                                      "BQACAgIAAxkBAAL7UmbpSAhEJG5bk8cKzj_8SSWOwg4HAAKSWgACxQnRSldI4Gpnk_t6NgQ"],
            "teor_obrat_funksiya" : ["BQACAgIAAxkBAAL7VGbpSJWvuyi1LhATnCi2jDGnKHkPAAKAVwAC2I5gSulvyMcKe8CeNgQ"],
            "teor_pokaz_urav_neravenstva" : ["BQACAgIAAxkBAAL7VmbpSKzsmCvOMRJyGctbMINTjTsdAAKuWgACxQnRSrvzb0I7Qp88NgQ",
                                             "BQACAgIAAxkBAAL7WGbpSMYofFCDyGaKeV1IKeBE2iVgAAKvWgACxQnRSnodEDeLn-G8NgQ",
                                             "BQACAgIAAxkBAAL7WmbpSM3ZHM61DeKz_J83IB0sqIbFAAKwWgACxQnRShshC7caJVVRNgQ"],
            "prim_pokaz_urav_neravenstva" : ["BQACAgIAAxkBAAL7XGbpSpo6jv8viwVEkzZJL0H1gtY7AAKzWgACxQnRSq5jp5FraowGNgQ",
                                             "BQACAgIAAxkBAAL7XmbpSp89Olm5UZ4v_2XgYR4HQ9b_AAK0WgACxQnRSkmijpF3B0slNgQ",
                                             "BQACAgIAAxkBAAL7YGbpSqNo6sL9OGmP3lpY-2HUZQGnAAK1WgACxQnRSgsAAU3welGLyTYE",
                                             "BQACAgIAAxkBAAL7YmbpSqe08k0VIm9bTMcjY1BEmwq3AAK2WgACxQnRStDqyya1S43ENgQ",
                                             "BQACAgIAAxkBAAL7ZGbpSqvO9H6DHrEOlThAA5xjvME6AAK3WgACxQnRSqQKuHMyafGkNgQ",
                                             "BQACAgIAAxkBAAL7ZmbpSrDJzp-R5HFUEumDvtAXlUFHAAK4WgACxQnRSsIK7unaFfRfNgQ"],
            "teor_log_preobrazovaniya" : ["BQACAgIAAxkBAAL7aGbpSwrbBPEp5Pd8fUqjKroz7koLAALLWgACxQnRSr5lElgcjzCBNgQ",
                                          "BQACAgIAAxkBAAL7ambpSw5H8Lnk29hzKkGrtq_OAAHr6gACzFoAAsUJ0Uox9gOnaMh-UjYE"],
            "prim_log_preobrazovaniya" : ["BQACAgIAAxkBAAL7bGbpSyyfAAGeCRr-9IQcLdyNofZa1gAC0loAAsUJ0Uo26qk5Is7eMTYE",
                                          "BQACAgIAAxkBAAL7bmbpSy9ej2GOcj16wCZZE6WVUOZCAALTWgACxQnRSn_7S4ujuRv9NgQ",
                                          "BQACAgIAAxkBAAL7cGbpSzT8LFtKLs7JL3CiLCRuns0pAALUWgACxQnRSmX-1-TUrc_hNgQ",
                                          "BQACAgIAAxkBAAL7cmbpSzhJ63QTGhJvMONjCEPWAAF8agAC1VoAAsUJ0UoQh6ni-GWP2jYE",
                                          "BQACAgIAAxkBAAL7dGbpSzy_wCh-Xspr7yD21W0b8tSgAALWWgACxQnRSqLdqVKIoJeWNgQ"],
            "teor_log_urav_neravenstva" : ["BQACAgIAAxkBAAL7dmbpS4r8S_0fxr2tUFE0ihD1Rj39AAIfWwACxQnRSorvQqYcM37_NgQ",
                                           "BQACAgIAAxkBAAL7eGbpS5ClOkEBSHAjFzBNjedQz9MeAAIgWwACxQnRSjBCQxcdZV3pNgQ"],
            "prim_log_urav_neravenstva" : ["BQACAgIAAxkBAAL7embpS6_hGucnTgJV_UZ3FnMzTNC2AAIzWwACxQnRSrwwuwOkQLhuNgQ",
                                           "BQACAgIAAxkBAAL7fGbpS7MN7Mj_A4rkWSjCg2Hj7gmGAAI0WwACxQnRShl_d1J5s178NgQ",
                                           "BQACAgIAAxkBAAL7fmbpS7egWiwyWtu1CY5rDj2jYnBIAAI1WwACxQnRSt5tgIBDhClaNgQ",
                                           "BQACAgIAAxkBAAL7gGbpS7seBFJWamLSEBQ7FlwAATzRkwACNlsAAsUJ0UpuUKqvA6rGyjYE",
                                           "BQACAgIAAxkBAAL7gmbpS7_LPqJ0MpQnPOcZtcvQgqd_AAI3WwACxQnRSmnLZLe_5xhgNgQ",
                                           "BQACAgIAAxkBAAL7hGbpS8azJ0YsflcBrjiCpqI-MH4sAAI_WwACxQnRStuGtC2maLcmNgQ",
                                           "BQACAgIAAxkBAAL7hmbpS8rsWuFwlmlAgDCx2l-nCka6AAJAWwACxQnRSqgSchlz3d_zNgQ",
                                           "BQACAgIAAxkBAAL7iGbpS8_Az8HwXDooIacenE_ydbp0AAJBWwACxQnRSvtN79tntMYJNgQ",
                                           "BQACAgIAAxkBAAL7imbpS9O1pRcKel5VWSerZsnrywgfAAJDWwACxQnRSoalZGsSxUL9NgQ",
                                           "BQACAgIAAxkBAAL7jGbpS9iOw0fclbUSgxTKTrt2M9buAAJEWwACxQnRSr0xUeDo5-ohNgQ"],
            "teor_log_funskiya" : ["BQACAgIAAxkBAAL7jmbpTFLgQQWsW4poBWtxoqm5uMFoAAJQWwACxQnRSrOiweguve51NgQ",
                                   "BQACAgIAAxkBAAL7kGbpTFj3TQoq6HeQzJ8C4431t98RAAJSWwACxQnRSnbTDIscrybiNgQ",
                                   "BQACAgIAAxkBAAL7kmbpTGQMTzwqdYu6YZWeReA9-n1gAAJTWwACxQnRSkFd0h3OEuVGNgQ"],
            "teor_osnov_ponyatiya" : ["BQACAgIAAxkBAAL7lGbpTKgdGLutf-uUX7h2QfVOBrMnAAJcWwACxQnRSlh-629ahFSgNgQ",
                                      "BQACAgIAAxkBAAL7lmbpTKxPymN8RRxDeeh9kVkVSNgzAAJdWwACxQnRSsnY-4kuTyXyNgQ"],
            "prim_osnov_ponyatiya" : ["BQACAgIAAxkBAAL7mGbpTMoMrwiaVshAQN-D1ZBO0KK_AAJlWwACxQnRSpPO8Igo0680NgQ",
                                      "BQACAgIAAxkBAAL7mmbpTM7yr6tSW1ZH79YxKT0H2PlbAAJmWwACxQnRSk4Q3DLWeAaRNgQ",
                                      "BQACAgIAAxkBAAL7nGbpTNJPOhHhtnhr3jHbDs4LQAABPgACZ1sAAsUJ0Upw6YEEB-VkXTYE"],
            "teor_osnov_tokdestva" : ["BQACAgIAAxkBAAL7nmbpTRoeRBk8orLnbH5Z9gvBRcK2AAKoUAACxQnhShYouPd1jCiiNgQ",
                                      "BQACAgIAAxkBAAL7oGbpTR5JxChEglmizTopukoZ0mppAAKpUAACxQnhSlGo8i9RrKXeNgQ"],
            "prim_osnov_tokdestva" : ["BQACAgIAAxkBAAL7ombpTTyu-spvWzIw0zJ6_x5IiscNAAKsUAACxQnhShCigkqhfnzANgQ",
                                      "BQACAgIAAxkBAAL7pGbpTT_8pLZT4bJ4k4nI4W2mL0D6AAKtUAACxQnhSiflFXY3B0HlNgQ",
                                      "BQACAgIAAxkBAAL7pmbpTUX2fa-s5100SkVIX5Xal6eNAAKuUAACxQnhSvuBAAH1m4gNWzYE"],
            "teor_formuli_privedeniya" : ["BQACAgIAAxkBAAL7qGbpTX0-sNAzxMXre_kq0DWeYRJbAALHUAACxQnhShnJzSPzUp_9NgQ",
                                          "BQACAgIAAxkBAAL7qmbpTYGN-UazhoHtw7bccNe08vWuAALJUAACxQnhSoN7VbVMp4LsNgQ"],
            "prim_formuli_privedeniya" : ["BQACAgIAAxkBAAL7tWbpUXuwsHv7L__f1Sut8hAtvgX0AALMUAACxQnhSkGZsXYi0mzeNgQ",
                                          "BQACAgIAAxkBAAL7t2bpUX9WKsoh6c8LOv-7E0NOgHjaAALNUAACxQnhSudUR5ch4DU4NgQ"],
            "teor_formuli_slojeniya" : ["BQACAgIAAxkBAAL7uWbpUapUfiqyVmm-oZSkaGirQbU2AAIXUQACxQnhSpsfyn5R8mWtNgQ",
                                        "BQACAgIAAxkBAAL7u2bpUa7UZiIgcTQIh2-exPzgj8LnAAIYUQACxQnhSgIBa4pXylJlNgQ"],
            "prim_formuli_slojeniya" : ["BQACAgIAAxkBAAL7vWbpUc6d-0kfzNyOJxlrzwz5bhVoAAIbUQACxQnhSr94fQpzqLRdNgQ",
                                        "BQACAgIAAxkBAAL7v2bpUdPBb4mfYOfT7YIcEXmcfDaSAAIcUQACxQnhShW_69omvr1kNgQ",
                                        "BQACAgIAAxkBAAL7wWbpUdg0Kn7Xe3aAtwx_zGVO663BAAIdUQACxQnhStp8LEYy-9IgNgQ"],
            "teor_dvoynoy_ugol" : ["BQACAgIAAxkBAAL7yWbpUjhix8tO7LyAYXOyWMRU8SixAALDUQACxQnhSpyeMhk0WGnCNgQ",
                                   "BQACAgIAAxkBAAL7y2bpUj1h1NLWuZdOpHZSyhgkZ715AALEUQACxQnhStbSQ3qLojl5NgQ"],
            "prim_dvoynoy_ugol" : ["BQACAgIAAxkBAAL7zWbpUl4sITmumWyMtq6twhbKaLbKAALPUQACxQnhSiOnQQABGTV1tzYE",
                                   "BQACAgIAAxkBAAL7z2bpUmUETMQsmwNJsJWFosrXDX0CAALQUQACxQnhSgp_ga1WtpjlNgQ",
                                   "BQACAgIAAxkBAAL70WbpUmoXpuXUilj9twIkY-dzm3V7AALRUQACxQnhSoxvhyqZT-XRNgQ",
                                   "BQACAgIAAxkBAAL702bpUm_R94GM6lL4o19FyuZACDoTAALSUQACxQnhSqbnYExRaIDnNgQ"],
            "teor_form_sum_rznost" : ["BQACAgIAAxkBAAL71WbpUqvMLo4tlXymeEzAo4PQJnXjAAIWUgACxQnhSpQmXZgT0NtxNgQ",
                                      "BQACAgIAAxkBAAL712bpUq7Jvbhg9NzJQ2AB2RCkkwH8AAIVUgACxQnhSlUubQHNkPfJNgQ"],
            "prim_form_sum_rznost" : ["BQACAgIAAxkBAAL72WbpUstVARN1_uLRe1_euc7FfdSpAAIaUgACxQnhSnNeWjGZDGgPNgQ",
                                      "BQACAgIAAxkBAAL722bpUs-vpaNnYokQtx5ftCfv5ZneAAIbUgACxQnhSr5eZrMSY3KeNgQ",
                                      "BQACAgIAAxkBAAL73WbpUtP2rT1lD5H1neyHk6IB_F-FAAIcUgACxQnhShzxG_ucJwhDNgQ"],
            "teor_form_proizved" : ["BQACAgIAAxkBAAL732bpUxJnyhmhUFW0EXmW-MAiXxjeAAIhUgACxQnhStyhsl6fj7DnNgQ"],
            "prim_form_proizved" : ["BQACAgIAAxkBAAL74WbpUxYBnJ-zrhRyxCTOnOC97YKuAAIkUgACxQnhSvO5TuI1Fzb9NgQ"],
            "teor_form_pol_ugla" : ["BQACAgIAAxkBAAL742bpU0k0yxoJtCwY8KC5lCnuG6rsAAKAVgACTf3oSlojrfe-JDFbNgQ"],
            "prim_form_pol_ugla" : ["BQACAgIAAxkBAAL75WbpU1e49reJY7CTkXFGF10UXQ33AAKDVgACTf3oSmLF--VYRdA5NgQ",
                                    "BQACAgIAAxkBAAL752bpU1sd7QhCSe9tbxP8XhueckcyAAKEVgACTf3oSo9Sb5l0EVBkNgQ",
                                    "BQACAgIAAxkBAAL76WbpU2AdqRqhx70TdfrCvYE6KphcAAKFVgACTf3oSvp-oIdqulz7NgQ"],
            "teor_obr_trigio_funk" : ["BQACAgIAAxkBAAL762bpU-gpG6GOTon6rzkhtdiQRnyzAAKuVgACTf3oShr_7Puj4WakNgQ",
                                      "BQACAgIAAxkBAAL77WbpU-zFQs_mfuM7Z4JqDtQfQppyAAKvVgACTf3oSgyXUH3sRpt4NgQ"],
            "prim_obr_trigio_funk" : ["BQACAgIAAxkBAAL772bpVAWBOc3VSNk5a_UQhvDeczNRAAKxVgACTf3oStoTV77lfvg_NgQ",
                                      "BQACAgIAAxkBAAL78WbpVAoomHh-QRrLynzrilsnSQjOAAKyVgACTf3oSgKLM6KaRm3FNgQ"],
            "teor_trigo_uravneniya" : ["BQACAgIAAxkBAAL782bpVEWJ6lqDHus8WMhbq_2gpNi7AALWVgACTf3oSoScERddGgyHNgQ",
                                       "BQACAgIAAxkBAAL79WbpVEl8hgE7yw0ItWyXsoF5c-rwAALXVgACTf3oShkf0-ub7IdLNgQ",
                                       "BQACAgIAAxkBAAL792bpVEyWUJaRpNHk8BkDQnlBMrHOAALZVgACTf3oSon9ILWwpBIhNgQ",
                                       "BQACAgIAAxkBAAL7-WbpVFC6VexpMRcenNXdkdKu5OzaAALYVgACTf3oSpiLGKEEjcnvNgQ"],
            "prim_trigo_uravneniya" : ["BQACAgIAAxkBAAL7-2bpVHpnesPehfh-4y5SMPdoHL6WAALXSgAC3CnxStyJRhDpb4c7NgQ",
                                       "BQACAgIAAxkBAAL7_WbpVH5tqqWQcadzTlH5OEXCUlPgAALYSgAC3CnxStMUzf9ZCQMPNgQ",
                                       "BQACAgIAAxkBAAL7_2bpVII8UFHA95mBg9bbI8zdZgcqAALZSgAC3CnxStH_mA7b1yZhNgQ",
                                       "BQACAgIAAxkBAAL8AWbpVIbp8v_UlYfKLSI5ToWTym4pAALaSgAC3CnxSpguTBUXmGIONgQ",
                                       "BQACAgIAAxkBAAL8A2bpVIoKlYNPepsPB5-aohSHhUr3AALbSgAC3CnxSpxKGa6y55xKNgQ",
                                       "BQACAgIAAxkBAAL8BWbpVI53-Ca_wGFDVrOnmKyIJ1noAALcSgAC3CnxSjoJEUHUyNsbNgQ"],
            "teor_trigo_nerav" : ["BQACAgIAAxkBAAL8B2bpVOCbdRF48QTrHZip-aoE4faWAALsSgAC3CnxStgzzdiojpG-NgQ",
                                  "BQACAgIAAxkBAAL8CWbpVOOiwbEpWT587iET3QdSpsSfAALtSgAC3CnxSmHrn3gLfsrHNgQ",
                                  "BQACAgIAAxkBAAL8C2bpVOdLfPMfYqFWiqXUxaLI3b5IAALuSgAC3CnxSi1ViF-B6B1xNgQ",
                                  "BQACAgIAAxkBAAL8DWbpVO3spwG05K42Li9loFG8KRozAALvSgAC3CnxSsxRm5SCJlHVNgQ"],
            "prim_trigo_nerav" : ["BQACAgIAAxkBAAL8D2bpVR_1Ca563gY0oPiCijmNjjpqAALwSgAC3CnxStMsdXNC7k4qNgQ"],
            "teor_trigo_funk" : ["BQACAgIAAxkBAAL8EWbpVUccT7z-ukDplRSHHidpmsM_AAIISwAC3CnxShzPajQXGzf3NgQ",
                                 "BQACAgIAAxkBAAL8E2bpVUt-fWHhFHD4_rQxSiEhQPInAAIJSwAC3CnxSlDbAtezh8rmNgQ",
                                 "BQACAgIAAxkBAAL8FWbpVU-78Pe3rfOlqr6fk8yTe-V8AAIKSwAC3CnxSmtK7g7Ml-zINgQ",
                                 "BQACAgIAAxkBAAL8F2bpVVPgx2RL_wYxXwABriVEDE-ugwACC0sAAtwp8UqPyyBqDQyuhzYE",
                                 "BQACAgIAAxkBAAL8GWbpVVg_DIclFGTCsGjV0eTem3KFAAIMSwAC3CnxStc86BRYofVHNgQ",
                                 "BQACAgIAAxkBAAL8G2bpVVztjXRc9hknLD7gU2GQEtMqAAINSwAC3CnxSivWFkZ30UyYNgQ",
                                 "BQACAgIAAxkBAAL8HWbpVWHyfhsnF_mpm8i2uKKABpR6AAIOSwAC3CnxStXUYPZwpHvpNgQ",
                                 "BQACAgIAAxkBAAL8H2bpVWWMxrg1kGQ8VKI5hLlpeus8AAIPSwAC3CnxStHuhLgSqqImNgQ"],
            "prim_trigo_funk" : ["BQACAgIAAxkBAAL8IWbpVajVV9zn8MmllZsvsQ-6prv-AAITSwAC3CnxShNHEm_pScqlNgQ",
                                 "BQACAgIAAxkBAAL8I2bpVasNN8EgTx6GhJ-arMhzWKppAAIUSwAC3CnxSjhwSXn9beRvNgQ",
                                 "BQACAgIAAxkBAAL8JWbpVa9Xv9zvFvBKXcJbEyKinGcKAAIVSwAC3CnxSvSX_7tNShqbNgQ",
                                 "BQACAgIAAxkBAAL8J2bpVbRzu0xEDCJi-X3k7wGRA5zyAAIWSwAC3CnxSkINVXHnXSX5NgQ"],
            "teor_roizvod_prost_func" : ["BQACAgIAAxkBAAL8KWbpVfGDa9CH3_3pilQW4hJeCrX9AAIjSwAC3CnxSouKqI-44QHUNgQ",
                                         "BQACAgIAAxkBAAL8K2bpVfWk5R8DKIXrUAIy7QABLLf1IQACJEsAAtwp8UpkrcYEVSQ6iDYE",
                                         "BQACAgIAAxkBAAL8LWbpVfnhC7UG8wwc9w_HkzuMFsNMAAIlSwAC3CnxSli2cpkNRxv2NgQ"],
            "prim_roizvod_prost_func" : ["BQACAgIAAxkBAAL8L2bpViW_X4qDOOAndQ3as-CeZvG7AAIuSwAC3CnxSuL2oobYStiZNgQ",
                                         "BQACAgIAAxkBAAL8MWbpVilN2YHmQl4DUPE1psC2pWRfAAIvSwAC3CnxSuM_mNvtVygFNgQ"],
            "teor_proizvod_sloj_func" : ["BQACAgIAAxkBAAL8M2bpVmgogtF83CCutQu2yxJysQN4AAJdSwAC3CnxSvxylDFpdAH5NgQ"],
            "prim_proizvod_sloj_func" : ["BQACAgIAAxkBAAL8NWbpVnYq3oLY0M7HqTQHJAELTSkIAAJeSwAC3CnxSpZrZgvsuGyrNgQ",
                                         "BQACAgIAAxkBAAL8N2bpVnoTtCctsMJG7877VLsljgKLAAJfSwAC3CnxSrTae4a6XbV-NgQ"],
            "teor_issled_func" : ["BQACAgIAAxkBAAL8OWbpVq6O6pCr_suO9LSO0jwumDGiAALZSwAC3CnxSlAdwzalZ0MpNgQ",
                                  "BQACAgIAAxkBAAL8O2bpVrJ8Vl4ziTtbocKbJvrZB_hpAALaSwAC3CnxSlS4SFunpT2KNgQ",
                                  "BQACAgIAAxkBAAL8PWbpVre9U6xTF7FNGqUyfr6bxtExAALbSwAC3CnxSjLwkUrOZLeINgQ"],
            "prim_issled_func" : ["BQACAgIAAxkBAAL8P2bpVtUn1Oe4mmdBtiZW7j_OGvt1AALcSwAC3CnxSjyhwfVKYODVNgQ",
                                  "BQACAgIAAxkBAAL8QWbpVtgm1VczH4cfkgyjsKYjEsr_AALdSwAC3CnxSiIwhkzWZGfANgQ"],
            "teor_fiz_mex_func" : ["BQACAgIAAxkBAAL8Q2bpVw0ZnPFa5r5TmwFWjT2Cj0c2AALjSwAC3CnxSlsFdjmG0pLFNgQ",
                                   "BQACAgIAAxkBAAL8RWbpVxGGzGDXXs83UlZqJmPE7qLfAALkSwAC3CnxSgWEMZBxQgm9NgQ"],
            "prim_fiz_mex_func" : ["BQACAgIAAxkBAAL8R2bpVyu_dfJO7mSvZCeglxTF50gpAALnSwAC3CnxSu-kE-VZP9XrNgQ",
                                   "BQACAgIAAxkBAAL8SWbpVy-b-PpBOeeLbxA0_pAremCCAALoSwAC3CnxSk1tVA951I3oNgQ",
                                   "BQACAgIAAxkBAAL8S2bpVzPGtt55e8E2nBcBG7ISpps9AALpSwAC3CnxSqhBtuK-Nx5DNgQ",
                                   "BQACAgIAAxkBAAL8TWbpVzdu0gs3sBeU6pTvrLoXX0YgAALqSwAC3CnxSj40fYA23HoqNgQ",
                                   "BQACAgIAAxkBAAL8UmbpVzxcjDfaKESlWH5od9Awu6d5AALrSwAC3CnxSpUM-bsCDPsVNgQ",
                                   "BQACAgIAAxkBAAL8VWbpV0CniSPgn6q2_uM4BQpj8GJcAALsSwAC3CnxSlgqsMvq16rlNgQ",
                                   "BQACAgIAAxkBAAL8WGbpV0SBDzPiyHkk_B6Shvtri8EgAALtSwAC3CnxSk6O1mdK_SfJNgQ"],
            "teor_pervob_integral" : ["BQACAgIAAxkBAAL8XGbpV5grN_IGUkVbb_0tljQ9fhG8AALxSwAC3CnxSoppyVaaRU4TNgQ",
                                      "BQACAgIAAxkBAAL8XmbpV5z0h0FgigmZeYgHMWP5acPoAALwSwAC3CnxSuwdtd6NWbvSNgQ"],
            "prim_pervob_integral" : ["BQACAgIAAxkBAAL8YGbpV71tCE7DvGYdhfaZDOsw_WyrAALySwAC3CnxSnJFcUVMtfUvNgQ",
                                      "BQACAgIAAxkBAAL8YmbpV8K6TOYidBCPj-PbrS9DUDWVAALzSwAC3CnxSgyPbFkSJeGXNgQ"],
            "teor_metod_zamen_peremen" : ["BQACAgIAAxkBAAL8ZGbpV--RHep9C_-uXstlss2fSBXNAAL3SwAC3CnxSgeI302pucFTNgQ",
                                          "BQACAgIAAxkBAAL8ZmbpV_PSfXyZusYl4vKPkqg_TlySAAL4SwAC3CnxSnvGrNZIMX0XNgQ"],
            "prim_metod_zamen_peremen" : ["BQACAgIAAxkBAAL8aGbpWA9plL1hEKTN7FmCDpGqFNghAAL5SwAC3CnxSt32r7OHQcvhNgQ",
                                          "BQACAgIAAxkBAAL8ambpWBP_RXD7yqfkJ8_HxswB6vbkAAL6SwAC3CnxStMfG1UkjZMENgQ"],
            "teor_integ_chasti" : ["BQACAgIAAxkBAAL8bGbpWDwDrqsSn8Vf4Y9ThcwhpIsLAAL7SwAC3CnxSuVt0MsEKtYONgQ",
                                   "BQACAgIAAxkBAAL8bmbpWEDZ_9w8OQd6Lp12_D71ODPVAAL8SwAC3CnxSip9KGEp5WsQNgQ"],
            "prim_integ_chasti" : ["BQACAgIAAxkBAAL8cGbpWFRlMsUTSWlsx-yRqOVJP58qAAL9SwAC3CnxSvVti9KWuEyFNgQ",
                                   "BQACAgIAAxkBAAL8cmbpWFfWjoic5AyRx6Rf90HwWqHjAAL-SwAC3CnxSpoQPwYUUGGCNgQ"],
            "teor_opred_integral" : ["BQACAgIAAxkBAAL8dGbpWJMYcwi1eS-E_xEveXrYVyFuAAL_SwAC3CnxSjyIGwkFkUYHNgQ",
                                     "BQACAgIAAxkBAAL8dmbpWJcVp_DlW50pS477R0iexr21AANMAALcKfFKIQu1zWMBowc2BA",
                                     "BQACAgIAAxkBAAL8eGbpWJqMJcLZkJUSkL0YNlQLgOpeAAIBTAAC3CnxSgcm3WqDVE0NNgQ",
                                     "BQACAgIAAxkBAAL8embpWJ4RJw-xWzP12TfuGGv0pJ7FAAICTAAC3CnxSiT-nFxBTvjoNgQ",
                                     "BQACAgIAAxkBAAL8fGbpWKNdmF9gT_mmhEZgqDCPsTmDAAIDTAAC3CnxSuOGSF0CQ3W6NgQ"],
            "prim_opred_integral" : ["BQACAgIAAxkBAAL8fmbpWNJ2Q62p7IiPt33JvTTJF4RiAAIETAAC3CnxSrORcX8kI9yxNgQ",
                                     "BQACAgIAAxkBAAL8gGbpWNaC_Cw7hBdtcru0YriseKw8AAIFTAAC3CnxSpFov_sf7faANgQ"],
            "teor_mnojestva" : ["BQACAgIAAxkBAAL8gmbpWPu6xjhQYwmsyrZYm991DOAlAAIGTAAC3CnxStc4wb8QC6iANgQ",
                                "BQACAgIAAxkBAAL8hGbpWP9y1z_DLcpAMge8QWjXDHNLAAIHTAAC3CnxSsaGQcsZt2wLNgQ"],
            "prim_mnojestva" : ["BQACAgIAAxkBAAL8hmbpWRYaPQ_6P6q7WPEfnysVMXWyAAIITAAC3CnxSi7z_xbs7gkhNgQ"],
            "teor_kombinatorika" : ["BQACAgIAAxkBAAL8iGbpWTOP7HbAwxo3uCn-tmMh7tHaAAIJTAAC3CnxSlaXyMkr-iknNgQ",
                                    "BQACAgIAAxkBAAL8imbpWTf-1U5mYgZgVDiGb-BBe9lQAAIKTAAC3CnxSl9E0Qtmw00vNgQ"],
            "prim_kombinatorika" : ["BQACAgIAAxkBAAL8jGbpWUtgu4HNBBIFwDMID9EqAl4GAAILTAAC3CnxSvrfY02t_gaRNgQ"],
            "teor_teor_veroyat" : ["BQACAgIAAxkBAAL8j2bpWXYPK8mLH_GqoX_ug6k5UOYsAAIMTAAC3CnxSqtALUiSGoelNgQ",
                                   "BQACAgIAAxkBAAL8kWbpWXnZ9T6oBw3PK0JwhEbu2j19AAINTAAC3CnxSjF03wTBFOvnNgQ"],
            "prim_teor_veroyat" : ["BQACAgIAAxkBAAL8l2bpWY6ggJaQhlzOReNsAtSoYoIvAAIOTAAC3CnxSjUx1ND5X37jNgQ",
                                   "BQACAgIAAxkBAAL8mWbpWZI3dwwktd1McSG_8iN98wzuAAIPTAAC3CnxShrZibMegavsNgQ",
                                   "BQACAgIAAxkBAAL8m2bpWZavTOS8QlU2cuYvn2L4Qfm0AAIQTAAC3CnxSuZrZqrc5rh3NgQ",
                                   "BQACAgIAAxkBAAL8nWbpWZvMaAy2ePMmlud7xxKyBoIkAAIRTAAC3CnxSuQOyvkgASuINgQ",
                                   "BQACAgIAAxkBAAL8n2bpWZ8V1fGJWYa1YR8BIm19pKt2AAISTAAC3CnxSm7HODK6lPGdNgQ",
                                   "BQACAgIAAxkBAAL8oWbpWaOQIyNJfrNAqWH5e_i7v1rnAAITTAAC3CnxSlgD5w8R5ycUNgQ"],
            "teor_param_lin_urav" : ["BQACAgIAAxkBAAL8o2bpWemeiaLW6SvGOYyPOy1S5cnHAAIUTAAC3CnxSkxztMK0mtxSNgQ",
                                     "BQACAgIAAxkBAAL8pWbpWe0zqtsxVa4jLqR4mJVzhKxJAAIVTAAC3CnxSqbKjnZKQkDxNgQ"],
            "teor_param_kvadrat_urav" : ["BQACAgIAAxkBAAL8p2bpWimurIxcFEz04exUPUflDEpEAAIWTAAC3CnxSlxr7RiLHn0aNgQ",
                                         "BQACAgIAAxkBAAL8qWbpWi1iH6-0pNr9AmArblwoHSttAAIXTAAC3CnxSlsmtZ3VwxmXNgQ"],
            "teor_sistema_param_urav" : ["BQACAgIAAxkBAAL8q2bpWlS9kjlizHfHM46SrxzRCH4NAAIZTAAC3CnxSvrMd94vOx82NgQ",
                                         "BQACAgIAAxkBAAL8rWbpWlh9w5QPF1PTOp3Et0vTCsNdAAIaTAAC3CnxSiQ-9wfhB5YkNgQ"],
            "teor_zadach_chisla" : ["BQACAgIAAxkBAAL8r2bpWoOZsOZkhXFCEx5NzjEoY18pAAIbTAAC3CnxSh2VVil2JZywNgQ",
                                    "BQACAgIAAxkBAAL8sWbpWofzooAQz8eeHsa7EtbPruviAAIcTAAC3CnxShauZthg19t7NgQ"],
            "teor_zadach_dvij" : ["BQACAgIAAxkBAAL8s2bpWsKZxYdGF7eLHyC0vAw7sLKdAAIeTAAC3CnxSrFEqOUaMs5uNgQ"],
            "teor_zadach_sovm_rabota" : ["BQACAgIAAxkBAAL8tWbpWuQ2zJVAPY5aA1n4Hnvo3iysAAIgTAAC3CnxSt7Ungn1y170NgQ",
                                         "BQACAgIAAxkBAAL8t2bpWuj5AzTaTv_cBGsGPC8Od7yQAAIhTAAC3CnxSo5o7h_sAAEWCjYE"],
            "teor_zadach_protsent" : ["BQACAgIAAxkBAAL8uWbpWyz411LyAQFAUjNxJ-w-ZJSpAAIiTAAC3CnxSmYIVrKOBG38NgQ",
                                      "BQACAgIAAxkBAAL8u2bpWzH6RFFTqp51ymQ8EBlZtXj5AAIjTAAC3CnxSpqQOCm0-_l1NgQ"],
            "teor_zadach_smes" : ["BQACAgIAAxkBAAL8vWbpW0ok3P9iyDUMFQhj_n43cIlrAAIkTAAC3CnxSq-4HJXWyN9NNgQ",
                                  "BQACAgIAAxkBAAL8v2bpW005xSisCviUN_6ORY9kkx-PAAIlTAAC3CnxSifAlvGBJAs0NgQ"]
            }


all_teors_geometriya = {"teor_geot_ugli" : ["BQACAgIAAxkBAAEBGntnBVpl8dJTfOULDDNBjcwdqFLiCQACYF8AAgpMKEgQQxoqwu2IyDYE"],
                        "teor_geot_paralel_pramoy" : ["BQACAgIAAxkBAAEBGn9nBVp5bRjpH0gUoyzjDFbFfCECSQACYl8AAgpMKEjnGxg80RCH1jYE"],
                        "teor_geot_treugolnik" : ["BQACAgIAAxkBAAEBGoFnBVqB4PBjkae-j-UxdSLe4smYbAACZF8AAgpMKEjCw_8naAUjfTYE"],
                        "teor_geot_vidi_treugolnikov" : ["BQACAgIAAxkBAAEBGoNnBVqG1CJZ7NuowT7C_N_0er6vFgACZV8AAgpMKEjzD7h1sUXEazYE"],
                        "teor_geot_sin_kos_tan_cotan" : ["BQACAgIAAxkBAAEBGoVnBVqMunbakSYJkFlN-L-wHxniegACZl8AAgpMKEhpbC_vbBIdBzYE"],
                        "teor_geot_biss_mediana_visota" : ["BQACAgIAAxkBAAEBGodnBVqS_YtYaTfgOT9lno1kqYw8qAACZ18AAgpMKEiHOJhFIfMhUjYE"],
                        "teor_geot_ploshad_treugolnikov" : ["BQACAgIAAxkBAAEBGolnBVqWWSkQsBPXyfPrzQXEvUd3UgACaF8AAgpMKEh2Gsu9SohTiTYE"],
                        "teor_geot_podobiye_treugolnikov" : ["BQACAgIAAxkBAAEBGotnBVqeDUGGWKd9-wJCN2qM3UKxhAACal8AAgpMKEiQI8WTbMidVjYE"],
                        "teor_geot_kvadrat" : ["BQACAgIAAxkBAAEBGo1nBVqiaFvJQSdxqAmKBEOHxUaEtwACbF8AAgpMKEiPVTK2BD5IvzYE"],
                        "teor_geot_parallelogram" : ["BQACAgIAAxkBAAEBGo9nBVqoobFsUMt90DvZHtiA7Q1H5AACbl8AAgpMKEhHIEc7DO8G_DYE"],
                        "teor_geot_trapetsiya" : ["BQACAgIAAxkBAAEBGpFnBVqtU2CVqrqLed20U7yitz43IAACb18AAgpMKEgbvO7e3HUaQjYE"],
                        "teor_geot_mnogougolnik" : ["BQACAgIAAxkBAAEBGpNnBVqxwJVNQaP-IkcWnRK6aNA_FgACcF8AAgpMKEhN78A2fBsSFjYE"],
                        "teor_geot_okrujnost_krug" : ["BQACAgIAAxkBAAEBGpVnBVq2ouHPfQ_LLqtxMankUviHXwACcV8AAgpMKEhnlGvdhME87DYE"],
                        "teor_geot_ploshad" : ["BQACAgIAAxkBAAEBGpdnBVq6ErB6lZBByr1ZDxCs3oSmOwACc18AAgpMKEhLMFf9zassJzYE"],
                        "teor_geot_okrujnost_treugolnik" : ["BQACAgIAAxkBAAEBGplnBVq_6M7v-vXDagyo1sghLfqMlwACdF8AAgpMKEjgt_UReH4DBzYE"],
                        "teor_geot_okrujnost_chugolnik" : ["BQACAgIAAxkBAAEBGptnBVrEBjfbtOXDEgABjBs32tvhRpQAAnVfAAIKTChId5MaakmqTRM2BA"],
                        "teor_geot_sistema_koordinat" : ["BQACAgIAAxkBAAEBGp1nBVrZauxeIer5gqvoP3tO7-ZKVgACdl8AAgpMKEgXPmjcNmJPwDYE"],
                        "teor_geot_prizma" : ["BQACAgIAAxkBAAEBGp9nBVrh2cm1EOJ7Q_owXKUJs1O2iAACd18AAgpMKEhsQ1l_bsvGcjYE"],
                        "teor_geot_piramida" : ["BQACAgIAAxkBAAEBGqFnBVrqyWCYBQj7rTsMWOhW1yICFQACeV8AAgpMKEhaMjvy_SrwtjYE"],
                        "teor_geot_silindr" : ["BQACAgIAAxkBAAEBGqNnBVryvLSXX_usMgzWKJpRPT345QACe18AAgpMKEgyfnsFitkHNzYE"],
                        "teor_geot_konus" : ["BQACAgIAAxkBAAEBGqVnBVr4vldX-24CqqVF8YOYF9q4HwACfF8AAgpMKEjw6DLlfOwc9zYE"],
                        "teor_geot_shar_sfera" : ["BQACAgIAAxkBAAEBGqdnBVsBiDLJtnDVTix4JaBEQ8xWcQACfV8AAgpMKEgAATfzI3b_hAY2BA"],
                        "teor_geot_kombinasiya" : ["BQACAgIAAxkBAAEBGqlnBVsGJ4c9thmUvISnxYFFa7qrrwACfl8AAgpMKEgAAXjmHAABcX8NNgQ"]}

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_obiknovenniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfdGWOxpvhvnTf9HuQSdQxgrFJOEibAAKTOAACbbVpSBF-e-foZX0yNAQ")
#     await call.message.delete()

@dp.callback_query_handler(lambda call: 'teor_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


@dp.callback_query_handler(lambda call: 'shpar_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()

@dp.callback_query_handler(lambda call: 'prim_geot' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors_geometriya[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()



@dp.callback_query_handler(lambda call: 'teor' in call.data)
async def buying_corse(call: CallbackQuery):
    print(call.data.split(":"))
    for i in all_teors[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


@dp.callback_query_handler(lambda call: 'shpar' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()

@dp.callback_query_handler(lambda call: 'prim' in call.data)
async def buying_corse(call: CallbackQuery):
    for i in all_teors[call.data.split(":")[1]]:
        await call.message.reply_document(document = i)
    await call.message.delete()


@dp.callback_query_handler(text='nazad_5_6')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  await give_class_themes("5_6_class"))
    await call.message.delete()


@dp.callback_query_handler(text='nazad_7_8')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  await give_class_themes("7_8_class"))
    await call.message.delete()


@dp.callback_query_handler(text='nazad_9')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  await give_class_themes("9_class"))
    await call.message.delete()


@dp.callback_query_handler(text='nazad_10')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  await give_class_themes("10_class"))
    await call.message.delete()


@dp.callback_query_handler(text='nazad_geometry_1')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  geometriya_themes_1)
    await call.message.delete()


@dp.callback_query_handler(text='nazad_geometry_2')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  geometriya_themes_2)
    await call.message.delete()

@dp.callback_query_handler(text='nazad_geometry_3')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  geometriya_themes_3)
    await call.message.delete()

@dp.callback_query_handler(text='nazad_geometry_4')
async def buying_corse(call: CallbackQuery):
    await call.message.answer('Выберите тему', reply_markup =  geometriya_themes_4)
    await call.message.delete()



# @dp.callback_query_handler(lesson_callback.filter(item_name = 'shpar_obiknovenniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfiGWOyeyUUAYW39whOI92HCVk76jEAAKUOAACbbVpSBuXt7y0M1d9NAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_desyatichniye_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfdmWOxyiocBZUc56H5Iudwk4p8SGEAAKWOAACbbVpSPnsJ9lNYQvHNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_per_drobi'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfeGWOx2N0tVbjEeNakM6j13MtuNYFAAKXOAACbbVpSPtrWbv0I6IWNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_ratsion_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfemWOx687mk6KlAz63pc2NVewIQG_AAKdOAACbbVpSL3QiJOThY5yNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKffGWOx8elJzPEYAgImX8wF4oZdPmMAAKeOAACbbVpSITFkcln8suNNAQ")
#     await call.message.delete()

# @dp.callback_query_handler(lesson_callback.filter(item_name = 'teor_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKfimWOygJKz45-FZOd0V2BktW7kCYaAAKgOAACbbVpSIzppBMGo7c3NAQ")
#     await call.message.delete()


# @dp.callback_query_handler(lesson_callback.filter(item_name = 'shpar_stepen_rat_chisla'))
# async def buying_corse(call: CallbackQuery, callback_data: dict):
#     await call.message.reply_document(document = "BQACAgIAAxkBAAKhsGWU8ZBch2aTt497bBPFOg92lxDwAAImRwACSEyoSCYrFX29LNWYNAQ")
#     await call.message.delete()