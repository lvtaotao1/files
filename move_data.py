from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

engine = create_engine(url=settings.DATABASE_URI,pool_pre_ping=True)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base:
    id: Any
    __name__: str

    # 设置表的字符集
    __table_args__ = {"mysql_charset": "utf8"}

    # 将类名小写并转化为表名 __tablename__
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

def drop_db():
    """ 删除 db/base 下的所有表 """
    try:
        Base.metadata.drop_all(bind=engine)
        print("删除表成功!!!")
    except Exception as e:
        print(f"删除表失败!!! -- 错误信息如下:\n{e}")


def init_db():
    """ 创建 db/base 下的所有表 """
    try:
        drop_db()  # 删除所有的表
        Base.metadata.create_all(bind=engine)
        print("创建表成功!!!")
    except Exception as e:
        print(f"创建表失败!!! -- 错误信息如下:\n{e}")



if __name__ == '__main__':
    init_db()

