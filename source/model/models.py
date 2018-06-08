from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
NAME_DB = "cinema_reservations.db"


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float,
                    CheckConstraint('rating>=1.0 and rating<=10.0'),
                    nullable=False)

    def __str__(self):
        return f"[{self.id}] - {self.name} ({self.rating})"

    def __repr__(self):
        return self.__str__


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    type = Column(String(10))
    date = Column(String)
    time = Column(String)
    movie_id = Column(Integer, ForeignKey(Movies.id))
    movie = relationship(Movies, backref='movies')

    def __str__(self):
        return f"[{self.id}] - {self.date} {self.time} ({self.type})"

    def __repr__(self):
        return self.__str__


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id))
    user = relationship(Users, backref='users')
    projections_id = Column(Integer, ForeignKey(Projections.id))
    projection = relationship(Projections, backref='projections')
    row = Column(Integer,
                 CheckConstraint("row>= 0 AND row<=9"),
                 nullable=False)
    col = Column(Integer,
                 CheckConstraint("col>=0 AND col<=9"),
                 nullable=False)

    def __str__(self):
        return f"{self.projection.date} {self.projection.time} {self.projection.movie.name} Seat: {self.row} {self.col} "

    def __repr__(self):
        return self.__str__


class CreateDatabase:
    engine = create_engine(f"sqlite:///{NAME_DB}")

    @classmethod
    def create_db(cls):
        Base.metadata.create_all(cls.engine)
