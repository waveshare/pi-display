import subprocess
import pkg_resources
import platform
import os

 
def platform_model_str():
    with open('/proc/device-tree/model', 'r') as f:
        return str(f.read()[:-1])


def platform_is_nano():
    return 'jetson-nano' in platform_model_str()


def ip_address(interface):
    try:
        if network_interface_state(interface) == 'down':
            return None
        cmd = "ifconfig %s | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'" % interface
        return subprocess.check_output(cmd, shell=True).decode('ascii')[:-1]
    except:
        return None


def network_interface_state(interface):
    try:
        with open('/sys/class/net/%s/operstate' % interface, 'r') as f:
            return f.read()
    except:
        return 'down' # default to down

    
def cpu_usage():
    """Gets the Jetson's current CPU usage fraction
    
    Returns:
        float: The current CPU usage fraction.
    """
    return float(subprocess.check_output("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'", shell = True ).decode('utf-8'))

    
def memory_usage():
    """Gets the Jetson's current RAM memory usage fraction
    
    Returns:
        float: The current RAM usage fraction.
    """
    return float(subprocess.check_output("free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'", shell = True ).decode('utf-8')) / 100.0


def disk_usage():
    """Gets the Jetson's current disk memory usage fraction
    
    Returns:
        float: The current disk usage fraction.
    """
    return float(subprocess.check_output("df -h | awk '$NF==\"/\"{printf \"%s\", $5}'", shell = True ).decode('utf-8').strip('%')) / 100.0
    
def temp():
    """Gets the temperature
    Returns:
        float: The current cpu temperature.
    """
    return float(subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell = True ).decode('utf-8')) / 1000.0