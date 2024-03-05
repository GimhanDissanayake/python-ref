from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from google.cloud import secretmanager

def export_from_azure(keyvault_name, azure_tenant_id):
    # Authenticate to Azure Key Vault
    credential = DefaultAzureCredential(authority="https://login.microsoftonline.com/" + azure_tenant_id)
    secret_client = SecretClient(vault_url=f"https://{keyvault_name}.vault.azure.net", credential=credential)

    secrets = secret_client.list_properties_of_secrets()
    exported_secrets = {}
    for secret in secrets:
        secret_bundle = secret_client.get_secret(secret.name)
        exported_secrets[secret.name] = secret_bundle.value

    print('Secret export is completed')
    return exported_secrets

def import_to_gcp(project_id, secrets):
    # Authenticate to GCP Secret Manager
    client = secretmanager.SecretManagerServiceClient()

    for secret_name, secret_value in secrets.items():
        # Create a secret payload
        payload = {"data": secret_value.encode("UTF-8")}

        # Build the parent resource name
        parent = f"projects/{project_id}"

        # Create the secret
        secret_id = f"{parent}/secrets/{secret_name}"
        secret = {"replication": {"automatic": {}}}
        try:
            created_secret = client.create_secret(request={"parent": parent, "secret_id": secret_name, "secret": secret})
        except Exception as error:
            print("An exception occurred:", error)
            break
        # Add the secret version.
        version = client.add_secret_version(request={"parent": created_secret.name, "payload": payload})

        print(f'Secret "{created_secret.name}" created.')

def delet_secrets_from_gcp(project_id, secrets):
    # Authenticate to GCP Secret Manager
    client = secretmanager.SecretManagerServiceClient()

    for secret_name, secret_value in secrets.items():
        # Build the parent resource name
        parent = f"projects/{project_id}"

        # Create the secret
        secret_id = f"{secret_name}"

        # Build the resource name of the secret.
        name = client.secret_path(project_id, secret_id)

        # Delete the secret.
        client.delete_secret(request={"name": name})
        print(f'Secret "{secret_name}" Deleted.')

if __name__ == "__main__":
    # Azure Key Vault details
    azure_tenant_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    print(f'Tenant Id is set to {azure_tenant_id} | xxxxxxxxxxxxxxx.onmicrosoft.com')
    azure_keyvault_name = input('Enter the key vault name: ')
    # GCP Project ID
    gcp_project_id = input('Enter the GCP Project ID: ')

    # Export secrets from Azure Key Vault
    exported_secrets = export_from_azure(azure_keyvault_name, azure_tenant_id)

    # Import secrets to GCP Secret Manager
    import_to_gcp(gcp_project_id, exported_secrets)

    # # Delete secrets
    # delet_secrets_from_gcp(gcp_project_id, exported_secrets)