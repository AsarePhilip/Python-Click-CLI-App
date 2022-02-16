import click


@click.command()
@click.option('--time_of_day', default=1, help='1: Morning, 2: Evening, 3: Evening')
@click.argument('name')
def hello(name, time_of_day):
    if time_of_day == 2:
        time = "Good Afternoon"
    elif time_of_day == 3:
        time = "Good Evening"
    else:
        time = "Good Morning"
    click.echo(f' {time} {name} ')


if __name__ == '__main__':
    hello()
