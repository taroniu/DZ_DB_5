import psycopg2
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = 'postgresql://postgres:9ZUkK4725@localhost:5432/netology_db'
engine = sq.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

# publishers
pushkin = Publisher(name='Александр Сергеевич Пушкин')
sholohov = Publisher(name='Михаил Александрович Шолохов')
tolstoi = Publisher(name='Лев Николаевич Толстой')
session.add_all([pushkin, sholohov, tolstoi])

# print(pushkin.id_pub)
# print(pushkin)
# print(sholohov)
# print(tolstoi)

# books
onegin = Book(title='Евгений Онегин', publisher=pushkin)
kapitanskaya_dochka = Book(title='Капитанская дочка', publisher=pushkin)
ruslan = Book(title='Руслан и Людмила', publisher=pushkin)
saltan = Book(title='Сказа о царе Салтане', publisher=pushkin)
ribak = Book(title='Сказа о рыбаке и рыбке', publisher=pushkin)

sudba = Book(title='Судьба человека', publisher=sholohov)
tihi_don = Book(title='Тихий Дон', publisher=sholohov)
celina = Book(title='Поднятая целина', publisher=sholohov)
zherebenok = Book(title='Жеребенок', publisher=sholohov)
rasskazi = Book(title='Донские рассказы', publisher=sholohov)

voina_i_mir = Book(title='Война и мир', publisher=tolstoi)
karenina = Book(title='Анна Каренина', publisher=tolstoi)
plennik = Book(title='Кавказский пленник', publisher=tolstoi)

session.add_all([onegin, kapitanskaya_dochka, ruslan, saltan, ribak, sudba, tihi_don,
                 celina, zherebenok, rasskazi, voina_i_mir, karenina, plennik])

# shops
knizhka = Shop(name='Книжка')
chitai_gorod = Shop(name='Читай город')
centr_kniga = Shop(name='Центр книга')
znaika = Shop(name='Знайка')
misl = Shop(name='Мысль')
session.add_all([knizhka, chitai_gorod, centr_kniga, znaika, misl])

#stocks
stock14 = Stock(book=onegin, shop=chitai_gorod, count=12)
stock15 = Stock(book=kapitanskaya_dochka, shop=chitai_gorod, count=17)
stock16 = Stock(book=ruslan, shop=chitai_gorod, count=10)
stock17 = Stock(book=saltan, shop=chitai_gorod, count=2)
stock18 = Stock(book=ribak, shop=chitai_gorod, count=19)
stock19 = Stock(book=sudba, shop=chitai_gorod, count=18)
stock20 = Stock(book=tihi_don, shop=chitai_gorod, count=11)
stock21 = Stock(book=celina, shop=chitai_gorod, count=20)
stock22 = Stock(book=zherebenok, shop=chitai_gorod, count=29)
stock23 = Stock(book=rasskazi, shop=chitai_gorod, count=11)
stock24 = Stock(book=voina_i_mir, shop=chitai_gorod, count=50)
stock25 = Stock(book=karenina, shop=chitai_gorod, count=20)
stock26 = Stock(book=plennik, shop=chitai_gorod, count=40)

stock1 = Stock(book=onegin, shop=knizhka, count=10)
stock2 = Stock(book=kapitanskaya_dochka, shop=knizhka, count=15)
stock3 = Stock(book=ruslan, shop=knizhka, count=11)
stock4 = Stock(book=saltan, shop=knizhka, count=12)
stock5 = Stock(book=ribak, shop=knizhka, count=13)
stock6 = Stock(book=sudba, shop=knizhka, count=14)
stock7 = Stock(book=tihi_don, shop=knizhka, count=15)
stock8 = Stock(book=celina, shop=knizhka, count=16)
stock9 = Stock(book=zherebenok, shop=knizhka, count=17)
stock10 = Stock(book=rasskazi, shop=knizhka, count=18)
stock11 = Stock(book=voina_i_mir, shop=knizhka, count=19)
stock12 = Stock(book=karenina, shop=knizhka, count=20)
stock13 = Stock(book=plennik, shop=knizhka, count=21)

stock27 = Stock(book=onegin, shop=centr_kniga, count=100)
stock28 = Stock(book=kapitanskaya_dochka, shop=centr_kniga, count=150)
stock29 = Stock(book=ruslan, shop=centr_kniga, count=110)
stock30 = Stock(book=saltan, shop=centr_kniga, count=120)
stock31 = Stock(book=ribak, shop=centr_kniga, count=130)
stock32 = Stock(book=sudba, shop=centr_kniga, count=140)
stock33 = Stock(book=tihi_don, shop=centr_kniga, count=150)
stock34 = Stock(book=celina, shop=centr_kniga, count=160)
stock35 = Stock(book=zherebenok, shop=centr_kniga, count=170)
stock36 = Stock(book=rasskazi, shop=centr_kniga, count=180)
stock37 = Stock(book=voina_i_mir, shop=centr_kniga, count=190)
stock38 = Stock(book=karenina, shop=centr_kniga, count=200)
stock39 = Stock(book=plennik, shop=centr_kniga, count=210)

stock40 = Stock(book=onegin, shop=znaika, count=105)
stock41 = Stock(book=kapitanskaya_dochka, shop=znaika, count=130)
stock42 = Stock(book=ruslan, shop=znaika, count=143)
stock43 = Stock(book=saltan, shop=znaika, count=166)
stock44 = Stock(book=ribak, shop=znaika, count=177)
stock45 = Stock(book=sudba, shop=znaika, count=123)
stock46 = Stock(book=tihi_don, shop=znaika, count=117)
stock47 = Stock(book=celina, shop=znaika, count=124)
stock48 = Stock(book=zherebenok, shop=znaika, count=176)
stock49 = Stock(book=rasskazi, shop=znaika, count=188)
stock50 = Stock(book=voina_i_mir, shop=znaika, count=155)
stock51 = Stock(book=karenina, shop=znaika, count=158)
stock52 = Stock(book=plennik, shop=znaika, count=150)

stock53 = Stock(book=onegin, shop=misl, count=115)
stock54 = Stock(book=kapitanskaya_dochka, shop=misl, count=140)
stock55 = Stock(book=ruslan, shop=misl, count=153)
stock56 = Stock(book=saltan, shop=misl, count=176)
stock57 = Stock(book=ribak, shop=misl, count=187)
stock58 = Stock(book=sudba, shop=misl, count=133)
stock59 = Stock(book=tihi_don, shop=misl, count=127)
stock60 = Stock(book=celina, shop=misl, count=134)
stock61 = Stock(book=zherebenok, shop=misl, count=186)
stock62 = Stock(book=rasskazi, shop=misl, count=198)
stock63 = Stock(book=voina_i_mir, shop=misl, count=165)
stock64 = Stock(book=karenina, shop=misl, count=168)
stock65 = Stock(book=plennik, shop=misl, count=160)

session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7,
                 stock8, stock9, stock10, stock11, stock12, stock13, stock14,
                 stock15, stock16, stock17, stock18, stock19, stock20,
                 stock21, stock22, stock23, stock24, stock25, stock26,
                 stock27, stock28, stock29, stock30, stock31, stock32,
                 stock33, stock34, stock35, stock36, stock37, stock38, stock39,
                 stock40, stock41, stock42, stock43, stock44, stock45, stock46,
                 stock47, stock48, stock49, stock50, stock51, stock52, stock53,
                 stock54, stock55, stock56, stock57, stock58, stock59, stock60,
                 stock61, stock62, stock63, stock64, stock65,
                 ])

sale1 = Sale(price=500, date_sale='28-05-2023', id_stock=1, count=5)

session.add_all([sale1])
session.commit()


def filter(name_):
    # for i in session.query(Shop).filter(Shop.id ==
    #                                     Stock.id_shop).filter(Stock.id_book ==
    #                                     Book.id).filter(Book.id_pub ==
    #                                     Publisher.id_pub).filter(Publisher.name == name_).all():
    #     print(i)

    for book_name, shop_name, sale in session.query(Book, Shop, Sale).filter(Shop.id ==
                                        Stock.id_shop).filter(Stock.id_book ==
                                        Book.id).filter(Book.id_pub ==
                                        Publisher.id_pub).filter(Publisher.name == name_).all():
        print(book_name.title, '|', shop_name.name, '|', sale.price, '|', sale.date_sale)

    for book_name, shop_name, sale in session.query(Book, Shop, Sale).filter(Shop.id ==
                                        Stock.id_shop).filter(Stock.id_book ==
                                        Book.id).filter(Book.id_pub ==
                                        Publisher.id_pub).filter(Publisher.name == name_).all():
        print(book_name.title, '|', shop_name.name, '|', sale.price, '|', sale.date_sale)
name_ = input('Введите ФИО автора')
filter(name_)


# print(q.)
session.commit()
session.close()


# for i in range(53, 101): print(f'stock{i}', end=', ')

