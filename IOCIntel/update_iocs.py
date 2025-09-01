import os
import requests

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

# ✅ Replace with your raw GitHub links for IOC sources
ioc_sources = {
    "ip": "https://raw.githubusercontent.com/<your-repo>/main/ip_addresses.txt",
    "c2": "https://raw.githubusercontent.com/<your-repo>/main/c2.txt",
    "commands": "https://raw.githubusercontent.com/<your-repo>/main/commands.txt",
    "domains": "https://raw.githubusercontent.com/<your-repo>/main/domains.txt",
    "urls": "https://raw.githubusercontent.com/<your-repo>/main/urls.txt",
    "hashes": "https://raw.githubusercontent.com/<your-repo>/main/hashes.txt",
    "hostnames": "https://raw.githubusercontent.com/<your-repo>/main/hostnames.txt",
    "cves": "https://raw.githubusercontent.com/<your-repo>/main/cves.txt",
    "signers": "https://raw.githubusercontent.com/<your-repo>/main/signers.txt",
}

# Ensure directory exists
os.makedirs(IOC_DIR, exist_ok=True)

# Fetch and update each IOC file
for key, url in ioc_sources.items():
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            content = resp.text.strip()
            with open(files[key], "w", encoding="utf-8") as f:
                f.write(content + "\n")
            print(f"✅ Updated {files[key]}")
        else:
            print(f"⚠️ Failed to fetch {url} (status {resp.status_code})")
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")

print("🎯 IOC update process completed")
