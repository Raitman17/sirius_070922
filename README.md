# Вопросы:

- Fast api
  - Что такое Middleware / Depends? Для чего? Как реализуется? 
  - Что такое gunicorn / uvicorn? Как правильно запускать Fast api на нескольких worker
  - Что такое lifespan? Когда отрабатывает код после yield?
  - Зачем нужен exec в startup.sh? Что будет если его убрать?
  - Как работают соединения к базе? Что такое Null Pool, какие альтернативы?
  - Где хранить настройки(конфиги) приложения? Какие удобные инструменты для этого?
  - Какая разница между аутентификацией и авторизацией? Как работает jwt?
- Docker
  - Что такое image?
  - Что такое слои image?
  - Что такое volume?
  - Что такое container?
  - Что такое ports?
  - Как вести разработку с докером, не пересобирая Image?
  - Что такое healthcheck?
- Telegram
  - Разница работы polling и webhook
  - Уметь рассказать как правильно организовать работы webhook
  - Что такое State?
  - Где хранить данные о пользователе?
  - Как передать данные через callback?
- RabbitMQ
  - Что такое exchange?
  - Что такое queue? За что отвечает параметр no_ack?
  - Что такое routing key, bind?
  - Как отправить и получить сообщение в очередь?
  - Как получить сообщение из очереди?
  - Как в рамках Fast api сделать получение сообщения из очереди?
  - Уметь рассказать про парадигму асинхронного бекенда? Зачем оно надо? Чем надежнее?
- Общие вопросы
  - Что такое сквозное логирование? Как его настроить?
  - Где лежат данные в вашем проекте? Уметь ответить на вопросы - что лежит в бд? Что лежит в очереди? И подобные
  - Знать что делает каждая библиотека в pyproject.toml

# Темы
1. Бот-календарь, с помощью которого можно создать свое расписание, напоминать о дедлайнах.
   - Из функционала должна быть возможность:
     - запомнить учетку, чтобы в любой момент я мог посмотреть свое расписание
     - Создать дело со сроком когда оно должно закончится. 
     - Оповестить за день, за 12ч и за 1ч до начала этого дела

2. Тема: Бот для изучения программирования на Python
   Из функционала должна быть возможность:
   - запомнить учетку, чтобы в любой момент человек мог посмотреть свои решенные задачи
   - Выбрать рандомно из существующего списка задачу
     - при выборе задачи в ответ ожидается код, который нужно скомпилить и выполнить.
     - при успешном выполнении простановка статуса об успешности
     - при неуспешном соответствующее сообщение с ошибкой
     - P.S В разработке не будем думать об безопаности, что могут заслать плохой код
   - создать задачу в этапы
     - название задачи
     - описание задачи
     - кол-во примеров
     - пример
     - ответ

3. Реализация бота для поддержки клиентов и обработки запросов через чат
   - Несколько видов учеток - админ и клиент.
     - если клиент шлет сообщение то оно рандомно доставляется одному из админов
     - когда сообщение приходит, то ответ админа на это сообщение уходит к клиенту. 
     - В моменте у админа может быть только одно сообщение от клиента
     - Если приходит сообщение от клиента, а админы заняты, то нужно подождать пока хотя бы один админ освободится

4. Разработка бота для организации и проведения опросов и анкетирования.
   - У бота должны быть две роли:
     - админ, который умеет создавать опросники в формате
       - кол-во вопросов = N
       - вопрос
       - ... (N штук)
       - вопрос
     - опрашиваемый
       - После регистрации админ может прислать этому пользователю опрос, с подтверждением согласия на проходждение опрос
       - если пользователь соглашается, то начинается опрос по вопросам из опросника

5. \* Бот для обработки ИИ модели
   - пользователь нужен только для отслеживания статуса задачи
   - можно посмотреть статусы обработок и их результаты
   - сама модель:
     - использование модели в консумере моделей
     - получение информации о результате "predict" в отдельном консумере
     - отправка результатов пользователю и их сохранение

6. Бот для хранения фотографий
   - пользователь нужен для возможности получить загруженные фото
   - можно посмотреть все загруженные фото в разрезе месяца и потом дня
   - в разрезе дня можно нажать на нужную фотку и подгрузить ее
   - Саму фото можно грузить на любое хранилище, можно использовать яндекс диса или гугл диск или любое другое хранилище.

7. Бот для заказа еды
   - две роли пользователя:
     - курьер - ему приходят готовые заказы на доставку
     - пользователь - умеет выбирать из меню товары, которые готовы к выдаче
   - выбор товаров:
     - В базе должен быть список товаров с категориями
     - при запросе выбора товаров изначально кидается список категорий в которых есть хотя бы один товар
     - далее по кнопке можно выбрать нужную категории и посмотреть список товаров
     - сам список товаров небольшой, сделать пагинацию через offset + limit на 10 товаров.
   - У товара есть возможность нажать "добавить в корзину", тогда он попадает в корзину
   - отдельной кнопкой можно оформить заказ, тогда все товары в заказе должны попасть в чат с курьером
     - если их несколько, то одному из них рандомно

8. Бот для подбора рецепта
   - роль пользователя одна:
     - можно посмотреть свои созданные рецепты
   - меню бота:
     - создать новый рецепт
     - получить рецепт по продуктам
     - подобрать самый популярный рецепт
   - создать новый рецепт
     - записать в бд сам рецепт и ингредиенты
     - ингредиенты в формате название + граммы (пусть все в граммах будет)
   - получить рецепт
     - запрашиваются имеющиеся продукты
     - после описание всех продуктов можно нажать "подобрать рецепт"
     - должна быть пагинация рецептов
     - предложенные рецепты можно лайкнуть и дизлайкнуть (пусть просто счетчик лайков у рецепта)
   - получить самый популярный рецепт по лайкам

9. Бот для подсчета калорий
   - пользователь для которого считаем калории
   - меню
     - внести калории
     - вывести статистику по калориям
       - после нажатия выпадающие кнопки
         - посмотреть статистику за день
         - посмотреть статистику за неделю
         - посмотреть статистику за месяц
     - возможность изменить время ежедневного уведомления
   - ежедневное уведомление о статистике за день

10. Бот для тайм менеджмента
   - пользователь для которого мы считаем время
   - меню
     - вывести статистику по делам
       - после нажатия выпадающие кнопки
         - посмотреть статистику дел за день
         - посмотреть статистику дел за неделю
         - посмотреть статистику дел за месяц
     - начать дело
       - выбор дела с кнопкой старт таймера
       - отправка завершения о финише дела
     - добавить дело
   - ежедневное уведомление о статистике за день

11. Бот для документа-хранения 
   - пользователь для который будет управлять документами
   - меню
     - добавить документ 
       - после нажатия диалог с помощью которого можно добавить тип документа, его название
     - показать документы
       - первым на выбор идут типы документов (в разрезе типа может быть много объектов)
       - после нажатия на тип, сам выбор документа

12. Бот для мемов
   - пользователь 
   - меню
     - добавить мем (фото + текст) 
       - после нажатия диалог с помощью которого можно добавить фото + текст
       - возможность добавить в общую корзину мемов и в личную
     - выбрать рандомный мем из общей
       - оценить лайк или дизлайк
     - выбрать рандомный мем из личной
     - посмотреть свой список мемов
     - выбрать самый популярный

13. Бот крестики-нолики 
   - пользователь 
   - меню
     - посмотреть статистику прошлый игр (результат и с кем) 
     - поиск игры 
       - после нажатия вы встаете в "очередь"
       - как нашелся второй игрок, то игра начинается
       - рандомно назначается первый ходящий, второй ходящий при этом так же получает игру, но с оговоркой, что он ждет
       - дальше ходим по очереди. Обработка ошибок, если походил тот кто не должен или тот кто должен, но не корректный выбор ячейки

14. Бот помошник в поездку
   - пользователь
   - возможность создать вещи, которые нужно взять с собой
     - данные вещи можно привязать отдельное к длительности поездке, например 1д, 2д, 3д и тд
   - меню
     - проверка на сбор вещей
       - указывается длительность поездки
       - выскакивает меню с тем, что нужно взять
         - при нажатии этот объект считается взятый и уходит из списка
     - добавить предмет
     - добавить длительность (тут можно и переиграть как-то, возможно удобнее диапазонами)

15. Бот знакомства
   - пользователь
   - возможность создать анкету, загрузить туда фото и описание
   - при старте просит загрузить описание и анкету, только потом пускает в бота
   - меню
     - поиск знакомств
       - подбирает следующую анкету (пусть будет рандом из бд)
         - лайк или дизлайк
       - при нажатии на лайк, если вас тоже уже лайкнул этот пользователь, то присылается ссылка на телеграм в оба чата

16. Бот нотификатор
   - Идея - у вас уже есть готовый бот и вам поступила задача сделать систему рассылок в боте 
   - Пользователь
   - Отдельная панель для создания нотификация (можно взять и джанго админ, можно сделать в самом боте)
   - Оповещение выбранных пользователей с учетом допустимой нагрузки в телеграм
   - Оповещение = Какое-то сообщение, которое можно создать в базе данных + картинка при надобности

17. Алерт менеджер
   - Пользователь
   - Сервис с прометеусом, в который можно собирать метрики
   - Проверять метрики в прометеусе и в случае негативного сценария слать сообщение в телеграм
   - P.S. Можно сделать просто на канале
   - P.S. Так как нужны метрики, то потребуется фиктивный "генератор" метрик в виде сервиса,
   - чтобы "сломать" его и получить алерт

Требования к проекту:
- Упаковка проекта в докер-компоуз и запуск через docker compose up без дополнительной настройки
- Два формата запуска - через polling и через webhook
- прохождение flake8 + mypy в соответствии с конфигурациями проекта
- Стейт отдельный под каждого пользователя
- Без доступа к бд
- Метрики: 
  - Время выполнения всех интеграционных методов (запросы на бекенд и телеграм)
- Настройки в env
  - Без дублирования кода
- poetry как сборщик пакетов
- Обработка ошибок и соответствующие ответы от бота
- Обработка флуда
- В README.md ожидается увидеть как что работает, чтобы можно было ознакомиться проще с проектом
- Сквозное логирование



1 - 2
Максим, [12.09.2024 19:34]
Проект
Нудьга Максим @Cinimin12
Телегин Сергей @gymabody
Дружинин Никита @agent_yandexxx


2 - 14
Мой Господин, [12.09.2024 20:31]
🔤🔤🔤🔤🔤🔤🔤
Арсенович Марко @n0tsSzzz  🚬

3 - 9
Areg, [12.09.2024 20:41]
Матвей Озорнин @spl3g
Крдян Арег @Areg000


4 - 3
Владислав, [12.09.2024 20:52]
Проект
Осипов Владислав @wtf_my_life

5 - 7
Dan'Ke, [12.09.2024 21:01]
Проект
Турапов Илья @irontoast

6 - 8
Настик, [12.09.2024 21:03]
Проект
Зорина Анастасия @nafanyufka
Зорина Екатерина @adorable_kitty
Григорян Артем @Twbworse

7 - 9
Dayana, [12.09.2024 21:32]
Проект
Колкарева Даяна @iamreallysleepy
Тяпкова Виктория @pienchik

8 - 15
Slavik Demyanenko, [13.09.2024 09:09]
Проект
@SlavikYD - Демьяненко Вячеслав
@dimmmension - Никифоров Вадим
@Egorik_4 - Литвинов Егор

9 - 10
Тима К, [13.09.2024 09:24]
Проект
@Myamei44 - Носков Михаил
@KristevTim - Кристьев Тимофей

10 - 11
Denariadna, [13.09.2024 09:25]
Проект
Денисова Арина - @denariadna

11 - 2
Проект
Василенко Дмитрий @adaptabiIity 🌟



 1 - сириус
fedya eremin, [12.09.2024 19:27]
Задача от Сириуса и проект
Загора Анна @s_curlyn
Ерёмин Фёдор @half_truism

2 - мемы
MD, [12.09.2024 19:39]
Проект
До слободы продакшн
Тюрин Артем @rrtire
Роганов Егор @roganofff
Дятлова Мария @tofick_brodaga

3 - своя тема
Антон, [12.09.2024 20:20]
Проект
Отрощенко Антон @ot_anton
Кривенко Артём @A_P_T_E_M_K_aaa
Зайцев Алексей @SlgmaMaIe


Exchange и queue в одном сервере?
Приоритезация*
