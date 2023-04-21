from sqlalchemy import ForeignKey, Integer, MetaData, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    display_id: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128))
    name: Mapped[str] = mapped_column(String(128))
    addresses: Mapped[list["Address"]] = relationship(back_populates="user")


class Address(Base):
    __tablename__ = "address"
    address_id: Mapped[int] = mapped_column(primary_key=True)
    address_line1: Mapped[str] = mapped_column(String(128))
    address_line2: Mapped[str] = mapped_column(String(128))
    is_primary: Mapped[bool] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    user: Mapped["User"] = relationship(back_populates="addresses")


class pets(Base):
    __tablename__ = "Pets"
    PetId: Mapped[int] = mapped_column(primary_key=True, index=True)
    Name = mapped_column(String(4096), index=True)

    user_id: Mapped[int] = mapped_column(Integer, index=True)
