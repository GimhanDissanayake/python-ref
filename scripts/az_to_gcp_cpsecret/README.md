## Install dependancies
```commandline
pip install -r requirements.txt
```

## Authenticate to Azure and GCP
```commandline
az login
gcloud auth application-default login
```

## Execute main.py
```commandline
python main.py

Enter the key vault name: 
Enter the GCP Project ID: 
```

## Use this function to delete the secret: delet_secrets_from_gcp(gcp_project_id, exported_secrets)