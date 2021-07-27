"""This file contains code to interact with docker api"""

from typing import Optional

import click
import docker
from docker import DockerClient
from docker.errors import ImageNotFound
from docker.models.images import Image


def get_client() -> DockerClient:
    """Return docker client instance for interacting with docker api."""
    return docker.from_env()


def get_image(docker_client: DockerClient, name: str, pull: bool) -> Optional[Image]:
    """Return Image object."""
    image = None

    try:
        if pull:
            click.echo(f"Pulling image {name}")
            docker_client.images.pull(name)

        image = docker_client.images.get(name)
    except ImageNotFound as image_not_found:
        click.echo(f"{ImageNotFound.__name__}: {image_not_found}", err=True)
        if not pull:
            click.echo("Did you want to --pull the image?")

    return image
