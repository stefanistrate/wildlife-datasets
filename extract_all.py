from pathlib import Path

from wildlife_datasets import datasets

if __name__ == "__main__":
    for dataset in datasets.names_all:
        print("EXTRACTING:", dataset.display_name())

        base_dir = Path("data") / dataset.display_name()
        already_downloaded = base_dir / "already_downloaded"
        if not already_downloaded.exists():
            print(">>> MISSING:", dataset.display_name())
            continue
        already_extracted = base_dir / "already_extracted"
        if already_extracted.exists():
            print("ALREADY EXTRACTED")
            continue

        try:
            dataset.extract(base_dir)
        except Exception as e:
            print(">>> FAILED:", dataset.display_name())
            continue

        with open(already_extracted, "w"):
            pass
        print("FINISHED EXTRACTING.")
