from datetime import datetime

def find_hostname():
    with open('/etc/hostname', 'r') as f:
        return f.read().strip()
    
def find_kernel():
    with open('/proc/version', 'r') as f:
        kernel=f.read().strip()
    return kernel

def find_uptime():
    with open('/proc/uptime', 'r') as f:
        seconds=float(f.read().split()[0])
        days=int(seconds//86400)
        hours=int((seconds%86400)//3600)
        minutes=int((seconds%3600)//60)
    return f"{days}j {hours}h {minutes}min"

#def find_temperatures():
  #  time=[]
   # for zone in glob.glob('/sys/class/thermal/thermal_zone*'):
      # with open(f"")



    















    
def generate_html(hostname,kernel,uptime,output):
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Rapport Système SupKrellM</title>
</head>
<body>
    <h1>SupKrellM</h1>
    <h2>Informations générales du système :</h2>
    <p>Le {datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}</p>
    <p>Nom d'hôte : {hostname}</p>
    <p>Version du noyau: {kernel}</p>
    <p>Temps de fonctionnement des différents composants: {uptime}</p>
</body>
</html>"""
    
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    hostname = find_hostname()
    kernel = find_kernel()
    uptime = find_uptime()
    generate_html(hostname,kernel,uptime, "projets1.html")

if __name__=="__main__":
    main()
    







