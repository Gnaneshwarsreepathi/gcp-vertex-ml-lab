import os
import joblib
from google.cloud import storage

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def upload_to_gcs(local_file, gcs_uri):
    if not gcs_uri.startswith("gs://"):
        raise ValueError("AIP_MODEL_DIR must be a gs:// path")

    artifact_filename = "model.joblib"
    destination_uri = os.path.join(gcs_uri, artifact_filename)

    client = storage.Client()
    blob = storage.blob.Blob.from_string(
        destination_uri,
        client=client
    )

    blob.upload_from_filename(local_file)

    print(f"Uploaded model artifact to: {destination_uri}")


def main():
    print("Loading Iris dataset")

    iris = load_iris()

    X = iris.data
    y = iris.target

    print("Splitting dataset")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training RandomForestClassifier")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Evaluating model")

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print(f"Accuracy: {accuracy}")

    local_model_path = "/tmp/model.joblib"

    joblib.dump(
        model,
        local_model_path
    )

    print(f"Saved local model: {local_model_path}")

    aip_model_dir = os.environ.get("AIP_MODEL_DIR")

    print(f"AIP_MODEL_DIR={aip_model_dir}")

    if not aip_model_dir:
        raise RuntimeError(
            "AIP_MODEL_DIR is missing. This script must run inside Vertex AI."
        )

    upload_to_gcs(
        local_model_path,
        aip_model_dir
    )

    print("Training job completed successfully")


if __name__ == "__main__":
    main()
