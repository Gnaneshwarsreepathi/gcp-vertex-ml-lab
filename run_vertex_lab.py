
import os
from google.cloud import aiplatform

PROJECT_ID = os.environ["PROJECT_ID"]
REGION = os.environ["REGION"]
BUCKET = os.environ["BUCKET"]

TRAINING_CONTAINER = "us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-6:latest"
PREDICTION_CONTAINER = "us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-6:latest"


def main():
    aiplatform.init(
        project=PROJECT_ID,
        location=REGION,
        staging_bucket=f"gs://{BUCKET}"
    )

    print("Starting Vertex AI custom training job")

    job = aiplatform.CustomTrainingJob(
        display_name="iris-sklearn-training-job",
        script_path="train.py",
        container_uri=TRAINING_CONTAINER,
        requirements=["google-cloud-storage"],
        model_serving_container_image_uri=PREDICTION_CONTAINER
    )

    model = job.run(
        model_display_name="iris-random-forest-model",
        replica_count=1,
        machine_type="n1-standard-4",
        base_output_dir=f"gs://{BUCKET}/vertex-output",
        sync=True
    )

    print("Training completed")
    print(f"MODEL_RESOURCE_NAME={model.resource_name}")
    print(f"MODEL_ID={model.name}")

    print("Deploying model to Vertex AI endpoint")

    endpoint = model.deploy(
        deployed_model_display_name="iris-rf-v1",
        machine_type="n1-standard-2",
        min_replica_count=1,
        max_replica_count=1,
        traffic_percentage=100,
        sync=True
    )

    print("Deployment completed")
    print(f"ENDPOINT_RESOURCE_NAME={endpoint.resource_name}")
    print(f"ENDPOINT_ID={endpoint.name}")

    print("Testing online prediction")

    instances = [
        [5.1, 3.5, 1.4, 0.2],
        [6.7, 3.1, 4.7, 1.5],
        [7.2, 3.6, 6.1, 2.5]
    ]

    prediction = endpoint.predict(
        instances=instances
    )

    print("Prediction response")
    print(prediction)

    print("LAB_OUTPUT_START")
    print(f"PROJECT_ID={PROJECT_ID}")
    print(f"REGION={REGION}")
    print(f"BUCKET={BUCKET}")
    print(f"MODEL_ID={model.name}")
    print(f"ENDPOINT_ID={endpoint.name}")
    print("LAB_OUTPUT_END")


if __name__ == "__main__":
    main()
