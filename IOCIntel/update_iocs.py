import os

IOC_DIR = "IOCIntel"

files = {
    "ip": f"{IOC_DIR}/ip_addresses.txt",
    "c2": f"{IOC_DIR}/c2.txt",
    "commands": f"{IOC_DIR}/commands.txt",
    "domains": f"{IOC_DIR}/domains.txt",
    "urls": f"{IOC_DIR}/urls.txt",
    "hashes": f"{IOC_DIR}/hashes.txt",
    "hostnames": f"{IOC_DIR}/hostnames.txt",
    "cves": f"{IOC_DIR}/cves.txt",
    "signers": f"{IOC_DIR}/signers.txt"
}

# 1. Ensure IOC directory exists
os.makedirs(IOC_DIR, exist_ok=True)

# 2. Example data (replace this with your IOC collection logic later)
dummy_data = {
    "ip": ["192.168.1.10", "10.0.0.5"],
    "c2": ["maliciousc2.example.com"],
    "commands": ["powershell -nop -w hidden"],
    "domains": ["bad-domain.com", "evil.com"],
    "urls": ["http://malware.test/abc", "https://phish.example/login"],
    "hashes": ["44d88612fea8a8f36de82e1278abb02f"],  # MD5/SHA1/SHA256 all in one
    "hostnames": ["infected-host"],
    "cves": ["CVE-2024-12345", "CVE-2025-67890"],
    "signers": ["FakeSigner Inc"]
}

# 3. Write IOCs into respective files
for key, path in files.items():
    with open(path, "w") as f:
        for item in dummy_data.get(key, []):
            f.write(item + "\n")

print("✅ IOC files updated successfully")
