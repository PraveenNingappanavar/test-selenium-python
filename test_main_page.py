from pages.main_page import MainPage

URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_open_login_page(browser):
    main_page = MainPage(browser, URL)

    main_page.open()
    main_page.go_to_login_page()

    assert "login" in browser.current_url
