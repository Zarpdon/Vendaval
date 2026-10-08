from pathlib import Path


def load_stylesheet() -> str:
    path = Path(__file__).parent.parent / "ui" / "styles.qss"

    with open(path, "r", encoding="utf-8") as file:
        return file.read()