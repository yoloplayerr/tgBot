from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Жанры
button_genre1 = KeyboardButton('Ужасы')
button_genre2 = KeyboardButton('Триллер')
button_genre3 = KeyboardButton('Фантастика')
button_back_to_genre=KeyboardButton('К выбору жанра')
button_back_to_author_hor=KeyboardButton('К выбору автора в жанре: Ужасы')
button_back_to_author_thril=KeyboardButton('К выбору автора в жанре: Триллер')
button_back_to_author_phant=KeyboardButton('К выбору автора в жанре: Фантастика')
#Писатели ужасов
button_hor_king = KeyboardButton('Стивен Кинг')
button_hor_kraft = KeyboardButton('Говард Лавкрафт')
button_hor_po = KeyboardButton('Эдгар По')

#Писатели триллеров
button_thril_nesbe = KeyboardButton('Ю Несбё')
button_thril_lihein = KeyboardButton('Деннис Лихейн')
button_thril_grange = KeyboardButton('Жан-Кристоф Гранже')


#Писатели фантастики
button_phant_azimov = KeyboardButton('Айзек Азимов')
button_phant_belaev = KeyboardButton('Александр Беляев')
button_phant_bradber = KeyboardButton('Рэй Брэдбери')

#Произведения Кинга
button_hor_king_1 = KeyboardButton('Жребий Салема')
button_hor_king_2 = KeyboardButton('Оно')
button_hor_king_3 = KeyboardButton('Кладбище домашних животных')
button_hor_king_4 = KeyboardButton('Мистер Мерседес')

#Произведения Лавкрафта
button_hor_kraft_1 = KeyboardButton('Зов Ктулху')
button_hor_kraft_2 = KeyboardButton('Тень над Иннсмутом')
button_hor_kraft_3 = KeyboardButton('Хребты безумия')
button_hor_kraft_4 = KeyboardButton('Ужас Данвича')

#Произведения По
button_hor_po_1 = KeyboardButton('Падение дома Ашеров')
button_hor_po_2 = KeyboardButton('Золотой жук')
button_hor_po_3 = KeyboardButton('Маска красной смерти')
button_hor_po_4 = KeyboardButton('Лигейя')


#Произведения Несбё
button_thril_nesbe_1 = KeyboardButton('Снеговик')
button_thril_nesbe_2 = KeyboardButton('Нетопырь')
button_thril_nesbe_3 = KeyboardButton('Призрак')
button_thril_nesbe_4 = KeyboardButton('Леопард')

#Произведения Лихейна
button_thril_lihein_1 = KeyboardButton('Остров проклятых')
button_thril_lihein_2 = KeyboardButton('Таинственная река')
button_thril_lihein_3 = KeyboardButton('Общак')
button_thril_lihein_4 = KeyboardButton('Когда под ногами бездна')

#Произведения Гранже
button_thril_grange_1 = KeyboardButton('Багровые реки')
button_thril_grange_2 = KeyboardButton('Пассажир')
button_thril_grange_3 = KeyboardButton('Присягнувшие тьме')
button_thril_grange_4 = KeyboardButton('Чёрная линия')



#Произведения Азимова
button_phant_azimov_1 = KeyboardButton('Основание')
button_phant_azimov_2 = KeyboardButton('Конец вечности')
button_phant_azimov_3 = KeyboardButton('Сами боги')
button_phant_azimov_4 = KeyboardButton('Двухсотлетний человек')

#Произведения Беляева
button_phant_belaev_1 = KeyboardButton('Голова профессора Доуэля')
button_phant_belaev_2 = KeyboardButton('Остров погибших кораблей')
button_phant_belaev_3 = KeyboardButton('Ариэль')
button_phant_belaev_4 = KeyboardButton('Небесный гость')

#Произведения Брэдбери
button_phant_bradber_1 = KeyboardButton('451 градус по Фаренгейту')
button_phant_bradber_2 = KeyboardButton('Марсианские хроники')
button_phant_bradber_3 = KeyboardButton('Человек в картинках')
button_phant_bradber_4 = KeyboardButton('Надвигается беда')











#Клавиатура с жанрами
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_genre1).add(button_genre2).add(button_genre3)
#Клавиатура с ужасами
greet_kb_hor = ReplyKeyboardMarkup()
greet_kb_hor.add(button_hor_king).add(button_hor_kraft).add(button_hor_po).add(button_back_to_genre)

#Клавиатура с Кингом
greet_kb_hor_king = ReplyKeyboardMarkup()
greet_kb_hor_king.add(button_hor_king_1).add(button_hor_king_2).add(button_hor_king_3).add(button_hor_king_4).add(button_back_to_author_hor).add(button_back_to_genre)

#Клавиатура с Лавкрафтом
greet_kb_hor_kraft = ReplyKeyboardMarkup()
greet_kb_hor_kraft.add(button_hor_kraft_1).add(button_hor_kraft_2).add(button_hor_kraft_3).add(button_hor_kraft_4).add(button_back_to_author_hor).add(button_back_to_genre)

#Клавиатура с По
greet_kb_hor_po = ReplyKeyboardMarkup()
greet_kb_hor_po.add(button_hor_po_1).add(button_hor_po_2).add(button_hor_po_3).add(button_hor_po_4).add(button_back_to_author_hor).add(button_back_to_genre)




#Клавиатура с триллерами
greet_kb_thril = ReplyKeyboardMarkup()
greet_kb_thril.add(button_thril_nesbe).add(button_thril_lihein).add(button_thril_grange).add(button_back_to_genre)

#Клавиатура с Несбё
greet_kb_thril_nesbe= ReplyKeyboardMarkup()
greet_kb_thril_nesbe.add(button_thril_nesbe_1).add(button_thril_nesbe_2).add(button_thril_nesbe_3).add(button_thril_nesbe_4).add(button_back_to_author_thril).add(button_back_to_genre)

#Клавиатура с Лихейном
greet_kb_thril_lihein = ReplyKeyboardMarkup()
greet_kb_thril_lihein.add(button_thril_lihein_1).add(button_thril_lihein_2).add(button_thril_lihein_3).add(button_thril_lihein_4).add(button_back_to_author_thril).add(button_back_to_genre)

#Клавиатура с Гранже
greet_kb_thril_grange = ReplyKeyboardMarkup()
greet_kb_thril_grange.add(button_thril_grange_1).add(button_thril_grange_2).add(button_thril_grange_3).add(button_thril_grange_4).add(button_back_to_author_thril).add(button_back_to_genre)



#Клавиатура с фантастикой
greet_kb_phant = ReplyKeyboardMarkup()
greet_kb_phant.add(button_phant_azimov).add(button_phant_belaev).add(button_phant_bradber).add(button_back_to_genre)

#Клавиатура с Азимовым
greet_kb_phant_azimov= ReplyKeyboardMarkup()
greet_kb_phant_azimov.add(button_phant_azimov_1).add(button_phant_azimov_2).add(button_phant_azimov_3).add(button_phant_azimov_4).add(button_back_to_author_phant).add(button_back_to_genre)

#Клавиатура с Беляевым
greet_kb_phant_belaev = ReplyKeyboardMarkup()
greet_kb_phant_belaev.add(button_phant_belaev_1).add(button_phant_belaev_2).add(button_phant_belaev_3).add(button_phant_belaev_4).add(button_back_to_author_phant).add(button_back_to_genre)

#Клавиатура с Брэдбери
greet_kb_phant_bradber = ReplyKeyboardMarkup()
greet_kb_phant_bradber.add(button_phant_bradber_1).add(button_phant_bradber_2).add(button_phant_bradber_3).add(button_phant_bradber_4).add(button_back_to_author_phant).add(button_back_to_genre)





greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_genre1).add(button_genre2).add(button_genre3)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_genre1).add(button_genre2).add(button_genre3)

