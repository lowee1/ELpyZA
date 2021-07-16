import time
import random
import pyfiglet
import click
import elpyza_scripts


@click.group()
def main():
    pass


@main.command(name="run")
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

    click.echo(selected_script.initial)
    while selected_script.active:
        user_input = click.prompt(selected_script.user_prompt)
        response = selected_script.get_script_response(user_input)
        click.echo(selected_script.script_prefix + response)
        time.sleep(random.randint(0, 4))


@main.command(name="list")
def list_scripts():
    click.echo("\n".join(elpyza_scripts.list_scripts()))


if __name__ == "__main__":
    main()
