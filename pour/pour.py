import shutil
import click


@click.command()
@click.option('-n', default='app', help='Desired name of app.')
@click.option('-t', is_flag=True, help='Generate test skeleton.')
def generate(n, t):
    shutil.copy(n + '.py', '.')
    if t:
        shutil.copy('test.py', '.')


if __name__ == '__main__':
    generate()
