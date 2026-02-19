import datetime




# 1.Создайте словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


# 2. Добавьте дату отправки
now = datetime.datetime.now()
send_date = now.strftime('%Y-%m-%d')
email["date"] = send_date


# 3. Нормализуйте e-mail адреса
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()


# 4. Извлеките логин и домен отправителя
login, domain = email["from"].split('@')


# 5. Создайте сокращённую версию текста
email["short_body"] = email["body"][:10] + "..."


# 6. Списки доменов
personal_domain_raw = ['gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru',
                       'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru']
corporate_domain_raw = ['company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru',
                        'business.net']
personal_domain = list(set(personal_domain_raw))
corporate_domain = list(set(corporate_domain_raw))


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
assert set(personal_domain) & set(corporate_domain) == set()


# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domain


# 9. Соберите «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")


# 10. Сформируйте текст отправленного письма
email["sent_text"] = (f"""
Кому: {email['to']}, от {email['from']}, 
Тема: {email['subject']}, дата {email['date']} 
{email['clean_body']}
""")


# 11. Рассчитайте количество страниц печати
text = email["sent_text"]
pages = (len(text) + 499) // 500


# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()


# 13. Создайте «маску» e-mail отправителя
email["masked_from"] = login[:2] + "***@" + domain


# 14. Удалите из списка личных доменов
personal_domain.remove("list.ru")
personal_domain.remove("bk.ru")


# Ключевые результаты
print(email)
print(is_corporate)
print(pages)
print(is_subject_empty)
print(is_body_empty)
