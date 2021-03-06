import uvloop

from .button_click import ButtonClick
from .sliders import SineWave

# To use uvloop as event loop for panel
uvloop.install()


# Fill out with new models
_models = [
    #  [url, title, model]
    ["buttonclick", "Button Click", ButtonClick],
    ["sinewave", "Sine Wave", SineWave],
]

titles = {m[0]: m[1] for m in _models}
serving = {f"/panel/{m[0]}": m[2] for m in _models}
