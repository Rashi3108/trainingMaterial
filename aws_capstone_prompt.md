Create a complete beginner-friendly AWS capstone project using **only
AWS Console (GUI) steps**. Do NOT use CLI or IaC. Please follow the
requirements below:

## 🎯 Objective

Build a simple but realistic architecture demonstrating how AWS services
integrate. You may choose appropriate services from: - VPC - EC2 - S3 -
Lambda - Auto Scaling Group (ASG) - Application Load Balancer (ALB) -
API Gateway (REST) - RDS or DynamoDB - ElastiCache (optional)

You do NOT need to use all services --- only enough to form a clean
beginner-level architecture.

Use an example project theme such as: **"Todo App Backend"** or
**"Simple Notes API"**.

## 📘 Output Format

Produce everything in **Markdown format** and include:

### 1. Step-by-step instructions using **AWS Console (GUI)** for:

-   Creating the VPC
-   Creating subnets, route tables, IGW/NAT (if needed)
-   Creating EC2 instance OR Lambda
-   Creating S3 bucket
-   Creating DynamoDB or RDS
-   Creating ALB & target groups (if EC2 is used)
-   Creating Auto Scaling Group (if applicable)
-   Creating API Gateway REST API
-   Wiring API Gateway → Lambda or ALB
-   Testing end-to-end

Every step must have: - Navigation path (e.g., "Go to AWS Console → EC2
→ Instances → Launch Instance") - What to click - What to enter in input
boxes - Screenshots references like "(screenshot: Instance Launch page)"
*(no real image required)*

### 2. Create a fully structured **project folder layout** such as:

    capstone-project/
     ├── README.md
     ├── architecture/
     │    └── diagram.mmd
     ├── docs/
     │    └── step-by-step-instructions.md
     ├── lambda/
     │    └── index.py
     └── sample-data/
          └── test-event.json

### 3. Provide all required **files/content** inside the markdown (code blocks):

-   Lambda function code (Python or Node)
-   Sample API Gateway test event
-   Example response JSON
-   Sample HTML for S3 (if needed)

### 4. Include an **architecture diagram** using Mermaid:

-   Show flow from user → API Gateway → Lambda → DynamoDB/S3, etc.
-   Or user → ALB → EC2 → DB

### 5. Provide a simple **README.md** summarizing the project.

### 6. Keep everything beginner-friendly:

-   Explain WHY each service is created
-   Explain how each integrates with others
-   Highlight best practices in simple terms

## 📌 Important

All steps MUST be **console-based (GUI)**.\
No Terraform.\
No CLI.\
No SDK.

Create the entire project in one complete Markdown output.
