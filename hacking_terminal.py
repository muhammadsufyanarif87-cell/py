import time
import random
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# HISTORY
history = []

# FAKE FILE SYSTEM
fake_files = [
    "config.txt", "passwords.sh", "exploit.py", "tool.sh",
    "readme.md", "hack.py", "scan.sh", "payload.txt"
]

fake_dirs = [
    "tools/", "scripts/", "logs/", "backup/", "tmp/", "home/"
]

# WINDOW
root = tk.Tk()
root.title("SA TERMUX")
root.geometry("950x600")
root.config(bg="#1a1a1a")

# TERMINAL
terminal = ScrolledText(
    root,
    bg="#1a1a1a",
    fg="lime",
    insertbackground="lime",
    font=("Courier New", 11),
    border=0,
    padx=10,
    pady=2
)

terminal.pack(fill="both", expand=True, padx=10, pady=10)

# READ ONLY
terminal.config(state="disabled")

# BANNER
banner = [
'███████╗ █████╗     ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗',
'██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝',
'███████╗███████║       ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ ',
'╚════██║██╔══██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ ',
'███████║██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗',
'╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝'
]

# WRITE FUNCTION
def write(text=""):
    terminal.config(state="normal")
    terminal.insert("end", text + "\n")
    terminal.see("end")
    terminal.config(state="disabled")

# SHOW BANNER
for i in banner:
    write(i)
    root.update()
    time.sleep(0.15)

write("")
write("  Version 2.0  |  Type sudo --help for commands")
write("")

# COMMAND FUNCTION
def run_command(event=None):

    user = entry.get().strip()

    if user == "":
        return

    entry.delete(0, "end")

    write("┌──(root㉿SA-Termux)-[~]")
    write(f"└─# {user}")
    write("")

    if user != "clear":
        history.append(user)

    # CLEAR
    if user == "clear":
        terminal.config(state="normal")
        terminal.delete("1.0", "end")
        terminal.config(state="disabled")
        return

    # HISTORY
    elif user == "history":
        if len(history) == 1:
            write("No command history yet.")
        else:
            write("COMMAND HISTORY")
            write("")
            for index, cmd in enumerate(history[:-1]):
                write(f"  {index + 1}  {cmd}")

    # SUDO --HELP
    elif user == "sudo --help":
        write("=" * 60)
        write("  SA TERMUX - AVAILABLE COMMANDS")
        write("=" * 60)
        write("")
        commands = [
            ("SYSTEM", [
                "sudo update          - Update package lists",
                "sudo upgrade -y      - Upgrade all packages",
                "sudo reboot          - Reboot the system",
                "sudo shutdown        - Shutdown the system",
                "sudo apt install     - Install a package",
                "sudo apt remove      - Remove a package",
                "sudo apt list        - List installed packages",
                "sudo apt search      - Search for a package",
            ]),
            ("INFO", [
                "uname                - Show kernel name",
                "uname -a             - Full system information",
                "neofetch             - System info with logo",
                "date                 - Show current date/time",
                "uptime               - Show system uptime",
                "whoami               - Show current user",
                "id                   - Show user/group IDs",
                "hostname             - Show machine hostname",
                "env                  - Show environment variables",
                "which <cmd>          - Find location of command",
            ]),
            ("FILES", [
                "ls                   - List files",
                "ls -la               - List files (detailed)",
                "pwd                  - Print working directory",
                "cat <file>           - Show file contents",
                "mkdir <name>         - Create a directory",
                "rm <file>            - Remove a file",
                "rm -rf <dir>         - Remove directory (force)",
                "cp <src> <dst>       - Copy a file",
                "mv <src> <dst>       - Move/rename a file",
                "chmod 777 <file>     - Change file permissions",
                "find / -name <file>  - Search for a file",
            ]),
            ("NETWORK", [
                "ifconfig             - Show network interfaces",
                "ip addr              - Show IP addresses",
                "ping <host>          - Ping a host",
                "curl <url>           - Fetch URL content",
                "wget <url>           - Download a file",
                "netstat -an          - Show network connections",
                "ssh <user@host>      - Connect via SSH",
                "nmap <host>          - Network scan",
            ]),
            ("PROCESS", [
                "ps                   - Show running processes",
                "ps aux               - Show all processes",
                "top                  - Live process monitor",
                "kill <pid>           - Kill a process by PID",
                "killall <name>       - Kill process by name",
                "df -h                - Disk usage (human)",
                "free -h              - Memory usage (human)",
            ]),
            ("OTHER", [
                "echo <text>          - Print text",
                "history              - Show command history",
                "clear                - Clear the terminal",
                "exit                 - Exit SA Termux",
            ]),
        ]
        for section, cmds in commands:
            write(f"  [{section}]")
            for cmd in cmds:
                write(f"    {cmd}")
                root.update()
                time.sleep(0.05)
            write("")
        write("=" * 60)

    # SUDO UPDATE
    elif user == "sudo update":
        for s in ['[✓] Connecting to repository...','[✓] Fetching package lists...','[✓] Reading package information...','[✓] Checking for new packages...','[✓] Package lists updated successfully']:
            write(s); root.update(); time.sleep(0.6)

    # SUDO UPGRADE -Y
    elif user == "sudo upgrade -y":
        for s in ['[✓] Reading package lists...','[✓] Building dependency tree...','[✓] Calculating upgrade...',f'[✓] {random.randint(10,50)} packages will be upgraded...','[✓] Downloading packages...','[✓] Installing upgrades...','[✓] Cleaning temporary files...','[✓] System upgrade completed successfully']:
            write(s); root.update(); time.sleep(0.6)

    # SUDO REBOOT
    elif user == "sudo reboot":
        for s in ['[✓] Stopping services...','[✓] Saving system state...','[✓] Rebooting now...']:
            write(s); root.update(); time.sleep(0.8)
        write(""); write("System is rebooting..."); root.update(); time.sleep(1.5)
        terminal.config(state="normal"); terminal.delete("1.0", "end"); terminal.config(state="disabled")
        for i in banner:
            write(i); root.update(); time.sleep(0.1)
        write(""); write("  System rebooted successfully!"); write("")

    # SUDO SHUTDOWN
    elif user == "sudo shutdown":
        for s in ['[✓] Stopping all services...','[✓] Unmounting filesystems...','[✓] Shutting down...']:
            write(s); root.update(); time.sleep(0.8)
        root.after(1000, root.destroy)

    # SUDO APT INSTALL
    elif user.startswith("sudo apt install"):
        parts = user.split()
        pkg = parts[3] if len(parts) > 3 else "package"
        for s in [f'[✓] Reading package lists...',f'[✓] Building dependency tree...',f'[✓] Downloading {pkg}...',f'[✓] Unpacking {pkg}...',f'[✓] Setting up {pkg}...',f'[✓] {pkg} installed successfully']:
            write(s); root.update(); time.sleep(0.6)

    # SUDO APT REMOVE
    elif user.startswith("sudo apt remove"):
        parts = user.split()
        pkg = parts[3] if len(parts) > 3 else "package"
        for s in [f'[✓] Reading package lists...',f'[✓] Removing {pkg}...',f'[✓] Cleaning up configuration...',f'[✓] {pkg} removed successfully']:
            write(s); root.update(); time.sleep(0.6)

    # SUDO APT LIST
    elif user == "sudo apt list":
        pkgs = ["python3/stable 3.11.0 installed","nmap/stable 7.93 installed","curl/stable 7.88.1 installed","wget/stable 1.21.3 installed","git/stable 2.39.2 installed","openssh/stable 9.2p1 installed","netcat/stable 1.10 installed","hydra/stable 9.4 installed","sqlmap/stable 1.7 installed","metasploit/stable 6.3 installed"]
        write(f"Listing installed packages ({len(pkgs)} total):"); write("")
        for p in pkgs:
            write(f"  {p}"); root.update(); time.sleep(0.08)

    # SUDO APT SEARCH
    elif user.startswith("sudo apt search"):
        parts = user.split()
        query = parts[3] if len(parts) > 3 else "tool"
        write(f"Searching for '{query}'..."); write("")
        for r in [f"{query}-utils/stable 1.0.0",f"{query}-dev/stable 1.0.0",f"lib{query}/stable 1.0.0",f"python3-{query}/stable 1.0.0"]:
            write(f"  {r}"); root.update(); time.sleep(0.1)

    # UNAME
    elif user == "uname":
        write("Linux")

    elif user == "uname -a":
        write("Linux SA-Termux 5.15.0-kali3-amd64 #1 SMP Debian 5.15.15-2kali1 x86_64 GNU/Linux")

    # NEOFETCH
    elif user == "neofetch":
        for line in ["        #####          root@SA-Termux","       #######         ─────────────","       ##O#O##         OS: Kali Linux x86_64","       #######         Host: SA-Termux 2.0","     ###########       Kernel: 5.15.0-kali3","    #############      Shell: SA-Termux","   ###############     Terminal: SA-Termux v2.0","  #################    CPU: Intel Core i7 (8) @ 3.6GHz"," #####################  Memory: 2048MiB / 8192MiB","  ###################   Disk: 15GB / 50GB"]:
            write(line); root.update(); time.sleep(0.1)

    # DATE
    elif user == "date":
        write(time.ctime())

    # UPTIME
    elif user == "uptime":
        h = random.randint(1,23); m = random.randint(0,59)
        write(f" {time.strftime('%H:%M:%S')}  up {h}:{m:02d},  1 user,  load average: 0.{random.randint(10,99)}, 0.{random.randint(10,99)}, 0.{random.randint(10,99)}")

    # WHOAMI
    elif user == "whoami":
        write("root")

    # ID
    elif user == "id":
        write("uid=0(root) gid=0(root) groups=0(root)")

    # HOSTNAME
    elif user == "hostname":
        write("SA-Termux")

    # ENV
    elif user == "env":
        for e in ["USER=root","HOME=/root","SHELL=/bin/bash","TERM=xterm-256color","PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin","LANG=en_US.UTF-8","PWD=/root/home","HOSTNAME=SA-Termux"]:
            write(e); root.update(); time.sleep(0.05)

    # WHICH
    elif user.startswith("which"):
        parts = user.split()
        write(f"/usr/bin/{parts[1]}" if len(parts) > 1 else "which: missing argument")

    # LS
    elif user == "ls":
        write("  ".join(fake_dirs + fake_files))

    elif user == "ls -la":
        write("total 64")
        write("drwxr-xr-x  8 root root 4096 " + time.strftime("%b %d %H:%M") + " .")
        write("drwxr-xr-x 24 root root 4096 " + time.strftime("%b %d %H:%M") + " ..")
        for d in fake_dirs:
            write(f"drwxr-xr-x  2 root root 4096 {time.strftime('%b %d %H:%M')} {d}"); root.update(); time.sleep(0.05)
        for f in fake_files:
            write(f"-rwxr-xr-x  1 root root {random.randint(100,9999):4d} {time.strftime('%b %d %H:%M')} {f}"); root.update(); time.sleep(0.05)

    # PWD
    elif user == "pwd":
        write("/root/home")

    # CAT
    elif user.startswith("cat"):
        parts = user.split()
        fname = parts[1] if len(parts) > 1 else ""
        if fname in fake_files:
            write(f"--- {fname} ---"); write("[SA-Termux] File content loaded."); write("This is a simulated file in SA Termux.")
        elif fname == "":
            write("cat: missing file operand")
        else:
            write(f"cat: {fname}: No such file or directory")

    # MKDIR
    elif user.startswith("mkdir"):
        parts = user.split()
        if len(parts) > 1:
            fake_dirs.append(parts[1] + "/"); write(f"Directory '{parts[1]}' created.")
        else:
            write("mkdir: missing operand")

    # RM
    elif user.startswith("rm"):
        parts = user.split()
        write(f"[✓] Removed: {parts[-1]}" if len(parts) > 1 else "rm: missing operand")

    # CP
    elif user.startswith("cp"):
        parts = user.split()
        write(f"[✓] Copied '{parts[1]}' to '{parts[2]}'" if len(parts) >= 3 else "cp: missing file operand")

    # MV
    elif user.startswith("mv"):
        parts = user.split()
        write(f"[✓] Moved '{parts[1]}' to '{parts[2]}'" if len(parts) >= 3 else "mv: missing file operand")

    # CHMOD
    elif user.startswith("chmod"):
        parts = user.split()
        write(f"[✓] Permissions changed: {parts[1]} -> {parts[2]}" if len(parts) >= 3 else "chmod: missing operand")

    # FIND
    elif user.startswith("find"):
        parts = user.split()
        fname = parts[-1] if len(parts) > 1 else ""
        write(f"Searching for '{fname}'..."); root.update(); time.sleep(0.8)
        write(f"/root/home/{fname}"); write(f"/root/tools/{fname}")

    # IFCONFIG
    elif user == "ifconfig":
        write("eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500")
        write("      inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255")
        write("      ether 00:0c:29:ab:cd:ef  txqueuelen 1000  (Ethernet)")
        write(""); write("lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536")
        write("      inet 127.0.0.1  netmask 255.0.0.0")

    # IP ADDR
    elif user == "ip addr":
        write("1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536")
        write("    inet 127.0.0.1/8 scope host lo")
        write("2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500")
        write("    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0")

    # PING
    elif user.startswith("ping"):
        parts = user.split()
        host = parts[1] if len(parts) > 1 else "localhost"
        write(f"PING {host}: 56 data bytes")
        for i in range(4):
            write(f"64 bytes from {host}: icmp_seq={i+1} ttl=64 time={random.randint(10,99)}.{random.randint(1,9)} ms")
            root.update(); time.sleep(0.5)
        write(f"--- {host} ping statistics ---")
        write("4 packets transmitted, 4 received, 0% packet loss")

    # CURL
    elif user.startswith("curl"):
        parts = user.split()
        if len(parts) > 1:
            write(f"[✓] Connecting to {parts[1]}..."); root.update(); time.sleep(0.8)
            write("HTTP/1.1 200 OK"); write("Content-Type: text/html"); write(""); write("<html><body>Response received.</body></html>")
        else:
            write("curl: no URL specified")

    # WGET
    elif user.startswith("wget"):
        parts = user.split()
        if len(parts) > 1:
            fname = parts[1].split("/")[-1] or "index.html"
            for s in [f"--{time.strftime('%H:%M:%S')}--  {parts[1]}","Connecting to server... connected.","HTTP request sent, awaiting response... 200 OK",f"Length: {random.randint(1000,99999)} bytes",f"Saving to: '{fname}'","",f"[✓] '{fname}' saved"]:
                write(s); root.update(); time.sleep(0.4)
        else:
            write("wget: missing URL")

    # NETSTAT
    elif user == "netstat -an":
        write("Proto  Local Address          Foreign Address        State")
        for p in [22, 80, 443, 8080, 3306]:
            write(f"tcp    0.0.0.0:{p:<5}         0.0.0.0:*              {random.choice(['LISTEN','ESTABLISHED'])}")
            root.update(); time.sleep(0.1)

    # SSH
    elif user.startswith("ssh"):
        parts = user.split()
        target = parts[1] if len(parts) > 1 else "host"
        write(f"SSH: Connecting to {target}..."); root.update(); time.sleep(1)
        write(f"Warning: Permanently added '{target}' to known hosts.")
        root.update(); time.sleep(0.8); write(f"[✓] Connected to {target}")

    # NMAP
    elif user.startswith("nmap"):
        parts = user.split()
        host = parts[1] if len(parts) > 1 else "192.168.1.1"
        write(f"Starting Nmap scan on {host}..."); root.update(); time.sleep(1.2)
        write(f"Nmap scan report for {host}")
        write(f"Host is up ({random.randint(1,99)}ms latency)."); write(""); write("PORT     STATE  SERVICE")
        for port, service in [("22/tcp","ssh"),("80/tcp","http"),("443/tcp","https"),("3306/tcp","mysql"),("8080/tcp","http-proxy")]:
            write(f"{port:<10} open   {service}"); root.update(); time.sleep(0.2)
        write(""); write("Nmap done: 1 IP address scanned")

    # PS
    elif user == "ps":
        write("  PID TTY          TIME CMD")
        for pid,tty,t,cmd in [("1234","pts/0","00:00:00","bash"),("1235","pts/0","00:00:01","python3"),("1236","pts/0","00:00:00","ps")]:
            write(f"{pid:>5} {tty:<12} {t} {cmd}")

    elif user == "ps aux":
        write("USER       PID %CPU %MEM  COMMAND")
        for p in [("root","1","0.0","0.1","init"),("root","423","0.0","0.3","sshd"),("root","512","0.1","0.5","python3"),("root","1234","0.0","0.2","bash"),("root","1235","0.5","1.2","sa_termux")]:
            write(f"{p[0]:<10} {p[1]:<6} {p[2]:<5} {p[3]:<5} {p[4]}"); root.update(); time.sleep(0.08)

    # TOP
    elif user == "top":
        write(f"top - {time.strftime('%H:%M:%S')} up {random.randint(1,12)}:{random.randint(10,59):02d},  1 user")
        write(f"%Cpu(s): {random.randint(1,15)}.0 us,  {random.randint(1,5)}.0 sy")
        write(f"MiB Mem:  8192.0 total,  {random.randint(2000,5000)}.0 free"); write("")
        write("  PID USER     %CPU %MEM  COMMAND")
        for t in [("1235","root","12.3","2.1","sa_termux"),("512","root","3.2","1.0","python3"),("423","root","0.5","0.3","sshd"),("1","root","0.0","0.1","init")]:
            write(f"{t[0]:>6} {t[1]:<10} {t[2]:<5} {t[3]:<5} {t[4]}"); root.update(); time.sleep(0.1)

    # KILL
    elif user.startswith("kill"):
        parts = user.split()
        write(f"[✓] Process {parts[1]} killed." if len(parts) > 1 else "kill: missing PID")

    # KILLALL
    elif user.startswith("killall"):
        parts = user.split()
        write(f"[✓] All '{parts[1]}' processes terminated." if len(parts) > 1 else "killall: missing process name")

    # DF -H
    elif user == "df -h":
        write("Filesystem      Size  Used Avail Use% Mounted on")
        write("/dev/sda1        50G   15G   35G  30% /")
        write("tmpfs           4.0G  128M  3.9G   4% /tmp")
        write("/dev/sda2       100G   60G   40G  60% /home")

    # FREE -H
    elif user == "free -h":
        used = random.randint(1,5); free = 8 - used
        write("              total    used    free")
        write(f"Mem:           8.0G    {used}.{random.randint(0,9)}G    {free}.{random.randint(0,9)}G")
        write(f"Swap:          2.0G    0.0G    2.0G")

    # ECHO
    elif user.startswith("echo"):
        write(user[5:].strip())

    # EXIT
    elif user == "exit":
        write("Goodbye from SA Termux!"); root.update(); time.sleep(1); root.destroy()

    # UNKNOWN
    else:
        write(f"bash: {user.split()[0]}: command not found")
        write("Type 'sudo --help' for available commands")

    write("")

# INPUT FRAME
bottom = tk.Frame(root, bg="#1a1a1a")
bottom.pack(fill="x", padx=15, pady=10)

sign = tk.Label(bottom, text="└─#", fg="lime", bg="#1a1a1a", font=("Courier New", 13))
sign.pack(side="left", padx=(0, 5))

entry = tk.Entry(bottom, bg="#1a1a1a", fg="lime", insertbackground="lime", font=("Courier New", 13), border=0)
entry.pack(side="left", fill="x", expand=True)

entry.bind("<Return>", run_command)
entry.focus()

root.mainloop()