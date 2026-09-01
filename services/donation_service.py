"""Donation processing and reference ID generation."""
import uuid


class DonationService:
    """Handles donation allocation, receipt generation, and reference ID creation."""

    @staticmethod
    def generate_reference_id() -> str:
        """Generate a human-readable unique reference ID."""
        short_code = uuid.uuid4().hex[:8].upper()
        return f"REF-ATAA-{short_code}"
