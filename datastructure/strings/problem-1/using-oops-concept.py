from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Dict, Optional


class DomainCounter(ABC):
    """Interface / contract."""

    @abstractmethod
    def count(self, emails: Iterable[str]) -> Dict[str, int]:
        raise NotImplementedError


@dataclass(frozen=True)
class DomainCountConfig:
    strict: bool = False          # if True -> invalid email raises error
    lowercase: bool = True        # normalize provider name
    max_emails: Optional[int] = None  # optional guardrail


class EmailDomainCounter(DomainCounter):
    def __init__(self, config: DomainCountConfig | None = None) -> None:
        self._config = config or DomainCountConfig()

    def count(self, emails: Iterable[str]) -> Dict[str, int]:
        counts: Counter[str] = Counter()

        for idx, email in enumerate(emails):
            if self._config.max_emails is not None and idx >= self._config.max_emails:
                break

            provider = self._extract_provider(email)
            if provider is None:
                continue
            counts[provider] += 1

        return dict(counts)

    # "private" helper (by convention in Python)
    def _extract_provider(self, email: str) -> Optional[str]:
        email = email.strip()
        if not email or "@" not in email:
            if self._config.strict:
                raise ValueError(f"Invalid email (missing @): {email!r}")
            return None

        local, domain = email.rsplit("@", 1)
        if not local or not domain or "." not in domain:
            # domain might be "sap" (no dot). Decide your business rule.
            if self._config.strict:
                raise ValueError(f"Invalid email domain: {email!r}")
            # if you want to allow "a@sap" then provider=domain
            provider = domain.split(".", 1)[0] if domain else ""
            return provider.lower() if (provider and self._config.lowercase) else provider or None

        provider = domain.split(".", 1)[0]
        if not provider:
            if self._config.strict:
                raise ValueError(f"Invalid email provider: {email!r}")
            return None

        return provider.lower() if self._config.lowercase else provider


if __name__ == "__main__":
    emails = ["hello@gmail.com", "jio@outlook.com", "world@sap.com", "hero@gmail.com"]
    counter = EmailDomainCounter(DomainCountConfig(strict=False))
    print(counter.count(emails))