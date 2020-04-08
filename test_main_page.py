URL = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_open_login_page(browser):
    browser.get(URL)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

    assert "login" in browser.current_url
