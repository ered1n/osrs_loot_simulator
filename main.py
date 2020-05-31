import requests

API_URL = "https://oldschool.runescape.wiki/api.php"
TITLE = "Abyssal_demon"

PARAMS = {
    "action": "parse",
    "page": TITLE,
    "prop": "wikitext",
    "section": 2,
    "format": "json"
}

def fetch_droprates():
    res = requests.get(url=API_URL, params=PARAMS)
    data = res.json()
    wikitext = data['parse']['wikitext']['*']
    lines = wikitext.splitlines()
    entries = []

    primary = []
    secondary = []
    tertiary = []

    for line in lines:
        line = line.strip()
        if line.startswith("="):
            print(line)

if __name__ == "__main__":
    fetch_droprates()
