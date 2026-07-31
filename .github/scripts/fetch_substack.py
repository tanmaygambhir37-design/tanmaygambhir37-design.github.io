"""Writes posts.json from the Substack RSS feed.

The page used to read the feed in the visitor's browser through third-party
CORS proxies (corsproxy.io, allorigins.win). That put every visitor's request
through a service neither of us controls, and left the section blank whenever
one of them was rate-limited. Fetching here instead means the page loads its
own data, same-origin and immediately.
"""

import json
import pathlib
import urllib.request
from xml.etree import ElementTree

FEED = "https://tanmaydiary.substack.com/feed"
LIMIT = 3
OUTPUT = pathlib.Path(__file__).resolve().parents[2] / "posts.json"


def text_of(item, tag: str) -> str:
    node = item.find(tag)
    return (node.text or "").strip() if node is not None else ""


def main() -> None:
    request = urllib.request.Request(FEED, headers={"User-Agent": "tanmaygambhir37-design.github.io"})
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ElementTree.fromstring(response.read())

    posts = [
        {
            "title": text_of(item, "title"),
            "link": text_of(item, "link"),
            "date": text_of(item, "pubDate"),
        }
        for item in root.findall("./channel/item")[:LIMIT]
    ]
    posts = [p for p in posts if p["title"] and p["link"]]

    # A malformed or empty response must not blank the section on the live site.
    if not posts:
        raise SystemExit("feed returned no usable items — leaving posts.json untouched")

    OUTPUT.write_text(json.dumps(posts, indent=2) + "\n")
    print(f"wrote {len(posts)} posts to {OUTPUT.name}")


if __name__ == "__main__":
    main()
