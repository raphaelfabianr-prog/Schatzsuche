import json
from pathlib import Path
import qrcode
BASE_URL = "https://DEINE-GITHUB-PAGES-URL-HIER"
ROOT = Path(__file__).parent
stations = json.loads((ROOT / "stations.json").read_text(encoding="utf-8"))
if "DEINE-GITHUB-PAGES-URL-HIER" in BASE_URL: raise SystemExit("Trage zuerst die echte Website-Adresse bei BASE_URL ein.")
for i,s in enumerate(stations,1):
    url=BASE_URL.rstrip("/")+"/"+s["token"]
    qrcode.make(url).save(ROOT/"qr-codes"/f"posten-{i:02d}.png")
    print(f"Posten {i}: {url}")
