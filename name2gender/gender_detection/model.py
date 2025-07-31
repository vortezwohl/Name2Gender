from deeplotx import LogisticRegression
from deeplotx.nn import BaseNeuralNetwork

from name2gender import __CACHE_DIR__


def load_model(model_name: str = 'name2gender-small') -> BaseNeuralNetwork:
    n2g_model = None
    match model_name:
        case 'name2gender-base' | 'n2g-base' | 'base':
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=12, num_layers=4,
                                           head_layers=1, expansion_factor=2,
                                           model_name='name2gender-base')
        case 'name2gender-small' | 'n2g-base' | 'small':
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=6, num_layers=2,
                                           head_layers=1, expansion_factor=1.5,
                                           model_name='name2gender-small')
        case _:
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=6, num_layers=2,
                                           head_layers=1, expansion_factor=1.5,
                                           model_name='name2gender-small')
    return n2g_model.load(model_dir=__CACHE_DIR__)
