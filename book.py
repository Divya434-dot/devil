import os
import subprocess
import sys

def create_virtual_env(env_name):
    # Create a virtual environment
    if not os.path.exists(env_name):
        print(f"Creating virtual environment: {env_name}")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
    else:
        print(f"Virtual environment '{env_name}' already exists.")

def activate_and_install(env_name, package_name):
    # Activate the virtual environment and install a package
    if os.name == 'nt':  # For Windows
        activate_script = os.path.join(env_name, "Scripts", "activate")
    else:  # For macOS/Linux
        activate_script = os.path.join(env_name, "bin", "activate")

    if os.path.exists(activate_script):
        print(f"Activating virtual environment: {env_name}")
        activate_command = f"{activate_script} && pip install {package_name}"
        subprocess.run(activate_command, shell=True, check=True)
    else:
        print("Activation script not found. Ensure the virtual environment was created successfully.")

if __name__ == "__main__":
    env_name = "myenv"  # Name of the virtual environment
    package_name = "requests"  # Replace with the package you want to install

    try:
        create_virtual_env(env_name)
        activate_and_install(env_name
