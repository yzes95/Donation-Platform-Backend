from datetime import datetime
from sqlalchemy import String, DateTime, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class Donation(Base):
    __tablename__ = "donations"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    reference_id: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    payment_method: Mapped[str] = mapped_column(String(50), nullable=False)  # "instapay", "card", "fawry"
    status: Mapped[str] = mapped_column(String(50), default="pending")        # "pending", "completed"
    is_anonymous: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # TODO: Add family_id, need_id, donor details, platform tip, and gateway transaction IDs
