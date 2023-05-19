####### create 3 instances through AWSCLI #######
#import boto3

# Create an EC2 resource object
#ec2 = boto3.resource('ec2')

# Create instances
#dev = ec2.create_instances(
#    ImageId='ami-04e914639d0cca79a',
#    InstanceType='t2.micro',
#    MaxCount=3,
#    MinCount=3,
#    TagSpecifications=[
#        {
#            'ResourceType': 'instance',
#            'Tags': [
#                {'Key': 'Name', 'Value': 'Development'},  # Tag for instance name
#                {'Key': 'ENV', 'Value': 'Development'}     # Tag for environment
#            ]
#        }
#    ]
#)

# Print the created instances
#print(dev)

###### Stop Instances #####
import boto3

# Create an EC2 resource object
ec2 = boto3.resource('ec2')

# Filter running instances with 'Development' tag
instances = ec2.instances.filter(
    Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},  # Filter for running instances
        {'Name': 'tag:ENV', 'Values': ['Development']}            # Filter for instances with 'Development' tag
    ]
)

# Stop each running instance
for instance in instances:
    try:
        instance.stop()  # Stop the instance
        print(f'{instance} all instances stopped')
    except:
        print(f'There are no more instances to be stopped')
