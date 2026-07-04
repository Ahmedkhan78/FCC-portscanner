````md
# Port Scanner 🔍

This project is part of the freeCodeCamp Information Security Certification.

It is a Python-based port scanner that checks a range of ports on a given target (IP address or hostname) and returns which ports are open.

---

## 🚀 Project Description

The goal of this project is to build a function that can:

- Accept a **hostname or IP address**
- Accept a **range of ports**
- Scan each port in that range
- Return a list of open ports
- Optionally return a formatted verbose output

---

## 📌 Function Requirements

You must implement:

```python
get_open_ports(target, port_range, verbose=False)
```
````

### Parameters:

- `target` → IP address or URL (e.g. `"scanme.nmap.org"`)
- `port_range` → list of two numbers `[start, end]`
- `verbose` → optional boolean for formatted output

---

## 📤 Return Values

### Normal mode:

Returns a list of open ports:

```python
[22, 80]
```

---

### Verbose mode:

Returns a formatted string:

```
Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http
```

---

## ⚠️ Error Handling

Your function must handle invalid input:

- Invalid hostname:

```
Error: Invalid hostname
```

- Invalid IP address:

```
Error: Invalid IP address
```

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

Run the project using:

```bash
python main.py
```

Run tests using:

```bash
python test_module.py
```

---

## 📁 Project Structure

```
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

Build a working port scanner that behaves like a simplified version of tools such as `nmap`.

---

## 📚 Reference

Project instructions:
[https://www.freecodecamp.org/learn/information-security/information-security-projects/port-scanner](https://www.freecodecamp.org/learn/information-security/information-security-projects/port-scanner)

```

```
