from pathlib import Path

# Absolute path to the project root (basketballshooter).
ROOT_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT_DIR / "assets"


def asset_path(*parts):
    """Build an absolute path under the assets folder."""
    return str(ASSETS_DIR.joinpath(*parts))
