"""This module contains main codebase for dockerfile-recover tool."""

import click
import docker
from docker.errors import APIError, ImageNotFound
from docker.models.images import Image

from dockerfile_recover.parser import parse_history


@click.command(
    help="Recover Dockerfile given an image name. Will search `docker images` to find the image, or can optionally --pull it first."
)
@click.option(
    "--pull",
    is_flag=True,
    default=False,
    help="Pull the image first. Default is to search for image in `docker images` without pulling.",
)
@click.argument("name")
def main(name: str, pull: bool) -> None:
    """Command line interface entrypoint."""

    docker_client = docker.from_env()

    try:
        if pull:
            click.echo(f"Pulling image {name}")
            docker_client.images.pull(name)

        image: Image = docker_client.images.get(name)
    except ImageNotFound as image_not_found:
        click.echo(f"{ImageNotFound.__name__}: {image_not_found}", err=True)
        if not pull:
            click.echo(f"Did you want to --pull the image?")
        return
    except APIError as api_error:
        click.echo(f"{APIError.__name__}: {api_error}", err=True)
        return

    try:
        history = image.history()
    except APIError as api_error:
        click.echo(f"{APIError.__name__}: {api_error}", err=True)
        return

    history.reverse()

    lines = parse_history(history)
    click.echo("Recovered Dockerfile:")
    click.echo("")
    for line in lines:
        click.echo(line)


if __name__ == "__main__":
    main()
