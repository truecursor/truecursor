import random
from pathlib import Path
import re

STATUSES = [
    "cursor locked. executing.<br>",
    "enhanced precision mode disabled.<br>",
    "signal stable. iterating quietly.<br>",
    "input → output.<br>",
    "small commits, big ideas.<br>",
]

readme_path = Path("README.md")
text = readme_path.read_text()

new_status = random.choice(STATUSES)

pattern = r"<!--STATUS_START-->(.|\n)*?<!--STATUS_END-->"
replacement = f"<!--STATUS_START-->\n{new_status}\n<!--STATUS_END-->"
new_text = re.sub(pattern, replacement, text)

readme_path.write_text(new_text)
