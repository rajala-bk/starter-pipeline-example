import os

fixture = os.environ.get("MY_FIXTURE", "not set")
print(f"MY_FIXTURE is: {fixture}")
print("Script completed successfully.")