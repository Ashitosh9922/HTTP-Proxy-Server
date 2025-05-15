# HTTP-Proxy-Server
Sure! Below is a **complete `README.md` file** you can directly use in your GitHub repo for your **Python Proxy Server** project. Just copy and paste it into your `README.md` file and customize your **name**, **GitHub username**, or any specific links if you'd like.

---

```markdown
# 🔐 Python Proxy Server

A simple Python-based **HTTP Proxy Server** that:

- 🌐 Forwards HTTP requests to destination websites
- ❌ Blocks specific websites and keywords
- 📝 Logs all client requests with IP and timestamp
- 📄 Shows custom HTML pages for blocked sites or keywords

---

## 🚀 Features

- Acts as a basic HTTP proxy server
- Blocks requests based on:
  - Hostnames (e.g., `example.com`, `yahoo.com`)
  - Keywords in the URL (e.g., `gambling`, `movies`)
- Logs each client request to a file named `log_YYYY-MM-DD.txt`
- Sends a **custom response page** when a website or keyword is blocked

---

## 🛠️ Technologies Used

- Python 3
- Built-in `socket` module for networking
- `requests` module for forwarding HTTP requests
- `datetime` module for timestamps
- Custom Python classes: `RequestParser`, `ResponseManager`

---

## 📁 Project Structure

```

ProxyServer/
├── main.py                # Main proxy server logic
├── RequestParser.py       # Extracts HTTP method, host, and URL
├── ResponseManager.py     # Returns custom blocked response pages
├── log\_YYYY-MM-DD.txt     # Daily log file for request logging

````

---

## 🧩 How It Works

1. Browser sends HTTP request to the proxy
2. Proxy parses request:
   - Extracts URL and host
   - Checks if host or URL contains blocked items
3. If blocked:
   - Sends custom "Blocked" HTML page to browser
   - Logs the attempt
4. If allowed:
   - Forwards the request using `requests.get()`
   - Sends the website's response back to browser
   - Logs the successful request

---

## 🔧 How to Run the Proxy Server

1. 📥 Clone the repository

```bash
git clone https://github.com/yourusername/python-proxy-server.git
cd python-proxy-server
````

2. ▶️ Run the proxy server

```bash
python main.py
```

3. 🌐 Configure your browser to use proxy:

* Address: `localhost`
* Port: `2647` (default port used in `main.py`)

4. ✅ Try accessing allowed websites
5. ❌ Try accessing blocked sites (like `http://gambling.com`) to see the blocked response

---

## 🔒 Blocked Items

Update these lists in `main.py`:

```python
self.blocked_hosts = ["yahoo.com", "example.com"]
self.blocked_keywords = ["movies", "gambling"]
```

---

## 📝 Sample Log Entry (in `log_YYYY-MM-DD.txt`)

```
[2025-05-15 14:35:20] 127.0.0.1 requested http://example.com/
```

Each request is logged with date, time, IP address, and the requested URL.

---



---

## 🖼️ Demo Screenshot

> *(Add a screenshot of the browser showing the blocked message here if available)*

---





## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

```

---

