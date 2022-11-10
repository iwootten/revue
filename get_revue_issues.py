import os
from datetime import datetime

import requests
from slugify import slugify

REVUE_KEY = os.getenv('REVUE_API_KEY')

r = requests.get('https://www.getrevue.co/api/v2/issues', headers={
    "Authorization": f"Bearer {REVUE_KEY}"
})

if not os.path.exists("issues"):
    os.makedirs("issues")

for issue in r.json():
    sent_at = datetime.fromisoformat(issue["sent_at"])
    slug = slugify(f"{sent_at.date()}-{issue['title']}")

    with open(f"issues/{slug}.html", "w+") as issue_file:
        issue_file.write(issue['html'])
