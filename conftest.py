import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """Resolves and injects the target infrastructure environment URL."""
    return os.getenv("BASE_URL", "https://www.saucedemo.com")

@pytest.fixture(scope="session")
def env_credentials():
      """Securely provisions runtime credentials isolated from the source repository."""
      return {
            "user": os.getenv("TEST_USER"),
            "pass": os.getenv("TEST_PASSWORD")
      }

@pytest.fixture(scope="function")
def api_context(playwright, base_url):
        """
        Provisions an isolated API request context for backend integration testing.
        Dynamically inherits the session-scoped base_url to eliminate hardcoded strings.
        """
        request_context = playwright.request.new_context(base_url=base_url)
        yield request_context
        request_context.dispose()

@pytest.fixture(scope="function", autouse=True)
def execution_telemetry():
    """Custom context interceptor tracking system execution lifecycles."""
    print("\n[SUITE LIFE-CYCLE] Spawning isolated browser worker instance...")
    yield
    print("\n[SUITE LIFE-CYCLE] Tearing down worker execution thread. Tracing dump completed.")