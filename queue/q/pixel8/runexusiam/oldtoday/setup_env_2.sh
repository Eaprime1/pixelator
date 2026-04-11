#!/bin/bash
set -e


# UNEXUSI Development Environment Setup Script
# Multi-location development environment configuration
# Author: Unexusi Team
# Date: 2025-12-05


# Colors for output
RED='\e[0;31m'
GREEN='\e[0;32m'
YELLOW='\e[1;33m'
BLUE='\e[0;34m'
NC='\e[0m' # No Color


# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"


echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   UNEXUSI Development Environment Setup                   ║${NC}"
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo ""


# Function to print status messages
print_status() {
   echo -e "${BLUE}[*]${NC} $1"
}


print_success() {
   echo -e "${GREEN}[✓]${NC} $1"
}


print_warning() {
   echo -e "${YELLOW}[!\]${NC} $1"
}


print_error() {
   echo -e "${RED}[✗]${NC} $1"
}


# Check if running as root (for certain operations)
check_sudo() {
   if [[ $EUID -eq 0 ]]; then
       print_warning "Running as root"
       IS_ROOT=true
   else
       IS_ROOT=false
   fi
}


# Load environment variables from .env if exists
load_env() {
   if [ -f "$PROJECT_ROOT/.env" ]; then
       print_status "Loading environment variables from .env"
       set -a
       source "$PROJECT_ROOT/.env"
       set +a
       print_success "Environment variables loaded"
   else
       print_warning "No .env file found. Copy .env.example to .env and configure it."
   fi
}


# System dependencies installation
install_system_dependencies() {
   print_status "Checking system dependencies..."


   if command -v apt-get &> /dev/null; then
       PKG_MANAGER="apt-get"
   elif command -v yum &> /dev/null; then
       PKG_MANAGER="yum"
   elif command -v brew &> /dev/null; then
       PKG_MANAGER="brew"
   else
       print_warning "Package manager not detected. Skipping system dependencies."
       return
   fi


   DEPS="python3 python3-pip python3-venv git curl wget"


   if [ "$PKG_MANAGER" = "apt-get" ]; then
       print_status "Using apt-get to check dependencies..."
       for dep in $DEPS; do
           if ! dpkg -l | grep -q "^ii  $dep "; then
               print_warning "$dep not found. Install it manually if needed: sudo apt-get install $dep"
           else
               print_success "$dep is installed"
           fi
       done
   fi
}


# Python virtual environment setup
setup_python_venv() {
   print_status "Setting up Python virtual environment..."


   VENV_DIR="${VENV_DIR:-$PROJECT_ROOT/venv}"


   if [ -d "$VENV_DIR" ]; then
       print_warning "Virtual environment already exists at $VENV_DIR"
       read -p "Do you want to recreate it? (y/N): " -n 1 -r
       echo
       if [[ $REPLY =~ ^[Yy]$ ]]; then
           rm -rf "$VENV_DIR"
       else
           print_status "Using existing virtual environment"
           return
       fi
   fi


   python3 -m venv "$VENV_DIR"
   print_success "Virtual environment created at $VENV_DIR"


   # Activate and upgrade pip
   source "$VENV_DIR/bin/activate"
   print_status "Upgrading pip..."
   pip install --upgrade pip setuptools wheel
   print_success "pip upgraded"
}


# Install Python dependencies
install_python_dependencies() {
   print_status "Installing Python dependencies..."


   VENV_DIR="${VENV_DIR:-$PROJECT_ROOT/venv}"


   if [ ! -d "$VENV_DIR" ]; then
       print_error "Virtual environment not found. Run setup_python_venv first."
       return 1
   fi


   source "$VENV_DIR/bin/activate"


   if [ -f "$PROJECT_ROOT/requirements.txt" ]; then
       pip install -r "$PROJECT_ROOT/requirements.txt"
       print_success "Python dependencies installed"
   else
       print_warning "No requirements.txt found. Skipping Python dependency installation."
   fi
}


# Mount drives configuration
setup_drive_mounts() {
   print_status "Configuring drive mounts..."


   # Load mount points from .env or use defaults
   MOUNT_POINTS="${DRIVE_MOUNT_POINTS:-}"


   if [ -z "$MOUNT_POINTS" ]; then
       print_warning "No DRIVE_MOUNT_POINTS defined in .env. Skipping drive mounting."
       print_status "To configure drive mounts, add to .env:"
       print_status "  DRIVE_MOUNT_POINTS='/mnt/data:/dev/sdb1,/mnt/backup:/dev/sdc1'"
       return
   fi


   IFS=',' read -ra MOUNTS <<< "$MOUNT_POINTS"
   for mount in "${MOUNTS[@]}"; do
       IFS=':' read -ra MOUNT_INFO <<< "$mount"
       MOUNT_DIR="${MOUNT_INFO[0]}"
       DEVICE="${MOUNT_INFO[1]}"


       if [ -z "$MOUNT_DIR" ] || [ -z "$DEVICE" ]; then
           print_warning "Invalid mount specification: $mount"
           continue
       fi


       # Create mount directory if it doesn't exist
       if [ ! -d "$MOUNT_DIR" ]; then
           if [ "$IS_ROOT" = true ]; then
               mkdir -p "$MOUNT_DIR"
               print_success "Created mount directory: $MOUNT_DIR"
           else
               print_warning "Cannot create mount directory $MOUNT_DIR (requires root)"
               continue
           fi
       fi


       # Check if already mounted
       if mountpoint -q "$MOUNT_DIR" 2>/dev/null; then
           print_success "$MOUNT_DIR is already mounted"
       else
           if [ "$IS_ROOT" = true ]; then
               if [ -b "$DEVICE" ]; then
                   mount "$DEVICE" "$MOUNT_DIR"
                   print_success "Mounted $DEVICE to $MOUNT_DIR"
               else
                   print_warning "Device $DEVICE not found"
               fi
           else
               print_warning "Cannot mount $DEVICE to $MOUNT_DIR (requires root)"
               print_status "Run: sudo mount $DEVICE $MOUNT_DIR"
           fi
       fi
   done
}


# Git configuration
setup_git() {
   print_status "Configuring Git..."


   # Check if git is configured
   if ! git config user.name &> /dev/null; then
       print_warning "Git user.name not configured"
       print_status "Configure with: git config --global user.name 'Your Name'"
   else
       print_success "Git user: $(git config user.name)"
   fi


   if ! git config user.email &> /dev/null; then
       print_warning "Git user.email not configured"
       print_status "Configure with: git config --global user.email 'your@email.com'"
   else
       print_success "Git email: $(git config user.email)"
   fi


   # Set up useful git aliases
   print_status "Setting up Git aliases..."
   git config --global alias.st status
   git config --global alias.co checkout
   git config --global alias.br branch
   git config --global alias.cm commit
   git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
   print_success "Git aliases configured"
}


# Create useful directories
setup_directories() {
   print_status "Setting up project directories..."


   DIRS=("src" "tests" "docs" "scripts" "data" "logs" "config")


   for dir in "${DIRS[@]}"; do
       if [ ! -d "$PROJECT_ROOT/$dir" ]; then
           mkdir -p "$PROJECT_ROOT/$dir"
           print_success "Created directory: $dir"
       fi
   done
}


# Install development tools
install_dev_tools() {
   print_status "Installing development tools..."


   VENV_DIR="${VENV_DIR:-$PROJECT_ROOT/venv}"


   if [ -d "$VENV_DIR" ]; then
       source "$VENV_DIR/bin/activate"


       # Install common dev tools
       print_status "Installing code formatters and linters..."
       pip install black flake8 pylint mypy isort pytest pytest-cov ipython >/dev/null 2>&1 || true
       print_success "Development tools installed"
   fi
}


# Setup shell integration
setup_shell_integration() {
   print_status "Setting up shell integration..."


   SHELL_RC=""
   if [ -n "$BASH_VERSION" ]; then
       SHELL_RC="$HOME/.bashrc"
   elif [ -n "$ZSH_VERSION" ]; then
       SHELL_RC="$HOME/.zshrc"
   fi


   if [ -n "$SHELL_RC" ]; then
       # Check if alias already exists
       if grep -q "alias unexusi=" "$SHELL_RC" 2>/dev/null; then
           print_success "Shell alias 'unexusi' already configured"
       else
           print_status "Adding 'unexusi' alias to $SHELL_RC"
           echo "" >> "$SHELL_RC"
           echo "# UNEXUSI Development Environment" >> "$SHELL_RC"
           echo "alias unexusi='source \"$PROJECT_ROOT/activate_env.sh\"'" >> "$SHELL_RC"
           print_success "Alias 'unexusi' added to $SHELL_RC"
           print_warning "Run 'source $SHELL_RC' or restart your terminal to use the alias"
       fi
   fi
}


# Create activation script
create_activation_script() {
   print_status "Creating environment activation script..."


   cat > "$PROJECT_ROOT/activate_env.sh" << 'ACTIVATION_EOF'
#!/bin/bash


# UNEXUSI Development Environment Activation Script


SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${VENV_DIR:-$SCRIPT_DIR/venv}"


# Colors
GREEN='\e[0;32m'
BLUE='\e[0;34m'
NC='\e[0m'


echo -e "${BLUE}Activating UNEXUSI Development Environment...${NC}"


# Load environment variables
if [ -f "$SCRIPT_DIR/.env" ]; then
   set -a
   source "$SCRIPT_DIR/.env"
   set +a
   echo -e "${GREEN}✓${NC} Environment variables loaded"
fi


# Activate virtual environment
if [ -d "$VENV_DIR" ]; then
   source "$VENV_DIR/bin/activate"
   echo -e "${GREEN}✓${NC} Python virtual environment activated"
else
   echo -e "${BLUE}ℹ${NC} Virtual environment not found. Run: cd $SCRIPT_DIR && ./setup_env.sh"
fi


# Change to project directory
cd "$SCRIPT_DIR"
echo -e "${GREEN}✓${NC} Changed to project directory: $SCRIPT_DIR"


# Display helpful information
echo ""
echo -e "${BLUE}Available commands:${NC}"
echo "  python        - Python from virtual environment"
echo "  pip           - pip from virtual environment"
echo "  deactivate    - Exit virtual environment"
echo ""
echo -e "${BLUE}Quick start:${NC}"
echo "  cd src        - Navigate to source code"
echo "  cd tests      - Navigate to tests"
echo "  pytest        - Run tests"
echo ""


ACTIVATION_EOF


   chmod +x "$PROJECT_ROOT/activate_env.sh"
   print_success "Activation script created at activate_env.sh"
}


# Create environment info script
create_env_info_script() {
   print_status "Creating environment info script..."


   cat > "$PROJECT_ROOT/scripts/env_info.sh" << 'EOF'
#!/bin/bash


# Display environment information


echo "════════════════════════════════════════════════════════════"
echo "  UNEXUSI Development Environment Information"
echo "════════════════════════════════════════════════════════════"
echo ""


echo "System Information:"
echo "  OS: $(uname -s)"
echo "  Kernel: $(uname -r)"
echo "  Architecture: $(uname -m)"
echo ""


echo "Python Information:"
if command -v python3 &> /dev/null; then
   echo "  Python: $(python3 --version)"
   echo "  Location: $(which python3)"
fi


echo ""


echo "Git Information:"
if command -v git &> /dev/null; then
   echo "  Git: $(git --version)"
   echo "  Branch: $(git branch --show-current 2>/dev/null || echo 'Not in a git repo')"
fi


echo ""


echo "Virtual Environment:"
if [ -n "$VIRTUAL_ENV" ]; then
   echo "  Active: Yes"
   echo "  Location: $VIRTUAL_ENV"
else
   echo "  Active: No"
fi


echo ""


echo "Environment Variables:"
echo "  PROJECT_ROOT: ${PROJECT_ROOT:-Not set}"
echo "  VENV_DIR: ${VENV_DIR:-Not set}"


echo ""


echo "Mount Points:"
df -h | grep -E '^/dev/' || echo "  No external drives mounted"


echo ""


echo "════════════════════════════════════════════════════════════"


EOF


   chmod +x "$PROJECT_ROOT/scripts/env_info.sh"
   print_success "Environment info script created"
}


# Main setup function
main() {
   echo ""
   check_sudo
   load_env


   # Ask user what to set up
   echo ""
   print_status "What would you like to set up?"
   echo "  1) Full setup (recommended for first time)"
   echo "  2) Python environment only"
   echo "  3) Drive mounts only"
   echo "  4) Shell integration only"
   echo "  5) Custom setup (choose components)"
   echo ""
   read -p "Enter choice [1-5] (default: 1): " -n 1 -r
   echo ""
   CHOICE=${REPLY:-1}


   case $CHOICE in
       1)
           print_status "Running full setup..."
           install_system_dependencies
           setup_python_venv
           install_python_dependencies
           setup_drive_mounts
           setup_git
           setup_directories
           install_dev_tools
           create_activation_script
           create_env_info_script
           setup_shell_integration
           ;;
       2)
           setup_python_venv
           install_python_dependencies
           install_dev_tools
           ;;
       3)
           setup_drive_mounts
           ;;
       4)
           create_activation_script
           setup_shell_integration
           ;;
       5)
           print_status "Custom setup - select components:"
           read -p "Setup Python environment? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && setup_python_venv && install_python_dependencies


           read -p "Setup drive mounts? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && setup_drive_mounts


           read -p "Configure Git? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && setup_git


           read -p "Create project directories? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && setup_directories


           read -p "Install dev tools? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && install_dev_tools


           read -p "Setup shell integration? (Y/n): " -n 1 -r; echo
           [[ ! $REPLY =~ ^[Nn]$ ]] && create_activation_script && setup_shell_integration
           ;;
       *)
           print_error "Invalid choice"
           exit 1
           ;;
   esac


   echo ""
   echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
   echo -e "${GREEN}║   Setup Complete!                                          ║${NC}"
   echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
   echo ""
   print_success "Next steps:"
   echo "  1. Copy .env.example to .env and configure it: cp .env.example .env"
   echo "  2. Activate environment: source activate_env.sh"
   echo "  3. Or use the alias: unexusi (after restarting terminal)"
   echo "  4. Check environment: ./scripts/env_info.sh"
   echo ""
}


# Run main function
main