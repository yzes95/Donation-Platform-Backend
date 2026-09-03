from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class AssistanceNeed(Base):
    __tablename__ = "assistance_needs"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    family_id: Mapped[str] = mapped_column(String(50), ForeignKey("families.id"), nullable=False)
    title_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    title_en: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # "medical", "housing", "debt_relief"
    target_amount: Mapped[float] = mapped_column(Float, nullable=False)
    raised_amount: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(50), default="active")  # "active", "fulfilled"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # TODO: Add unit labels, donor counters, and descriptions
