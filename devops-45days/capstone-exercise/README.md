# 🚀 DevOps Automation Capstone Exercise

## 📋 Exercise Overview

**Scenario:** You're a DevOps engineer tasked with creating an automated deployment system for a web application. This exercise integrates all the knowledge from the scripting presentation: Linux commands, Python programming, and YAML configuration.

**Duration:** 2-3 hours  
**Difficulty:** Intermediate to Advanced  
**Skills Tested:** Linux, Python, YAML, Shell Scripting, Problem Solving

## 🎯 Learning Objectives

By completing this exercise, participants will demonstrate their ability to:
- ✅ Use Linux commands for system operations
- ✅ Write Python scripts for automation
- ✅ Create and validate YAML configurations
- ✅ Integrate multiple technologies in a real-world scenario
- ✅ Apply DevOps best practices
- ✅ Debug and troubleshoot issues

## 🏗️ Project Structure

You'll build a complete deployment automation system with these components:

```
deployment-automation/
├── config/
│   ├── app-config.yml          # Application configuration
│   ├── deployment-config.yml   # Deployment settings
│   └── monitoring-config.yml   # Monitoring setup
├── scripts/
│   ├── deploy.py              # Main deployment script
│   ├── health_check.py        # Health monitoring script
│   └── cleanup.py             # Cleanup and rollback script
├── templates/
│   ├── nginx.conf.j2          # Nginx configuration template
│   └── docker-compose.yml.j2  # Docker compose template
├── logs/
│   └── deployment.log         # Deployment logs
├── deploy.sh                  # Main deployment shell script
└── README.md                  # Project documentation
```

## 📝 Exercise Tasks

### Phase 1: Environment Setup & Linux Commands (30 minutes)

#### Task 1.1: Create Project Structure
```bash
# Use Linux commands to create the complete directory structure
# Include proper permissions and ownership
```

#### Task 1.2: System Information Gathering
```bash
# Create a script that gathers system information using Linux commands:
# - OS version and architecture
# - Available disk space
# - Memory usage
# - Network interfaces
# - Running services
# - Docker/container runtime status
```

#### Task 1.3: Log Management
```bash
# Set up log rotation and management
# Create directories with proper permissions
# Implement log cleanup policies
```

### Phase 2: YAML Configuration Files (45 minutes)

#### Task 2.1: Application Configuration (`config/app-config.yml`)
Create a comprehensive application configuration file:

```yaml
# Requirements:
# - Application metadata (name, version, environment)
# - Database connection settings
# - API endpoints and authentication
# - Feature flags and toggles
# - Resource limits and scaling parameters
# - Security settings
# - Logging configuration
# - Must pass yamllint validation
```

#### Task 2.2: Deployment Configuration (`config/deployment-config.yml`)
Create deployment-specific settings:

```yaml
# Requirements:
# - Deployment strategy (rolling, blue-green, canary)
# - Container image details
# - Port mappings and networking
# - Volume mounts and storage
# - Environment variables
# - Health check endpoints
# - Rollback configuration
# - Must be valid YAML with proper formatting
```

#### Task 2.3: Monitoring Configuration (`config/monitoring-config.yml`)
Create monitoring and alerting configuration:

```yaml
# Requirements:
# - Metrics collection settings
# - Alert thresholds and rules
# - Notification channels
# - Dashboard configurations
# - Log aggregation settings
# - Performance monitoring
# - Must follow YAML best practices
```

### Phase 3: Python Automation Scripts (60 minutes)

#### Task 3.1: Main Deployment Script (`scripts/deploy.py`)
Create a comprehensive Python deployment script:

```python
# Requirements:
# - Read and validate YAML configurations
# - Implement command-line argument parsing
# - Perform pre-deployment checks
# - Execute deployment steps with error handling
# - Generate deployment reports
# - Log all operations with timestamps
# - Support dry-run mode
# - Implement rollback functionality
# - Use functions for code reusability
# - Include proper error handling and logging
```

#### Task 3.2: Health Check Script (`scripts/health_check.py`)
Create a health monitoring system:

```python
# Requirements:
# - Check application health endpoints
# - Monitor system resources (CPU, memory, disk)
# - Validate database connectivity
# - Test API endpoints
# - Generate health reports
# - Send alerts for failures
# - Support multiple check types
# - Include retry logic and timeouts
# - Log all health check results
```

#### Task 3.3: Cleanup Script (`scripts/cleanup.py`)
Create a cleanup and maintenance script:

```python
# Requirements:
# - Clean up old deployment artifacts
# - Manage log file rotation
# - Remove unused Docker images/containers
# - Archive old configurations
# - Generate cleanup reports
# - Support different cleanup policies
# - Include safety checks to prevent data loss
# - Implement confirmation prompts for destructive operations
```

### Phase 4: Template Management (30 minutes)

#### Task 4.1: Nginx Configuration Template (`templates/nginx.conf.j2`)
Create a dynamic Nginx configuration template:

```nginx
# Requirements:
# - Use Jinja2 templating syntax
# - Support multiple server blocks
# - Include SSL/TLS configuration
# - Implement load balancing
# - Add security headers
# - Configure logging
# - Support environment-specific settings
```

#### Task 4.2: Docker Compose Template (`templates/docker-compose.yml.j2`)
Create a dynamic Docker Compose template:

```yaml
# Requirements:
# - Multi-service application stack
# - Environment variable substitution
# - Volume and network configuration
# - Health checks and restart policies
# - Resource limits
# - Dependency management
# - Support for different environments
```

### Phase 5: Integration & Shell Scripting (45 minutes)

#### Task 5.1: Main Deployment Script (`deploy.sh`)
Create a master shell script that orchestrates everything:

```bash
# Requirements:
# - Parse command-line arguments
# - Validate prerequisites
# - Execute Python scripts in correct order
# - Handle errors and provide meaningful messages
# - Support different deployment modes
# - Generate summary reports
# - Include help documentation
# - Implement logging and progress indicators
```

#### Task 5.2: Integration Testing
Create tests to validate the complete system:

```bash
# Requirements:
# - Test YAML configuration validation
# - Test Python script functionality
# - Test template rendering
# - Test end-to-end deployment flow
# - Test rollback procedures
# - Test error handling scenarios
```

## 🎯 Specific Requirements

### Linux Commands Usage
Your solution must demonstrate proficiency with:
- File and directory operations (`mkdir`, `chmod`, `chown`, `find`, `grep`)
- Text processing (`sed`, `awk`, `cut`, `sort`, `uniq`)
- System monitoring (`ps`, `top`, `df`, `free`, `netstat`)
- Process management (`kill`, `jobs`, `nohup`)
- Archive operations (`tar`, `gzip`)
- Network operations (`curl`, `wget`, `ping`)

### Python Programming Features
Your Python scripts must include:
- **Variables and Data Types**: Use appropriate data structures
- **Input/Output**: File operations and user interaction
- **Conditional Statements**: Complex decision logic
- **Loops**: Process collections and implement retry logic
- **Functions**: Modular, reusable code with proper documentation
- **Error Handling**: Try-catch blocks and graceful failure handling
- **Libraries**: Use standard library modules (os, sys, json, yaml, logging, argparse)

### YAML Configuration Standards
Your YAML files must:
- Pass yamllint validation with zero errors
- Follow consistent formatting and indentation
- Use appropriate data structures (lists, dictionaries, scalars)
- Include meaningful comments and documentation
- Support environment-specific overrides
- Implement proper quoting and escaping

## 🏆 Success Criteria

### Minimum Requirements (Pass)
- [ ] All directory structures created correctly
- [ ] YAML files are valid and well-formatted
- [ ] Python scripts execute without errors
- [ ] Basic functionality works end-to-end
- [ ] Code includes comments and documentation

### Good Implementation (Merit)
- [ ] Comprehensive error handling and logging
- [ ] Modular, reusable code structure
- [ ] Advanced YAML features and validation
- [ ] Integration between all components
- [ ] Performance considerations implemented

### Excellent Implementation (Distinction)
- [ ] Production-ready code quality
- [ ] Advanced features (dry-run, rollback, monitoring)
- [ ] Comprehensive testing and validation
- [ ] Security best practices implemented
- [ ] Innovative solutions and optimizations

## 🛠️ Tools and Resources

### Required Tools
- Linux/Unix environment
- Python 3.6+
- Text editor or IDE
- yamllint (for YAML validation)
- Basic understanding of Docker (optional)

### Helpful Resources
- Python documentation
- YAML specification
- Linux command references
- Jinja2 templating guide

## 📊 Evaluation Rubric

| Criteria | Weight | Excellent (4) | Good (3) | Satisfactory (2) | Needs Improvement (1) |
|----------|--------|---------------|----------|------------------|----------------------|
| **Linux Commands** | 20% | Advanced usage, efficient solutions | Good command usage | Basic commands work | Limited command knowledge |
| **Python Programming** | 30% | Clean, modular, well-documented | Good structure, works well | Basic functionality | Poor structure, errors |
| **YAML Configuration** | 20% | Perfect formatting, advanced features | Good structure, valid | Basic valid YAML | Formatting issues |
| **Integration** | 20% | Seamless integration, robust | Good integration | Basic integration | Poor integration |
| **Problem Solving** | 10% | Creative, efficient solutions | Good problem-solving | Adequate solutions | Limited problem-solving |

## 🚀 Getting Started

1. **Read the complete requirements** carefully
2. **Plan your approach** - sketch out the solution architecture
3. **Start with Phase 1** - create the basic structure
4. **Work incrementally** - test each component as you build
5. **Document your work** - include README files and comments
6. **Test thoroughly** - validate each phase before moving on

## 💡 Bonus Challenges

For participants who complete the main exercise early:

### Advanced Features
- Implement blue-green deployment strategy
- Add Prometheus metrics collection
- Create a web dashboard for deployment status
- Implement automated testing pipeline
- Add Slack/email notifications
- Create Kubernetes deployment manifests

### Security Enhancements
- Implement secret management
- Add input validation and sanitization
- Include security scanning
- Implement access controls
- Add audit logging

## 🆘 Troubleshooting Guide

### Common Issues
- **YAML validation errors**: Use yamllint to identify issues
- **Python import errors**: Check module installation and paths
- **Permission errors**: Verify file permissions and ownership
- **Template rendering errors**: Check Jinja2 syntax and variables

### Getting Help
- Review the presentation materials
- Check the workshop examples
- Use online documentation
- Ask instructors for clarification

---

**Good luck!** This exercise will demonstrate your mastery of the complete scripting toolkit. Take your time, plan carefully, and build something you're proud of! 🎯
