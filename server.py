#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import subprocess
from urllib.parse import parse_qs
import cgi
import datetime

PORT = 8888

class UploadHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            # Parse multipart form data
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type'],
                }
            )
            
            # Get uploaded file
            file_item = form['file']
            
            if file_item.filename:
                # Create timestamp filename
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                ext = os.path.splitext(file_item.filename)[1]
                filename = f"foto_{timestamp}{ext}"
                
                # Save file
                filepath = os.path.join('/tmp/sommerfest-fotos-temp', filename)
                with open(filepath, 'wb') as f:
                    f.write(file_item.file.read())
                
                # Git add, commit and push
                try:
                    subprocess.run(['git', 'add', filename], cwd='/tmp/sommerfest-fotos-temp', check=True)
                    subprocess.run(['git', 'commit', '-m', f'Foto hochgeladen: {filename}'], cwd='/tmp/sommerfest-fotos-temp', check=True)
                    subprocess.run(['git', 'push', 'origin', 'main'], cwd='/tmp/sommerfest-fotos-temp', check=True)
                    
                    # Send success response
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'status': 'success', 'filename': filename}).encode())
                except Exception as e:
                    # Send error response
                    self.send_response(500)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode())
            else:
                self.send_response(400)
                self.end_headers()

# Configure git
os.system('git config --global user.email "frank@frankrath.de"')
os.system('git config --global user.name "Frank Rath"')

# Start server
with socketserver.TCPServer(("0.0.0.0", PORT), UploadHandler) as httpd:
    print(f"Server läuft auf Port {PORT}")
    print(f"Zugriff über: http://automatisierung.frankrath.de:{PORT}")
    httpd.serve_forever()
