"""Class with request details."""

from dataclasses import dataclass, field
from typing import Dict

from .http_method import HttpMethod


@dataclass
class RequestDetails:
    """Class with request details. Specify all http request details."""

    http_method: HttpMethod
    url: str
    headers: Dict[str, str] = field(default_factory=dict)
    params: Dict[str, str] = field(default_factory=dict)
    timeout: int = 10
