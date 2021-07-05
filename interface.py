import pyfiglet
import click
import elpyza_scripts


@click.command()
@click.argument("script", default="doctor")
def run_elpyza(script):
    banner = pyfiglet.figlet_format(
        "------------\n EL-py-ZA \n------------", font="starwars", width=100
    )
    click.echo(banner)

    introduction = """havn't written introduction yet"""
    click.echo(introduction)

    click.echo("You have selected the [" + script + "] script")

    selected_script = elpyza_scripts.load_script(script)

    while selected_script.active:
        click.prompt(selected_script.user_promp)

@click.command()
def list_scripts():
    for script in 

if __name__ == "__main__":
    run_elpyza()
