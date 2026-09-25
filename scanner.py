#!/usr/bin/env python3
import argparse, ipaddress, platform, socket, subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def alive(ip):
    win=platform.system()=="Windows"
    cmd=["ping","-n" if win else "-c","1","-w" if win else "-W","700" if win else "1",str(ip)]
    return subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0

def name(ip):
    try:return socket.gethostbyaddr(str(ip))[0]
    except socket.herror:return "-"

def main():
    p=argparse.ArgumentParser(description="Discover active hosts on an authorized network.")
    p.add_argument("network",help="CIDR, e.g. 192.168.1.0/24")
    p.add_argument("--workers",type=int,default=64)
    a=p.parse_args(); net=ipaddress.ip_network(a.network,strict=False)
    print(f"Scanning {net} ...")
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        jobs={ex.submit(alive,ip):ip for ip in net.hosts()}
        for job in as_completed(jobs):
            ip=jobs[job]
            if job.result(): print(f"[UP] {str(ip):15} {name(ip)}")
if __name__=="__main__": main()
