def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на корректность email-адресов
    valid_domains = [".com", ".ru", ".net"]

    def is_valid_email(email):
        return "@" in email and any(email.endswith(domain) for domain in valid_domains)

    if not is_valid_email(recipient) or not is_valid_email(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка, является ли отправитель по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Примеры вызовов функции
send_email("Тестовое сообщение", "user@example.com")  # Успешная отправка
send_email("Тестовое сообщение", "user@example.com", sender="custom.sender@gmail.com")  # Нестандартный отправитель
send_email("Тестовое сообщение", "user@example")  # Некорректный e-mail
send_email("Тестовое сообщение", "university.help@gmail.com", sender="university.help@gmail.com")  # Отсылка самому себе
