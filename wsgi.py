"""App entry point."""
from ghost_automation import create_admin_session
from config import Config

if __name__ == "__main__":
    create_admin_session(Config)
