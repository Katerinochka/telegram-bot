# coding = utf-8
import telebot
from telebot import apihelper
from telebot import types
from db import *

apihelper.proxy = {'http': 'http://78.42.42.40:8080'}
token = '1688655122:AAEoyZhdGRikykv-umnzlMeEpW_X4j3aM2s'
bot = telebot.TeleBot(token=token)

def get_msg_usr(message):
    return message.text

def get_id_usr(message):
    return message.chat.id

hideBoard = types.ReplyKeyboardRemove()

game_code = 0
uncle = 0

def hello(user):
    global game_code
    init_db()
    game_code = 0
    add_message(user, game_code)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да!")
    item2 = types.KeyboardButton("Вернусь позже")
    markup.add(item1, item2)
    photo = open('welcome.jpg', 'rb')
    bot.send_photo(user, photo,
                   caption='Вас приветствует 1900 год, ваша задача выжить в это суровое для всего мира время, в частности Российской империи, единственной стране, где сохранился и правит абсолютизм. Со скрипом идет индустриализация и ее последствия весьма ощутимы для всех слоев населения. Без лишних слов предлагаю вам начать и почувствовать себя участником ключевых событий этого периода, желаю вам удачи, и помните какие решения вы принимаете и на что они могут повлиять…')
    bot.send_message(user, 'Ты готов?',
                     parse_mode='html', reply_markup=markup)

def death(user, text):
    global game_code
    bot.send_message(user,
                     text,
                     parse_mode='html')
    game_code = -1
    add_message(user, game_code)
    game_progress(-1, user)

def shut_up(user):
    bot.send_message(user,'Или нажми на кнопку, или уходи', parse_mode='html')
    add_message(user, -2)

def game_progress(code, user):
    global game_code
    global uncle
    if code == -1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('/start')
        markup.add(item1)
        bot.send_message(user, "Ты можешь начать игру сначала", parse_mode='html', reply_markup=markup)
    elif code == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Соглашение на участие")
        item2 = types.KeyboardButton("Разубедить товарищей")
        item3 = types.KeyboardButton('Перевести тему')
        markup.add(item1, item2, item3)
        photo = open('worker.jpg', 'rb')
        bot.send_photo(user, photo,
                       caption='Александр Головин 1890 г.р., рабочий.\nНевзрачный внешний вид , характерен для его класса, простая цеховая одежда.')

        # bot.send_message(user,
                         # 'Александр Головин 1890 г.р., рабочий.\nНевзрачный внешний вид , характерен для его класса, простая цеховая одежда.',
                         # parse_mode='html')
        bot.send_message(user,
                         'Наш главный герой не смотря на свою "серую" наружность немного разбирается в происходящих событиях в тране, благодаря получению самого поверхностного образования за счёт мануфактуры на которой он работал, поэтому обдумывает предложение своих коллег по цеху принять участие в забастовке 7 января, его не устаривает рабочий вопрос в стране (12 часивой рабочий день, низкая зарплата, жизнь в бараке, отстутствие страхования и медпомощи)',
                         parse_mode='html', reply_markup=markup)
        # bot.send_message(user, "Вас зовут на забастовку. Вы пойдёте?", parse_mode='html', reply_markup=markup)
    elif code == 2:
        bot.send_message(user,
                         'Ваши товарищи довольны вами, ваша точка зрения не вызывает удивления.',
                         parse_mode='html')
        game_code = 5
        game_progress(game_code, user)
    elif code == 3:
        bot.send_message(user,
                         'Ваши аргументы не показались убедительными, тем более что рабочим и так терять было нечего, такая жизнь доконала их, они убедили вас присоединиться к ним.',
                         parse_mode='html')
        game_code = 5
        game_progress(game_code, user)
    elif code == 4:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Соглашаетесь с общественным мнением")
        item2 = types.KeyboardButton("Стоите на своём и отказываетесь")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Вас настойчиво призывают к участию, поступают угрозы. Ваша точка зрения возмущает и без того загнанных нищетой и голодом товарищей.',
                         parse_mode='html', reply_markup=markup)
    elif code == 5:
        photo = open('strike.jpg', 'rb')
        bot.send_photo(user, photo, caption='7 января.\nВы выходите на забастовку')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Идти с товарищами вперёд")
        item2 = types.KeyboardButton("Продолжаете идти с толпой")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Среди людей вы встретили своих знакомых. Они зовут вас на площадь - в самую гущу событий',
                         parse_mode='html', reply_markup=markup)
    elif code == 6:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Игнорируете и идёте дальше в толпе")
        item2 = types.KeyboardButton("Узнать что случилось")
        item3 = types.KeyboardButton('Вступаетесь за него')
        markup.add(item1, item2, item3)
        bot.send_message(user,
                         'По пути вы видите, как толпа линчует прохожего.',
                         parse_mode='html', reply_markup=markup)
    elif code == 7:
        bot.send_message(user, 'Толпа, разгневанная вашим поведением обступает вас и начинает избивать, но вовремя появившиеся правительственные войска разгоняют демонстрацию. Вас благодарит за помощь потерпевший, оказавшийся племянником начальника Петербуржского вагоностроительного завода. Он узнаёт ваше имя, предлагая медпомощь.', parse_mode='html')
        bot.send_message(user, 'После произошедшего возвращаетесь в бараки при заводе, но новое знакомство привносит в вашу жизнь заметные изменения, вы периодически общаетесь, повышаете уровень своего образования, получаете небольшую финансовую помощь за спасение.', parse_mode='html')
        bot.send_message(user, 'Вы продолжаете участвовать в стачках, на одной из них встречаете одноклассника, который разделяет ваши взгляды, предлагает вступить в рабочую организацию.', parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отказываетесь")
        item2 = types.KeyboardButton("Вступаете в профсоюз")
        markup.add(item1, item2)
        bot.send_message(user,
                         'По стране прокатывается волна революций, что все таки обратило внимание властей на Земельный голод, многочисленные нарушения прав рабочих, неудовлетворённость существующим уровнем гражданских свобод, деятельность либеральных и социалистических партий, контрреформы.',
                         parse_mode='html', reply_markup=markup)
    elif code == 8:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Согласиться")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Вами довольно начальство, вы хорошо работаете и не были замечены за революционной деятельностью, оно принимает решение назначиь вас мастером',
                         parse_mode='html', reply_markup=markup)
    elif code == 9:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Угнетать")
        item2 = types.KeyboardButton("Дружить")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Став мастером вы можете пойти по пути угнетения подчинённых или стараеться остаться с ними в хороших отношениях.',
                         parse_mode='html', reply_markup=markup)
    elif code == 10:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Согласиться")
        item2 = types.KeyboardButton("Отказаться")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Поддерживая общение с рабочими, они продолжают агитировать вас на вступление в рабочую организацию в руководящей должности.',
                         parse_mode='html', reply_markup=markup)
        #game_code = 19
        #game_progress(game_code, user)
    elif code == 11:
        bot.send_message(user,
                         'Вы отказываетесь от должности мастера, так как понимаете, какие последствия это может привести. На вас могут совершить покушение рабочие, как при демонстрациях, так и во время работы, подстроив несчастный случай.',
                         parse_mode='html')
        if uncle == 1:
            game_code = 12
            bot.send_message(user,
                             'Вами крайне недовольно начальство. Вас выгоняют с завода.',
                             parse_mode='html')
            game_progress(game_code, user)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton("Пойти в армию")
            item3 = types.KeyboardButton("Попрошайничать")
            markup.add(item2, item3)
            bot.send_message(user,
                             'Вами крайне недовольно начальство. Вас выгоняют с завода.',
                             parse_mode='html', reply_markup=markup)
    elif code == 12:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Работать")
        item2 = types.KeyboardButton("Учиться")
        item3 = types.KeyboardButton("Отказаться")
        markup.add(item1, item2, item3)
        bot.send_message(user,
                         'По дороге в жилище вы встречаете своего знакомого, которого вы спасли. Будучи человеком со связями, поручившись за вас - он предлагает вам следующие варианты:\n1) должность мастера на вагоностроительном заводе\n2) поступить в юнкерское училище',
                         parse_mode='html', reply_markup=markup)
    elif code == 13:
        photo = open('army.jpg', 'rb')
        bot.send_photo(user, photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Развитие карьеры")
        item3 = types.KeyboardButton("Довольствуетесь положением")
        markup.add(item2, item3)
        bot.send_message(user,
                         'Вы согласились поступить в училище, принимая во внимание перспективы военной карьеры и возможность получить дополнительное образование.',
                         parse_mode='html', reply_markup=markup)
    elif code == 14:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Увести людей")
        item3 = types.KeyboardButton("Возглавить шествие")
        markup.add(item2, item3)
        bot.send_message(user,
                         'В профсоюзе вы ведёте активную деятельность, повышаете образование, агитируете товарищей по цеху, распространяете идею революции. На очередной стачке главу вашего профсоюза убивают в столкновении с правительственными войсками. Перед вами встаёт выбор: увести людей и спасти их от бессмысленной бойни или возглавить демонстрацию и начать столкновение с правительственными войсками.',
                         parse_mode='html', reply_markup=markup)
    elif code == 15:
        photo = open('army.jpg', 'rb')
        bot.send_photo(user, photo, caption='Внезапно начинается Первая Мировая война, вас мобилизуют и направляют на фронт. Вы принимаете участие в отбитии Лодзи (Польша).',)
        death(user, 'Позже вас перевели на Кавказ, где Российская армия одержала победу на Османской империей. Вас перевели в крепость Осовец, 24 июля 1915 года немцы начали химическую атаку. Не смотря на тяжелейшие ранения выжившие крепости переходят в контратаку. В истории это событие известно как - Атака мертвецов. Получив смертельное отравление ипритом вы скончались от ожога лёгких.')
    elif code == 16:
        bot.send_message(user,
                         'Вы чувствуете у себя талант к военному делу, развиваете его. На вас обращает внимание начальство. Выпускаетесь в звании унтер-офицера.',
                         parse_mode='html')
        bot.send_message(user,
                         'Ответственно несёте службу, что открывает для вас дорогу в свет, вы бываете на светских мероприятиях, знакомитесь с другой стороной жизни, о которой даже не мечтали раньше.',
                         parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Интеллигенция")
        item2 = types.KeyboardButton("Сослуживцы")
        markup.add(item1, item2)
        bot.send_message(user,
                         'На одном из таких вечеров вы стали свидетелем обсуждения назревающей Первой Мировой войны и крайне острой общественной ситуации - непрекращающиеся стачки, бунтарское поведение рабочих и крестьян, перед вами встал выбор: поддержать революционно настроенную интеллигенцию или своих ослуживцев, симпатизирующих монархической позиции.',
                         parse_mode='html', reply_markup=markup)
    elif code == 17:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отказаться")
        item2 = types.KeyboardButton("Согласиться")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Руководство профсоюза обратило на вас внимание и предложило стать помощником главы, обратив внимание на вашу находчивость, образование и умение в критический момент вступиться за своих товарищей.',
                         parse_mode='html', reply_markup=markup)
    elif code == 18:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отказаться")
        item2 = types.KeyboardButton("Согласиться")
        markup.add(item1, item2)
        bot.send_message(user,
                         'Вас заметили представители РСДРП и пытаются завербовать',
                         parse_mode='html', reply_markup=markup)
    elif code == 19:
        death(user, 'Вы дожили до войны. Поздравляем...')

@bot.message_handler(commands=['start'])
def welcome(message):
    user = get_id_usr(message)
    hello(user)

@bot.message_handler(content_types=['text'])
def echo(message):
    text = get_msg_usr(message)
    user = get_id_usr(message)
    global game_code
    global uncle
    if game_code == -1:
        if text == '/start':
            #hello(user)
            pass
        else:
            shut_up(user)
    if game_code == 0:
        if text == 'Да!':
            game_code = 1
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Вернусь позже':
            bot.send_message(user, 'Возвращайся скорее!', parse_mode='html')
            #game_code = -1
            #game_progress(game_code, user)
            hello(user)
        else:
            shut_up(user)
    elif game_code == 1:
        if text == 'Соглашение на участие':
            game_code = 2
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Разубедить товарищей':
            game_code = 3
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Перевести тему':
            game_code = 4
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 4:
        if text == 'Соглашаетесь с общественным мнением':
            game_code = 5
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Стоите на своём и отказываетесь':
            death(user, 'Ваши товарищи расправляются с вами, забив инструментами до смерти')
        else:
            shut_up(user)
    elif game_code == 5:
        if text == 'Идти с товарищами вперёд':
            death(user, 'Всё закончилось, как вы и предполагали. С вами расправились правительственные войска расстрелом')
        elif text == 'Продолжаете идти с толпой':
            game_code = 6
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 6:
        if text == 'Игнорируете и идёте дальше в толпе':
            bot.send_message(user, 'Демонстрантов разгоняют правительственные войска. Вам удалось скрыться от них и вернуться в жильё от завода. "Дома" вы делитесь впечатлениями от произошедшего с уцелевшими товарищами.', parse_mode='html')
            bot.send_message(user, 'Вы ведёте обычную жизнь, пытаясь свести концы с концами', parse_mode='html')
            bot.send_message(user, 'По стране прокатывается волна революций, что все таки обратило внимание властей на Земельный голод, многочисленные нарушения прав рабочих, неудовлетворённость существующим уровнем гражданских свобод, деятельность либеральных и социалистических партий, контрреформы.', parse_mode='html')
            game_code = 8
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Узнать что случилось':
            bot.send_message(user, 'Слышите ответ - так и надо буржую', parse_mode='html')
            game_code = 7
            add_message(user, game_code)
            uncle = 1
            game_progress(game_code, user)
        elif text == 'Вступаетесь за него':
            game_code = 7
            add_message(user, game_code)
            uncle = 1
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 7:
        if text == 'Отказываетесь':
            game_code = 8
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Вступаете в профсоюз':
            game_code = 14
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 8:
        if text == 'Согласиться':
            game_code = 9
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Отказаться':
            game_code = 11
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 9:
        if text == 'Угнетать':
            bot.send_message(user,
                             'Получив новую должность вы угнетаете рабочик, не скрываете своё превосходство, отворачиваетесь от революционной идеологии.',
                             parse_mode='html')
            death(user, 'Поздравляем вас с повышением, через неделю вас подловили рабочие и убили на всероссийской стачке.')
        elif text == 'Дружить':
            game_code = 10
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 10:
        if text == 'Согласиться':
            game_code = 18
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Отказаться':
            bot.send_message(user,
                             '14 июля 1914 года начинается Первая Мировая война, вы решаете продолжать работу мастером.',
                             parse_mode='html')
        else:
            shut_up(user)
    elif game_code == 11:
        if text == 'Пойти в армию':
            game_code = 15
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Попрошайничать':
            photo = open('beggar.jpg', 'rb')
            bot.send_photo(user, photo)
            death(user, 'У вас нет средств к существованию, нищета и голод одолели вас')
        else:
            shut_up(user)
    elif game_code == 12:
        if text == 'Работать':
            game_code = 9
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Учиться':
            game_code = 13
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Отказаться':
            uncle = 0
            game_code = 11
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 13:
        if text == 'Развитие карьеры':
            game_code = 16
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Довольствуетесь положением':
            bot.send_message(user,
                             'Выпускаетесь подпрапорщиком в 13 роту 226 землянского полка, вы довольны своим положением, у вас стабильное общественное и финансовое положение.',
                             parse_mode='html')
            game_code = 15
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 14:
        if text == 'Увести людей':
            game_code = 17
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Возглавить шествие':
            death(user, 'Вас арестовала полиция, вы отбываете свой срок в ссылке, где загибаетесь от туберкулёза.')
        else:
            shut_up(user)
    elif game_code == 16:
        if text == 'Интеллигенция':
            bot.send_message(user,
                             'Прошлое всё же напомнило о себе, вы оказались верны своим взглядам, обзавелись влиятельными знакомствами среди революционеров, но ваше начальство оказалось крайне недовольно, вас хотят отдать под трибунал.',
                             parse_mode='html')
            bot.send_message(user,
                             'Ваше положение спасает внезапно начавшаяся Первая Мировая и вы в числе первых мобилизованных отправляетесь на фронт, участвуете во взятии Львова.',
                             parse_mode='html')
            game_code = 19
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Сослуживцы':
            bot.send_message(user,
                             'Такой ответ удовлетвроил ваших новых товарищей, ваш статус среди военнослужащих и начальства укрепился, за активное отстаивание такой позиции и безупречную службу вас решают повысить до штабс-капитана',
                             parse_mode='html')
            bot.send_message(user,
                             'В должности командира роты вас направляют в Галицию, где в первые годы в стремительной атаке вы возглавляете своих подчиненных и героически погибаете в одном из сражений.',
                             parse_mode='html')
            game_code = 19
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 17:
        if text == 'Отказаться':
            bot.send_message(user,
                             'Вы решили отказаться, чтобы не вызывать на себя лишних подозрений. Продолжаете состоять в профсоюзе, совмещая это с работой',
                             parse_mode='html')
            bot.send_message(user,
                             '14 июля 1914 года начинается Первая Мировая Война, вы решаете продолжать работу.',
                             parse_mode='html')
            game_code = 19
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Согласиться':
            bot.send_message(user,
                             'Вы решили согласиться и принять на себя такую ответственность.',
                             parse_mode='html')
            game_code = 18
            add_message(user, game_code)
            game_progress(game_code, user)
        else:
            shut_up(user)
    elif game_code == 18:
        if text == 'Согласиться':
            bot.send_message(user,
                             'Из-за политического преследования вас увольняют, работаете в подполье, прикинувшись Марксом и Энгельсом, готовите почву к революции...',
                             parse_mode='html')
            bot.send_message(user,
                             '14 июля 1914 года начинается Первая Мировая Война, вы далеки от этих событий, ваша задача - анализ ситуации и подготовка к революции.',
                             parse_mode='html')
            game_code = 19
            add_message(user, game_code)
            game_progress(game_code, user)
        elif text == 'Отказаться':
            bot.send_message(user,
                             'Следуя своим убеждениям, решаете вступить в ряды анархистов, так как уже не можете терпеть бездействие властей и мирное регулирование - не ваша забота.',
                             parse_mode='html')
            death(user, 'Из-за убийства Столыпина П.А. начинаются чистки, вас сдают и вы гибнете на каторге от туберкулёза.')
        else:
            shut_up(user)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
