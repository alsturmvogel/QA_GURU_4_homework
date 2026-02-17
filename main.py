import datetime




email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


now = datetime.datetime.now()
send_date = now.strftime('%Y-%m-%d')
email["date"] = send_date


email ["from"] = email["from"].strip().lower()
email ["to"] = email["to"].strip().lower()


parts = email["from"].split('@')
login = parts[0]
domain = parts[1]


email["short_body"] = email["body"][:10] + "..."


ldomen0 = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
kdomen0 = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
personal_domen = set(ldomen0)
corporate_domen = set(kdomen0)


intersection = personal_domen & corporate_domen


is_corporate = domain in corporate_domen


email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")


email["sent_text"] = (f"Кому: {email['to']}, от {email['from']}, Тема: {email['subject']}, дата {email['date']} {email['clean_body']}")


text = email["sent_text"]
pages = (len(text) + 499) // 500


is_subject_empty = not email["subject"]
is_body_empty = not email["body"]


email["masked_from"] = login[:2] + "***@" + domain


personal_domen.remove("list.ru")
personal_domen.remove("bk.ru")


print (email)
print (is_corporate)
print (pages)
print (is_subject_empty)
print (is_body_empty)