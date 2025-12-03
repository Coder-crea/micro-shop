from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    last_name: Mapped[str | None] = mapped_column(String(40), unique=False)
    bio: Mapped[str | None] = mapped_column(Text)
