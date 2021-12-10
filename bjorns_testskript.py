import subprocess

with open("min_input") as i:
    p = subprocess.Popen("python bjorns_exempel.py", stdin=i)
    p.wait()
