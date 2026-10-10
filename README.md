# Rumoro Python SDK

[![PyPI](https://img.shields.io/pypi/v/rumoro?label=pypi)](https://pypi.org/project/rumoro/)
[![Python](https://img.shields.io/pypi/pyversions/rumoro)](https://pypi.org/project/rumoro/)
[![license](https://img.shields.io/pypi/l/rumoro)](./LICENSE)
[![docs](https://img.shields.io/badge/docs-docs.rumoro.dev-blue)](https://docs.rumoro.dev/sdks/python)

Python access to [Rumoro](https://rumoro.dev), the social listening API for developers and AI agents. Rumoro picks up posts about your product, your competitors and your market on Reddit, X, Hacker News, GitHub, Bluesky, LinkedIn, Stack Overflow, DEV, YouTube, TikTok, Instagram and news, and rates each for relevance, sentiment and intent.

One client object gives you every endpoint as a method, generated from Rumoro's OpenAPI document. It's fully typed, works on Python 3.11 and later, and comes in sync and async versions.

## Install

```bash
pip install rumoro
```

You need an API key (it starts with `ref_`). Create one on the API keys page of the dashboard, or with `rumoro.api_keys.create(...)` using an existing key. New accounts include $5.80 of credit, no card required.

## First request

```python
from rumoro import Rumoro

rumoro = Rumoro(api_key="ref_...")

# Start tracking a product name on Hacker News and X.
keyword = rumoro.keywords.create(term="basil deploy", kind="brand", platforms=["hackernews", "x"])

# Fetch the latest relevant mentions.
for mention in rumoro.mentions.search(platform="hackernews", relevant=True, limit=25).data:
    print(mention.post.platform.value, mention.classification.relevance, mention.post.url)
```

## Client options

```python
rumoro = Rumoro(
    api_key="ref_...",                    # required
    base_url="https://api.rumoro.dev",    # only if you run your own deployment
    timeout=30.0,                         # seconds; None waits indefinitely
)
```

You can pass enum values as plain strings (`platform="hackernews"`). Times can be passed as a `datetime`, as ISO 8601 text or as epoch milliseconds. Request bodies accept a dict, a model instance, or the fields as keyword arguments.

## Recipes

### Fetch a week of mentions, page by page

```python
from datetime import datetime, timedelta, timezone

since = datetime.now(timezone.utc) - timedelta(days=7)
cursor = None
while True:
    page = rumoro.mentions.search(since=since, relevant=True, limit=100, cursor=cursor)
    for mention in page.data:
        print(mention.post.url)
    cursor = page.next_cursor
    if not cursor:
        break
```

### Buying signals from accounts with reach

```python
leads = rumoro.mentions.search(intent="buy_intent", min_followers=1000, sort="priority")
```

`intent` takes any of the classifier's 15 tags, such as `buy_intent`, `question`, `complaint`, `bug_report`, `churn_intent` or `pricing`. The [OpenAPI document](https://api.rumoro.dev/v1/openapi.json) lists them all. With `sort="priority"`, recent, relevant posts from people with reach come first.

### Close or dismiss mentions

```python
rumoro.mentions.update("mm_7f3a...", status="done", note="answered in the thread")
rumoro.mentions.update("mm_9c1b...", status="ignored")
```

### Send purchase intent to Slack as it happens

```python
slack = next(c for c in rumoro.channels.list().data if c.kind == "slack")

rumoro.alerts.create(
    name="Purchase intent",
    mode="instant",
    filter={"intents": ["buy_intent"], "minRelevance": 40},
    channelIds=[slack.id],
)
```

Body fields keep the API's own names (`channelIds`, `minRelevance`), while query parameters are snake_case (`min_followers`). `rumoro.channels.create(...)` adds email and webhook channels, and Slack channels once your Slack workspace is connected in the dashboard. Telegram chats are connected in the dashboard only. `rumoro.alerts.test(id)` fires a test delivery, and `rumoro.alerts.run(id)` delivers a digest alert's current period right away.

### Reports

```python
summary = rumoro.analytics.summary(range_="30d", compare=True, timezone="Europe/Vienna")
by_platform = rumoro.analytics.breakdown(range_="30d", by="platform")
sov = rumoro.analytics.share_of_voice(range_="90d")
```

### Tag influential authors

```python
people = rumoro.people.list(platforms=["x"], min_followers=5000)
rumoro.people.update(people.data[0].id, tags=["influencer"])
```

### Export to CSV

```python
csv_text = rumoro.mentions.export(since="2026-10-01T00:00:00Z")
```

## Async

For `asyncio`, `AsyncRumoro` offers the same methods.

```python
import asyncio
from rumoro import AsyncRumoro

async def main() -> None:
    rumoro = AsyncRumoro(api_key="ref_...")
    page = await rumoro.mentions.search(relevant=True, limit=10)
    for mention in page.data:
        print(mention.post.url)

asyncio.run(main())
```

## Errors

Failed requests raise `RumoroError`, which carries the HTTP `status` plus the API's `code` and `message`.

```python
from rumoro import Rumoro, RumoroError

try:
    rumoro.keywords.create(term="basil", kind="brand")
except RumoroError as err:
    if err.code == "duplicate_keyword":
        pass                          # this term is already tracked
    elif err.code == "insufficient_balance":
        print("add funds on the Billing page")
    elif err.code == "rate_limited":
        print("wait before retrying")
    else:
        raise
```

The codes you're most likely to see are `unauthorized`, `forbidden`, `read_only_key`, `validation_error`, `not_found`, `invalid_cursor`, `rate_limited`, `duplicate_keyword`, `insufficient_balance`, `keyword_limit_reached`, `upstream_unavailable`, `internal_error`.

## Method index

| Area | Methods |
| --- | --- |
| `rumoro.keywords` | `create`, `list`, `get`, `update`, `delete`, `health` |
| `rumoro.groups` | `create`, `list`, `get`, `update`, `delete` |
| `rumoro.mentions` | `search`, `get`, `update`, `export`, `export_json` |
| `rumoro.attention` | `list`, `dismiss` |
| `rumoro.views` | `create`, `list`, `get`, `update`, `delete` |
| `rumoro.filters` | `get`, `update` |
| `rumoro.people` | `list`, `get`, `update`, `merge`, `split`, `export`, `activities`, `log_activity`, `delete_activity` |
| `rumoro.segments` | `create`, `list`, `get`, `update`, `delete` |
| `rumoro.alerts` | `create`, `list`, `get`, `update`, `delete`, `test`, `run`, `mute`, `unmute` |
| `rumoro.channels` | `create`, `list`, `get`, `update`, `delete`, `test`, `rotate_secret`, `deliveries` |
| `rumoro.analytics` | `summary`, `series`, `breakdown`, `share_of_voice`, `reviews` |
| `rumoro.company` | `get`, `update` |
| `rumoro.members` | `list`, `remove`, `invitations`, `invite`, `revoke_invitation` |
| `rumoro.usage` | `get`, `breakdown` |
| `rumoro.billing` | `wallet`, `ledger`, `top_up`, `invoices`, `invoice_url` |
| `rumoro.api_keys` | `create`, `list`, `revoke` |
| `rumoro.auth` | `whoami` |
| `rumoro.system` | `health` |

Anything the client object doesn't wrap is still reachable through the generated modules in `rumoro.api` and `rumoro.models`.

## Prefer MCP?

Agents can use the same operations as MCP tools. In Claude Code, run this.

```bash
claude mcp add --transport http rumoro https://mcp.rumoro.dev/mcp
```

## Requirements

- Python 3.11 or later
- An API key from the Rumoro dashboard

## Links

- [Documentation](https://docs.rumoro.dev/sdks/python)
- [OpenAPI document](https://api.rumoro.dev/v1/openapi.json)
- [Dashboard](https://app.rumoro.dev)

To regenerate the SDK from a Rumoro checkout, run `scripts/generate.sh` in `packages/sdk-python`.

## License

MIT.
