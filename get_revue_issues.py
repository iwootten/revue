import os
from datetime import datetime

import requests
from slugify import slugify
from markdownify import markdownify as md

REVUE_KEY = os.getenv("REVUE_API_KEY")

r = requests.get(
    "https://www.getrevue.co/api/v2/issues",
    headers={"Authorization": f"Bearer {REVUE_KEY}"},
)

if not os.path.exists("issues/html"):
    os.makedirs("issues/html")

if not os.path.exists("issues/markdown"):
    os.makedirs("issues/markdown")

for issue in r.json():
    sent_at = datetime.fromisoformat(issue["sent_at"])
    slug = slugify(f"{sent_at.date()}-{issue['title']}")

    with open(f"issues/html/{slug}.html", "w+") as issue_file, open(
        f"issues/markdown/{slug}.md", "w+"
    ) as markdown_file:
        markdown = md(issue["html"])

        issue_file.write(issue["html"])
        markdown_file.write(markdown)
