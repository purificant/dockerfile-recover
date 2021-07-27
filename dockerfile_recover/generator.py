"""This module contains methods to reconstruct Dockerfile from available data."""

from dockerfile_recover.parser import parse_history


def generate_dockerfile(docker_history: list[str]):
    """Return generated Dockerfile."""
    docker_history.reverse()
    return parse_history(docker_history)
