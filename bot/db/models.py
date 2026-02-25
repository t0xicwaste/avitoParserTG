from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.types import JSON, BigInteger, VARCHAR, Boolean, Integer, DateTime, Text

from datetime import date

from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True) # telegram id
    username: Mapped[str] = mapped_column(VARCHAR, nullable=False) # @username
    first_name: Mapped[str] = mapped_column(VARCHAR, nullable=False) # name
    tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariffs.id"), nullable=False,) # current tariff
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False) # block/active
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False) # registration
    updated_at: Mapped[date] = mapped_column(DateTime, nullable=False) # updated

class Tariff(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True) # tariff id
    name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False) # name subscriptions (Free/Pro)
    max_subs: Mapped[int] = mapped_column(Integer, nullable=False) # sub limit
    check_interval_sec: Mapped[int] = mapped_column(Integer, nullable=False) # frequency subs
    price: Mapped[int] = mapped_column(BigInteger, nullable=False) # price in kopecks
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False) # active status
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False) # created status

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True) # id subscriptions
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False) # user_id
    city: Mapped[str] = mapped_column(VARCHAR, nullable=False) # city
    category: Mapped[str] = mapped_column(VARCHAR, nullable=False) # category
    subcategory: Mapped[str] = mapped_column(VARCHAR, nullable=False) # subcategory
    filters: Mapped[dict] = mapped_column(JSON, nullable=False) #filters
    search_url: Mapped[str] = mapped_column(Text, nullable=False) # url avito
    status: Mapped[str] = mapped_column(VARCHAR, nullable=False) # active/paused
    last_item_id: Mapped[int] = mapped_column(BigInteger, nullable=False) # deduplication
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False) # registration
    updated_at: Mapped[date] = mapped_column(DateTime, nullable=False) # updated

class parsedItem(Base):
    __tablename__ = "parsed_items"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    subscription_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriptions.id"), nullable=False)
    title: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    published_at: Mapped[date] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False)

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    tariff_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("tariffs.id"), nullable=False)
    provider: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    currency: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    status: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    external_id: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False)

class parsingLog(Base):
    __tablename__ = "parsing_logs"

    id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    subscription_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriptions.id"), nullable=False)
    status: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[date] = mapped_column(DateTime, nullable=False)
