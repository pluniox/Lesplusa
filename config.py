from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

DATA_URLS = {
    "caracteristiques": (
        "https://static.data.gouv.fr/resources/"
        "bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-"
        "routiere-annees-de-2005-a-2021/20231005-093927/carcteristiques-2022.csv"
    ),
    "lieux": (
        "https://static.data.gouv.fr/resources/"
        "bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-"
        "routiere-annees-de-2005-a-2021/20231005-094112/lieux-2022.csv"
    ),
    "usagers": (
        "https://static.data.gouv.fr/resources/"
        "bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-"
        "routiere-annees-de-2005-a-2021/20231005-094229/usagers-2022.csv"
    ),
}

RAW_FILENAMES = {
    "caracteristiques": "caracteristiques_2022.csv",
    "lieux": "lieux_2022.csv",
    "usagers": "usagers_2022.csv",
}

