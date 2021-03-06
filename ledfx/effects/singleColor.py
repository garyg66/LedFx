from ledfx.color import COLORS
from ledfx.effects.temporal import TemporalEffect
import voluptuous as vol
import numpy as np

class SingleColorEffect(TemporalEffect):

    NAME = "Single Color"
    CONFIG_SCHEMA = vol.Schema({
        vol.Optional('color', description='Color of strip', default = "red"): vol.In(list(COLORS.keys())),
    })

    def config_updated(self, config):
        self.color = np.array(COLORS[self._config['color']], dtype=float)

    def effect_loop(self):
        self.pixels = np.tile(self.color, (self.pixel_count, 1))
