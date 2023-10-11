import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Specify the S3 bucket name and folder (prefix)
bucket_name = 'kin-sandbox-tmpdatalake-raw'
folder_path = 'noaa/cat-event/wsp/2023/'  # Include the trailing slash to specify a folder

# Specify the file extension you want to filter by
file_extension = '.geojson'

# Initialize the continuation token
continuation_token = None

# Initialize a list to store file names
file_names = []

# List objects in the folder with paging
loop = 1
while True:
    if continuation_token:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_path, ContinuationToken=continuation_token)
    else:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)

    # Filter and add file names with the specified extension to the list
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith(file_extension):
            file_names.append(key)

    # Check if there are more objects to paginate through
    if response.get('IsTruncated', False):
        continuation_token = response['NextContinuationToken']
    else:
        break

    # loop +=1 
    # if loop == 3:
    #     break

print(file_names)

newest_data_lin_5day = (sorted([file_name for file_name in file_names if "5day_lin" in file_name], reverse=True)[0], "5day_lin")
newest_data_pgn_5day = (sorted([file_name for file_name in file_names if "5day_pgn" in file_name], reverse=True)[0], "5day_pgn")
newest_data_pts_5day = (sorted([file_name for file_name in file_names if "5day_pts" in file_name], reverse=True)[0], "5day_pts")
newest_data_lin = (sorted([file_name for file_name in file_names if ("lin" in file_name and "5day" not in file_name)], reverse=True)[0], "lin")
newest_data_pts = (sorted([file_name for file_name in file_names if ("pts" in file_name and "5day" not in file_name)], reverse=True)[0], "pts")
newest_data_radii = (sorted([file_name for file_name in file_names if ("radii" in file_name and "5day" not in file_name)], reverse=True)[0], "radii")
newest_data_windswath = (sorted([file_name for file_name in file_names if ("windswath" in file_name and "5day" not in file_name)], reverse=True)[0], "windswath")
#need to separate out storms from windspeed
newest_data_wsp34knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp34knt120hr_5km" in file_name], reverse=True)[0], "wsp34knt120hr_5km")
newest_data_wsp34knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp34knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp34knt120hr_halfDeg")
newest_data_wsp50knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp50knt120hr_5km" in file_name], reverse=True)[0], "wsp50knt120hr_5km")
newest_data_wsp50knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp50knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp50knt120hr_halfDeg")
newest_data_wsp64knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp64knt120hr_5km" in file_name], reverse=True)[0], "wsp64knt120hr_5km")
newest_data_wsp64knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp64knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp64knt120hr_halfDeg")

for file in [newest_data_wsp34knt120hr_5km, newest_data_wsp34knt120hr_halfDeg, newest_data_wsp50knt120hr_5km, newest_data_wsp50knt120hr_halfDeg, newest_data_wsp64knt120hr_5km, newest_data_wsp64knt120hr_halfDeg, newest_data_lin_5day, newest_data_pgn_5day, newest_data_pts_5day, newest_data_lin, newest_data_pts, newest_data_radii, newest_data_windswath]:
    print(file)

