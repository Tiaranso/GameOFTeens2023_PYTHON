"""
Імпортуємо бібліотеки (Початок)
"""
import sqlite3 # База даних
import telebot # Телеграм бот
from telebot import types # Для зазначення типів
"""
Імпортуємо бібліотеки (Кінець)
"""



"""
Функції (Початок)
"""
# Перевіряємо чи зареєстровано користувач, та якщо не зареєстровано, додаємо його в БД та повертаємо результат True, інакше - тільки повертаємо False
def db_reg_user(userId: int, userName: str): 
    cursor.execute("SELECT id FROM users WHERE uid=?", (userId,))
    rows = cursor.fetchall()
    id = False
    for row in rows:
        id = row[0]

    if id:
        return False
    else:
        cursor.execute('INSERT INTO users (uid, names, steep) VALUES (?, ?, ?)', (userId, userName, 0))
        conn.commit()
        return True


# Обновляємо на якому кроці (питанні) користувач. Потрібно для повернення в потрібне місце користувача, якщо він загубився та ввів команду /start і взагалі коректній роботі визначення на якому питанні користувач
def user_steep_update(userId: int, steep: str):
    update_query = """
        UPDATE users
        SET steep = ?
        WHERE uid = ?
    """
    cursor.execute(update_query, (steep, userId))
    conn.commit()
    return True


# Обновляємо категорію тарифів (питання з відповідями Повсякденне використання (1), Всій сім’ї (2), Інтернет-речей (3))
def user_category_update(userId: int, category: int):
    update_query = """
        UPDATE users
        SET category = ?
        WHERE uid = ?
    """
    cursor.execute(update_query, (category, userId))
    conn.commit()
    return True


# Обновляемо кількість інтернету, яку споживає користувач
def user_net_update(userId: int, net: int):
    update_query = """
        UPDATE users
        SET net = ?
        WHERE uid = ?
    """
    cursor.execute(update_query, (net, userId))
    conn.commit()
    return True


# Обновляемо кількість мінут, яку споживає користувач
def user_min_update(userId: int, min: int):
    update_query = """
        UPDATE users
        SET min = ?
        WHERE uid = ?
    """
    cursor.execute(update_query, (min, userId))
    conn.commit()
    return True


# Обновляемо чи хоче людина дізнатися о бонусах
def user_action_update(userId: int, action: int):
    update_query = """
        UPDATE users
        SET action = ?
        WHERE uid = ?
    """
    cursor.execute(update_query, (action, userId))
    conn.commit()
    return True


# Отримуємо дані про користувача
def user_info(userId: int):
    cursor.execute("SELECT id, names, steep, net, min, category, action FROM users WHERE uid=?", (userId,))
    rows = cursor.fetchall()
    id_id = False
    namesss_namesss = False
    steep_steep = False
    net_net = False
    min_min = False
    category_category = False
    action_action = False
    for row in rows:
        id_id = row[0]
        namesss_namesss = row[1]
        steep_steep = row[2]
        net_net = row[3]
        min_min = row[4]
        category_category = row[5]
        action_action = row[6]
    return {"id":id_id, "names":namesss_namesss, "steep":steep_steep, "net":net_net, "min":min_min, "category":category_category, "action":action_action}



# Викликається, якщо людина натискає кнопку старт, чи два рази натиснула кнопку старт та у другій відповіді на питання чи не бажала вона продовжити, де зупинилась, відповіла так
def start_comand(userId: int, userName: str):
    print(userId)
    db_reg_user(userId=userId, userName=userName)
    menu = telebot.types.InlineKeyboardMarkup()
    menu.add(telebot.types.InlineKeyboardButton(text = '👍 Так', callback_data='1'))
    menu.add(telebot.types.InlineKeyboardButton(text = '👎 Ні', callback_data='-1'))
    menu.add(types.InlineKeyboardButton("👨‍💻 Звязатися зі службою турботи", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/'))
    bot.send_message(userId, f'<b>Привіт від лайфу 😊</b>\n\nСхоже на те, що ви тут уперше, тож давайте познайомимося)? Мене звати СІМагочі, а Вас, як розумію, <b>{userName}</b>. Дуже гарне ім\'я)\n\nЯ допомагаю всім підібрати найкращий тариф для своїх потреб. Це абсолютно безкоштовно та безпечно. Бажаєте дізнатися вигідний тариф від Lifecell? ', parse_mode="HTML", reply_markup=menu)


# Видаляємо користувача та його дані. Потрібно, якщо людина вирішила знову підібрати тариф чи видалити акаунт
def user_delete(user_iid: int, user_nname: str):
    bot.send_video(user_iid, 'https://i.gifer.com/5BF0.gif', None, 'Text')
    cursor.execute('DELETE FROM users WHERE uid=?', (user_iid,))
    conn.commit()
    start_comand(userId=user_iid, userName=user_nname)

# Викликається, коли людина вказала скількі їй потрібно інтернету, чи натиснула кнопку старт (далі - загубилася :D) та у відповіді на питання чи не бажає вона продовжити, де зупинилась, відповіла так
def steep3(userId: int, net: int):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("0")
    btn2 = types.KeyboardButton("100")
    btn3 = types.KeyboardButton("250")
    btn4 = types.KeyboardButton("400")
    markup.row(btn1, btn2, btn3, btn4)
    bot.send_message(userId, f'<b>Файно 👍</b>\n\nСкільки хвилин на розмови ви зазвичай використовуєте протягом місяця? Введіть відповідь цифрами, чи виберіть готовий варіант в меню', parse_mode="HTML", reply_markup = markup)


# Викликається, коли людина вказала скількі їй потрібно хвилин, чи загубилася та у відповіді на питання чи не бажає вона продовжити, де зупинилась, відповіла так
def steep4(userId: int, min: int):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Так")
    btn2 = types.KeyboardButton("Ні")
    markup.row(btn1, btn2)

    bot.send_message(userId, f'<b>Клас 👌</b>\n\nЧи хочете ви дізнатися про програму лояльності Lifecell?', parse_mode="HTML", reply_markup = markup)


# Викликається, коли людина вказала скількі їй потрібно хвилин, чи загубилася та у відповіді на питання чи не бажає вона продовжити, де зупинилась, відповіла так
def steep5(userId: int, action: int):
    #markup = telebot.types.ReplyKeyboardRemove()
    #bot.send_message(userId, f'<b>Круто 😎</b>', parse_mode="HTML", reply_markup = markup)
    analysis(userId=userId)


# Знаходимо самий відповідний тариф для користувача
def analysis(userId: int):
    us_info = user_info(userId=userId)

    khv = us_info["min"] #мінімум хв
    if khv == -1:
        khv = 49000
    kgb = us_info["net"]  #мінімум гб
    if kgb == -1:
        khv = 10000

    if khv==0 and kgb==0:
        bot.send_message(userId, f'З вас 0 гривень 😉\n\nЯкщо без жартів, то таких тарифів в нас не існує. Якщо бажаєте підібрати тариф, який підійде саме Вам, введіть команду /start', parse_mode="HTML")
        return
    query = ''
    if khv>0:
        query += " AND minutes!=0"
    else:
        query += " AND minutes==0"
    if kgb>0:
        query += " AND net!=0"
    else:
        query += " AND net==0"

    cursor.execute("SELECT id, minutes, net, link,names FROM tariffs WHERE category=?", (us_info["category"],))
    rows = cursor.fetchall()
    id = False
    taryf = []
    for row in rows:
        id = row[0]
        min = row[1]
        net = row[2]
        link = row[3]
        names = row[4]
        taryf.append([min, net, link, id,names])

    #taryf = [ [400,10,'tar1',1] , [200,20,'tar2',2] , [150,100,'tar3',3], [300,10000,'tar4',4],[150,50,'tar5',5],[170,140,'tar6',6],[15,1,'tar7',7], ]#тариф формат хв,гб,назва,id

    ctar = taryf #список відфільтрованих тарифів

    # for i in taryf: #фільтрування за мінімумом хв і гб  
    #     if i[0] >= khv and i[1]>=kgb:
    #         ctar.append(i)
    # print(ctar)

    for k in range(len(ctar)):#сортування
            j=0
            for i in range(len(ctar)-1):
                if (abs(ctar[j][0] - khv)+abs(ctar[j][1] - kgb)*10) > (abs(ctar[j+1][0] - khv))+(abs(ctar[j+1][1] - kgb)*10):#різниця 1гб прирівнюється до  10хвилин 
                    ctar[j],ctar[j+1] = ctar[j+1],ctar[j]
                j+=1
    
    print(ctar)
    if us_info['action']==1:
        bot.send_message(userId, f'<b>🎁 Інформація щодо програми лояльності:</b>\n\n•	Я, СІМагочі, можу принести вам бонусний кешбек та "плюшки" за своєчасну оплату вашого тарифного плану.\n\n•	Є PLATINUM Клуб з персональним консультантом Lifecell, запрошеннями на івенти, майстер-класи, знижки, найактуальніші пропозиції та багато іншого, щоб ви відчули себе STAR PLATINUM!\n\n•	У нас є знижки для студентів. Lifecell CAMPUS Клуб пропонує все, що потрібно, щоб ви платили менше, розвивалися, розважалися та насолоджувалися смачненьким! Приходьте до клубу та насолоджуйтесь поки ви студенти!\n\n•	Послуга 🐹. Захом\'ячте все, що не використали у попередньому періоді!\n\n•	Абоненти Lifecell, які використовують тариф зі списку та є учасниками програми Fishka, мають можливість отримувати щомісяця 5% балами на карту Fishka.\n\n•	Немає коштів на дзвінок? Замовте 100 хвилин на всі номери по Україні з месенджера BiP! Встановлюйте застосунок «Мій lifecell» та вигравайте корисні подарунки від Lifecell (гігабайти, хвилини, SMS) та партнерів в оновленому розділі Shake&Win!', parse_mode="HTML")
    
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(userId, f'<b>Дякуємо🙂❗</b>', parse_mode="HTML", reply_markup=keyboard)
    menu = telebot.types.InlineKeyboardMarkup()
    menu.add(types.InlineKeyboardButton("👨‍💻 Звязатися зі службою турботи", url='https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/'))
    bot.send_message(userId, f'На цьому все. Я рекомендую Вам звернути увагу на <a href="{ctar[0][2]}">{ctar[0][4]}</a>, <a href="{ctar[1][2]}">{ctar[1][4]}</a> та <a href="{ctar[2][2]}">{ctar[2][4]}</a> тарифи. Вони максимально відповідають критеріям вашого пошуку 😉', parse_mode="HTML", reply_markup=menu)



    
    
"""
Функції (кінець)
"""



"""
Точка входу (початок)
"""
if __name__ == "__main__":
    bot = telebot.TeleBot("6290458022:AAHVwCw6nhuEKLd8WJ1w342d9wjEhHOJmGM") # Токен боту

    # Підключаємося к базі 
    conn = sqlite3.connect('db.db', check_same_thread=False) 
    cursor = conn.cursor() 

    # Кроки та їх опис для випадку, якщо користувач загубився
    crocy = {0: "привітанні", -1: "тому, що відмовились підбірати тариф", 1: "кроці, коли погодились підібрати тариф", 2: "виборі призначення тарифу", 3: "тому, що вказували кількість використання ГБ за місяць", 4: "тому, що вказували кількість використання хвилин за місяць", 5: "тому, що вказували чи хочете дізнатися про програму лояльності"}


    # Команда старт
    @bot.message_handler(commands=['start'])
    def start_message(message):
        # Отримаємо дані о користувачі
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        reg = db_reg_user(userId=us_id, userName=us_name) # Реєстрація та перевірка на реєстрацію

        if reg: # Якщо тільки зараз зареєструвався
            start_comand(userId=us_id, userName=us_name)

        else: # Якщо вже бувалий
            steep = user_info(userId=us_id)["steep"] # На якому користувач кроці (питанні)
            croc = crocy[steep] # Опис кроку (питання)
            if steep==0:
                reg = db_reg_user(userId=us_id, userName=us_name)
            menu = telebot.types.InlineKeyboardMarkup()
            menu.add(telebot.types.InlineKeyboardButton(text = '👍 Продовжити', callback_data=str(steep)))
            menu.add(telebot.types.InlineKeyboardButton(text = '👎 Почати спочатку', callback_data='delete'))
            markup = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, f'😊 Востаннє Ви зупинилися на {croc}.', parse_mode="HTML", reply_markup=markup)
            bot.send_message(message.chat.id, f'Хочете продовжити або почати спочатку?\n\n⚠️ Якщо Ви почнете спочатку, я зітру собі пам\'ять', parse_mode="HTML", reply_markup=menu)


    # Обробляємо кнопки
    @bot.callback_query_handler(func=lambda call: True)
    def name_call(message):
        # Отримаємо дані о користувачі
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_info = user_info(userId=us_id)

        # Користувач загубився
        if message.data == '0':
            #db_reg_user(userId=us_id, userName=us_name) # Реєстрація та перевірка на реєстрацію
            print(message.from_user.id)
            bot.delete_message(message.message.chat.id, message.message.message_id)
            start_comand(userId=us_id, userName=us_name)

        # Перший крок (питання)
        elif message.data == '1':
            bot.delete_message(message.message.chat.id, message.message.message_id)
            user_steep_update(userId=us_id, steep=1)
            menu = telebot.types.InlineKeyboardMarkup()
            menu.add(telebot.types.InlineKeyboardButton(text='⚽️ Повсякденне використання', callback_data='12'))
            menu.add(telebot.types.InlineKeyboardButton(text='👨‍👩‍👧‍👦 Всій сім’ї', callback_data='22'))
            menu.add(telebot.types.InlineKeyboardButton(text='🌐 Інтернет-речей', callback_data='32'))
            bot.send_message(message.from_user.id, f'<b>Чудово 🤗</b>\n\nЗараз ми проведемо невелике опитування, щоб підібрати найкращий тариф саме для Вас. Це займе менш, ніж 3 хвилини Вашого часу, а в кінці Вас чекає тортик, тож все буде супер 😉\n\nДавайте визначимося, для яких цілей Вам потрібен тариф, виберіть один з варіантів', parse_mode="HTML", reply_markup = menu)

        # Другий крок (питання)   
        elif message.data == '12' or message.data == '22' or message.data == '32' or message.data == '2':
            bot.delete_message(message.message.chat.id, message.message.message_id)
            user_steep_update(userId=us_id, steep=2)
            user_category_update(userId=us_id, category=message.data[:1])
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("0")
            btn2 = types.KeyboardButton("5")
            btn3 = types.KeyboardButton("10")
            btn4 = types.KeyboardButton("20")
            btn5 = types.KeyboardButton("Безліміт")
            markup.row(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, f'<b>Добре 👍</b>\n\nЯку мінімальну кількість гігабайт інтернет-трафіку ви споживаєте протягом місяця? Введіть відповідь цифрами, чи виберіть готовий варіант в меню', parse_mode="HTML", reply_markup = markup)
        
        # Третій крок (питання)
        elif message.data == '3':
            steep3(userId=us_id, net=us_info['net'])

        # Четвертий крок (питання)
        elif message.data == '4':
            steep4(userId=us_id, min=us_info['min'])

        # П'ятий крок (питання)
        elif message.data == '5':
            steep5(userId=us_id, action=us_info['action'])

        # Мінус перший крок (питання), людина не хоче шукати тариф :(
        elif message.data == '-1':
            bot.delete_message(message.message.chat.id, message.message.message_id)
            bot.send_message(message.from_user.id, f'Lifecell сумуватиме без вас! Якщо бажаєте знайти найбільш чудовий тариф, який підійде саме Вам, пишіть знову, я завжди тут та готовий допомогти 😉', parse_mode="HTML")
            user_steep_update(userId=us_id, steep=-1)

        # Видалелення даних о користувачі
        elif message.data == 'delete':
            bot.delete_message(message.message.chat.id, message.message.message_id)
            user_delete(user_iid=us_id, user_nname=us_name)
            #bot.send_message(message.from_user.id, f'Я забув про все, що ми говорили. Для того, щоб почати знову, напишіть команду /start 🙂', parse_mode="HTML")
            #user_steep_update(userId=us_id, steep=-1)


    # Обробляємо текст
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        # Отримаємо дані о користувачі
        us_id = message.from_user.id
        us_info = user_info(userId=us_id)

        # Обробляємо інтернет
        if ((message.text.lower().isdigit() and int(message.text.lower())>=0) or message.text.lower()=="безліміт") and us_info['steep']==2:
            user_steep_update(userId=us_id, steep=3)
            if(message.text.lower()=="безліміт"):
                neT = -1
            else:
                neT = message.text.lower()
            user_net_update(userId=us_id, net=neT)
            steep3(userId=us_id, net=neT)

        # Обробляємо хвилини
        elif ((message.text.lower().isdigit() and int(message.text.lower())>=0) or message.text.lower()=="безліміт") and us_info['steep']==3:
            user_steep_update(userId=us_id, steep=4)
            if(message.text.lower()=="безліміт"):
                miN = -1
            else:
                miN = message.text.lower()
            user_min_update(userId=us_id, min=miN)
            steep4(userId=us_id, min=miN)

        # Обробляємо бонуси
        elif (message.text.lower()=="так" or message.text.lower()=="ні") and us_info['steep']==4:
            user_steep_update(userId=us_id, steep=5)
            if(message.text.lower()=="ні"):
                actioN = -1
            else:
                actioN = 1
            user_action_update(userId=us_id, action=actioN)
            steep5(userId=us_id, action=actioN)


    # На старт, увага, пуск! 
    bot.polling(none_stop=True)
"""
Точка входу (кінець)
"""
