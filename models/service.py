"""Assistance Need / Service ORM model."""
import enum
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Enum, ForeignKey, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class NeedCategory(str, enum.Enum):
    """Assistance need category."""
    MEDICAL = "medical"
    HOUSING = "housing"
    DEBT_RELIEF = "debt_relief"
    EDUCATION = "education"
    ORPHAN_CARE = "orphan_care"
    EMERGENCIES = "emergencies"
    SEASONAL = "seasonal"


class NeedStatus(str, enum.Enum):
    """Need fulfillment status."""
    ACTIVE = "active"
    FULFILLED = "fulfilled"
    PAUSED = "paused"
    CANCELLED = "cancelled"


class AssistanceNeed(Base):
    """Specific verifiable need item for a family case."""
    __tablename__ = "assistance_needs"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    family_id: Mapped[str] = mapped_column(String(50), ForeignKey("families.id"), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    title_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    title_en: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[NeedCategory] = mapped_column(Enum(NeedCategory), nullable=False)
    unit_label_ar: Mapped[str] = mapped_column(String(100), nullable=True)
    unit_label_en: Mapped[str] = mapped_column(String(100), nullable=True)
    target_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    raised_amount: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)
    description_ar: Mapped[str] = mapped_column(Text, nullable=True)
    description_en: Mapped[str] = mapped_column(Text, nullable=True)
    beneficiary_ar: Mapped[str] = mapped_column(String(255), nullable=True)
    beneficiary_en: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[NeedStatus] = mapped_column(Enum(NeedStatus), default=NeedStatus.ACTIVE)
    donors_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
