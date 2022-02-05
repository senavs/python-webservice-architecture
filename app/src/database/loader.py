from app.src.database import DeclarativeBase, engine


def create_all(reset: bool = False):
    if reset:
        DeclarativeBase.metadata.drop_all(engine)
    DeclarativeBase.metadata.create_all(engine)
