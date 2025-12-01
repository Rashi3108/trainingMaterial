# 🎯 YAML Linting Workshop Files

This directory contains all the materials needed for the YAML linting hands-on workshop.

## 📁 Workshop Files Overview

### 🔴 Broken YAML Files (for practice)
These files contain intentional linting errors for participants to identify and fix:

| File | Description | Issues Found |
|------|-------------|--------------|
| `messy-config.yml` | Application configuration | 13 linting issues |
| `broken-ci.yml` | GitHub Actions CI/CD pipeline | 26 linting issues |
| `broken-k8s.yml` | Kubernetes deployment manifest | 35 linting issues |
| `broken-ansible.yml` | Ansible playbook | 43 linting issues |

**Total Issues:** 117 linting problems across all files

### ✅ Fixed YAML Files (for reference)
These are the corrected versions showing proper YAML formatting:

| File | Description |
|------|-------------|
| `clean-config.yml` | Properly formatted application configuration |
| `fixed-ci.yml` | Clean GitHub Actions workflow |
| `fixed-k8s.yml` | Correctly formatted Kubernetes manifest |
| `fixed-ansible.yml` | Well-structured Ansible playbook |

### 📋 Workshop Materials

| File | Purpose |
|------|---------|
| `WORKSHOP_GUIDE.md` | Complete instructor guide with timing and exercises |
| `.yamllint.yml` | Sample custom linting configuration |
| `README.md` | This overview document |

## 🚀 Quick Start for Instructors

1. **Setup Environment:**
   ```bash
   pip install yamllint
   cd yaml-workshop/
   ```

2. **Test Broken Files:**
   ```bash
   yamllint messy-config.yml
   yamllint broken-ci.yml
   yamllint broken-k8s.yml
   yamllint broken-ansible.yml
   ```

3. **Verify Fixed Files:**
   ```bash
   yamllint clean-config.yml
   yamllint fixed-ci.yml
   yamllint fixed-k8s.yml
   yamllint fixed-ansible.yml
   ```

## 🎯 Common Issues Included

The broken files contain these types of linting errors:

### Spacing Issues
- Missing space after colons (`:`)
- Trailing whitespace
- Inconsistent spacing in lists and dictionaries

### Indentation Issues
- Mixed 2-space and 4-space indentation
- Tab characters instead of spaces
- Incorrect nesting levels

### Formatting Issues
- Lines exceeding 80 characters
- Inconsistent boolean values (`yes`/`true`/`false`)
- Mixed quote styles
- Too many blank lines

### Structure Issues
- Inconsistent list formatting
- Missing spaces in key-value pairs
- Improper YAML structure

## 📊 Workshop Statistics

- **Duration:** 45-60 minutes
- **Participants:** 4-20 people (works best in groups of 4-6)
- **Skill Level:** Beginner to Intermediate
- **Tools Required:** yamllint, text editor
- **Learning Outcomes:** 5 key objectives achieved

## 🛠️ Alternative Tools

If yamllint installation is problematic, participants can use:
- Online YAML validators
- VS Code YAML extensions
- IDE built-in YAML linting
- Python yaml module for basic validation

## 📝 Workshop Flow

1. **Setup** (10 min) - Install tools and copy files
2. **Identify** (15 min) - Run yamllint and analyze errors
3. **Fix** (20 min) - Correct issues in assigned files
4. **Configure** (10 min) - Create custom linting rules
5. **Review** (5 min) - Compare solutions and discuss

## 🎓 Learning Outcomes

After completing this workshop, participants will:
- ✅ Understand common YAML linting issues
- ✅ Use yamllint tool effectively
- ✅ Apply YAML formatting best practices
- ✅ Create custom linting configurations
- ✅ Integrate linting into development workflow

## 🔗 Additional Resources

- [yamllint Documentation](https://yamllint.readthedocs.io/)
- [YAML Specification](https://yaml.org/spec/)
- [Online YAML Validator](https://codebeautify.org/yaml-validator)
- [Pre-commit Hooks](https://pre-commit.com/hooks.html)

---

**Ready to run the workshop?** Start with the `WORKSHOP_GUIDE.md` for detailed instructions!
