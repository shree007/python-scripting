from typing import Iterable
from collections import Counter

def count_domains(emails: Iterable[str]) -> dict[str,int]:
    try:
        counts: Counter[str] = Counter()
        for email in emails:
            if "@" not in email:
                continue
            split_with_dot = email.rsplit("@",1)[1]
            split_without_dot = split_with_dot.rsplit(".",1)[0]
            if split_without_dot:
                counts[split_without_dot] +=1
        return dict(counts)
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    emails = ["hello@gmail.com", "jio@outlook.com", "world@sap.com", "hero@gmail.com","hare@india.com"]
    try:
        if len(emails)!=0:
            count_each_email_domains = count_domains(emails)
            print(count_each_email_domains)
        else:
            print("please provide email lists")
    
    except Exception as e:
        print(e)