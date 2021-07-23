"""This module contains main codebase for dockerfile-recover tool."""

import click
import docker
from docker.errors import ImageNotFound
from docker.models.images import Image

from dockerfile_recover.parser import parse_history


@click.command(
    help="Recover Dockerfile by providing an image name similar to: docker pull <name>"
)
@click.argument("name")
def main(name):
    """Command line interface entrypoint."""

    client = docker.from_env()

    try:
        client.images.pull(name)
    except ImageNotFound:
        click.echo(f"{ImageNotFound.__name__}: {name}", err=True)
        return

    image: Image = client.images.get(name)

    history = image.history()
    history.reverse()

    lines = parse_history(history)
    click.echo("Recovered Dockerfile:")
    click.echo("")
    for line in lines:
        click.echo(line)

if __name__ == "__main__":
    main()
