from socket import *
from ResponseManager import *
from RequestParser import *
import requests  # We will use this for HTTP requests to forward the requests
from datetime import datetime



class ProxyServer:
    def __init__(self, port):
        self.ip = "0.0.0.0"
        self.port = port
        self.http_header = "HTTP/1.1 200 OK\n\n"
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind((self.ip, self.port))
        self.responseManager = ResponseManager()

        # Blocked hosts and keywords (you can add more as needed)
        self.blocked_hosts = ["yahoo.com", "example.com"]  # List of blocked hosts
        self.blocked_keywords = ["movies", "gambling"]  # List of blocked keywords

    def listen(self, backlog):
        self.socket.listen(backlog)
        print(f"Proxy server is running on {self.port}")

    def accept(self):
        self.responseWriter, self.clientAddress = self.socket.accept()
        self.requestStr = self.responseWriter.recv(1024).decode()
        print(self.requestStr)
        reqParser = RequestParser(self.requestStr)
        self.url = reqParser.getReqUrl()
        self.host = reqParser.getReqHost()

        if self.isBlockedHost(self.host) or self.isBlockedKeyword(self.url):
            return  # Block the request and stop processing
        
        # ✅ Add this line
        self.logRequest(self.clientAddress[0], self.url)

        # Forward the valid request to the target server
        self.forwardRequest()

    def isBlockedHost(self, hostName):
        if hostName in self.blocked_hosts:
            msg = self.responseManager.getBlockedWebsitePage()
            self.responseWriter.sendall(msg.encode("utf-8"))
            self.responseWriter.close()
            return True  # Blocked host
        return False  # Not blocked

    def isBlockedKeyword(self, url):
        if any(keyword in url.lower() for keyword in self.blocked_keywords):
            msg = self.responseManager.getBlockedKeywordPage()
            self.responseWriter.sendall(msg.encode("utf-8"))
            self.responseWriter.close()
            return True  # Blocked keyword found
        return False  # Not blocked
    
    def logRequest(self, client_ip, url):
         timestamp = datetime.now()
         date_str = timestamp.strftime("%Y-%m-%d")
         time_str = timestamp.strftime("%H:%M:%S")
         log_entry = f"[{date_str} {time_str}] {client_ip} requested {url}\n"

         log_filename = f"log_{date_str}.txt"
         with open(log_filename, "a") as logfile:
                logfile.write(log_entry)

    
    def forwardRequest(self):
        try:
            # Use requests to get the content from the actual URL
          response = requests.get(self.url)

        # Send response back to the client
          self.responseWriter.sendall(f"HTTP/1.1 {response.status_code} OK\r\n".encode("utf-8"))
          self.responseWriter.sendall(f"Content-Type: {response.headers.get('Content-Type')}\r\n\r\n".encode("utf-8"))
          self.responseWriter.sendall(response.content)

          self.responseWriter.close()

        except Exception as e:
            print(f"Error forwarding request: {e}")
            self.responseWriter.sendall(f"HTTP/1.1 500 Internal Server Error\r\n\r\nError: {str(e)}".encode("utf-8"))
            self.responseWriter.close()

     
if __name__ == '__main__':
    proxy = ProxyServer(2647)
    proxy.listen(5)
    while True:
        proxy.accept()
