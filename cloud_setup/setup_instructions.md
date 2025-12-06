# Cloud Data Warehouse Setup Instructions

This project uses **Google Cloud Storage (GCS)** as the cloud layer for hosting the transformed bikeshare dataset.

## Steps Performed

1. Created a Google Cloud project.
2. Created a GCS bucket named `metro-bikeshare-storage`.
3. Uploaded the cleaned ETL output file `transformed_trips.csv` to GCS.
4. Configured public or private IAM access depending on usage.
5. The dataset can now be accessed by external tools such as Tableau or scripts via signed URLs.

## Files Included
- `transformed_trips.csv` (cleaned ETL output)
- Short instructions for accessing the cloud bucket.

This satisfies the cloud data warehouse requirement for CIS 9440 Assignment 2.
