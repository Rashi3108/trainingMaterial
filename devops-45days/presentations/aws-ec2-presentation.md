# AWS EC2 Introduction and Hands-On Demo

## Table of Contents
1. [What is AWS?](#what-is-aws)
2. [Introduction to EC2](#introduction-to-ec2)
3. [EC2 Key Concepts](#ec2-key-concepts)
4. [Hands-On Demo](#hands-on-demo)
   - [Method 1: EC2 with User Data](#method-1-ec2-with-user-data)
   - [Method 2: EC2 without User Data](#method-2-ec2-without-user-data)
5. [Best Practices](#best-practices)
6. [Cost Optimization](#cost-optimization)

---

## What is AWS?

**Amazon Web Services (AWS)** is a comprehensive cloud computing platform provided by Amazon.

### Key Benefits:
- **Scalability**: Scale resources up or down based on demand
- **Cost-Effective**: Pay only for what you use
- **Global Reach**: Data centers worldwide
- **Security**: Enterprise-grade security features
- **Reliability**: 99.99% uptime SLA

### Popular AWS Services:
- **EC2**: Virtual servers in the cloud
- **S3**: Object storage service
- **RDS**: Managed database service
- **Lambda**: Serverless computing
- **VPC**: Virtual private cloud networking

---

## Introduction to EC2

**Amazon Elastic Compute Cloud (EC2)** provides scalable virtual servers in the cloud.

### What is EC2?
- Virtual machines running in AWS data centers
- Complete control over the operating system
- Flexible instance types for different workloads
- Pay-per-use pricing model

### Use Cases:
- Web applications and websites
- Development and testing environments
- Big data processing
- Machine learning workloads
- Enterprise applications

---

## EC2 Key Concepts

### Instance Types
- **t2.micro**: 1 vCPU, 1 GB RAM (Free tier eligible)
- **t3.small**: 2 vCPU, 2 GB RAM
- **m5.large**: 2 vCPU, 8 GB RAM
- **c5.xlarge**: 4 vCPU, 8 GB RAM (Compute optimized)

### Amazon Machine Images (AMI)
- Pre-configured templates for instances
- Contains OS, applications, and configurations
- Popular AMIs: Amazon Linux 2, Ubuntu, Windows Server

### Security Groups
- Virtual firewalls for EC2 instances
- Control inbound and outbound traffic
- Rules based on protocols, ports, and IP ranges

### Key Pairs
- Secure login credentials for EC2 instances
- Public-private key cryptography
- Required for SSH access to Linux instances

---

## Hands-On Demo

We'll create two EC2 instances to host a simple web server:
1. **Method 1**: Using User Data (automated setup)
2. **Method 2**: Manual setup after instance creation

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured (optional)
- Basic understanding of Linux commands

---

## Method 1: EC2 with User Data

User Data allows you to run scripts automatically when an EC2 instance starts.

### Step 1: Launch EC2 Instance with User Data

**User Data Script:**
```bash
#!/bin/bash
# Update the system
yum update -y

# Install Apache HTTP Server
yum install -y httpd

# Start and enable Apache
systemctl start httpd
systemctl enable httpd

# Create a simple web page
cat > /var/www/html/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First AWS Web Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #232f3e;
            text-align: center;
        }
        p {
            color: #666;
            line-height: 1.6;
            font-size: 18px;
        }
        .aws-logo {
            text-align: center;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My AWS EC2 Web Server!</h1>
        <div class="aws-logo">🚀</div>
        <p>
            Congratulations! You have successfully deployed a web server on Amazon EC2 
            using User Data automation. This page was created automatically when the 
            instance started, demonstrating the power of infrastructure as code and 
            automated deployments in the cloud.
        </p>
        <p>
            <strong>Instance Details:</strong><br>
            - Created with User Data script<br>
            - Running Apache HTTP Server<br>
            - Hosted on Amazon Linux 2<br>
            - Deployed in AWS EC2
        </p>
    </div>
</body>
</html>
EOF

# Set proper permissions
chown apache:apache /var/www/html/index.html
chmod 644 /var/www/html/index.html
```

### Step 2: AWS CLI Commands (Alternative)

```bash
# Create security group
aws ec2 create-security-group \
    --group-name web-server-sg \
    --description "Security group for web server" \
    --region us-east-1

# Add HTTP rule to security group
aws ec2 authorize-security-group-ingress \
    --group-name web-server-sg \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0 \
    --region us-east-1

# Add SSH rule to security group
aws ec2 authorize-security-group-ingress \
    --group-name web-server-sg \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0 \
    --region us-east-1

# Launch EC2 instance with user data
aws ec2 run-instances \
    --image-id ami-0abcdef1234567890 \
    --count 1 \
    --instance-type t2.micro \
    --key-name your-key-pair \
    --security-groups web-server-sg \
    --user-data file://userdata.sh \
    --region us-east-1
```

---

## Method 2: EC2 without User Data

Manual setup after instance creation.

### Step 1: Launch Basic EC2 Instance

1. **Launch Instance**: Create a basic Amazon Linux 2 instance
2. **Security Group**: Allow HTTP (port 80) and SSH (port 22)
3. **Key Pair**: Select or create a key pair for SSH access

### Step 2: Connect and Configure Manually

```bash
# Connect to your instance
ssh -i "your-key.pem" ec2-user@your-instance-public-ip

# Update the system
sudo yum update -y

# Install Apache HTTP Server
sudo yum install -y httpd

# Start and enable Apache
sudo systemctl start httpd
sudo systemctl enable httpd

# Check Apache status
sudo systemctl status httpd
```

### Step 3: Create Web Page

```bash
# Create the HTML file
sudo tee /var/www/html/index.html > /dev/null << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Manual AWS Web Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #e8f4f8;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #232f3e;
            text-align: center;
            border-bottom: 3px solid #ff9900;
            padding-bottom: 10px;
        }
        p {
            color: #555;
            line-height: 1.6;
            font-size: 18px;
        }
        .manual-badge {
            background-color: #ff9900;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            display: inline-block;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Manually Configured Web Server!</h1>
        <div class="manual-badge">Manually Configured</div>
        <p>
            This web server was set up manually after launching the EC2 instance. 
            This approach gives you complete control over the installation process 
            and allows you to customize each step according to your specific requirements.
        </p>
        <p>
            <strong>Setup Process:</strong><br>
            1. Launched basic EC2 instance<br>
            2. Connected via SSH<br>
            3. Manually installed Apache<br>
            4. Created this custom web page<br>
            5. Configured proper permissions
        </p>
        <p>
            Both automated (User Data) and manual approaches have their advantages. 
            Choose the method that best fits your workflow and requirements!
        </p>
    </div>
</body>
</html>
EOF

# Set proper permissions
sudo chown apache:apache /var/www/html/index.html
sudo chmod 644 /var/www/html/index.html

# Restart Apache to ensure everything is working
sudo systemctl restart httpd
```

---

## Comparison: User Data vs Manual Setup

| Aspect | User Data | Manual Setup |
|--------|-----------|--------------|
| **Automation** | Fully automated | Manual intervention required |
| **Consistency** | Same setup every time | Potential for human error |
| **Speed** | Fast deployment | Slower, step-by-step |
| **Debugging** | Harder to troubleshoot | Easy to debug each step |
| **Flexibility** | Limited to script capabilities | Full control over process |
| **Learning** | Less hands-on learning | Better for understanding |

---

## Best Practices

### Security
- **Principle of Least Privilege**: Only open necessary ports
- **Regular Updates**: Keep OS and applications updated
- **Key Management**: Secure your private keys
- **Security Groups**: Use specific IP ranges when possible

### Performance
- **Right-sizing**: Choose appropriate instance types
- **Monitoring**: Use CloudWatch for performance metrics
- **Auto Scaling**: Scale based on demand
- **Load Balancing**: Distribute traffic across instances

### Cost Management
- **Instance Scheduling**: Stop instances when not needed
- **Reserved Instances**: For predictable workloads
- **Spot Instances**: For fault-tolerant applications
- **Regular Reviews**: Monitor and optimize costs

---

## Cost Optimization

### Free Tier Benefits
- **750 hours** of t2.micro instances per month
- **30 GB** of EBS storage
- **15 GB** of bandwidth out

### Cost-Saving Tips
1. **Use t2.micro** for development and testing
2. **Stop instances** when not in use
3. **Delete unused EBS volumes**
4. **Monitor billing** regularly
5. **Use AWS Cost Calculator** for estimates

### Monitoring Commands
```bash
# Check running instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]' --output table

# Stop an instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Start an instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Terminate an instance (permanent)
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

---

## Troubleshooting Common Issues

### Web Server Not Accessible
1. **Check Security Group**: Ensure port 80 is open
2. **Verify Apache Status**: `sudo systemctl status httpd`
3. **Check Instance State**: Ensure instance is running
4. **Firewall**: Check if local firewall is blocking

### SSH Connection Issues
1. **Key Permissions**: `chmod 400 your-key.pem`
2. **Security Group**: Ensure port 22 is open
3. **Public IP**: Use correct public IP address
4. **Username**: Use `ec2-user` for Amazon Linux

### User Data Not Working
1. **Check Logs**: `/var/log/cloud-init-output.log`
2. **Script Errors**: Verify bash syntax
3. **Permissions**: Ensure script has proper permissions
4. **AMI Compatibility**: Some AMIs may not support user data

---

## Next Steps

### Advanced Topics to Explore
- **Auto Scaling Groups**: Automatically scale instances
- **Load Balancers**: Distribute traffic across multiple instances
- **CloudFormation**: Infrastructure as Code
- **Docker on EC2**: Containerized applications
- **CI/CD Pipelines**: Automated deployments

### Additional AWS Services
- **RDS**: Managed databases
- **S3**: Object storage for static assets
- **CloudFront**: Content delivery network
- **Route 53**: DNS management
- **Certificate Manager**: SSL/TLS certificates

---

## Conclusion

You've successfully learned how to:
- ✅ Understand AWS and EC2 fundamentals
- ✅ Create EC2 instances with automated setup (User Data)
- ✅ Manually configure web servers on EC2
- ✅ Deploy simple web applications
- ✅ Apply security best practices
- ✅ Optimize costs and performance

**Remember**: Always follow the principle of least privilege and regularly review your AWS resources to optimize costs and security.

---

## Resources

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
