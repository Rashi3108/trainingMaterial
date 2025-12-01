#!/bin/bash
# setup.sh - Quick setup script for the capstone exercise

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

print_status "$BLUE" "🚀 DevOps Capstone Exercise Setup"
print_status "$BLUE" "=================================="

# Check if we're in the right directory
if [[ ! -f "README.md" ]] || [[ ! -d "starter-templates" ]]; then
    print_status "$RED" "❌ Please run this script from the capstone-exercise directory"
    exit 1
fi

# Create project structure
print_status "$YELLOW" "📁 Creating project structure..."

# Create main directories
mkdir -p deployment-automation/{config,scripts,templates,logs}

# Set proper permissions
chmod 755 deployment-automation
chmod 755 deployment-automation/{config,scripts,templates,logs}
chmod 644 deployment-automation/logs/.gitkeep 2>/dev/null || touch deployment-automation/logs/.gitkeep

print_status "$GREEN" "✅ Directory structure created"

# Copy starter templates
print_status "$YELLOW" "📋 Setting up starter templates..."

# Copy YAML templates
cp starter-templates/app-config.yml.template deployment-automation/config/
cp starter-templates/deployment-config.yml.template deployment-automation/config/

# Copy Python template
cp starter-templates/deploy.py.template deployment-automation/scripts/

# Copy shell script template
cp starter-templates/deploy.sh.template deployment-automation/

# Make shell scripts executable
chmod +x deployment-automation/deploy.sh.template

print_status "$GREEN" "✅ Starter templates copied"

# Check prerequisites
print_status "$YELLOW" "🔍 Checking prerequisites..."

# Check Python 3
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version 2>&1)
    print_status "$GREEN" "✅ Python found: $python_version"
else
    print_status "$RED" "❌ Python 3 not found. Please install Python 3.6+"
    exit 1
fi

# Check yamllint
if command -v yamllint &> /dev/null; then
    print_status "$GREEN" "✅ yamllint found"
else
    print_status "$YELLOW" "⚠️ yamllint not found. Installing..."
    if pip3 install yamllint --user; then
        print_status "$GREEN" "✅ yamllint installed successfully"
    else
        print_status "$RED" "❌ Failed to install yamllint. Please install manually: pip3 install yamllint"
    fi
fi

# Check other tools
tools=("curl" "nc" "docker")
for tool in "${tools[@]}"; do
    if command -v "$tool" &> /dev/null; then
        print_status "$GREEN" "✅ $tool found"
    else
        print_status "$YELLOW" "⚠️ $tool not found (optional but recommended)"
    fi
done

# Create initial README for the project
print_status "$YELLOW" "📝 Creating project README..."

cat > deployment-automation/README.md << 'EOF'
# DevOps Deployment Automation

This is your capstone exercise project. Complete the implementation by following the requirements in the main exercise README.

## Project Structure

```
deployment-automation/
├── config/                     # Configuration files
│   ├── app-config.yml         # Application configuration (TODO)
│   ├── deployment-config.yml  # Deployment settings (TODO)
│   └── monitoring-config.yml  # Monitoring setup (TODO)
├── scripts/                   # Python automation scripts
│   ├── deploy.py             # Main deployment script (TODO)
│   ├── health_check.py       # Health monitoring script (TODO)
│   └── cleanup.py            # Cleanup and rollback script (TODO)
├── templates/                 # Configuration templates
│   ├── nginx.conf.j2         # Nginx configuration template (TODO)
│   └── docker-compose.yml.j2 # Docker compose template (TODO)
├── logs/                     # Deployment logs
├── deploy.sh                 # Main deployment shell script (TODO)
└── README.md                 # This file
```

## Getting Started

1. Remove the `.template` suffix from the starter files
2. Complete the implementation according to the exercise requirements
3. Test each component as you build it
4. Validate YAML files with `yamllint`
5. Test Python scripts individually before integration

## Validation Commands

```bash
# Validate YAML files
yamllint config/*.yml

# Test Python syntax
python3 -m py_compile scripts/*.py

# Test shell script syntax
bash -n deploy.sh
```

## Success Criteria

- [ ] All YAML files pass yamllint validation
- [ ] Python scripts demonstrate all required concepts
- [ ] Shell script integrates all components
- [ ] End-to-end workflow functions correctly
- [ ] Comprehensive error handling implemented
- [ ] Code is well-documented and modular

Good luck with your capstone exercise! 🚀
EOF

print_status "$GREEN" "✅ Project README created"

# Create a simple validation script
print_status "$YELLOW" "🔧 Creating validation script..."

cat > deployment-automation/validate.sh << 'EOF'
#!/bin/bash
# validate.sh - Quick validation script for the project

echo "🔍 Validating project components..."

# Check YAML files
echo "📋 Checking YAML files..."
for yaml_file in config/*.yml; do
    if [[ -f "$yaml_file" ]]; then
        if yamllint "$yaml_file" >/dev/null 2>&1; then
            echo "✅ $yaml_file - Valid"
        else
            echo "❌ $yaml_file - Invalid"
            yamllint "$yaml_file"
        fi
    fi
done

# Check Python files
echo "🐍 Checking Python files..."
for py_file in scripts/*.py; do
    if [[ -f "$py_file" ]]; then
        if python3 -m py_compile "$py_file" 2>/dev/null; then
            echo "✅ $py_file - Valid syntax"
        else
            echo "❌ $py_file - Syntax errors"
            python3 -m py_compile "$py_file"
        fi
    fi
done

# Check shell scripts
echo "🐚 Checking shell scripts..."
for sh_file in *.sh; do
    if [[ -f "$sh_file" && "$sh_file" != "validate.sh" ]]; then
        if bash -n "$sh_file" 2>/dev/null; then
            echo "✅ $sh_file - Valid syntax"
        else
            echo "❌ $sh_file - Syntax errors"
            bash -n "$sh_file"
        fi
    fi
done

echo "🎯 Validation complete!"
EOF

chmod +x deployment-automation/validate.sh

print_status "$GREEN" "✅ Validation script created"

# Final instructions
print_status "$BLUE" "🎯 Setup Complete!"
print_status "$BLUE" "=================="

echo
print_status "$GREEN" "Your capstone exercise environment is ready!"
echo
print_status "$YELLOW" "Next steps:"
echo "1. cd deployment-automation"
echo "2. Remove .template suffix from starter files"
echo "3. Start with Phase 1: Environment Setup"
echo "4. Follow the exercise requirements in README.md"
echo "5. Use ./validate.sh to check your progress"
echo
print_status "$BLUE" "📚 Resources:"
echo "- Exercise README: ../README.md"
echo "- Instructor Guide: ../INSTRUCTOR_GUIDE.md"
echo "- Sample Solutions: ../sample-solutions/"
echo
print_status "$GREEN" "Good luck with your capstone exercise! 🚀"
