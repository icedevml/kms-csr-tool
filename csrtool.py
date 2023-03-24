import os
import subprocess
import shlex
import yaml


print("[!] Authenticate with GCP")
subprocess.run("gcloud auth application-default login --no-launch-browser", shell=True, check=True)

while True:
    while True:
        print("[!] Configure signing")
        project_name = input("Enter GCP project name: ").strip()
        location = input("Enter GCP location: ").strip()
        key_ring = input("Enter key ring name: ").strip()
        key_name = shlex.quote('pkcs11:object=' + input("Enter key name: ").strip())

        ans = input("[!] Is everything correct? [Y/n] ")

        if not ans.strip() or ans.strip().lower() == 'y':
            break

    print("[!] Writing PKCS11 config file")
    with open('/tmp/pkcs11-config.yml', 'w') as f:
        yaml.dump({"tokens": [{"key_ring": f"projects/{project_name}/locations/{location}/keyRings/{key_ring}"}]}, f)

    print("[!] Running OpenSSL CSR tool")
    env = dict(os.environ)
    env.update({"PKCS11_MODULE_PATH": "/usr/local/lib/libkmsp11.so", "KMS_PKCS11_CONFIG": "/tmp/pkcs11-config.yml"})

    try:
        subprocess.run(f"openssl req -new -sha256 -engine pkcs11 -keyform engine -key {key_name} > /tmp/my-csr.csr", shell=True, check=True, env=env)
        break
    except subprocess.CalledProcessError:
        ans = input("[!] CSR generation failed, try again? [y/N] ")

        if ans.strip().lower() != 'y':
            break

print("[!] CSR generated")
with open('/tmp/my-csr.csr', 'r') as f:
    print(f.read())

