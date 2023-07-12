# noaa-hurricane-tracking

This repository contains the latest data from NOAA. The data is replicated from S3 to GitHub on a daily basis.

## Contents
The repository contains the following files:
- replicate_s3_folder.yaml: A Git action that replicates the S3 folder which belongs to Kin Insurance to this GitHub repo (STORMNAME/geojson/). This git action runs at 10am UTC daily.
- newest_data_geojson.py: A Python script which is triggered by that finds the latest data for each storm and copies it to a folder called newest_data for each storm (STORMNAME/newest_data/).

## Usage

This repo is intended to be ingested by Looker. The newest_data folders will have consistand names, but updated data. This is to simplify the connection looker needs to make. 

