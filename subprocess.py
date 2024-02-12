import subprocess

def copy_gcs_bucket_to_s3(source_bucket, destination_bucket):
    command = [
        'gsutil',
        '-m',
        'cp',
        '-r',
        source_bucket,
        destination_bucket
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing gsutil command: {e}")
        print(e.stderr)