from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column  # noqa
from sqlalchemy import Integer


class MainBase(DeclarativeBase):
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.title()
