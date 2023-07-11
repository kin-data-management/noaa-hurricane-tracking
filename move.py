import boto3
import os


def replicate_s3_folder(s3_bucket, s3_folder, git_repo):
    """Replicates the contents of an S3 folder to a Git repo.

    Args:
      s3_bucket: The name of the S3 bucket.
      s3_folder: The name of the S3 folder to replicate.
      git_repo: The path to the Git repo.
    """

    s3 = boto3.resource("s3")
    for file in s3.Bucket(s3_bucket).objects.filter(Prefix=s3_folder):
        file_name = file.key.split("/")[-1]
        file_path = os.path.join(git_repo, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(file.content)


if __name__ == "__main__":
    s3_bucket = "kin-sandbox-tmpdatalake-raw"
    s3_folder = "noaa/cat_event/ARLENE/geojson/"
    git_repo = (
        "https://github.com/kin-data-management/noaa-hurricane-tracking/tree/main/"
    )
    replicate_s3_folder(s3_bucket, s3_folder, git_repo)
