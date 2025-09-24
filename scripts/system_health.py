#!/usr/bin/env python3
import psutil
import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def log_alert(message):
    now = datetime.datetime.now()
    print(f"{now} - ALERT: {message}")

cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > CPU_THRESHOLD:
    log_alert(f"High CPU usage: {cpu_usage}%")

memory = psutil.virtual_memory()
if memory.percent > MEMORY_THRESHOLD:
    log_alert(f"High Memory usage: {memory.percent}%")

disk = psutil.disk_usage('/')
if disk.percent > DISK_THRESHOLD:
    log_alert(f"High Disk usage: {disk.percent}%")
print("\nTop 5 CPU-consuming processes:")
for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:5]:
    print(f"PID={proc.info['pid']} | CPU={proc.info['cpu_percent']}% | Name={proc.info['name']}")


