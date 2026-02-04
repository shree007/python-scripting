
from collections import Counter
from typing import Iterable,Dict

def count_mail_domain(emails: Iterable[str]) -> Dict[str, int]:
    counts: Counter[str] = Counter()
    for email in emails:
        if "@" not in email:
            continue
        domain_part = email.rsplit("@", 1)[1]
        provider = domain_part.split(".",1)[0]
        if provider:
            counts[provider] +=1
    return dict(counts)



if __name__ == "__main__":
    emails = ["hello@gmail.com", "jio@outlook.com", "world@sap.com", "hero@gmail.com"]
    print(count_mail_domain(emails))