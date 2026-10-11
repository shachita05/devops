import docker

client = docker.from_env()
image_name = "flask-apparmor"
container_name = "flask-apparmor-security-test"
profile_name = "my-apparmor-profile"

try:
    print("Building Docker image...")
    image, _ = client.images.build(path=".", tag=image_name)
    print("Image built:", image.tags)

    print("Starting container with requested AppArmor profile...")
    container = client.containers.run(
        image_name,
        name=container_name,
        detach=True,
        ports={"5000/tcp": 5002},
        security_opt=[f"apparmor={profile_name}"]
    )

    container.reload()
    print("Security options:", container.attrs["HostConfig"]["SecurityOpt"])
    print("Requested options do not prove AppArmor enforcement.")

except docker.errors.APIError as error:
    print("Docker rejected the container configuration:")
    print(error)

finally:
    try:
        client.containers.get(container_name).remove(force=True)
        print("Test container removed.")
    except docker.errors.NotFound:
        pass
