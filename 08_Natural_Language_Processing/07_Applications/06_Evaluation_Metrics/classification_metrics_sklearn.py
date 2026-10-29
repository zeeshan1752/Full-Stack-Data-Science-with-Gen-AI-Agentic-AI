"""Calculate common classification metrics for a tiny illustrative example."""

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def evaluate_classification(true_labels, predicted_labels):
    """Return common binary classification metrics and the confusion matrix."""
    return {
        "accuracy": accuracy_score(true_labels, predicted_labels),
        "precision": precision_score(
            true_labels, predicted_labels, zero_division=0
        ),
        "recall": recall_score(true_labels, predicted_labels, zero_division=0),
        "f1": f1_score(true_labels, predicted_labels, zero_division=0),
        "confusion_matrix": confusion_matrix(
            true_labels, predicted_labels, labels=[0, 1]
        ).tolist(),
    }


def main() -> None:
    true_labels = [1, 0, 1, 1, 0, 0]
    predicted_labels = [1, 0, 0, 1, 0, 1]
    for name, value in evaluate_classification(
        true_labels, predicted_labels
    ).items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
