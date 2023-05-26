from dataclasses import dataclass


@dataclass
class Customer:
    """Class for customer domain."""
    name: str
    age: int
    balance: float
    rate: float
    address: str

    def total_amount(self) -> float:
        return self.balance * self.rate
