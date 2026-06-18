import os
from google.cloud import aiplatform

PROJECT_ID = os.environ["PROJECT_ID"]
REGION = os.environ["REGION"]
ENDPOINT_ID = input("Enter ENDPOINT_ID: ").strip()

endpoint_name = f"projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}"

aiplatform.init(
    project=PROJECT_ID,
    location=REGION
)

endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)

instances = [
    [5.9, 3.0, 5.1, 1.8]
]

response = endpoint.predict(instances=instances)

print(response)
