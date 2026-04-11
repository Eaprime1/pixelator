/home/user/unexusi_dev/README.md
# unexusi_dev
This is the development repo for all locations to work from as we create stuff we will launch it in a way from our dev repo to a new or existing repo.
# UNEXUSI Development Environment
 
This is the multi-location development repository for the UNEXUSI team. All locations work from this shared development environment, and as concepts are ready, we migrate them to dedicated repositories or projects.
 
## Quick Start
 
### First Time Setup
 
1. **Clone the repository** (if you haven't already):
  ```bash
  git clone https://github.com/Eaprime1/unexusi_dev.git
  cd unexusi_dev
  ```
 
2. **Make the setup script executable**:
  ```bash
  chmod +x setup_env.sh
  ```
 
3. **Run the setup script**:
  ```bash
  ./setup_env.sh
  ```
 
  The script will guide you through:
  - Installing system dependencies
  - Creating a Python virtual environment
  - Installing Python packages
  - Setting up drive mounts (if configured)
  - Configuring Git
  - Creating project directories
  - Installing development tools
  - Setting up shell integration
 
4. **Configure your environment**:
  ```bash
  cp .env.example .env
  nano .env  # or use your preferred editor
  ```
 
  Edit `.env` to customize settings for your location (database credentials, API keys, mount points, etc.)
 
5. **Activate the environment**:
  ```bash
  source activate_env.sh
  ```
 
  Or use the alias (after restarting your terminal):
  ```bash
  unexusi
  ```
 
### Daily Usage
 
Simply run the alias from any terminal to activate the environment:
 
```bash
unexusi
```
 
This will:
- Load environment variables from `.env`
- Activate the Python virtual environment
- Navigate to the project directory
- Display helpful information and commands
 
To deactivate the environment:
```bash
deactivate
```
 
## Project Structure
 
```
unexusi_dev/
├── .env.example          # Environment configuration template
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── requirements.txt     # Python dependencies
├── setup_env.sh        # Environment setup script
├── activate_env.sh     # Environment activation script
├── src/                # Source code
├── tests/              # Test files
├── docs/               # Documentation
├── scripts/            # Utility scripts
│   └── env_info.sh    # Display environment information
├── data/               # Data files (gitignored)
├── logs/               # Log files (gitignored)
├── config/             # Configuration files
└── venv/               # Python virtual environment (gitignored)
```
 
## Environment Configuration
 
### Environment Variables
 
The `.env` file contains location-specific configuration. Key sections include:
 
- **Project Configuration**: Project name, environment type, debug settings
- **Drive Mounting**: Configure external drives to mount on startup
- **Database Configuration**: PostgreSQL, MongoDB, Redis, SQLite settings
- **API Configuration**: API server settings and external API keys
- **Logging**: Log levels, formats, and file locations
- **Security**: Secret keys, JWT settings, CORS configuration
- **Cloud Storage**: AWS, GCP, Azure storage settings
- **Email**: SMTP configuration
- **Development Tools**: Testing, formatting, and linting settings
 
### Drive Mounting
 
To configure automatic drive mounting:
 
1. Edit `.env` and set `DRIVE_MOUNT_POINTS`:
  ```bash
  DRIVE_MOUNT_POINTS=/mnt/data:/dev/sdb1,/mnt/backup:/dev/sdc1
  ```
 
2. Run setup with sudo for mounting privileges:
  ```bash
  sudo ./setup_env.sh
  ```
 
## Available Commands
 
### After Activation
 
When the environment is activated, you have access to:
 
- `python` - Python from virtual environment
- `pip` - Package installer
- `pytest` - Run tests
- `black` - Code formatter
- `flake8` - Linter
- `pylint` - Code analysis
- `mypy` - Type checker
- `ipython` - Enhanced Python shell
- `jupyter` - Jupyter notebooks
 
### Utility Scripts
 
- `./scripts/env_info.sh` - Display environment information
 
### Git Aliases
 
The setup configures helpful Git aliases:
 
- `git st` - Status
- `git co` - Checkout
- `git br` - Branch
- `git cm` - Commit
- `git lg` - Pretty log graph
 
## Development Workflow
 
### Creating New Features
 
1. Activate the environment:
  ```bash
  unexusi
  ```
 
2. Create a new branch:
  ```bash
  git checkout -b feature/your-feature-name
  ```
 
3. Develop your feature in `src/`
 
4. Write tests in `tests/`
 
5. Run tests:
  ```bash
  pytest
  ```
 
6. Format and lint your code:
  ```bash
  black src/
  flake8 src/
  ```
 
7. Commit and push:
  ```bash
  git add .
  git commit -m "Add your feature"
  git push origin feature/your-feature-name
  ```
 
### Moving to Production
 
When a concept is ready to move from `unexusi_dev` to a dedicated repository:
 
1. Create the target repository
2. Copy the relevant code
3. Update dependencies in the new repo's `requirements.txt`
4. Document the migration in this repo
5. Archive or remove the code from `unexusi_dev` if appropriate
 
## Python Dependencies
 
The `requirements.txt` includes a comprehensive set of packages for:
 
- **Core Utilities**: Environment management, YAML parsing
- **Data Science**: NumPy, Pandas, Matplotlib, SciPy
- **Web Development**: FastAPI, Flask, Requests
- **Databases**: SQLAlchemy, PostgreSQL, MongoDB, Redis
- **Development Tools**: Black, Flake8, Pylint, MyPy
- **Testing**: Pytest, Coverage, Mocking
- **Documentation**: Sphinx
- **Logging**: Loguru, Colorlog
- **CLI Tools**: Click, Rich, Typer
- **Async**: AsyncIO, aiohttp, Celery
- **Security**: Cryptography, JWT, Bcrypt
- **And much more...**
 
Optional packages (ML, web scraping, cloud services) are commented out. Uncomment as needed.
 
## Multi-Location Support
 
This repository is designed to work across multiple development locations:
 
- Each location has its own `.env` file (not committed to git)
- Set `LOCATION_NAME` in `.env` to identify your location
- Configure location-specific paths, databases, and services
- Drive mounts can be configured per location
 
## Troubleshooting
 
### Virtual Environment Issues
 
If the virtual environment doesn't activate:
 
```bash
rm -rf venv
./setup_env.sh
```
 
### Permission Issues with Drive Mounting
 
Drive mounting requires root privileges:
 
```bash
sudo ./setup_env.sh
```
 
### Missing Dependencies
 
If you encounter missing system dependencies:
 
```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip python3-venv git
 
# RHEL/CentOS
sudo yum install python3 python3-pip git
 
# macOS
brew install python3 git
```
 
### Alias Not Working
 
After setup, restart your terminal or run:
 
```bash
source ~/.bashrc  # or ~/.zshrc
```
 
## Contributing
 
1. Keep the `main` branch stable
2. Use feature branches for development
3. Run tests before pushing
4. Format code with Black
5. Update documentation as needed
6. Communicate with the team about significant changes
 
## Support
 
For issues or questions:
 
- Check this README
- Review `.env.example` for configuration options
- Run `./scripts/env_info.sh` to check your environment
- Contact the team
 
## License
 
See [LICENSE](LICENSE) file for details.
 
---
 
**Last Updated**: 2025-12-05
**Repository**: https://github.com/Eaprime1/unexusi_dev