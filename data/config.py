from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
GUBKIN_BOOKS = env.list("GUBKIN_BOOKS")
AMITY_BOOKS = env.list("AMITY_BOOKS")
IUT_BOOKS = env.list("IUT_BOOKS")
WIUT_2015_BOOKS = env.list("WIUT_2015_BOOKS")
WIUT_2018_BOOKS = env.list("WIUT_2018_BOOKS")
WIUT_2019_BOOKS = env.list("WIUT_2019_BOOKS")
WIUT_2020_BOOKS = env.list("WIUT_2020_BOOKS")
WIUT_L_2015_BOOKS = env.list("WIUT_L_2015_BOOKS")
WIUT_L_2018_BOOKS = env.list("WIUT_L_2018_BOOKS")
WIUT_L_2019_BOOKS = env.list("WIUT_L_2019_BOOKS")
WIUT_L_2021_BOOKS = env.list("WIUT_L_2021_BOOKS")
LOGICAL = env.list("LOGICAL")
CAMBRIDGE = env.list("CAMBRIDGE")
SKANAVI = env.list("SKANAVI")
USMONOV = env.list("USMONOV")
SCHOOL_BOOKS = env.list("SCHOOL_BOOKS")
SHARIGINA = env.list("SHARIGINA")
TRENAJOR = env.list("TRENAJOR")
SBORNIK = env.list("SBORNIK")
MEDIC = env.list("MEDIC")
