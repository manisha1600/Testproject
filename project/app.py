from models import User
from utils.logging_utils import get_logger


def main():
    logger = get_logger("project.app")

    user = User(id=1, name="Alice", email="alice@example.com")
    logger.info("Created user: %s", user)

    # simulate an action
    logger.debug("Performing a sample action for user %s (id=%d)", user.name, user.id)

    print("Done. Check logs or console output.")


if __name__ == "__main__":
    main()
