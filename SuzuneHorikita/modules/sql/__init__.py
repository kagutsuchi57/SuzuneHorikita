from SuzuneHorikita import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


def start() -> scoped_session:
    engine = create_engine("postgres://ycuonyceejuevz:c107e86c014c8ea740e3dc51247e308126625a546c5add5ceb1e2389d05eb828@ec2-3-224-8-189.compute-1.amazonaws.com:5432/d83c311ir863sb", client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=True))


BASE = declarative_base()
SESSION = start()
