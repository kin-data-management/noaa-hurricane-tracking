import os
import re
import shutil

def get_storm_paths():
    paths = []
    cwd = os.getcwd()
    for path, subdirs, files in os.walk(cwd):
        if re.match(r"^.*/geojson", path):
            paths.append(path.replace(cwd + "/", ""))
    return paths

def get_files_in_folder(folder_path):
  files = []
  for file in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file)):
      files.append(file)
  return files

storm_paths = get_storm_paths()

for storm in storm_paths:
    storm_name = storm.split('/')[0]
    print(f"getting geojson for {storm_name}")

    file_names = get_files_in_folder(storm)
    
    newest_data = []
    try:
      newest_data_lin_5day = (sorted([file_name for file_name in file_names if "5day_lin" in file_name], reverse=True)[0], "5day_lin")
      newest_data.append(newest_data_lin_5day)
    except:
      pass
    try:
      newest_data_pgn_5day = (sorted([file_name for file_name in file_names if "5day_pgn" in file_name], reverse=True)[0], "5day_pgn")
      newest_data.append(newest_data_pgn_5day)
    except:
      pass
    try:
      newest_data_pts_5day = (sorted([file_name for file_name in file_names if "5day_pts" in file_name], reverse=True)[0], "5day_pts")
      newest_data.append(newest_data_pts_5day)
    except:
      pass
    try:
      newest_data_lin = (sorted([file_name for file_name in file_names if ("lin" in file_name and "5day" not in file_name)], reverse=True)[0], "lin")
      newest_data.append(newest_data_lin)
    except:
      pass
    try:
      newest_data_pts = (sorted([file_name for file_name in file_names if ("pts" in file_name and "5day" not in file_name)], reverse=True)[0], "pts")
      newest_data.append(newest_data_pts)
    except:
      pass
    try:
      newest_data_radii = (sorted([file_name for file_name in file_names if ("radii" in file_name and "5day" not in file_name)], reverse=True)[0], "radii")
      newest_data.append(newest_data_radii)
    except:
      pass
    try:
      newest_data_windswath = (sorted([file_name for file_name in file_names if ("windswath" in file_name and "5day" not in file_name)], reverse=True)[0], "windswath")
      newest_data.append(newest_data_windswath)
    except:
      pass
    try:
      newest_data_wsp34knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp34knt120hr_5km" in file_name], reverse=True)[0], "wsp34knt120hr_5km")
      newest_data.append(newest_data_wsp34knt120hr_5km)
    except:
      pass
    try:
      newest_data_wsp34knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp34knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp34knt120hr_halfDeg")
      newest_data.append(newest_data_wsp34knt120hr_halfDeg)
    except:
      pass
    try:
      newest_data_wsp50knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp50knt120hr_5km" in file_name], reverse=True)[0], "wsp50knt120hr_5km")
      newest_data.append(newest_data_wsp50knt120hr_5km)
    except:
      pass
    try:
      newest_data_wsp50knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp50knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp50knt120hr_halfDeg")
      newest_data.append(newest_data_wsp50knt120hr_halfDeg)
    except:
      pass
    try:
      newest_data_wsp64knt120hr_5km = (sorted([file_name for file_name in file_names if "wsp64knt120hr_5km" in file_name], reverse=True)[0], "wsp64knt120hr_5km")
      newest_data.append(newest_data_wsp64knt120hr_5km)
    except:
      pass
    try:
      newest_data_wsp64knt120hr_halfDeg = (sorted([file_name for file_name in file_names if "wsp64knt120hr_halfDeg" in file_name], reverse=True)[0], "wsp64knt120hr_halfDeg")
      newest_data.append(newest_data_wsp64knt120hr_halfDeg)
    except:
      pass
    
    for file in newest_data:
        src = f"{storm}/{file[0]}"
        dest = f"{storm_name}/newest_data/{file[1]}.geojson"
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(src, dest) 
