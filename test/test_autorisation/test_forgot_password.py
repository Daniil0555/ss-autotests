def test_page_login_validation(app):
    app.open_home_page()
    app.forgot.open_page_forgot_password()
    app.forgot.fill_disabled_email_and_submit(email="")
    app.forgot.fill_disabled_email_and_submit(email="smalik007")
    app.forgot.fill_disabled_email_and_submit(email="smalik007@mail.ru")
    app.forgot.fill_disabled_email_and_submit(email="вафпывапы")
    app.forgot.fill_email_and_submit(email="smalik007+42262@mail.ru") # Урезать дизейбл логин - не вызывать параметры явно, а через ENV
    # Нужно дописать проверку отправленного письма в меилкетчере