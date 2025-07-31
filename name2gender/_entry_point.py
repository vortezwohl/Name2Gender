import click

from name2gender import Name2Gender, load_model


@click.command()
@click.argument('name', required=False)
@click.option('--threshold', '-t', default=.5, type=float, help='threshold for prediction')
@click.option('--model', '-m', default='small', type=str, help='name2gender model')
def main(name: str, threshold: float, model: str):
    n2g = Name2Gender(load_model(model_name=model))
    if not name:
        click.echo('Please provide at least one name.', err=True)
    gender, prob = n2g(name=name, return_probability=True, threshold=threshold)
    click.echo(f'"{name}" is {gender.value} with an probability of {prob * 100:.2f}%.')
