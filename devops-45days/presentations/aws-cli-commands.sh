#!/bin/bash
# AWS CLI Commands for EC2 Web Server Setup
# Make sure AWS CLI is configured with: aws configure

# Variables (update these with your values)
REGION="us-east-1"
KEY_NAME="your-key-pair-name"
SECURITY_GROUP_NAME="web-server-sg"
INSTANCE_TYPE="t2.micro"
AMI_ID="ami-0abcdef1234567890"  # Amazon Linux 2 AMI (update with current AMI ID)

echo "=== AWS EC2 Web Server Setup Commands ==="

echo "1. Create Security Group"
aws ec2 create-security-group \
    --group-name $SECURITY_GROUP_NAME \
    --description "Security group for web server demo" \
    --region $REGION

echo "2. Add HTTP rule (port 80)"
aws ec2 authorize-security-group-ingress \
    --group-name $SECURITY_GROUP_NAME \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0 \
    --region $REGION

echo "3. Add SSH rule (port 22)"
aws ec2 authorize-security-group-ingress \
    --group-name $SECURITY_GROUP_NAME \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0 \
    --region $REGION

echo "4. Launch EC2 instance with User Data"
aws ec2 run-instances \
    --image-id $AMI_ID \
    --count 1 \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-groups $SECURITY_GROUP_NAME \
    --user-data file://userdata.sh \
    --region $REGION

echo "5. List running instances"
aws ec2 describe-instances \
    --query 'Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress,InstanceType]' \
    --output table \
    --region $REGION

echo "6. Get instance public IP (replace INSTANCE_ID)"
# aws ec2 describe-instances \
#     --instance-ids INSTANCE_ID \
#     --query 'Reservations[0].Instances[0].PublicIpAddress' \
#     --output text \
#     --region $REGION

echo "7. Stop instance (replace INSTANCE_ID)"
# aws ec2 stop-instances --instance-ids INSTANCE_ID --region $REGION

echo "8. Start instance (replace INSTANCE_ID)"
# aws ec2 start-instances --instance-ids INSTANCE_ID --region $REGION

echo "9. Terminate instance (replace INSTANCE_ID)"
# aws ec2 terminate-instances --instance-ids INSTANCE_ID --region $REGION

echo "10. Delete security group"
# aws ec2 delete-security-group --group-name $SECURITY_GROUP_NAME --region $REGION

echo ""
echo "=== Useful Commands ==="
echo "Check AWS CLI configuration:"
echo "aws configure list"
echo ""
echo "Get current AWS identity:"
echo "aws sts get-caller-identity"
echo ""
echo "List available AMIs (Amazon Linux 2):"
echo "aws ec2 describe-images --owners amazon --filters 'Name=name,Values=amzn2-ami-hvm-*' --query 'Images[*].[ImageId,Name,CreationDate]' --output table --region $REGION"
echo ""
echo "List key pairs:"
echo "aws ec2 describe-key-pairs --region $REGION"
