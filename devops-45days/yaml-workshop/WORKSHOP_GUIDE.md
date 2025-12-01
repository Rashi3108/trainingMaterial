# 🎯 YAML Linting Workshop - Instructor Guide

## 📋 Workshop Overview

This hands-on workshop teaches participants to identify and fix common YAML linting issues using real-world examples from DevOps scenarios.

**Duration:** 45-60 minutes  
**Skill Level:** Beginner to Intermediate  
**Prerequisites:** Basic YAML knowledge

## 🎯 Learning Objectives

By the end of this workshop, participants will be able to:
- Identify common YAML linting errors
- Use yamllint tool effectively
- Fix syntax and formatting issues
- Apply YAML best practices
- Create custom linting configurations

## 📁 Workshop Files

### Invalid YAML Files (for practice):
- `messy-config.yml` - Application configuration with multiple issues
- `broken-ci.yml` - GitHub Actions workflow with errors
- `broken-k8s.yml` - Kubernetes deployment manifest with issues
- `broken-ansible.yml` - Ansible playbook with formatting problems

### Corrected YAML Files (for reference):
- `clean-config.yml` - Fixed application configuration
- `fixed-ci.yml` - Corrected CI/CD pipeline
- `fixed-k8s.yml` - Clean Kubernetes manifest
- `fixed-ansible.yml` - Properly formatted Ansible playbook

## 🚀 Workshop Structure

### Phase 1: Setup (10 minutes)

1. **Install yamllint:**
   ```bash
   pip install yamllint
   yamllint --version
   ```

2. **Create workshop directory:**
   ```bash
   mkdir yaml-linting-workshop
   cd yaml-linting-workshop
   ```

3. **Copy workshop files** to the directory

### Phase 2: Identify Issues (15 minutes)

**Exercise 1: Run yamllint on broken files**

Have participants run yamllint on each broken file:

```bash
yamllint messy-config.yml
yamllint broken-ci.yml
yamllint broken-k8s.yml
yamllint broken-ansible.yml
```

**Expected Issues to Discuss:**

#### messy-config.yml Issues:
- Line 3: Missing space after colon (`app_name:MyApp`)
- Line 7: Inconsistent indentation
- Line 8: Missing space after colon and extra spaces
- Line 9: Wrong indentation level
- Line 12: Missing space after colon
- Line 13: Missing space after colon
- Line 21: Inconsistent list formatting
- Line 24-25: Line too long (>80 characters)
- Line 28: Inconsistent boolean format (`yes` vs `true`)
- Line 29: Missing space after colon
- Line 33-35: Too many blank lines
- Line 37: Trailing whitespace
- Line 38: Tab character instead of spaces

#### broken-ci.yml Issues:
- Line 2: Missing space after colon
- Line 4: Missing space after colon
- Line 5: Missing space in list formatting
- Line 9: Missing space after colon
- Line 10: Missing space after colon
- Line 13: Missing space after colon
- Line 15: Missing space after colon
- Line 16: Wrong indentation
- Line 17: Missing space after colon
- Line 23: Missing space after colon

#### broken-k8s.yml Issues:
- Multiple missing spaces after colons
- Inconsistent indentation throughout
- Mixed indentation levels
- Missing spaces in key-value pairs

#### broken-ansible.yml Issues:
- Missing spaces after colons in task names
- Inconsistent indentation in task parameters
- Missing spaces in key-value pairs
- Wrong indentation levels

### Phase 3: Fix Issues (20 minutes)

**Exercise 2: Fix the YAML files**

Divide participants into groups, assign each group 1-2 files to fix:

1. **Group 1:** `messy-config.yml`
2. **Group 2:** `broken-ci.yml`
3. **Group 3:** `broken-k8s.yml`
4. **Group 4:** `broken-ansible.yml`

**Fixing Process:**
1. Run yamllint to see errors
2. Fix errors one by one
3. Re-run yamllint to verify fixes
4. Continue until zero errors

### Phase 4: Custom Configuration (10 minutes)

**Exercise 3: Create custom yamllint config**

Create `.yamllint.yml` with project-specific rules:

```yaml
extends: default

rules:
  line-length:
    max: 120
    level: warning
  indentation:
    spaces: 2
  truthy:
    allowed-values: ['true', 'false']
  comments:
    min-spaces-from-content: 1
```

Test with custom config:
```bash
yamllint -c .yamllint.yml filename.yml
```

### Phase 5: Review & Discussion (5 minutes)

- Compare solutions between groups
- Discuss best practices
- Show corrected examples
- Q&A session

## 🎯 Common Issues & Solutions

### Issue Categories:

1. **Spacing Issues:**
   - Missing space after colons
   - Inconsistent spacing around brackets/braces
   - Trailing whitespace

2. **Indentation Issues:**
   - Mixed tabs and spaces
   - Inconsistent indentation levels
   - Wrong indentation depth

3. **Formatting Issues:**
   - Lines too long
   - Too many blank lines
   - Inconsistent boolean values
   - Mixed quote styles

4. **Structural Issues:**
   - Inconsistent list formatting
   - Missing document separators
   - Improper nesting

## 🛠️ Instructor Tips

### Before the Workshop:
- Test all files with yamllint to ensure they produce expected errors
- Prepare environment with yamllint pre-installed
- Have corrected versions ready for comparison

### During the Workshop:
- Encourage participants to read error messages carefully
- Show how to interpret yamllint output
- Demonstrate fixing one file as an example
- Walk around to help with individual issues

### Common Participant Mistakes:
- Using tabs instead of spaces
- Inconsistent indentation (mixing 2 and 4 spaces)
- Not reading the full error message
- Fixing syntax but ignoring style issues

### Troubleshooting:
- If yamllint is not installed: Use online YAML validators
- If participants struggle: Pair them up
- If time runs short: Focus on one file per group

## 📊 Assessment Criteria

Participants successfully complete the workshop when they can:
- ✅ Run yamllint and interpret output
- ✅ Fix all linting errors in assigned files
- ✅ Achieve zero errors with yamllint
- ✅ Explain the importance of consistent YAML formatting
- ✅ Create a basic custom yamllint configuration

## 🔗 Additional Resources

- [yamllint documentation](https://yamllint.readthedocs.io/)
- [YAML specification](https://yaml.org/spec/)
- [Online YAML validator](https://codebeautify.org/yaml-validator)
- [Pre-commit hooks for YAML](https://pre-commit.com/hooks.html)

## 📝 Workshop Feedback

After the workshop, collect feedback on:
- Difficulty level of exercises
- Clarity of instructions
- Usefulness of examples
- Suggested improvements

---

**Note:** Keep the corrected files hidden until the review phase to encourage independent problem-solving!
