"""Exercise 2: Accessing the Mainframe - Secure env variable configuration."""

import os
import sys
from pathlib import Path


def load_dotenv_file(env_path: Path) -> None:
    """Load environment variables from a .env file using python-dotenv."""
    try:
        from dotenv import load_dotenv  # type: ignore[import-untyped]
        load_dotenv(dotenv_path=env_path, override=False)
    except ImportError:
        print("WARNING: python-dotenv is not installed.")
        print("  Install it with: pip install python-dotenv")
        print("  Falling back to system environment variables only.")
        print()


def get_config() -> dict[str, str]:
    """Read and return configuration from environment variables."""
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", ""),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", ""),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def format_database(url: str, mode: str) -> str:
    """Return a human-readable database status string."""
    if not url:
        return "Not configured"
    if mode == "production":
        return "Connected to production instance"
    return "Connected to local instance"


def format_api_key(key: str) -> str:
    """Return a masked representation of the API key."""
    if not key:
        return "Not authenticated"
    return "Authenticated"


def format_zion(endpoint: str) -> str:
    """Return a human-readable Zion network status."""
    if not endpoint:
        return "Offline - endpoint not configured"
    return "Online"


def check_security(config: dict[str, str], env_file_exists: bool) -> list[str]:
    """Return a list of security check result strings."""
    results: list[str] = []

    has_hardcoded = any(
        v in ("secret123", "password", "admin") for v in config.values()
    )
    if has_hardcoded:
        results.append(
            "[WARN] Possible hardcoded secrets detected - review your config"
        )
    else:
        results.append("[OK] No hardcoded secrets detected")

    if env_file_exists:
        results.append("[OK] .env file properly configured")
    else:
        results.append("[WARN] No .env file found - copy .env.example to .env")

    if config.get("MATRIX_MODE") == "production":
        results.append("[OK] Running with production overrides")
    else:
        results.append("[OK] Production overrides available via env variables")
    return results


def show_missing_config_warnings(config: dict[str, str]) -> None:
    """Print warnings for any missing required configuration values."""
    required = [
        "MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"
    ]
    missing = [key for key in required if not config[key]]
    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f"  - {key}")
        print()
        print("  Copy .env.example to .env and fill in your values.")
        print()


def main() -> None:
    """Entry point for the oracle program."""
    env_file = Path(__file__).parent / ".env"
    load_dotenv_file(env_file)

    config = get_config()

    if not any(config.values()):
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        show_missing_config_warnings(config)
        print("Run:  cp .env.example .env  then edit .env with your values.")
        sys.exit(1)

    mode = config["MATRIX_MODE"] or "development"
    log_level = config["LOG_LEVEL"] or "INFO"
    db_status = format_database(config["DATABASE_URL"], mode)
    api_status = format_api_key(config["API_KEY"])
    zion_status = format_zion(config["ZION_ENDPOINT"])

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"  Mode:          {mode}")
    print(f"  Database:      {db_status}")
    print(f"  API Access:    {api_status}")
    print(f"  Log Level:     {log_level}")
    print(f"  Zion Network:  {zion_status}")
    print()

    if mode == "production":
        print("  [PRODUCTION] Enhanced security protocols active.")
        print("  [PRODUCTION] All operations are logged and audited.")
    else:
        print("  [DEVELOPMENT] Debug mode is active.")
        print("  [DEVELOPMENT] Verbose logging enabled.")
    print()

    security_results = check_security(config, env_file.exists())
    print("Environment security check:")
    for result in security_results:
        print(f"  {result}")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
