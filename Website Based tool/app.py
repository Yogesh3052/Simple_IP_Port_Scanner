from flask import Flask, render_template, request
import socket
from datetime import datetime
import re

app = Flask(__name__)

def is_valid_ip(ip):
    # Regular expression to validate an IP address
    ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(ip_regex, ip)

def is_valid_domain(domain):
    # Regular expression to validate a domain name
    domain_regex = r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return re.match(domain_regex, domain)

def resolve_target(target):
    if is_valid_ip(target):
        return target
    elif is_valid_domain(target):
        return socket.gethostbyname(target)
    else:
        raise ValueError("Invalid target. Please enter a valid IP address or domain name.")

def scan_ports(target, start_port, end_port):
    try:
        results = []
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                results.append(port)
            s.close()
        return results
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    try:
        target = request.form['target']
        target = resolve_target(target)  # Resolve target to IP address if it's a domain
        start_port = int(request.form['start_port'])
        end_port = int(request.form['end_port'])
        start_time = datetime.now()
        open_ports = scan_ports(target, start_port, end_port)
        end_time = datetime.now()
        return render_template('result.html', target=target, start_port=start_port, end_port=end_port, open_ports=open_ports, start_time=start_time, end_time=end_time)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
