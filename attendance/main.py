import click
from attendance.commands.register import register_face
from attendance.commands.scan import scan_faces
from attendance.commands.export import export_attendance

@click.group()
def cli():
    pass

cli.add_command(register_face)
cli.add_command(scan_faces)
cli.add_command(export_attendance)

if __name__ == "__main__":
    cli()
