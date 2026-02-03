from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, VARCHAR, Boolean, Integer, DateTime

from .base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True) # telegram id
    username: Mapped[str] = mapped_column(VARCHAR, nullable=False) # @username
    first_name: Mapped[str] = mapped_column(VARCHAR, nullable=False) # name
    tariff_id: Mapped[int] = mapped_column(Integer, nullable=False) # current tariff // TODO: Добавить вторичный ключ
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False) # block/active
    created_at: Mapped[int] = mapped_column(DateTime, nullable=False) # registration
    updated_at: Mapped[int] = mapped_column(DateTime, nullable=False) # updated
