install:
	uv sync

build:
	uv build --out-dir ./dist

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games
