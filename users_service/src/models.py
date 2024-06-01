from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = Column(String, nullable=False)
    permissions: Mapped[dict] = Column(JSON)

    users: Mapped[list["User"]] = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role(name='{self.name}', permissions='{self.permissions}')>"


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = Column(String, nullable=False)
    username: Mapped[str] = Column(String, nullable=False)
    registered_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = Column(Integer, ForeignKey('role.id'))
    role: Mapped[Role] = relationship("Role", back_populates="users")
    hashed_password: Mapped[str] = Column(String, nullable=False)

    is_active: Mapped[bool] = Column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return (f"<User(email='{self.email}', username='{self.username}', registered_at='{self.registered_at}', "
                f"is_active='{self.is_active}', is_superuser='{self.is_superuser}', is_verified='{self.is_verified}')>")
