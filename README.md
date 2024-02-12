# Network Scanner

A simple Python script for scanning ports on a target system within a specified range.

## Overview

This Python script allows you to scan a target system for open ports using a specified port range. It's a straightforward tool that provides basic functionality for network exploration.

## Features

- **Port Scanning:** Scan a specified range of ports on a given target.
- **User Input:** Input target, start port, and end port as command-line arguments.
- **Timestamps:** Displays the time the scan started for reference.

## Usage

### Prerequisites

- Python 3.x

### Running the Scanner

Clone the repository and navigate to the project directory in your terminal.

```bash
git clone https://github.com/your-username/network-scanner.git
cd network-scanner
```

Run the script with the following syntax:

```bash
python3 scanner.py <target> <start_port> <end_port>
```

## Example

Scan ports 50 to 85 on a target system:

```bash
python3 scanner.py example.com 50 85
```

## Contributing

Feel free to contribute to enhance the functionality or fix any issues. Create a pull request, and let's make this network scanner even better!
