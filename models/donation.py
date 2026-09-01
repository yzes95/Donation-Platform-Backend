"""Donation and Payment Transaction ORM models."""
import enum
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Enum, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class DonationType(str, enum.Enum):
    """Donation designation."""
    FAMILY = "family"
    PLATFORM = "platform"


class DonationStatus(str, enum.Enum):
    """Donation lifecycle status."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class PaymentMethod(str, enum.Enum):
    """Supported payment gateways."""
    INSTAPAY = "instapay"
    VODAFONE_CASH = "vodafone_cash"
    CARD = "card"
    FAWRY = "fawry"
    PAYPAL = "paypal"


class Donation(Base):
    """Donation ledger entry."""
    __tablename__ = "donations"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    reference_id: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    type: Mapped[DonationType] = mapped_column(Enum(DonationType), default=DonationType.FAMILY)
    family_id: Mapped[str] = mapped_column(String(50), ForeignKey("families.id"), nullable=True)
    need_id: Mapped[str] = mapped_column(String(50), ForeignKey("assistance_needs.id"), nullable=True)
    donor_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    platform_tip: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)
    total_paid: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    is_anonymous: Mapped[bool] = mapped_column(Boolean, default=False)
    donor_name_ar: Mapped[str] = mapped_column(String(255), nullable=True)
    donor_name_en: Mapped[str] = mapped_column(String(255), nullable=True)
    donor_email: Mapped[str] = mapped_column(String(255), nullable=True)
    donor_phone: Mapped[str] = mapped_column(String(50), nullable=True)
    payment_method: Mapped[PaymentMethod] = mapped_column(Enum(PaymentMethod), nullable=False)
    status: Mapped[DonationStatus] = mapped_column(Enum(DonationStatus), default=DonationStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    delivered_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class PaymentTransaction(Base):
    """Payment gateway webhook and transaction log."""
    __tablename__ = "payment_transactions"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    donation_id: Mapped[str] = mapped_column(String(50), ForeignKey("donations.id"), nullable=False)
    gateway_name: Mapped[str] = mapped_column(String(50), nullable=False)
    gateway_reference: Mapped[str] = mapped_column(String(255), nullable=True)
    raw_payload: Mapped[str] = mapped_column(String(4000), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="success")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
