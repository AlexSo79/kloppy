import logging
import sys

from kloppy import datasets


def main():
    """
    This example shows the use of Metrica datasets, and how we can pass argument
    to the dataset loader.
    """
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # The metrica dataset loader loads by default the 'game1' dataset
    dataset = datasets.load(
        "metrica_tracking", options={"sample_rate": 1.0 / 12, "limit": 10}
    )
    print(len(dataset.frames))

    # We can pass additional keyword arguments to the loaders to specify a different dataset
    dataset = datasets.load(
        "metrica_tracking", options={"limit": 1000}, game="game2"
    )

    data_frame = dataset.to_pandas()
    print(data_frame)


if __name__ == "__main__":
    main()
