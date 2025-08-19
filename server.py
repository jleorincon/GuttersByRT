#!/usr/bin/env python3
"""
Simple HTTP server to host the Gutters by RT website locally.
Run this script and visit http://localhost:8000 to view the website.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create the server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"🌐 Gutters by RT website is now running!")
        print(f"📍 Local URL: http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🔧 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Try to open the browser automatically
        try:
            webbrowser.open(f"http://localhost:{PORT}")
            print("🚀 Opening website in your default browser...")
        except:
            print("💡 Manually open http://localhost:8000 in your browser")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped. Thanks for using Gutters by RT!")
            sys.exit(0)

if __name__ == "__main__":
    main()
