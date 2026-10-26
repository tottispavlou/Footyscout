from pathlib import Path
import requests

OUTPUT = Path("data/raw/clubelo/elo.csv")

URL = "RAW_GITHUB_CSV_URL_HERE"


def download_clubelo():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(URL)
    response.raise_for_status()

    OUTPUT.write_bytes(response.content)

    print(f"Saved Elo data to {OUTPUT}")


if __name__ == "__main__":
    download_clubelo()