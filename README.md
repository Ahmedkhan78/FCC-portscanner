# Port Scanner 🔍

This project is part of the **freeCodeCamp Information Security Certification**.

It is a Python-based port scanner that checks a range of ports on a given target (IP address or hostname) and returns which ports are open.

---

## 🚀 Project Description

The goal of this project is to build a function that:

- Accepts a **hostname or IP address**
- Accepts a **range of ports**
- Scans each port in that range
- Returns a list of open ports
- Optionally returns a formatted verbose output

---

## 📌 Function Requirements

You must implement the following function in `port_scanner.py`:

```python
def get_open_ports(target, port_range, verbose=False):
    """
    Scans a target for open ports.

    Args:
        target (str): IP address or URL (e.g., "scanme.nmap.org")
        port_range (list): List of two integers [start, end]
        verbose (bool): Optional flag for formatted output

    Returns:
        list | str:
            - Normal mode: List of open ports (e.g., [22, 80])
            - Verbose mode: Formatted string with port and service details
    """
    pass
```

### Return Values

**Normal Mode (`verbose=False`):**
Returns a list of open ports:

```python
[22, 80]
```

**Verbose Mode (`verbose=True`):**
Returns a formatted string:

```text
Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http
```

### ⚠️ Error Handling

Your function must handle invalid input gracefully:

| Input Issue        | Error Message               |
| :----------------- | :-------------------------- |
| Invalid hostname   | `Error: Invalid hostname`   |
| Invalid IP address | `Error: Invalid IP address` |

---

## 🧠 Key Concepts Used

- Python `socket` module
- TCP connection scanning
- DNS resolution
- Error handling
- String formatting
- Network fundamentals

---

## 🛠️ How to Run

**Run the project:**

```bash
python main.py
```

**Run tests:**

```bash
python test_module.py
```

---

## 📁 Project Structure

```text
port-scanner/
│
├── port_scanner.py     # Main implementation
├── common_ports.py     # Port-service mapping
├── main.py             # Entry point for testing
├── test_module.py      # Unit tests
└── README.md           # Project documentation
```

---

## 🎯 Objective

Build a working port scanner that behaves like a simplified version of tools such as **nmap**.

---

## 📚 Reference

- **Project Instructions:** [freeCodeCamp Port Scanner](https://www.freecodecamp.org/learn/information-security/information-security-projects/port-scanner)

```

### What I improved:
1.  **Structure:** Organized into clear sections (Description, Requirements, Usage, Structure).
2.  **Formatting:** Converted the messy text into clean Markdown code blocks for Python, Bash, and text outputs.
3.  **Clarity:** Used a table for error handling to make it scannable.
4.  **Visuals:** Added a standard directory tree structure for the file layout.
5.  **Docstring:** Added a proper Python docstring example to the function requirement to help with implementation.

```
