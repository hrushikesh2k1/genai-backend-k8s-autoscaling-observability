import time
import random

RESPONSES = [
    "Kubernetes helps deploy and scale containerized applications.",
    "Docker packages applications with all dependencies.",
    "DevOps focuses on automation, reliability, and fast delivery.",
    "Containers make applications portable and scalable."
]

def generate_text(prompt: str) -> str:
    # Simulate inference latency
    time.sleep(random.uniform(0.5, 1.5))

    prompt_lower = prompt.lower()

    if "kubernetes" in prompt_lower:
        return "Kubernetes is used to orchestrate and manage containers."
    elif "docker" in prompt_lower:
        return "Docker allows applications to run consistently across environments."
    else:
        return random.choice(RESPONSES)
