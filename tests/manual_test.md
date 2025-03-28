# ✅ Manual Test Log – TCP Client and Server

This document contains a record of the manual tests performed to validate the TCP client and server functionality.

---

## Test 1: Uppercase Response

**Objective:** Verify that the server returns the same message in uppercase.

**Steps:**
1. Start the server:
   ```bash
   python server/server.py
   ```
2. Start the client:
   ```bash
   python client/client.py
   ```
3. Enter the following message:
   ```
   hello world
   ```

**Expected Result:**
```
Server response: HELLO WORLD
```

**Status:** ✅ Passed

---

## Test 2: Graceful Disconnection

**Objective:** Verify that the client can disconnect using the special command `DESCONEXION`.

**Steps:**
1. With the server still running, start a new client session.
2. Enter the following message:
   ```
   DESCONEXION
   ```

**Expected Result:**
- Client prints no response and exits.
- Server logs:
  ```
  🔒 Disconnecting client ('127.0.0.1', XXXXX)
  ❌ Connection with ('127.0.0.1', XXXXX) closed
  ```
- Server stays running and ready for new clients.

**Status:** ✅ Passed

---

## Test 3 (Optional): Multiple Clients Simultaneously

**Objective:** Ensure that the server can handle more than one client connection concurrently.

**Steps:**
1. Start the server.
2. Open two terminal windows, start a client in each.
3. In both clients, send different messages (e.g. "foo", "bar").

**Expected Result:**
- Both clients receive independent responses.
- No crash or overlap in logs.

**Status:** ✅ Passed (optional)

---

## Notes

- All tests were run on macOS 14 using Python 3.12 and Poetry-managed virtual environments.
- Socket communication was stable during all manual tests.
