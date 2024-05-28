from flask import Flask

app = Flask(__name__)

cache_loaded = False


@app.route('/')
def Hello_st():
  return "<h1>My_simple_memoize_app</h1>"


@app.route('/about')
def author():
  return "<h2>Maks Stecuk 1.2</h1> \n <p>@MaksTulenchik</p>"


@app.route("/calc/<string:func>/<int:number>")
def calculate(func, number):
  global cache_loaded
  if not cache_loaded:
    _load_from_cache()
  from utils import factorial1, factorial2
  res = ''
  if func == 'f1':
    res = str(factorial1(number))
    return f'factorial of {number} = {res}'
  if func == 'f2':
    res = str(factorial2(number))
    return f'factorial of {number} = {res}'
  return 'No this type of func!'


@app.route('/load_from_cache')
def _load_from_cache():
  from utils import factorial1, factorial2, load_from_cache
  global cache_loaded
  cache_loaded = True
  cache = load_from_cache('cache.json')
  factorial1.cache = cache
  factorial2.cache = cache
  return f'Loaded cache: {cache}'


@app.route('/save_to_cache')
def save_to_cache():
  global cache_loaded
  if not cache_loaded:
    _load_from_cache()
  from utils import factorial1, factorial2, save_to_cache
  cache = factorial1.cache | factorial2.cache
  save_to_cache('cache.json', cache)
  return f'Saved cache: {cache}'


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
