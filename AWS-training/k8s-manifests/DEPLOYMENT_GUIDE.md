# Kubernetes nginx Deployment Guide for Amazon EKS

This guide provides step-by-step instructions for deploying nginx on Amazon EKS using all major Kubernetes objects.

## Prerequisites

- AWS CLI configured with appropriate permissions
- kubectl installed and configured
- eksctl installed (recommended)
- Helm installed (for AWS Load Balancer Controller)

## 1. Create EKS Cluster

### Using eksctl (Recommended)
```bash
# Create cluster
eksctl create cluster \
  --name nginx-cluster \
  --region us-west-2 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 3 \
  --nodes-min 1 \
  --nodes-max 4 \
  --managed

# Update kubeconfig
aws eks update-kubeconfig --region us-west-2 --name nginx-cluster
```

### Verify Cluster
```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

## 2. Install AWS Load Balancer Controller

### Create IAM OIDC Provider
```bash
eksctl utils associate-iam-oidc-provider \
  --region=us-west-2 \
  --cluster=nginx-cluster \
  --approve
```

### Create IAM Service Account
```bash
eksctl create iamserviceaccount \
  --cluster=nginx-cluster \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name "AmazonEKSLoadBalancerControllerRole" \
  --attach-policy-arn=arn:aws:iam::aws:policy/ElasticLoadBalancingFullAccess \
  --approve
```

### Install Controller
```bash
# Install CRDs
kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"

# Add Helm repo
helm repo add eks https://aws.github.io/eks-charts
helm repo update

# Install controller
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=nginx-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

## 3. Deploy nginx Application

### Option A: Deploy Complete Application
```bash
kubectl apply -f nginx-complete-app.yaml
```

### Option B: Deploy Individual Components
```bash
# Create namespace first
kubectl create namespace nginx-app

# Deploy components in order
kubectl apply -f nginx-configmap.yaml -n nginx-app
kubectl apply -f nginx-secret.yaml -n nginx-app
kubectl apply -f nginx-deployment.yaml -n nginx-app
kubectl apply -f nginx-service.yaml -n nginx-app
kubectl apply -f nginx-ingress.yaml -n nginx-app
```

## 4. Verify Deployment

### Check All Resources
```bash
kubectl get all -n nginx-app
```

### Check Specific Resources
```bash
# Pods
kubectl get pods -n nginx-app -o wide

# Services
kubectl get services -n nginx-app

# Ingress
kubectl get ingress -n nginx-app

# ConfigMaps and Secrets
kubectl get configmaps,secrets -n nginx-app
```

### Check Pod Logs
```bash
kubectl logs -f deployment/nginx-deployment -n nginx-app
```

### Describe Resources (for troubleshooting)
```bash
kubectl describe deployment nginx-deployment -n nginx-app
kubectl describe service nginx-service -n nginx-app
kubectl describe ingress nginx-ingress -n nginx-app
```

## 5. Access the Application

### Get LoadBalancer URL
```bash
kubectl get service nginx-service -n nginx-app -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

### Get Ingress URL
```bash
kubectl get ingress nginx-ingress -n nginx-app -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

### Port Forward (for testing)
```bash
kubectl port-forward service/nginx-service 8080:80 -n nginx-app
# Access at http://localhost:8080
```

## 6. Scaling and Updates

### Manual Scaling
```bash
kubectl scale deployment nginx-deployment --replicas=5 -n nginx-app
```

### Auto-scaling
```bash
kubectl autoscale deployment nginx-deployment --cpu-percent=50 --min=1 --max=10 -n nginx-app
kubectl get hpa -n nginx-app
```

### Rolling Updates
```bash
# Update image
kubectl set image deployment/nginx-deployment nginx=nginx:1.22 -n nginx-app

# Check rollout status
kubectl rollout status deployment/nginx-deployment -n nginx-app

# Rollback if needed
kubectl rollout undo deployment/nginx-deployment -n nginx-app
```

## 7. Monitoring

### Resource Usage
```bash
kubectl top nodes
kubectl top pods -n nginx-app
```

### Events
```bash
kubectl get events -n nginx-app --sort-by='.lastTimestamp'
```

### Logs
```bash
# All pods
kubectl logs -l app=nginx -n nginx-app

# Specific pod
kubectl logs <pod-name> -n nginx-app

# Follow logs
kubectl logs -f deployment/nginx-deployment -n nginx-app
```

## 8. Troubleshooting

### Common Issues

1. **ImagePullBackOff**
   ```bash
   kubectl describe pod <pod-name> -n nginx-app
   # Check image name and registry access
   ```

2. **CrashLoopBackOff**
   ```bash
   kubectl logs <pod-name> -n nginx-app
   # Check application logs and resource limits
   ```

3. **Service Not Accessible**
   ```bash
   kubectl get endpoints -n nginx-app
   # Verify selectors match pod labels
   ```

4. **Ingress Not Working**
   ```bash
   kubectl describe ingress nginx-ingress -n nginx-app
   # Check ingress controller and DNS settings
   ```

### Debug Commands
```bash
# Execute commands in pod
kubectl exec -it <pod-name> -n nginx-app -- /bin/bash

# Check service endpoints
kubectl get endpoints nginx-service -n nginx-app

# Test connectivity
kubectl run test-pod --image=busybox -it --rm -- wget -qO- nginx-service.nginx-app.svc.cluster.local
```

## 9. Cleanup

### Delete Application
```bash
kubectl delete -f nginx-complete-app.yaml
# OR
kubectl delete namespace nginx-app
```

### Delete Cluster
```bash
eksctl delete cluster --name nginx-cluster --region us-west-2
```

## 10. Best Practices

### Security
- Use IAM roles for service accounts (IRSA)
- Enable Pod Security Standards
- Use network policies
- Scan images for vulnerabilities
- Rotate secrets regularly

### Resource Management
- Set resource requests and limits
- Use horizontal pod autoscaling
- Implement cluster autoscaling
- Monitor resource usage

### Deployment
- Use rolling updates
- Implement health checks
- Use namespaces for isolation
- Version your manifests
- Test in staging first

### Monitoring
- Use Prometheus and Grafana
- Enable CloudWatch Container Insights
- Set up alerting
- Monitor application metrics

## File Structure

```
k8s-manifests/
├── nginx-pod.yaml              # Basic pod manifest
├── nginx-deployment.yaml       # Deployment with replicas
├── nginx-service.yaml          # Service (LoadBalancer, ClusterIP, NodePort)
├── nginx-configmap.yaml        # Configuration data
├── nginx-secret.yaml           # Sensitive data
├── nginx-ingress.yaml          # HTTP/HTTPS routing
├── nginx-complete-app.yaml     # All-in-one manifest
└── DEPLOYMENT_GUIDE.md         # This guide
```

## Next Steps

1. Explore Helm for package management
2. Implement CI/CD pipelines
3. Learn about service mesh (Istio/App Mesh)
4. Study advanced networking and security
5. Practice with different application types
