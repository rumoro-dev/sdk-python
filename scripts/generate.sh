#!/bin/sh
# Regenerates rumoro/ from packages/sdk/openapi.json (run `npm run export-openapi` in packages/sdk first), then the facade.
# Needs .venv with openapi-python-client and ruff: python3 -m venv .venv && .venv/bin/pip install openapi-python-client ruff
set -e
cd "$(dirname "$0")/.."
PATH="$PWD/.venv/bin:$PATH" openapi-python-client generate --path ../sdk/openapi.json --config generator.yml --output-path rumoro --meta none --overwrite
.venv/bin/python scripts/generate_facade.py
