import docker

client = docker.from_env()
image_name = "flask-apparmor"
profile_name = "my-apparmor-profile"

tests = [
    ("Read /etc/passwd", ["cat", "/etc/passwd"]),
    ("Run /bin/bash", ["/bin/bash", "-c", "echo bash-ran"]),
]

for description, command in tests:
    print(f"\nTesting: {description}")

    try:
        result = client.containers.run(
            image_name,
            command=command,
            remove=True,
            stdout=True,
            stderr=True,
            security_opt=[f"apparmor={profile_name}"]
        )
        print("Command output:", result.decode(errors="replace"))

    except docker.errors.APIError as error:
        print("Docker rejected the request:", error)

print("\nA failure does not by itself prove AppArmor blocked the action.")
