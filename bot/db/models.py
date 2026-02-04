from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.types import BigInteger, VARCHAR, Boolean, Integer, DateTime

from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True) # telegram id
    username: Mapped[str] = mapped_column(VARCHAR, nullable=False) # @username
    first_name: Mapped[str] = mapped_column(VARCHAR, nullable=False) # name
    tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tarrifs.id"), nullable=False,) # current tariff
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False) # block/active
    created_at: Mapped[int] = mapped_column(DateTime, nullable=False) # registration
    updated_at: Mapped[int] = mapped_column(DateTime, nullable=False) # updated

class Tariff(Base):
    __tablename__ = "tarrifs"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True) # tariff id
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False) # name subscriptions (Free/Pro)
    max_subs: Mapped[int] = mapped_column(Integer, nullable=False) # sub limit
    check_interval_sec: Mapped[int] = mapped_column(Integer, nullable=False) # frequency subs
    price: Mapped[int] = mapped_column(BigInteger, nullable=False) # price
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False) # active status
    created_at: Mapped[int] = mapped_column(DateTime, nullable=False) # created status
