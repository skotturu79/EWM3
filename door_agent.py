"""Simple door state agent."""

from dataclasses import dataclass


@dataclass
class DoorAgent:
    is_open: bool = False
    is_locked: bool = True

    def request_open(self) -> bool:
        if self.is_locked:
            return False
        self.is_open = True
        return True

    def request_close(self) -> bool:
        self.is_open = False
        return True

    def request_lock(self) -> bool:
        if self.is_open:
            return False
        self.is_locked = True
        return True

    def request_unlock(self) -> bool:
        self.is_locked = False
        return True

    @property
    def status(self) -> str:
        if self.is_open:
            return "open"
        if self.is_locked:
            return "closed_locked"
        return "closed_unlocked"
