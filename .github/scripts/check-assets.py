"""Validate tracked logo bytes without modifying image data or filenames."""
from pathlib import Path
import subprocess
import warnings

from PIL import Image

count = 0
errors = []
# NUL-delimited paths preserve accented, quoted and whitespace-containing names.
paths = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
for name in filter(None, paths):
    path = Path(name)
    if path.suffix.lower() != ".png":
        continue
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with Image.open(path) as picture:
                assert picture.format == "PNG", "Logo is not a PNG"
                assert picture.width > 0 and picture.height > 0, "Empty image"
                picture.verify()
            # verify checks PNG chunks; load also checks the compressed pixel stream.
            with Image.open(path) as picture:
                picture.load()
        count += 1
    except (OSError, ValueError, AssertionError, Warning) as error:
        errors.append(f"{name}: {error}")
assert count > 0, "No logos were validated"
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated and decoded {count} PNG logos")
