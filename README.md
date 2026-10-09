# Rumoro Python SDK

[![PyPI](https://img.shields.io/pypi/v/rumoro?label=pypi)](https://pypi.org/project/rumoro/)
[![Python](https://img.shields.io/pypi/pyversions/rumoro)](https://pypi.org/project/rumoro/)
[![license](https://img.shields.io/pypi/l/rumoro)](./LICENSE)
[![docs](https://img.shields.io/badge/docs-docs.rumoro.dev-blue)](https://docs.rumoro.dev/sdks/python)

Social listening for developers and AI agents, in Python. [Rumoro](https://rumoro.dev) watches Reddit, X, Hacker News, GitHub, Bluesky, LinkedIn, Stack Overflow, DEV, YouTube, TikTok, Instagram and news for your product, your competitors and your topics, and scores every mention for relevance, sentiment and intent. This package is the official Python client for its API: one object with one call per endpoint, generated from the OpenAPI document. It supports Python 3.11+, sync and async, and is fully typed.

## Installation

```bash
pip install rumoro
```

## Quick start

```python
from rumoro import Rumoro

rumoro = Rumoro(api_key="ref_...")

# Track a keyword on two platforms.
keyword = rumoro.keywords.create(term="acme cloud", kind="brand", platforms=["hackernews", "x"])

# Read what arrived, relevant posts only, newest first.
for mention in rumoro.mentions.search(platform="hackernews", relevant=True, limit=25).data:
    print(mention.post.platform.value, mention.classification.relevance, mention.post.url)
```

Create an API key in the dashboard (API keys), or call `rumoro.api_keys.create(...)` with an existing key. Keys start with `ref_`. Every account starts with $5.80 of credit, and no card is needed.

## Configuration

```python
rumoro = Rumoro(
    api_key="ref_...",                    # required
    base_url="https://api.rumoro.dev",    # another deployment's host, if you run one
    timeout=30.0,                         # seconds, or None for no timeout
)
```

Enum-valued arguments take plain strings (`platform="hackernews"`). Instants take a `datetime`, an ISO 8601 string, or epoch milliseconds. Bodies take a dict, a model, or their fields as keyword arguments.

## Examples

### Page through every mention of the last week

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

### Filter by intent and sentiment

```python
hot = rumoro.mentions.search(intent="buy_intent", sentiment="negative", min_followers=1000, sort="priority")
```

The intents are `buy_intent`, `question`, `complaint`, `praise` and `comparison`, and topic tags such as `bug_report` and `pricing` filter the same way. `sort="priority"` puts fresh, relevant, high-reach posts first.

### Triage

```python
rumoro.mentions.update("mm_7f3a...", status="done", note="replied 2026-10-03")
rumoro.mentions.update("mm_9c1b...", status="ignored")
```

### An instant Slack alert for buying signals

```python
slack = next(c for c in rumoro.channels.list().data if c.kind == "slack")

rumoro.alerts.create(
    name="Buying signals",
    mode="instant",
    filter={"intents": ["buy_intent"], "minRelevance": 40},
    channelIds=[slack.id],
)
```

Body fields keep the API's names (`channelIds`, `minRelevance`); query parameters are snake_case (`min_followers`). Create Slack, Telegram, email and webhook channels with `rumoro.channels.create(...)`. `rumoro.alerts.test(id)` sends a sample, and `rumoro.alerts.run(id)` sends a digest alert's latest window now.

### Analytics

```python
summary = rumoro.analytics.summary(range_="30d", compare=True, timezone="Europe/Berlin")
by_platform = rumoro.analytics.breakdown(range_="30d", by="platform")
sov = rumoro.analytics.share_of_voice(range_="90d")
```

### People

```python
people = rumoro.people.list(platforms=["x"], min_followers=5000)
rumoro.people.update(people.data[0].id, tags=["influencer"], muted=False)
```

### CSV export

```python
csv_text = rumoro.mentions.export(since="2026-09-01T00:00:00Z")
```

## Async

`AsyncRumoro` mirrors every call for `asyncio`:

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

## Error handling

A non-2xx response raises `RumoroError` with the API's `status`, `code` and `message`:

```python
from rumoro import Rumoro, RumoroError

try:
    rumoro.keywords.create(term="acme", kind="brand")
except RumoroError as err:
    if err.code == "duplicate_keyword":
        pass                          # already tracked
    elif err.code == "insufficient_balance":
        print("top up from Billing")
    elif err.code == "rate_limited":
        print("slow down")
    else:
        raise
```

Common codes: `unauthorized`, `forbidden`, `read_only_key`, `validation_error`, `not_found`, `invalid_cursor`, `rate_limited`, `duplicate_keyword`, `insufficient_balance`, `keyword_limit_reached`, `upstream_unavailable`, `internal_error`.

## SDK reference

| Resource | Methods |
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

The generated low-level client and models live under `rumoro.api` and `rumoro.models`, for anything the facade does not cover.

## MCP server

The same API is available to MCP clients as tools. In Claude Code:

```bash
claude mcp add --transport http rumoro https://mcp.rumoro.dev/mcp
```

## Requirements

- Python 3.11+
- A Rumoro API key

## Links

- [Documentation](https://docs.rumoro.dev)
- [OpenAPI document](https://api.rumoro.dev/v1/openapi.json)
- [Dashboard](https://app.rumoro.dev)

Regenerate from a checkout with `scripts/generate.sh` in `packages/sdk-python`.

## License

MIT.
