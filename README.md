# 🧠 TCP Client and Server in Python

![Code Quality](https://github.com/homodeusdev/server_client_tcp_in_python/actions/workflows/code-quality.yml/badge.svg)
![Test Status](https://github.com/homodeusdev/server_client_tcp_in_python/actions/workflows/tests.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Code Style](https://img.shields.io/badge/code%20style-black-000000)
![License](https://img.shields.io/badge/license-none-lightgrey)

A simple Python implementation of a TCP client and server communicating over `localhost:5000`.

---

## 🛠 Requirements

- Python 3.12
- [Poetry](https://python-poetry.org/docs/#installation)

---

## ⚙️ Installation

Clone the repository and install dependencies using Poetry:

```bash
git clone https://github.com/homodeusdev/server_client_tcp_in_python.git
cd server_client_tcp_in_python
poetry install
```

Activate the virtual environment:

```bash
source $(poetry env info --path)/bin/activate
```

---

## 🚀 Running the Server and Client

### ✅ Start the TCP Server

In one terminal window:

```bash
python server/server.py
```

You should see a log message indicating the server is listening on `localhost:5000`.

---

### ✅ Start the TCP Client

In a **separate** terminal (also inside the poetry environment):

```bash
python client/client.py
```

The client will prompt for input:

```text
Enter a message: hello server
Server response: HELLO SERVER
```

To gracefully disconnect:

```text
Enter a message: DESCONEXION
```

---

## ✅ Manual Test Cases

### 🔹 Test 1: Uppercase Response

1. Start the server (`python server/server.py`)
2. Start the client (`python client/client.py`)
3. Type a normal message:
   ```
   Enter a message: hello world
   ```
4. Expected response:
   ```
   Server response: HELLO WORLD
   ```

---

### 🔹 Test 2: Disconnection

1. In the client, type:
   ```
   Enter a message: DESCONEXION
   ```
2. Expected behavior:
   - Server logs a message about client disconnection
   - Client session ends
   - Server remains available for new connections

---

## 📁 Project Structure

```
tcp_chat/
│
├── client/
│   └── client.py
├── server/
│   └── server.py
├── tests/
│   └── manual_test.md
├── README.md
├── pyproject.toml
└── .gitignore
```

---

## 📄 License

**No license.**

---
