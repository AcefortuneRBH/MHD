import random

def scan_for_threats():
    threats = ["SQL Injection", "Phishing", "Zero-Day Exploit", "Quantum Hack"]
    return f"🛡️ Threat Neutralized: {random.choice(threats)}"

print(scan_for_threats())

