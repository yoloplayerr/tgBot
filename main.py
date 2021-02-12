from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher
from DBConnection import con,cur
from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Это книжный бот. Выберите интересующий вас жанр: ", reply_markup=kb.greet_kb)

@dp.message_handler(text=['Ужасы'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Ужасы. Выберите автора: ", reply_markup=kb.greet_kb_hor)
@dp.message_handler(text=['Стивен Кинг'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://www.kino-teatr.ru/blog/991/25163.jpg')
    await bot.send_message(message.from_user.id, text='Американский писатель, работающий в разнообразных жанрах, включая ужасы, триллер, фантастику, фэнтези, мистику, драму; получил прозвище «Король ужасов». Продано более 350 миллионов экземпляров его книг, по которым было снято множество художественных фильмов и сериалов, телевизионных постановок, а также нарисованы комиксы. Кинг опубликовал 60 романов, в том числе семь под псевдонимом Ричард Бахман, и 5 научно-популярных книг.')
    await message.reply("Выбранный автор: Стивен Кинг. Выберите книгу: ", reply_markup=kb.greet_kb_hor_king)

@dp.message_handler(text=['Говард Лавкрафт'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://3.bp.blogspot.com/-tew79URlxhs/VYbioKf1bcI/AAAAAAAA4q0/iCyVB2OO3Bc/s1600/Howard%2BPhillips%2BLovecraft%2B2.png')
    await bot.send_message(message.from_user.id, text='Американский писатель и журналист, работавший в жанрах ужасов, мистики, фэнтези и научной фантастики, совмещая их в оригинальном стиле. Его творчество уникально настолько, что произведения Лавкрафта выделяются в отдельный поджанр - так называемые лавкрафтовские ужасы. Ядро творчества Лавкрафта составляют мифы Ктулху - произведения, объединённые своеобразной общей мифологией')
    await message.reply("Выбранный автор: Говард Лавкрафт. Выберите книгу: ", reply_markup=kb.greet_kb_hor_kraft)
@dp.message_handler(text=['Эдгар По'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://klimbim2014.files.wordpress.com/2019/06/poe-publicity-15_poe-whitman-daguerreotype-color.jpg')
    await bot.send_message(message.from_user.id, text='Американский писатель, поэт, эссеист, литературный критик и редактор, представитель американского романтизма. Создатель формы классического детектива и жанра психологической прозы. Некоторые работы Эдгара По способствовали формированию и развитию научной фантастики, а такие черты его творчества, как иррациональность, мистицизм, обречённость, аномальность изображаемых состояний, предвосхитили литературу декадентства. Наиболее известен как автор «страшных» и мистических рассказов, а также стихотворения «Ворон».')
    await message.reply("Выбранный автор: Эдгар По. Выберите книгу: ", reply_markup=kb.greet_kb_hor_po)

@dp.message_handler(text=['К выбору жанра'])
async def process_start_command(message: types.Message):
    await message.reply("Выберите интересующий вас жанр: ", reply_markup=kb.greet_kb)


@dp.message_handler(text=['К выбору автора в жанре: Ужасы'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Ужасы. Выберите автора: ", reply_markup=kb.greet_kb_hor)
@dp.message_handler(text=['К выбору автора в жанре: Триллер'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Триллер. Выберите автора: ", reply_markup=kb.greet_kb_thril)
@dp.message_handler(text=['К выбору автора в жанре: Фантастика'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Фантастика. Выберите автора: ", reply_markup=kb.greet_kb_phant)





@dp.message_handler(text=['Триллер'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Триллер. Выберите автора: ", reply_markup=kb.greet_kb_thril)

@dp.message_handler(text=['Ю Несбё'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://24smi.org/public/media/celebrity/2017/11/20/cxwylhhkvldd-iu-nesbe.jpg')
    await bot.send_message(message.from_user.id, text='Норвежский писатель и музыкант, бывший экономист и журналист. Обладатель нескольких литературных премий.Известность ему принесли детективные романы об инспекторе Харри Холе. Он также является автором детских книг о докторе Прокторе.')
    await message.reply("Выбранный автор: Ю Несбё. Выберите книгу: ", reply_markup=kb.greet_kb_thril_nesbe)

@dp.message_handler(text=['Деннис Лихейн'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://sun1-84.userapi.com/AaE3xb_j3oREIiIZwfrOiWJmnU_ITj-TYO-raQ/PPoGa2PXCvY.jpg')
    await bot.send_message(message.from_user.id, text='Американский писатель и сценарист, автор детективов и триллеров, получивший известность благодаря романам «Таинственная река», «Остров проклятых» и циклу «Патрик Кензи и Энджи Дженнаро».')
    await message.reply("Выбранный автор: Деннис Лихейн. Выберите книгу: ", reply_markup=kb.greet_kb_thril_lihein)
@dp.message_handler(text=['Жан-Кристоф Гранже'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://i.livelib.ru/auface/024007/o/1091/ZhanKristof_Granzhe.jpg')
    await bot.send_message(message.from_user.id, text='Французский писатель и сценарист. Долгое время в качестве журналиста-фрилансера сотрудничал со многими известными периодическими изданиями. Свой журналистский опыт Гранже использовал в написании романов, которые, являясь по жанру остросюжетными детективами, часто затрагивают сложные темы международного терроризма, политического экстремизма, сомнительную деятельность оккультных организаций.')
    await message.reply("Выбранный автор: Жан-Кристоф Гранже. Выберите книгу: ", reply_markup=kb.greet_kb_thril_grange)



@dp.message_handler(text=['Фантастика'])
async def process_start_command(message: types.Message):
    await message.reply("Выбранный жанр: Фантастика. Выберите автора: ", reply_markup=kb.greet_kb_phant)

@dp.message_handler(text=['Айзек Азимов'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://www.culture.ru/storage/images/2253383b406f09f19a347cf9b3786154/90f05c1c22f277f2fd77c63155b92bb4.jpeg')
    await bot.send_message(message.from_user.id, text='Американский писатель-фантаст, популяризатор науки, биохимик. Автор около 500 произведений, в основном художественных и научно-популярных. Многократный лауреат премий «Хьюго» и «Небьюла». Некоторые термины из его произведений - robotics, positronic, psychohistory - прочно вошли в английский и другие языки. В англо-американской литературной традиции Айзека Азимова вместе с Артуром Кларком и Робертом Хайнлайном относят к «Большой тройке» писателей-фантастов.')
    await message.reply("Выбранный автор: Айзек Азимов. Выберите книгу: ", reply_markup=kb.greet_kb_phant_azimov)

@dp.message_handler(text=['Александр Беляев'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://www.culture.ru/storage/images/8176c31ac62464b7abae651764dff3fe/363f39649e690f4dc2d6ca184ab8d1d3.jpg')
    await bot.send_message(message.from_user.id, text='Русский и советский писатель-фантаст, репортёр, юрист. Один из основоположников советской научно-фантастической литературы, первый из советских писателей, целиком посвятивший себя этому жанру. Среди наиболее известных его романов: «Голова профессора Доуэля», «Человек-амфибия», «Ариэль», «Звезда КЭЦ» и многие другие. За значительный вклад в русскую фантастику и провидческие идеи Беляева называют «русским Жюлем Верном».')
    await message.reply("Выбранный автор: Александр Беляев. Выберите книгу: ", reply_markup=kb.greet_kb_phant_belaev)
@dp.message_handler(text=['Рэй Брэдбери'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://persons-info.com/userfiles/image/persons/0-10000/4000-5000/4394/BREDBERI_Rei_Duglas5.jpg')
    await bot.send_message(message.from_user.id, text='Американский писатель, известный по антиутопии «451 градус по Фаренгейту», циклу рассказов «Марсианские хроники» и частично автобиографической повести «Вино из одуванчиков». Брэдбери создал более восьмисот литературных произведений, в том числе несколько романов и повестей, сотни рассказов, десятки пьес, ряд статей, заметок и стихотворений.')
    await message.reply("Выбранный автор: Рэй Брэдбери. Выберите книгу: ", reply_markup=kb.greet_kb_phant_bradber)






#####Для книг
@dp.message_handler(text=['Жребий Салема'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://i.pinimg.com/736x/09/78/ce/0978ceda3e5e5eac7a3cb67b65a1b0a4--catalog-book.jpg')
    await bot.send_message(message.from_user.id,text='Все началось с того, что в провинциальном американском городке стали пропадать люди - поодиночке и целыми семьями. Их не могли найти ни родственники, ни даже полиция. А когда надежда, казалось, исчезла навсегда, пропавшие вернулись, и городок содрогнулся от ужаса...')
    await bot.send_message(message.from_user.id,
                         text='https://online-knigi.com.ua/page/14169')
    await message.reply("Вы выбрали книгу: Жребий Салема")
    cur.execute("INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Стивен Кинг','Жребий салема')")
    con.commit()



@dp.message_handler(text=['Оно'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cdn1.ozone.ru/s3/multimedia-o/6009443400.jpg')
    await bot.send_message(message.from_user.id,text='В маленьком провинциальном городке Дерри много лет назад семерым подросткам пришлось столкнуться с кромешным ужасом - живым воплощением ада.Прошли годы... Подростки повзрослели, и ничто, казалось, не предвещало новой беды. Но кошмар прошлого вернулся, неведомая сила повлекла семерых друзей назад, в новую битву со Злом. Ибо в Дерри опять льется кровь и бесследно исчезают люди. Ибо вернулось порождение ночного кошмара, настолько невероятное, что даже не имеет имени...')
    await bot.send_message(message.from_user.id,
                         text='https://www.mnogobook.ru/fantastika/ujasyi/323125/fulltext.htm')
    await message.reply("Вы выбрали книгу: Оно")
    cur.execute("INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Стивен Кинг','Оно')")
    con.commit()

@dp.message_handler(text=['Кладбище домашних животных'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://horrorzone.ru/uploads/_books/42146/89437.jpg')
    await bot.send_message(message.from_user.id,text='Казалось бы, семейство Крид - это настоящее воплощение "американской мечты": отец - преуспевающий врач, красавица мать, прелестные дети. Для полной идиллии им не хватает лишь большого старинного дома, куда они вскоре и переезжают.Но идиллия вдруг стала превращаться в кошмар. Потому что в окружающих их новое жилище вековых лесах скрывается НЕЧТО, более ужасное, чем сама смерть и… более могущественное.')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_399241-1')
    await message.reply("Вы выбрали книгу: Кладбище домашних животных")
    cur.execute("INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Стивен Кинг','Кладбище домашних животных')")
    con.commit()
@dp.message_handler(text=['Мистер Мерседес'])
async def process_start_command(message: types.Message):
        await bot.send_photo(message.from_user.id,
                             'https://cdn1.ozone.ru/s3/multimedia-6/6008243610.jpg')
        await bot.send_message(message.from_user.id,
                               text='Восемь убитых и пятнадцать раненых на счету бесследно исчезнувшего убийцы, протаранившего на "мерседесе" ни в чем не повинных людей…Стивен Кинг написал триллер, который заставит вас в ужасе оглядываться на каждый проезжающий мимо "мерседес" и совершенно по-другому смотреть на людей, с которыми вы сталкиваетесь каждый день.Кто знает, какие жуткие тайны скрываются за соседней дверью и кто хочет свести счеты именно с вами?..')
        await bot.send_message(message.from_user.id,
                               text='https://mir-knig.com/read_94759-1')
        await message.reply("Вы выбрали книгу: Мистер Мерседес")
        cur.execute(
            "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Стивен Кинг','Мистер Мерседес')")
        con.commit()


@dp.message_handler(text=['Зов Ктулху'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://7books.ru/wp-content/uploads/2019/04/Zov-Ktulkhu-sbornik22680358.jpg')
    await bot.send_message(message.from_user.id,text='Дагон, Ктулху, Йог-Сотот и многие другие темные божества, придуманные Говардом Лавкрафтом в 1920-е годы, приобрели впоследствии такую популярность, что сотни творцов фантастики, включая Нила Геймана и Стивена Кинга, до сих пор продолжают расширять его мифологию. Каждое монструозное божество в лавкрафтианском пантеоне олицетворяет собой одну из бесчисленных граней хаоса. Таящиеся в глубинах океана или пребывающие в глубине непроходимых лесов, спящие в египетских пирамидах или замурованные в горных пещерах, явившиеся на нашу планету со звезд или из бездны неисчислимых веков, они неизменно враждебны человечеству и неподвластны разуму. И единственное, что остается человеку - это всячески избегать столкновения с этими таинственными существами и держаться настороже…')
    await bot.send_message(message.from_user.id,
                           text='https://online-knigi.com.ua/page/177322')
    await message.reply("Вы выбрали книгу: Зов Ктулху")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Говард Лавкрафт','Зов Ктулху')")
    con.commit()

@dp.message_handler(text=['Тень над Иннсмутом'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://zakznaet.ru/wp-content/uploads/2017/07/382977-1.jpg')
    await bot.send_message(message.from_user.id,text='Иннсмут, маленький рыбацкий городок неподалеку от Аркхэма, уже много лет имеет дурную славу. В округе ходят жуткие истории о его угрюмых и уродливых жителях, от которых лучше держаться подальше. Немногое связывает город с окружающим миром: туда ходит лишь один полуразвалившийся автобус с вызывающим отвращение водителем, и горе тому, кто решится в него сесть.')
    await bot.send_message(message.from_user.id,
                           text='https://lovecraftian.ru/g-f-lavkraft-ten-nad-innsmutom/')
    await message.reply("Вы выбрали книгу: Тень над Иннсмутом")
    await bot.send_message(message.from_user.id,'https://surik00.gitbooks.io/aiogram-lessons/content/chapter2.html')
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Говард Лавкрафт','Тень над Иннсмутом')")
    con.commit()
@dp.message_handler(text=['Хребты безумия'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://g.pggcdn.net/product/1572668754537424115/w720/Хребты-безумия.jpg')
    await bot.send_message(message.from_user.id,text='«Хребты безумия» написаны в документальной манере повествования, постепенно привыкая к которой, становишься свидетелем особой реальности описываемых событий. Полярная экспедиция сталкивается с запредельным ужасом древних веков. Лучшее кошмарно-прекрасно-завораживающее описание в творчестве Лавкрафта запечатлено именно в этом произведении. Это описание заброшенного ледяного города «древних», уводящего в недра земли.')
    await bot.send_message(message.from_user.id,
                           text='https://lovecraftian.ru/g-f-lavkraft-hrebty-bezumija/')
    await message.reply("Вы выбрали книгу: Хребты безумия")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Говард Лавкрафт','Хребты безумия')")
    con.commit()
@dp.message_handler(text=['Ужас Данвича'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://static-sl.insales.ru/images/products/1/6277/118732933/ITD000000000862242-05.jpg')
    await bot.send_message(message.from_user.id,text='В Данвиче происходят таинственные события: кто-то зверски убивает животных и даже людей. Невидимое существо, гость из другого мира, внушает ужас местным жителям. Что же им делать? Забыть всё и просто уехать? А если бежать некуда? Группа смельчаков решает остановить дьявольскую тварь.')
    await bot.send_message(message.from_user.id,
                           text='https://lovecraftian.ru/g-f-lavkraft-uzhas-danvicha/')
    await message.reply("Вы выбрали книгу: Ужас Данвича")

    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Говард Лавкрафт','Ужас Данвича')")
    con.commit()

@dp.message_handler(text=['Падение дома Ашеров'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv1.litres.ru/pub/c/bumajnaya-kniga/cover_max1500/16319611-edgar-po-padenie-doma-asherov-po-edgar-allan-16319611.jpg')
    await bot.send_message(message.from_user.id,text='Родерик Ашер, последний отпрыск древнего рода, приглашает друга юности навестить его и погостить в фамильном замке на берегу мрачного озера. Леди Мэдилейн, сестра Родерика тяжело и безнадежно больна, дни её сочтены и даже приезд друга не в состоянии рассеять печаль Ашера.После смерти Мэдилейн местом её временного погребения выбирается одно из подземелий замка. В течение нескольких дней Родерик пребывал в смятении, пока ночью не разразилась буря и не выяснилось одно чудовищное обстоятельство...')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_69304-1')
    await message.reply("Вы выбрали книгу: Падение дома Ашеров")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Эдгар По','Падение дома Ашеров')")
    con.commit()

@dp.message_handler(text=['Золотой жук'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv3.litres.ru/pub/c/bumajnaya-kniga/cover_max1500/41443734-avtor-zolotoy-zhuk-41443734.jpg')
    await bot.send_message(message.from_user.id,text='История о сокровищах, ключ к местонахождению которых был зашифрован. Один из героев сумел разгадать его, используя остроумную систему подсчета знаков шифра и сопоставление с частотой использования букв в английском языке.')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_162923-1')
    await message.reply("Вы выбрали книгу: Золотой жук")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Эдгар По','Золотой жук')")
    con.commit()

@dp.message_handler(text=['Маска красной смерти'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv3.litres.ru/pub/c/bumajnaya-kniga/cover_max1500/49043032-edgar-po-maska-krasnoy-smerti-49043032.jpg')
    await bot.send_message(message.from_user.id,text='Принц Просперо с тысячей приближенных во время эпидемии скрывается в закрытом монастыре, бросив своих подданных на произвол судьбы. Монастырь всем обеспечен и изолирован, поэтому они могут не бояться заразы. Устроенный принцем бал-маскарад, настолько великолепен, что в нем приходит участвовать сама Красная Смерть...')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_342127-1')
    await message.reply("Вы выбрали книгу: Маска красной смерти")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Эдгар По','Маска красной смерти')")
    con.commit()
@dp.message_handler(text=['Лигейя'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://kbimages1-a.akamaihd.net/e8cf43a9-e64d-454d-9771-8d5a4e124144/1200/1200/False/NY0JaNDfkjqdgsPoFv-LJg.jpg')
    await bot.send_message(message.from_user.id,text='Счастье и радость дарит герою леди Лигейя — друг, помощник и возлюбленная супруга. Однако злой рок уносит её трепетную жизнь и горе приходит в дом.Второй брак оказался недолгим и молодая жена Ровена, внезапно сраженная неизвестным недугом, медленно и тихо угасает. Но окончания страданий нашему герою это не приносит...')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_62132-1')
    await message.reply("Вы выбрали книгу: Лигейя")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Ужасы','Эдгар По','Лигейя')")
    con.commit()

@dp.message_handler(text=['Снеговик'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://interkniga.net/app/files/2019/01/978-5-389-04992-5.jpg')
    await bot.send_message(message.from_user.id,text='Поистине в первом снеге есть что-то колдовское. Он сводит любовников, заглушает звуки, удлиняет тени, скрывает следы. Разыскивая пропавшую Бирту Беккер, Харри Холе приходит к выводу, что годами в Норвегии в тот день, когда выпадает первый снег, бесследно исчезают замужние женщины.Впервые Харри сталкивается с серийным убийцей на своей родной земле. Преступник, которому газеты дали прозвище Снеговик, будто дразнит старшего инспектора, доводя его до последней грани безумия...')
    await bot.send_message(message.from_user.id,
                           text='https://litgroup.info/read/?book=952')
    await message.reply("Вы выбрали книгу: Снеговик")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Ю Несбё','Снеговик')")
    con.commit()

@dp.message_handler(text=['Нетопырь'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv7.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/162774-u-nesbe-netopyr.jpg')
    await bot.send_message(message.from_user.id,text='Харри Холе прилетает в Сидней, чтобы помочь в расследовании зверского убийства норвежской подданной. Австралийская полиция не принимает его всерьез, а между тем дело гораздо сложнее, чем может показаться на первый взгляд. Древние легенды аборигенов оживают, дух смерти распростер над землей черные крылья летучей мыши, и Харри, подобно герою, победившему страшного змея Буббура, предстоит вступить в схватку с коварным врагом, чтобы одолеть зло и отомстить за смерть возлюбленной. Это дело станет для Харри началом его несколько эксцентрической полицейской карьеры, а для его создателя, Ю.Несбе, — первым шагом навстречу головокружительной мировой славе.')
    await bot.send_message(message.from_user.id,
                           text='https://booksread.com.ua/read/netopyr')
    await message.reply("Вы выбрали книгу: Нетопырь")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Ю Несбё','Нетопырь')")
    con.commit()

@dp.message_handler(text=['Призрак'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'http://audio-knigki.ru/uploads/posts/2014-09/1410276541_o72lfgzs0vkdcrk.jpg')
    await bot.send_message(message.from_user.id,text='После трехлетнего отсутствия бывший полицейский Харри Холе возвращается в Норвегию, чтобы расследовать еще одно убийство. На этот раз им движут глубоко личные мотивы: обвиняемый — сын его прежней возлюбленной Ракели. Харри знал Олега еще ребенком и теперь готов разбиться в лепешку, чтобы доказать его невиновность. Поскольку убитый был наркодилером, Харри начинает поиски в этом направлении. В ходе своего неофициального расследования он узнает о существовании таинственного человека, заправляющего местной наркосетью. Его имени никто не знает. Он появляется из ниоткуда, как призрак, дает указания, казнит и милует, а затем вновь исчезает. Его помощники действуют жестко и убивают не задумываясь. Харри понимает, что, только подобравшись к этому зловещему «призраку», он сумеет помочь Олегу...')
    await bot.send_message(message.from_user.id,
                           text='https://booksread.com.ua/read/prizrak')
    await message.reply("Вы выбрали книгу: Призрак")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Ю Несбё','Призрак')")
    con.commit()

@dp.message_handler(text=['Леопард'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv5.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/4578359-u-nesbe-leopard.jpg')
    await bot.send_message(message.from_user.id,text='В Осло обнаружены трупы двух молодых женщин, умерщвленных с помощью неизвестного орудия. Безжалостный убийца подкрадывается к своим жертвам бесшумно, как леопард, отнимая у них жизнь с изощренной жестокостью. Следствие топчется на месте, и Харри Холе вызывают из бессрочного отпуска. Пока полицейское начальство пытается использовать его в межведомственной борьбе, измученному охотнику предстоит пройти долгий путь по кровавому следу хищника.')
    await bot.send_message(message.from_user.id,
                           text='https://litgroup.info/read/?book=4395')
    await message.reply("Вы выбрали книгу: Леопард")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Ю Несбё','Леопард')")
    con.commit()

@dp.message_handler(text=['Остров проклятых'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cdn1.ozone.ru/multimedia/1005448901.jpg')
    await bot.send_message(message.from_user.id,text='Накануне урагана два судебных пристава прибывают в клинику «Эшклиф» для опасных невменяемых преступников, которая находится на одиноком острове. Сбежала преступница — убийца троих детей. Только вот приставы обнаруживают, что никто их не звал на остров, да и сбежавшая,возможно, никуда и не сбегала, а тайна и истина для них в равной степени становится опасной.')
    await bot.send_message(message.from_user.id,
                           text='https://www.mnogobook.ru/detektiyi_i_trilleryi/triller/306416/fulltext.htm')
    await message.reply("Вы выбрали книгу: Остров проклятых")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Деннис Лихейн','Остров проклятых')")
    con.commit()
@dp.message_handler(text=['Таинственная река'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv2.litres.ru/pub/c/cover/127486.jpg')
    await bot.send_message(message.from_user.id,text='К трем маленьким приятелям, Шону, Джимми и Дейву, озорничающим на улице, подъезжают два мнимых полицейских и увозят в своей машине самого слабого и беззащитного из них — Дейва. Через несколько дней мальчик убегает от похитителей и возвращается домой, но эта история оставляет рубец в душе каждого из ее участников и через двадцать пять лет вновь сводит их вместе в чудовищном кошмаре.')
    await bot.send_message(message.from_user.id,
                           text='https://libking.ru/books/det-/thriller/213797-dennis-leheyn-tainstvennaya-reka.html')
    await message.reply("Вы выбрали книгу: Таинственная река")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Деннис Лихейн','Таинственная река')")
    con.commit()
@dp.message_handler(text=['Общак'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://handmade.minemegashop.ru/pictures/1010904950.jpg')
    await bot.send_message(message.from_user.id,text='Почти двадцать лет Боб Сагиновски стоял за стойкой бара - каждый день с четырех дня до двух ночи - "странноватый, одинокий Боб-бармен", человек с темным прошлым, погруженный в воспоминания, почти потерявший надежду обрести простое человеческое счастье. Перемены всегда наступают неожиданно. Размеренная жизнь Боба стремительно разворачивается в бурную кинодраму, участниками которой становятся грабители, покусившиеся на воровской "Общак", чеченские бандиты, любопытный коп-пуэрториканец и сумасшедший шантажист, вообразивший себя суперменом. А также загадочная девушка Надя. Но все началось с того, что на третий день после Рождества в баке для мусора Боб нашел собаку…')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_377007-1')
    await message.reply("Вы выбрали книгу: Общак")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Деннис Лихейн','Общак')")
    con.commit()
@dp.message_handler(text=['Когда под ногами бездна'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://bookbear.net/thumb/work/big/?src=1337348137383')
    await bot.send_message(message.from_user.id,text='Итак, познакомьтесь с Рейчел Чайлдс. Бывшая журналистка, она ушла из профессии после скандального срыва в прямом эфире и теперь живет затворницей; а в остальном это идеальная жизнь с идеальным мужем — пока случайная встреча не заставляет Рейчел усомниться во всем, что ее окружает, а то и в собственном рассудке. Хватит ли ей внутренних сил, чтобы совладать с невообразимыми страхами и немыслимой правдой?')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_287529-1')
    await message.reply("Вы выбрали книгу: Когда под ногами бездна")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Деннис Лихейн','Когда под ногами бездна')")
    con.commit()

@dp.message_handler(text=['Багровые реки'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv3.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/119038-zhan-kristof-granzhe-bagrovye-reki.jpg')
    await bot.send_message(message.from_user.id,text='В маленький университетский городок Гернон прибывает комиссар Пьер Ньеман из Парижа — расследовать жестокое убийство библиотекаря, которому удалили глаза после пыток и засунули в расщелину скалы. Однако это лишь первое убийство в кровавой цепочке.Параллельно, в городке Сарзак, который расположен за 250 км от Гернона, офицер полиции Карим Абдуф расследует небольшое дело о взломе школы и осквернении могилы маленького мальчика, который умер 14 лет назад. Расследование приводит его в Гернон, где все звенья складываются в одну долгую цепь ужаса.')
    await bot.send_message(message.from_user.id,
                           text='https://online-knigi.com.ua/page/10728')
    await message.reply("Вы выбрали книгу: Багровые реки")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Жан-Кристоф Гранже','Багровые реки')")
    con.commit()

@dp.message_handler(text=['Пассажир'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv9.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/6028898-zhan-kristof-granzhe-passazhir.jpg')
    await bot.send_message(message.from_user.id,text='Встреча с пациентом, страдающим амнезией, приводит психиатра Матиаса Фрера к ужасному открытию: у него тот же синдром «пассажира без багажа». Раз за разом он теряет память и из осколков прошлого создает себе новую личность. Чтобы обрести свое подлинное «я», ему придется пройти через все свои прежние ипостаси. Фрера преследуют загадочные убийцы в черном, за ним гонится полиция, убежденная, что именно он — серийный маньяк, совершивший жуткие убийства, имитирующие древнегреческие мифы. Да он и сам не уверен в своей невиновности… Как ему выбраться из этого лабиринта? Быть может, лейтенант полиции Анаис Шатле, для которой он — главный подозреваемый, дарует ему путеводную нить?')
    await bot.send_message(message.from_user.id,
                           text='https://online-knigi.com.ua/page/148018')
    await message.reply("Вы выбрали книгу: Пассажир")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Жан-Кристоф Гранже','Пассажир')")
    con.commit()

@dp.message_handler(text=['Присягнувшие тьме'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cdn1.ozone.ru/multimedia/1010369695.jpg')
    await bot.send_message(message.from_user.id,text='Сотрудник уголовного розыска Матье Дюрей узнает, что его лучший друг Люк, тоже полицейский, пытался покончить с собой. Вскоре Дюрей выясняет, что Люк тайно расследовал серию убийств, совершенных в разных уголках Европы. Убийцы неизвестным способом управляют процессами разложения трупов, к тому же их преступления объединяет сатанинская символика. В прошлом все убийцы пережили клиническую смерть или кому. Шаг за шагом Матье открывает невероятную истину: преступники служат дьяволу, вернувшему их к жизни.')
    await bot.send_message(message.from_user.id,
                           text='https://knizhnik.org/zhan-kristof-granzhe/prisjagnuvshie-tme/1')
    await message.reply("Вы выбрали книгу: Присягнувшие тьме")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Жан-Кристоф Гранже','Присягнувшие тьме')")
    con.commit()

@dp.message_handler(text=['Чёрная линия'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv5.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/141451-zhan-kristof-granzhe-chernaya-liniya.jpg')
    await bot.send_message(message.from_user.id,text='В Юго-Восточной Азии жестоко убита девушка, датская туристка, — ее изуродованный труп обнаруживают в хижине, где живет в уединении бывший чемпион мира по дайвингу Жак Реверди. Однажды спортсмена уже подозревали в тяжком преступлении, но освободили за недостатком улик. Реверди упорно молчит, и его помещают в психиатрическую лечебницу. Заинтересовавшись личностью предполагаемого убийцы, журналист Марк Дюпейра затевает жестокий эксперимент: он начинает писать подозреваемому письма от имени юной наивной девушки, пытаясь вызвать его на откровенность.')
    await bot.send_message(message.from_user.id,
                           text='https://libbox.club/books/chernaya-liniya')
    await message.reply("Вы выбрали книгу: Чёрная линия")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Триллер','Жан-Кристоф Гранже','Чёрная линия')")
    con.commit()

@dp.message_handler(text=['Основание'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://toposrednik.ru/wp-content/uploads/2020/11/matematika-2.jpg')
    await bot.send_message(message.from_user.id,text='Великий План Гэри Селдона предвещал упадок империи через пятьсот лет. Это — неизбежность. Это — инертный процесс, в котором участвуют все население Галактики, действия отдельных людей в котором не сравнить даже с комариным укусом для слона.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/azimov_ayzek-osnovanie-49563.html#p1')
    await message.reply("Вы выбрали книгу: Основание")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Айзек Азимов','Основание')")
    con.commit()

@dp.message_handler(text=['Конец вечности'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv0.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/122306-ayzek-azimov-konec-vechnosti-122306.jpg')
    await bot.send_message(message.from_user.id,text='«Вечность» — организация, возникшая в 27 столетии как структура для межвременной торговли, а потом переросшая в инструмент управления целыми эпохами... Миллионы веков с миллиардами человеческих душ, которые могут исчезнуть в мгновение ока по воле Вечных. Так бы и продолжалось дальше, если бы с Техником по имени Эндрю Харлан не стали происходить довольно странные вещи, описанные в романе...')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/azimov_isaac-konec_vechnosti-230496.html#p1')
    await message.reply("Вы выбрали книгу: Конец вечности")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Айзек Азимов','Конец вечности')")
    con.commit()

@dp.message_handler(text=['Сами боги'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://forteacher.minemshop.ru/images/1014962729.jpg')
    await bot.send_message(message.from_user.id,text='Фридрих Шиллер — «Против глупости сами Боги бессильны». Две Вселенных. Два мира, угасающий — и полный сил. Величайшее открытие в истории человечества дарит людям неисчерпаемый источник дешевой энергии. И надежду на спасение умирающему миру. Голоса, предупреждающие об опасности — мстительность и людская зависть? Гениальные умы, но всего лишь люди. Невероятный мир удивительных, непохожих на нас, существ. Уникальная фантазия Айзека Азимова, Гроссмейстера научной фантастики.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/azimov_ayzek-sami_bogi-49591.html#p1')
    await message.reply("Вы выбрали книгу: Сами боги")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Айзек Азимов','Сами боги')")
    con.commit()

@dp.message_handler(text=['Двухсотлетний человек'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://www.cibum.ru/assets/books/32/2302681/book.jpg')
    await bot.send_message(message.from_user.id,text='Семья Мартинов, приобретшая робота Эндрю, вскоре обнаруживает у него выдающиеся способности к творчеству. Через некоторое время Эндрю начинает продавать свои работы, деля прибыль между собой и семьей Мартинов. У него появляется счет в банке, он сам себя обеспечивает, но этого мало... Эндрю хочет быть свободным. И он становится таковым, с каждым днем становясь все больше и больше похожим на человека.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/azimov_ayzek-dvuhsotletniy_chelovek-250004.html#p1')
    await message.reply("Вы выбрали книгу: Двухсотлетний человек")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Айзек Азимов','Двухсотлетний человек')")
    con.commit()


@dp.message_handler(text=['Голова профессора Доуэля'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://upload-7df14150aa387ef737992a43afb5ffe5.hb.bizmrg.com/iblock/325/325fb1684ab0d80fc210d191a72c370f/d19d24b5e2b8df888fe2bfa843684ad6.jpg')
    await bot.send_message(message.from_user.id,text='Профессор Керн проводит в своей лаборатории эксперименты по оживлению органов, отделенных от человеческого тела. Пренебрегая морально-этическими принципами поведения врача, для достижения личных, эгоистических целей он не останавливается ни перед чем…')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/belyaev_aleksandr-golova_professora_douelya-3386.html#p1')
    await message.reply("Вы выбрали книгу: Голова профессора Доуэля")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Александр Беляев','Голова профессора Доуэля')")
    con.commit()


@dp.message_handler(text=['Остров погибших кораблей'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://skidka-samara.ru/images/prodacts/sourse/61750/61750113_ostrov-pogibshih-korabley-ast.jpg')
    await bot.send_message(message.from_user.id,text='В Атлантическом океане, в районе Бермудских островов образовалось скопление саргассовых водорослей. Эти водоросли расположены настолько плотно, что все суда, попадающие в скопление, остаются в нем навсегда. Вместе с людьми, находящимися на борту, попадают в это скопление и герои книги.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/belyaev_aleksandr-ostrov_pogibshih_korabley-54600.html#p1')
    await message.reply("Вы выбрали книгу: Остров погибших кораблей")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Александр Беляев','Остров погибших кораблей')")
    con.commit()

@dp.message_handler(text=['Ариэль'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://fantasticbook.ru/pict/1015846601.jpg')
    await bot.send_message(message.from_user.id,text='Неподалеку от Мадраса, где расположилась таинственная школа Дандарат, великий, но не признанный ученый доктор Хайд изобретает средство, при помощи которого человек может летать без всякого технического устройства.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/belyaev_aleksandr-ariel-3384.html#p1')
    await message.reply("Вы выбрали книгу: Ариэль")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Александр Беляев','Ариэль')")
    con.commit()

@dp.message_handler(text=['Небесный гость'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://kbimages1-a.akamaihd.net/f3ec7be7-f557-4b65-9dd8-c8655b62ef81/1200/1200/False/Ll27bZMTPzKzRXGpndgLYQ.jpg')
    await bot.send_message(message.from_user.id,text='Тюменев открыл двойную звезду, которая должна пролететь в непосредственной близости от Солнечной системы. Когда она пройдет в наиближайшем расстоянии от Земли то оторвет часть земной атмосферы и несколько тысяч кубических километров океанской воды, которые должны упасть на одну из планет этой звезды. Его друг академик Шипольский сконструировал аппарат для глубоководных экспедиций, который прочнее межпланетной ракеты и если его поместить в рассчитанном месте океана, то можно достичь небесной гостьи. Это путешествие во славу науки в один конец…')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/belyaev_aleksandr-nebesnyy_gost-250506.html#p1')
    await message.reply("Вы выбрали книгу: Небесный гость")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Александр Беляев','Небесный гость')")
    con.commit()

@dp.message_handler(text=['451 градус по Фаренгейту'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://russkiypro.ru/wp-content/uploads/2020/09/kniga10.jpg')
    await bot.send_message(message.from_user.id,text='451 градус по Фаренгейту — температура, при которой воспламеняется и горит бумага. Главный герой — Монтэг — пожарник, но смысл этой профессии давно изменился. Дома теперь строятся из термостойких сплавов, а пожарники занимаются тем, что сжигают книги. Не произведения определенных авторов — запрещена литература вообще и люди, хранящие и читающие книги, совершают преступление против государства. Бессмысленные развлечения, успокоительные таблетки, выматывающая работа — вот и все занятия человека.Уставший от такой жизни Монтэг прочитывает первую свою книгу.')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_100663-1')
    await message.reply("Вы выбрали книгу: 451 градус по Фаренгейту")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Рэй Брэдбери','451 градус по Фаренгейту')")
    con.commit()

@dp.message_handler(text=['Марсианские хроники'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://fkniga.ru/media/product/cat4805n/n16060205/KA-00157117.jpg')
    await bot.send_message(message.from_user.id,text='Первые шаги освоения Марса... Первый контакт с внеземной цивилизацией...Рассказы-хроники, составляющие роман, наполненные авторскими размышлениями по характерным вопросам существования человечества. За конкретными сюжетными ситуациями встают общие явления цивилизации землян, их тревоги и надежды перед лицом завтрашнего дня')
    await bot.send_message(message.from_user.id,
                           text='https://libbox.club/books/marsianskie-xroniki')
    await message.reply("Вы выбрали книгу: Марсианские хроники")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Рэй Брэдбери','Марсианские хроники')")
    con.commit()
@dp.message_handler(text=['Человек в картинках'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://cv2.litres.ru/pub/c/elektronnaya-kniga/cover_max1500/125628-rey-bredberi-chelovek-v-kartinkah.jpg')
    await bot.send_message(message.from_user.id,text='В такую жару на нём была наглухо застёгнутая шерстяная рубашка. А под рубашкой всегда они, картинки. Как мне их описать? Если бы Эль Греко в расцвете сил и таланта писал миниатюры... Стоп. Я кажется повторяю слова мастера. Ничего не поделаешь, — сказать об этом лучше автора выше моих сил. Скажу лишь, что я не разделяю взгляды главного героя на смертную казнь путём отмщения. За что мстить, спросите вы? Посмотрел бы я на вас, когда б вас расписали, точно ярмарочную игрушку, живыми катренами Нострадамуса. Расписали, а сами удрали в будущее.')
    await bot.send_message(message.from_user.id,
                           text='https://bookscafe.net/read/bredberi_rey-chelovek_v_kartinkah-78626.html#p1')
    await message.reply("Вы выбрали книгу: Человек в картинках")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Рэй Брэдбери','Человек в картинках')")
    con.commit()
@dp.message_handler(text=['Надвигается беда'])
async def process_start_command(message: types.Message):
    await bot.send_photo(message.from_user.id,'https://top10a.ru/wp-content/uploads/2019/11/10-15.jpg')
    await bot.send_message(message.from_user.id,text='Жизнь, в сущности, довольно скучное дело. Обыденное. Иногда даже неунывающие мальчишки изменяют своему обычному оптимизму и скучают.Другое дело — карнавал! Здесь каждому найдется развлечение по душе. Карнавал может воплотить самые потаенные мечты.А если вдруг Ему это не удастся — то Он возьмется за самые тайные страхи.Но кто будет сопротивляться, если ему предложат исполнение желаний, сейчас, немедленно, и даже не заикаясь о плате?')
    await bot.send_message(message.from_user.id,
                           text='https://mir-knig.com/read_420426-1')
    await message.reply("Вы выбрали книгу: Надвигается беда")
    cur.execute(
        "INSERT INTO  logirovanie(genre,author,book) values ('Фантастика','Рэй Брэдбери','Надвигается беда')")
    con.commit()























@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры",
                        reply_markup=kb.greet_kb1)


help_message = text(
    "Приветствуем вас в меню помощи книжного бота! Данный бот дает представление о самых популярных писателях в жанрах: Ужасы, Триллер, Фантастика, а также о самых популярных авторах в данных жанрах и их наиболее популярных произведениях"
    "Чтобы получить интересующую вас информацию, нажимайте соответствующие кнопки в меню выбора."
    "/start - начать работу"
    "/help - получить информацию о боте"

)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


if __name__ == '__main__':
    executor.start_polling(dp)