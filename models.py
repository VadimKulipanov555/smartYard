from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

user_chat = Table('user_chat', Base.metadata,
                  Column('id_user', Integer(), ForeignKey("User.id_user")),
                  Column('id_chat', Integer(), ForeignKey("Chat.id_chat"))
                  )


class User(Base):

    __tablename__ = 'User'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String(60))
    surname_user = Column(String(60))
    password_user = Column(String(500))
    email_user = Column(String(320), unique=True)
    telephone_user = Column(String(15), unique=True)
    info_user = Column(String(70))
    address_user = Column(String(320))
    date_registration_user = Column(DateTime)

    def __init__(self, name_user, surname_user, password_user, email_user, telephone_user,
                 address_user='Добавьте адрес', date_registration_user=datetime.utcnow(), info_user='Пока ничего'):

        self.name_user = name_user
        self.surname_user = surname_user
        self.password_user = password_user
        self.email_user = email_user
        self.telephone_user = telephone_user
        self.info_user = info_user
        self.address_user = address_user
        self.date_registration_user = date_registration_user


class Chat(Base):

    __tablename__ = 'Chat'

    id_chat = Column(Integer, primary_key=True, autoincrement=True)
    name_chat = Column(String(60))
    date_registration_chat = Column(DateTime)
    id_creator = Column(Integer, ForeignKey('User.id_user'))

    List_Chat_Participants = relationship('User', secondary=user_chat, backref="Chat")

    def __init__(self, name_chat, id_creator, date_registration_chat=datetime.utcnow()):

        self.name_chat = name_chat
        self.date_registration_chat = date_registration_chat
        self.id_creator = id_creator


class Group_Chat(Base):

    __tablename__ = 'Group_Chat'

    id_group_chat = Column(Integer, primary_key=True, autoincrement=True)
    id_chat = Column(Integer, ForeignKey('Chat.id_chat'))
    name_group_chat = Column(String(120))

    def __init__(self, id_chat, name_group_chat):

        self.id_chat = id_chat
        self.name_group_chat = name_group_chat


class Message(Base):

    __tablename__ = 'Message'

    id_message = Column(Integer, primary_key=True, autoincrement=True)
    text_message = Column(String(320))
    id_creator = Column(Integer, ForeignKey('User.id_user'))
    id_chat = Column(Integer, ForeignKey('Chat.id_chat'))

    def __init__(self, text_message, id_creator, id_chat):

        self.text_message = text_message
        self.id_creator = id_creator
        self.id_chat = id_chat


class Answer(Base):

    __tablename__ = 'Answer'

    id_answer = Column(Integer, primary_key=True, autoincrement=True)
    text_answer = Column(String(120))

    def __init__(self, text_answer):

        self.text_answer = text_answer


class Voting(Base):

    __tablename__ = 'Voting'

    id_voting = Column(Integer, primary_key=True, autoincrement=True)
    question_voting = Column(String(320))
    id_answer_voting = Column(Integer, ForeignKey('Answer.id_answer'))
    id_chat = Column(Integer, ForeignKey('Chat.id_chat'))

    def __init__(self, question_voting, id_answer_voting, id_chat):

        self.question_voting = question_voting
        self.id_answer_voting = id_answer_voting
        self.id_chat = id_chat



class Voice(Base):

    __tablename__ = 'Voice'

    id_voice = Column(Integer, primary_key=True, autoincrement=True)
    id_voting = Column(Integer, ForeignKey('Voting.id_voting'))
    id_answer = Column(Integer, ForeignKey('Answer.id_answer'))
    id_user = Column(Integer, ForeignKey('User.id_user'))

    def __init__(self, id_voting, id_answer, id_user):

        self.id_voting = id_voting
        self.id_answer = id_answer
        self.id_user = id_user


class Notification(Base):

    __tablename__ = 'Notification'

    id_notification = Column(Integer, primary_key=True, autoincrement=True)
    text_notification = Column(String(320))
    date_notification = Column(DateTime)
    id_chat = Column(Integer, ForeignKey('Chat.id_chat'))

    def __init__(self, text_notification, datenotification, id_chat):

        self.text_notification = text_notification
        self.date_notification = datenotification
        self.id_chat = id_chat

