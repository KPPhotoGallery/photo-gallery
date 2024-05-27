import click

from pathlib import Path

root_gallery_dir = Path("./gallery")

@click.command()
@click.option("--dir-name", prompt="Directory name", help="The directory which will be created underneath ./gallery")
@click.option("--title", prompt="Title", help="The title which will sit at the top of the gallery")
def main(dir_name, title):
    click.echo("Creating new gallery")

    new_gallery_dir = (root_gallery_dir / dir_name)
    new_photo_dir = (root_gallery_dir / "photos" / dir_name)
    if new_gallery_dir.exists():
        click.echo(f"Gallery {dir_name} already exists, aborting.")
        return 1
    if new_photo_dir.exists():
        click.echo(f"Photo repo {dir_name} already exists, aborting.")
        return 1
    
    new_gallery_dir.mkdir()
    new_photo_dir.mkdir()

    return

if __name__ == "__main__":
    main()