import datetime


email = {
    "subject": "Отчет",
    "from": "  Alice.Cooper@Company.ru",
    "to": "  bob_smith@Gmail.com",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

## 2
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date


## 3
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

## 4
login_from, domain_from = str.split(email["from"], ("@"))

print(login_from)
print(domain_from)

## 5
email["short_body"] = (
    (email["body"][:10] + "..") if len(email["body"]) > 10 else email["body"]
)

## 6
personal_domain = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]


corporate_domain = [
    "company.ru",
    "corporation.com",
    "corporate.ru",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]


personal_domain = list(set(personal_domain))
corporate_domain = list(set(corporate_domain))
print(personal_domain)
print(corporate_domain)

## 7
intersection = list(set(personal_domain).intersection(corporate_domain))
print(intersection)

## 8
is_corporate = domain_from in corporate_domain
print(is_corporate)

## 9
clean_body = email["body"].replace("\t", " ").replace("\n", " ")
email["clean_body"] = clean_body

print(email)

## 10
print(
    f"Кому: {email['to']}, от {email['from']} Тема: {email['subject']}, дата {email['date']} {email['clean_body']}"
)

## 11
pages = (len(email["clean_body"]) + 499) // 500
print(pages)

## 12
s_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

print(s_subject_empty)
print(is_body_empty)

## 13
email["masked_from"] = login_from[:2] + "***@" + domain_from

print(email["masked_from"])

## 14
domains_to_remove = ["list.ru", "bk.ru"]
for domain_to_remove in domains_to_remove:
    if domain_to_remove in personal_domain:
        personal_domain.remove(domain_to_remove)

print(personal_domain)
