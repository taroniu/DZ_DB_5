import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id_pub = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)

    # publisher = relationship(Book, back_populates='id_pub')

    def __str__(self):
        return f'{self.id_pub}: {self.name}'

pushkin = Publisher(name='Александр Сергеевич Пушкин')
sholohov = Publisher(name='Михаил Александрович Шолохов')
tolstoi = Publisher(name='Лев Николаевич Толстой')


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    id_pub = sq.Column(sq.Integer, sq.ForeignKey("publisher.id_pub"), nullable=False)

    # publisher = relationship(Publisher, back_populates='id_pub')
    publisher = relationship(Publisher, backref='publisher.id_pub')

    def __str__(self):
        return f'{self.id}: {self.title}, autor id - {self.id_pub}'


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='book.id')
    shop = relationship(Shop, backref='shop.id')

    def __str__(self):
        return f'{self.id}: {self.id_book}, {self.id_shop}, {self.count}'


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship(Stock, backref='stock.id')

    def __str__(self):
        return f'{self.id}: price - {self.price}, date - {self.date_sale}, stock - {self.id_stock}, count - {self.count}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)




