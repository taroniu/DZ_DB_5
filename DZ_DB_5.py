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
onegin = Book(title='Евгений Онегин', id_pub=1)
kapitanskaya_dochka = Book(title='Капитанская дочка', id_pub=1)
ruslan = Book(title='Руслан и Людмила', id_pub=1)
saltan = Book(title='Сказа о царе Салтане', id_pub=1)
ribak = Book(title='Сказа о рыбаке и рыбке', id_pub=1)

sudba = Book(title='Судьба человека', id_pub=2)
tihi_don = Book(title='Тихий Дон', id_pub=2)
celina = Book(title='Поднятая целина', id_pub=2)
zherebenok = Book(title='Жеребенок', id_pub=2)
rasskazi = Book(title='Донские рассказы', id_pub=2)

voina_i_mir = Book(title='Война и мир', id_pub=3)
karenina = Book(title='Анна Каренина', id_pub=3)
plennik = Book(title='Кавказский пленник', id_pub=3)

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
stock14 = Stock(id_book=1, shop=2, count=12)
stock15 = Stock(id_book=2, shop=2, count=17)
stock16 = Stock(id_book=3, shop=2, count=10)
stock17 = Stock(id_book=4, shop=2, count=2)
stock18 = Stock(id_book=5, shop=2, count=19)
stock19 = Stock(id_book=6, shop=2, count=18)
stock20 = Stock(id_book=7, shop=2, count=11)
stock21 = Stock(id_book=8, shop=2, count=20)
stock22 = Stock(id_book=9, shop=2, count=29)
stock23 = Stock(id_book=10, shop=2, count=11)
stock24 = Stock(id_book=11, shop=2, count=50)
stock25 = Stock(id_book=12, shop=2, count=20)
stock26 = Stock(id_book=13, shop=2, count=40)

stock1 = Stock(id_book=1, shop=1, count=10)
stock2 = Stock(id_book=2, shop=1, count=15)
stock3 = Stock(id_book=3, shop=1, count=11)
stock4 = Stock(id_book=4, shop=1, count=12)
stock5 = Stock(id_book=5, shop=1, count=13)
stock6 = Stock(id_book=6, shop=1, count=14)
stock7 = Stock(id_book=7, shop=1, count=15)
stock8 = Stock(id_book=8, shop=1, count=16)
stock9 = Stock(id_book=9, shop=1, count=17)
stock10 = Stock(id_book=10, shop=1, count=18)
stock11 = Stock(id_book=11, shop=1, count=19)
stock12 = Stock(id_book=12, shop=1, count=20)
stock13 = Stock(id_book=13, shop=1, count=21)

stock27 = Stock(id_book=1, shop=3, count=100)
stock28 = Stock(id_book=2, shop=3, count=150)
stock29 = Stock(id_book=3, shop=3, count=110)
stock30 = Stock(id_book=4, shop=3, count=120)
stock31 = Stock(id_book=5, shop=3, count=130)
stock32 = Stock(id_book=6, shop=3, count=140)
stock33 = Stock(id_book=7, shop=3, count=150)
stock34 = Stock(id_book=8, shop=3, count=160)
stock35 = Stock(id_book=9, shop=3, count=170)
stock36 = Stock(id_book=10, shop=3, count=180)
stock37 = Stock(id_book=11, shop=3, count=190)
stock38 = Stock(id_book=12, shop=3, count=200)
stock39 = Stock(id_book=13, shop=3, count=210)

stock40 = Stock(id_book=1, shop=4, count=105)
stock41 = Stock(id_book=2, shop=4, count=130)
stock42 = Stock(id_book=3, shop=4, count=143)
stock43 = Stock(id_book=4, shop=4, count=166)
stock44 = Stock(id_book=5, shop=4, count=177)
stock45 = Stock(id_book=6, shop=4, count=123)
stock46 = Stock(id_book=7, shop=4, count=117)
stock47 = Stock(id_book=8, shop=4, count=124)
stock48 = Stock(id_book=9, shop=4, count=176)
stock49 = Stock(id_book=10, shop=4, count=188)
stock50 = Stock(id_book=11, shop=4, count=155)
stock51 = Stock(id_book=12, shop=4, count=158)
stock52 = Stock(id_book=13, shop=4, count=150)

stock53 = Stock(id_book=1, shop=5, count=115)
stock54 = Stock(id_book=2, shop=5, count=140)
stock55 = Stock(id_book=3, shop=5, count=153)
stock56 = Stock(id_book=4, shop=5, count=176)
stock57 = Stock(id_book=5, shop=5, count=187)
stock58 = Stock(id_book=6, shop=5, count=133)
stock59 = Stock(id_book=7, shop=5, count=127)
stock60 = Stock(id_book=8, shop=5, count=134)
stock61 = Stock(id_book=9, shop=5, count=186)
stock62 = Stock(id_book=10, shop=5, count=198)
stock63 = Stock(id_book=11, shop=5, count=165)
stock64 = Stock(id_book=12, shop=5, count=168)
stock65 = Stock(id_book=13, shop=5, count=160)

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

sale1 = Sale(price=500, date_sale='28-05-2023', id_stock=1, count=57)
sale2 = Sale(price=510, date_sale='27-05-2023', id_stock=2, count=5)
sale3 = Sale(price=520, date_sale='26-05-2023', id_stock=3, count=5)
sale4 = Sale(price=530, date_sale='25-05-2023', id_stock=4, count=5)
sale5 = Sale(price=540, date_sale='24-05-2023', id_stock=5, count=5)
sale6 = Sale(price=550, date_sale='23-05-2023', id_stock=19, count=5)
sale7 = Sale(price=560, date_sale='22-05-2023', id_stock=61, count=5)
sale8 = Sale(price=570, date_sale='21-05-2023', id_stock=62, count=5)
sale9 = Sale(price=580, date_sale='20-05-2023', id_stock=63, count=5)
sale10 = Sale(price=590, date_sale='29-05-2023', id_stock=64, count=5)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10])
session.commit()


def get_shops(autor):
    if autor.isdigit():
        result = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).
                  join(Stock).
                  join(Book).
                  join(Publisher).
                  join(Sale)
                  ).filter(autor == Publisher.id_pub)
    else:
        result = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).
                  join(Stock).
                  join(Book).
                  join(Publisher).
                  join(Sale)
                  ).filter(autor == Publisher.name)

    for title, name, price, date in result:
        print(f"{title} | {name} | {price} | {date.strftime('%d-%m-%Y')}")

session.commit()
session.close()

if __name__ == '__main__':
    autor = input('Введите ФИО автора ')
    get_shops(autor)


