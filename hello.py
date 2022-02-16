import click


@click.command()
@click.option('--time_of_day', default=1, help='1: Morning, 2: Afternoon, 3: Evening')
@click.argument('fname')
@click.argument('lname')
def hello(fname, lname, time_of_day):
    """Greet the user according to time of the day.
    \n
    Usage:\n
    python hello.py  [name] [--time_of_day]
    """
    if time_of_day == 2:
        time = "Good Afternoon"
    elif time_of_day == 3:
        time = "Good Evening"
    else:
        time = "Good Morning"
    click.echo(f' {time} {fname.capwords()} {lname} ')


if __name__ == '__main__':
    hello()
