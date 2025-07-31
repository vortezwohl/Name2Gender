import os

import requests
import gdown
from deeplotx import LogisticRegression
from deeplotx.nn import BaseNeuralNetwork

from name2gender import __CACHE_DIR__


BASE_MODEL = 'name2gender-base'
SMALL_MODEL = 'name2gender-small'


def download_model(model_name: str, quiet: bool = False):
    os.makedirs(__CACHE_DIR__, exist_ok=True)
    _proxies = {
        'http': os.getenv('HTTP_PROXY', os.getenv('http_proxy')),
        'https': os.getenv('HTTPS_PROXY', os.getenv('https_proxy'))
    }
    model_path = os.path.join(__CACHE_DIR__, model_name)
    if not os.path.exists(model_path):
        url = f'https://github.com/vortezwohl/Name2Gender/releases/download/RESOURCE/{model_name}.dlx'
        if requests.get(url=url, proxies=_proxies).status_code == 200:
            try:
                gdown.download(
                    url=url,
                    output=model_path,
                    quiet=quiet,
                    proxy=_proxies.get('https')
                )
            except Exception as e:
                os.remove(model_path)
                raise e
        else:
            raise ConnectionError(f'Failed to download model {model_name}.')


def load_model(model_name: str = 'name2gender-small') -> BaseNeuralNetwork:
    n2g_model = None
    match model_name:
        case 'name2gender-base' | 'n2g-base' | 'base':
            download_model(BASE_MODEL)
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=12, num_layers=4,
                                           head_layers=1, expansion_factor=2,
                                           model_name=BASE_MODEL)
        case 'name2gender-small' | 'n2g-base' | 'small':
            download_model(SMALL_MODEL)
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=6, num_layers=2,
                                           head_layers=1, expansion_factor=1.5,
                                           model_name=SMALL_MODEL)
        case _:
            download_model(SMALL_MODEL)
            n2g_model = LogisticRegression(input_dim=768, output_dim=1,
                                           num_heads=6, num_layers=2,
                                           head_layers=1, expansion_factor=1.5,
                                           model_name=SMALL_MODEL)
    return n2g_model.load(model_dir=__CACHE_DIR__)
