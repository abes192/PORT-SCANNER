import socket

# Fungsi untuk memindai port
def scan_port(host, port):
    try:
        # Membuat socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Mencoba untuk terhubung ke host dan port yang ditentukan
        sock.connect((host, port))
        return True
    except:
        return False

# Meminta input alamat web atau IP
host = input("Masukkan alamat web atau IP: ")

# Daftar port yang akan di scan
ports = [5060, 21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 465, 587, 993, 995, 1433, 9100]

# Nama port yang akan di scan
port_names = ["SIP", "FTP", "SSH", "TELNET", "SMTP", "DNS", "HTTP", "POP3", "SMB", "HTTPS", "SMB", "SMTP w/SSL", "MSA", "IMAP", "POPS", "MS SQL SERVER", "PRINTER"]

# Scanning port
print("Mulai scanning port...")
for i in range(len(ports)):
    if scan_port(host, ports[i]):
        print("Port", ports[i], "("+port_names[i]+"): YES")
    else:
        print("Port", ports[i], "("+port_names[i]+"): NO")

print("Scanning selesai.")
