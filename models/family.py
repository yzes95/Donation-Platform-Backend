"""Family, FamilyGroup, and FieldVerification ORM models."""
import enum
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Enum, ForeignKey, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class FamilyStatus(str, enum.Enum):
    """Family case verification status."""
    DRAFT = "draft"
    PENDING_VERIFICATION = "pending_verification"
    VERIFIED = "verified"
    REJECTED = "rejected"
    COMPLETED = "completed"


class UrgencyLevel(str, enum.Enum):
    """Urgency level classification."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class FamilyGroup(Base):
    """Family lineage or registered tribal group (e.g., Abo Nafee, Aboshwemy)."""
    __tablename__ = "family_groups"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    name_en: Mapped[str] = mapped_column(String(255), nullable=False)
    region_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    region_en: Mapped[str] = mapped_column(String(255), nullable=False)


class Family(Base):
    """Verified family case profile."""
    __tablename__ = "families"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    family_group_id: Mapped[str] = mapped_column(String(100), ForeignKey("family_groups.id"), nullable=True)
    representative_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    name_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    name_en: Mapped[str] = mapped_column(String(255), nullable=False)
    governorate_ar: Mapped[str] = mapped_column(String(255), nullable=False)
    governorate_en: Mapped[str] = mapped_column(String(255), nullable=False)
    members_count: Mapped[int] = mapped_column(Integer, default=1)
    monthly_income: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)
    social_status_ar: Mapped[str] = mapped_column(Text, nullable=True)
    social_status_en: Mapped[str] = mapped_column(Text, nullable=True)
    housing_status_ar: Mapped[str] = mapped_column(Text, nullable=True)
    housing_status_en: Mapped[str] = mapped_column(Text, nullable=True)
    summary_ar: Mapped[str] = mapped_column(Text, nullable=True)
    summary_en: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[FamilyStatus] = mapped_column(Enum(FamilyStatus), default=FamilyStatus.PENDING_VERIFICATION)
    urgency: Mapped[UrgencyLevel] = mapped_column(Enum(UrgencyLevel), default=UrgencyLevel.HIGH)
    verified_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    verified_by_ar: Mapped[str] = mapped_column(String(255), nullable=True)
    verified_by_en: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FieldVerification(Base):
    """Field researcher audit and document verification log."""
    __tablename__ = "field_verifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    family_id: Mapped[str] = mapped_column(String(50), ForeignKey("families.id"), nullable=False)
    researcher_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    report_notes_ar: Mapped[str] = mapped_column(Text, nullable=False)
    report_notes_en: Mapped[str] = mapped_column(Text, nullable=True)
    document_urls: Mapped[str] = mapped_column(Text, nullable=True)
    verified_status: Mapped[str] = mapped_column(String(50), default="approved")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
