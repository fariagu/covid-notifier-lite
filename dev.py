from dotenv import load_dotenv
import os
import subprocess
from backend.main import start

load_dotenv()

def main():
    db_container_name = os.environ.get("DB_CONTAINER_NAME")
    db_container_port = os.environ.get("DB_CONTAINER_PORT")
    db_username = os.environ.get("DB_USERNAME")
    db_password = os.environ.get("DB_PASSWORD")

    port = f"{db_container_port}:{db_container_port}"
    username = f"MONGO_INITDB_ROOT_USERNAME={db_username}"
    password = f"MONGO_INITDB_ROOT_PASSWORD={db_password}"

    docker_filter = f"docker ps -a --filter name={db_container_name}"

    docker_filter_output = subprocess.check_output(docker_filter, shell=True)
    
    if db_container_name in str(docker_filter_output):
        docker_inspect = f"docker container inspect -f '{{{{.State.Status}}}}' {db_container_name}"

        try:
            docker_inspect_output = subprocess.check_output(docker_inspect, shell=True)
        except Exception:
            docker_inspect_output = ""

        if "exited" in str(docker_inspect_output):
            docker_start = f"docker start {db_container_name}"
            subprocess.check_output(docker_start, shell=True)
        
    else:
        docker_run = f"docker run --name mongodb -d -p {port} -e {username} -e {password} mongo"
        subprocess.check_output(docker_run, shell=True)

    start()