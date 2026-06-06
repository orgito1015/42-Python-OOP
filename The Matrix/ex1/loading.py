"""Exercise 1: Loading Programs - Data analysis: pandas/numpy/matplotlib."""

import importlib
import sys
from typing import Any

REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def check_dependencies() -> dict[str, Any]:
    """Check which packages are available and return their module objects."""
    print("Checking dependencies:")
    results: dict[str, Any] = {}

    for package, description in REQUIRED_PACKAGES.items():
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown")
            print(f"  [OK] {package} ({version}) - {description} ready")
            results[package] = mod
        except ImportError:
            print(f"  [MISSING] {package} - {description}")
            results[package] = None

    return results


def show_package_manager_comparison() -> None:
    """Show the differences between pip and Poetry package managers."""
    print()
    print("Package Manager Comparison: pip vs Poetry")
    print("=" * 50)
    print()
    print("  pip:")
    print("    - Built-in Python package installer")
    print("    - Uses requirements.txt for dependency lists")
    print("    - Install command: pip install -r requirements.txt")
    print("    - No built-in virtual environment management")
    print("    - No lock file by default (use pip freeze)")
    print()
    print("  Poetry:")
    print("    - Modern dependency and packaging manager")
    print("    - Uses pyproject.toml for project metadata")
    print("    - Install command: poetry install")
    print("    - Automatically manages virtual environments")
    print("    - Generates poetry.lock for reproducible installs")
    print()
    print("  This project supports both:")
    print("    pip    -> requirements.txt")
    print("    Poetry -> pyproject.toml")
    print()


def show_install_instructions() -> None:
    """Show installation instructions for missing packages."""
    print()
    print("To install missing dependencies:")
    print()
    print("  Using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("  Using Poetry:")
    print("    poetry install")


def run_analysis(modules: dict[str, Any]) -> None:
    """Run matrix data analysis using numpy, pandas and matplotlib."""
    np = modules["numpy"]
    pd = modules["pandas"]
    plt_mod = importlib.import_module("matplotlib.pyplot")

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(42)
    matrix_signal: Any = rng.normal(loc=0.0, scale=1.0, size=1000)
    matrix_noise: Any = rng.uniform(low=-0.5, high=0.5, size=1000)
    matrix_time: Any = np.linspace(0, 100, 1000)

    df = pd.DataFrame(
        {
            "time": matrix_time,
            "signal": matrix_signal,
            "noise": matrix_noise,
            "combined": matrix_signal + matrix_noise,
        }
    )

    print()
    print("Matrix Data Statistics:")
    print(df[["signal", "noise", "combined"]].describe().to_string())

    print()
    print("Generating visualization...")
    fig, axes = plt_mod.subplots(2, 1, figsize=(10, 6))

    axes[0].plot(
        df["time"], df["signal"],
        alpha=0.7, label="Matrix Signal", color="green"
    )
    axes[0].plot(
        df["time"], df["noise"],
        alpha=0.5, label="System Noise", color="red"
    )
    axes[0].set_title("The Matrix: Signal vs Noise")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].hist(
        df["combined"], bins=50,
        color="green", alpha=0.7, edgecolor="black"
    )
    axes[1].set_title("Distribution of Combined Matrix Data")
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")
    axes[1].grid(True, alpha=0.3)

    plt_mod.tight_layout()
    output_file = "matrix_analysis.png"
    plt_mod.savefig(output_file)
    plt_mod.close()

    print()
    print("Analysis complete!")
    print("Results saved to:")
    print(f"  {output_file}")


def main() -> None:
    """Entry point for the loading program."""
    print("LOADING STATUS: Loading programs...")
    print()

    modules = check_dependencies()

    missing = [
        pkg for pkg, mod in modules.items()
        if mod is None and pkg in REQUIRED_PACKAGES
    ]
    if missing:
        show_install_instructions()
        sys.exit(1)

    show_package_manager_comparison()
    run_analysis(modules)


if __name__ == "__main__":
    main()
