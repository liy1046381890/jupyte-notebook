import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, ForeignKey

import enum 
'''
echo标志是设置SQLAlchemy日志记录的快捷方式，通过Python的标准logging模块完成。
启用后，将看到所有生成的SQL。
'''
engine = create_engine('mysql://root:root@localhost:3306/test?charset=utf8', echo=True)

Base = declarative_base()

'''
scoped_session

'''
Session = scoped_session(sessionmaker(bind=engine))

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    articles  = relationship('Article', back_populates='author')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

'''
sqlalchemy.Enum   enum.Enum要区分
'''
class ArticleTypes(enum.Enum):
    F = 'fiction'
    P = 'poetry'
    E = 'essay'

class Article(Base):
    '''
    表名
    表结构
    '''
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(Enum(ArticleTypes), nullable=False)
    view_count = Column(Integer)
    created_at = Column(DateTime)
    isvaild = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='articles')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

# class Orm_test(object):

#     def __init__(self):
#         self.session = Session()
    
#     def add(self):
#         new_object = News(
#             title='alice',
#             content='dream away',
#             types=NewsTypes.GLO
#         )
#         self.session.add(new_object)

#         # new_object = [
#         #     News(title='lucian', content='abc', types='a'),
#         #     News(title='lilian', content='bcd', types='b'),
#         #     News(title='lee', content='cde', types='c')
#         # ]
#         # self.session.add_all(new_object)
#         self.session.commit()
#         return dir(new_object)
#     def delete(self, pk):
#         obj = self.session.query(News).get(pk)
#         self.session.delete(obj)
#         self.session.commit()

#     def query(self):
#         return self.session.query(News).all()




if __name__ == "__main__":
    # 建表
    Base.metadata.create_all(engine)
    

    # test = Orm_test()
    # test.add()
    # print(NewsTypes.LO)
