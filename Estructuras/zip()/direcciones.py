dispositivos = ["router", "servidor", "impresora", "laptop"]
ips = ["192.168.1.1", "192.168.1.10", "192.168.1.20", "192.168.1.35"]
red = dict(zip(dispositivos, ips))
print(red)
for dispositivo, ip in red.items():
    print(dispositivo + ":", ip)
