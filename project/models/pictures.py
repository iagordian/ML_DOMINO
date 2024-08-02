
from db import Base

from sqlalchemy import UUID, Integer, TEXT
from sqlalchemy.orm import mapped_column, Mapped

class Picture(Base):
    __tablename__ = 'pictures'

    uid: Mapped[UUID] = mapped_column(UUID, primary_key=True, comment='Уникальный идентификатор')
    up: Mapped[int] = mapped_column(Integer, comment='Верхнее значение')
    down: Mapped[int] = mapped_column(Integer, comment='Нижнее значение')
    img: Mapped[str] = mapped_column(TEXT, comment='Изображение домино в байт')