
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "jenkins-pipeline-lab"}


if __name__ == "__main__":
    print(health_check())

