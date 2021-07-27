"""This module contains main codebase for dockerfile-recover tool."""

import click
import docker
from docker.errors import APIError
from docker.models.images import Image

from dockerfile_recover.docker_api import get_client, get_image
from dockerfile_recover.generator import generate_dockerfile


@click.group()
def cli():
    """This tool reconstructs Dockerfile by reverse engineering a docker image."""


@click.command()
@click.option(
    "--pull",
    is_flag=True,
    default=False,
    help="Pull the image first. Default is to search for image in `docker images` without pulling.",
)
@click.argument("image_name")
def recover(image_name: str, pull: bool) -> None:
    """Recover Dockerfile given an image name, searches `docker images` to find the image,
    or can optionally --pull it first."""

    try:

        docker_client: docker.DockerClient = get_client()

        image: Image = get_image(docker_client, image_name, pull)
        if not isinstance(image, Image):
            return

        lines = generate_dockerfile(image.history())

        click.echo("Recovered Dockerfile:")
        click.echo("")
        for line in lines:
            click.echo(line)

    except APIError as api_error:
        click.echo(f"{APIError.__name__}: {api_error}", err=True)


# use full help text in place of short_help
recover.short_help = recover.__doc__
cli.add_command(recover)
cli()
