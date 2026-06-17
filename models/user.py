from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    password_hash: str
    status: bool = False
    created_at: datetime = field(default_factory=datetime.now)
