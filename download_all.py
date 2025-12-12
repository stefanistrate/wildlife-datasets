from wildlife_datasets import datasets

if __name__ == "__main__":
    for dataset in datasets.names_all:
        try:
            dataset.download("data/" + dataset.display_name())
        except Exception as e:
            print(">>> FAILED:", dataset.display_name())
