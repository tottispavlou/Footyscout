from pathlib import Path
import requests

URL = (
    "https://pub-e682421888d945d684bcae8890b0ec20.r2.dev/"
    "data/transfermarkt-datasets.duckdb"
)

OUTPUT = Path("data/raw/transfermarkt/transfermarkt.duckdb")


def download_transfermarkt():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if OUTPUT.exists():
        print(f"Transfermarkt database already exists at: {OUTPUT}")
        return

    print("Downloading Transfermarkt database...")

    with requests.get(URL, stream=True) as response:
        response.raise_for_status()

        with open(OUTPUT, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    download_transfermarkt()