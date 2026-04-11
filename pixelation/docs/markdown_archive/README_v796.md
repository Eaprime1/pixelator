# System Snapshot - 2026-02-12

This directory contains a snapshot of the system state, created on February 12, 2026. It serves as a baseline reference for the Termux environment and key user directories on the phone's shared storage.

## Contents

### Package and Installation Lists

*   `termux_packages.txt`: A list of all packages installed via the Termux `pkg` manager.
*   `python_packages.txt`: A list of all Python packages installed in the global environment via `pip`.
*   `npm_global_packages.txt`: A list of globally installed Node.js packages.
*   `cargo_installed_crates.txt`: A list of Rust crates installed via `cargo install`.

### System State and Configuration

*   `disk_usage.txt`: Output of `df -h`, showing storage space usage for all mounted filesystems.
*   `environment_variables.txt`: A dump of all environment variables at the time of the snapshot.
*   `running_processes.txt`: A list of all processes running at the time of the snapshot.
*   `dotfiles/`: A subdirectory containing copies of key configuration files:
    *   `.bashrc`
    *   `.bash_aliases`
    *   `.gitconfig`
    *   `.npmrc`

### File System Trees

These files contain a recursive listing of files and directories (`ls -laR`) for key locations.

*   `termux_home_file_tree.txt`: A complete file listing of the Termux home directory (`~/`).
*   `pixel8a_external_file_tree.txt`: A complete file listing of the external `pixel8a` project directory (`~/storage/shared/pixelate`), representing the "phone" portion of the PIXEL ecosystem.
