__all__ = ['read_params']

PARAMS = {
  'precision': '0',
}

def read_params():
  import configparser
  global PARAMS
  config = configparser.ConfigParser()
  config.read('Tulenchik_package/params.ini')
  PARAMS['precision'] = config['settings']['precision']
  return PARAMS
