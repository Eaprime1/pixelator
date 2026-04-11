Write/home/user/unexusi_dev/QUICKSTART.md
# Quick Start Guide
 
Get up and running with the UNEXUSI development environment in 5 minutes!
 
## Installation (One Time)
 
```bash
# 1. Navigate to the repo
cd /home/user/unexusi_dev
 
# 2. Make setup script executable
chmod +x setup_env.sh
 
# 3. Run the setup
./setup_env.sh
 
# 4. Create your .env file
cp .env.example .env
 
# 5. Edit .env for your location (optional but recommended)
nano .env
```
 
## Daily Use
 
### Option 1: Use the Alias (Easiest)
 
After restarting your terminal:
 
```bash
unexusi
```
 
### Option 2: Manual Activation
 
```bash
source /home/user/unexusi_dev/activate_env.sh
```
 
## What You Get
 
When activated, you'll have:
 
- Python virtual environment with 50+ useful packages
- All development tools (pytest, black, flake8, etc.)
- Environment variables loaded from `.env`
- Working directory set to project root
- Git aliases configured
 
## Common Tasks
 
### Run Tests
```bash
pytest
```
 
### Format Code
```bash
black src/
```
 
### Lint Code
```bash
flake8 src/
```
 
### Check Environment
```bash
./scripts/env_info.sh
```
 
### Deactivate
```bash
deactivate
```
 
## Drive Mounting
 
To mount drives automatically on activation:
 
1. Edit `.env`:
  ```bash
  DRIVE_MOUNT_POINTS=/mnt/data:/dev/sdb1
  ```
 
2. Re-run setup with sudo:
  ```bash
  sudo ./setup_env.sh
  ```
 
## Troubleshooting
 
### Alias doesn't work
```bash
source ~/.bashrc  # or ~/.zshrc
```
 
### Virtual environment issues
```bash
rm -rf venv
./setup_env.sh
```
 
### Need help?
```bash
cat README.md
./scripts/env_info.sh
```
 
## That's It!
 
You're ready to develop. Happy coding!
 
---
 
For full documentation, see [README.md](README.md)