from pathlib import Path
from zipfile import ZipFile
root = Path(__file__).resolve().parent
for archive in sorted(root.glob("yahwa-source-*.zip")):
    with ZipFile(archive) as z:
        z.extractall(root)
print("Source extracted. Run: python -m http.server 8000 --directory app")
