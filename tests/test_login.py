from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Validation
    assert "inventory.html" in page.url
    assert page.locator(".title").text_content() == "Products"

def test_failed_login(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("locked_out_user", "wrong_password")
    
    # Check error message visibility
    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.error_message.text_content()

def test_dashboard_load(page):
    page.goto("https://saucedemo.com")
    
    assert page.title() == "FAIL"
