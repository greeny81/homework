
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    suff = (".com", ".ru", ".net")
    if recipient.find("@") == -1 or sender.find("@") == -1 or sender.endswith(suff) == False or recipient.endswith(suff) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')



#text_ = "sender"
#print(text_[-2:len(text_)])

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')