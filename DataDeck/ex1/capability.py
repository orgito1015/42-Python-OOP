from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract class defining healing capability for a creature."""

    @abstractmethod
    def heal(self) -> str:
        """Return the heal action message."""
        pass


class TransformCapability(ABC):
    """Abstract class defining transformation capability for a creature."""

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transform the creature and return the action message."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert to normal form and return the action message."""
        pass
