# Disable all records in the hosted zone, except the default NS and SOA records.
import boto3
import copy


def disable_dns_records(hosted_zone_id, hosted_zone_name):
    client = boto3.client('route53')
    records = client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id
    )

    for record in records["ResourceRecordSets"]:
        if record["Name"] != f'{hosted_zone_name}.':
            new_record = copy.copy(record)
            new_record["Name"] = f'disable_{record["Name"]}'

            response = client.change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch={
                    'Changes': [
                        {
                            'Action': 'CREATE',
                            'ResourceRecordSet': new_record
                        }, {
                            'Action': 'DELETE',
                            'ResourceRecordSet': record
                        },
                    ]
                }
            )


if __name__ == "__main__":
    HOSTED_ZONE_ID = input('Enter the Hosted Zone ID: ')
    HOSTED_ZONE_NAME = input('Enter the Hosted Zone Name: ')
    disable_dns_records(HOSTED_ZONE_ID, HOSTED_ZONE_NAME)
