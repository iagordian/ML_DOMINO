from domino.db import Base

from typing import Optional
from sqlalchemy import TEXT, String, JSON, Integer, LargeBinary, FLOAT
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.mutable import MutableDict

class ML_Object(Base):
    __tablename__ = 'ml_objects'

    model_name: Mapped[str] = mapped_column(String(64), primary_key=True, comment='Название модели')
    model_obj: Mapped[Optional[bytes]] = mapped_column(LargeBinary, comment='Модель в байтах')
    threshold: Mapped[Optional[str]] = mapped_column(TEXT, comment='Пороговое значние')
    logs: Mapped[Optional[dict]] = mapped_column(MutableDict.as_mutable(JSON), comment='Логирование процесса обучения')
    is_the_best_classifier_model: Mapped[Optional[int]] = mapped_column(Integer, default=0, comment='Флаг лучшей модели классификации')


class RandomForestObject(Base):
    __tablename__ = 'random_forest_objects'

    field_size: Mapped[int] = mapped_column(primary_key=True, comment='Размер ряда')
    model_obj: Mapped[Optional[bytes]] = mapped_column(LargeBinary, comment='Модель в байтах')
