from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        # Structural mapping using specific data-test attributes
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """Executes navigation using the dynamically injected framework URL context."""
        self.page.goto(self.base_url)

    def login(self, username, password):
        """Encapsulates the UI interaction sequence with explicit synchronization."""
        self.username_input.wait_for(state='visible', timeout=5000)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
