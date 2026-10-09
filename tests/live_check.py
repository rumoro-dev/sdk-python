"""The facade against a running app (tests/sdk-scenarios.mjs): RUMORO_API_URL and RUMORO_API_KEY name it. Prints ok."""

from __future__ import annotations

import asyncio
import os

from rumoro import AsyncRumoro, Rumoro, RumoroError

url, key = os.environ["RUMORO_API_URL"], os.environ["RUMORO_API_KEY"]
rumoro = Rumoro(key, base_url=url)

assert rumoro.auth.whoami().workspace.name == "SDK workspace"
keyword = rumoro.keywords.create(term="pyword", kind="topic", platforms=["x"])
assert [item.id for item in rumoro.keywords.list(kind=["topic"]).data] == [keyword.id]
assert rumoro.keywords.update(keyword.id, context="Python check").context == "Python check"
try:
    rumoro.keywords.create(term="pyword", kind="topic")
    raise AssertionError("a duplicate was accepted")
except RumoroError as error:
    assert (error.status, error.code) == (409, "duplicate_keyword")

# The three fixture mentions, two to a page.
first = rumoro.mentions.search(limit=2)
second = rumoro.mentions.search(limit=2, cursor=first.next_cursor)
assert len(first.data) == 2 and len(second.data) == 1
assert {m.post.platform.value for m in rumoro.mentions.search(platforms=["x"]).data} == {"x"}
assert len(rumoro.mentions.export().strip().splitlines()) == 4
assert len(rumoro.mentions.export_json(not_sentiments=["negative"]).data) == 3
assert rumoro.channels.list().data == []
assert rumoro.keywords.delete(keyword.id) is None


async def check_async() -> None:
    async with AsyncRumoro(key, base_url=url) as client:
        assert (await client.auth.whoami()).workspace.name == "SDK workspace"


asyncio.run(check_async())
print("ok")
