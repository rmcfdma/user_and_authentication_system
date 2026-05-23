from datetime import datetime, timezone
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from app.models.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    role: Mapped[str] = mapped_column(
        Integer,
        default = 0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )