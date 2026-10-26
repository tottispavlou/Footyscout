from pathlib import Path
import subprocess

DATA_DIR = Path("data/raw/statsbomb")

REPO_URL = "https://github.com/statsbomb/open-data.git"


def download_statsbomb():
    DATA_DIR.parent.mkdir(parents=True, exist_ok=True)

    if DATA_DIR.exists():
        print("StatsBomb data already exists.")
        return

    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            REPO_URL,
            str(DATA_DIR),
        ],
        check=True,
    )

    print("StatsBomb Open Data downloaded.")


if __name__ == "__main__":
    download_statsbomb()