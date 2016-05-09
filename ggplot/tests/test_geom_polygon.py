from __future__ import absolute_import, division, print_function

import pandas as pd

from .. import ggplot, aes, geom_polygon
from .tools import assert_ggplot_equal, cleanup

df = pd.DataFrame({
        'x': ([1, 2, 3, 2] +
              [5, 6, 7] +
              [9, 9, 10, 11, 11, 10]),
        'y': ([2, 3, 2, 1] +
              [1, 3, 1] +
              [1.5, 2.5, 3, 2.5, 1.5, 1]),
        'z': ([1]*4 + [2]*3 + [3]*6)
    })


@cleanup
def test_aesthetics():
    p = (ggplot(df, aes('x', group='factor(z)')) +
         geom_polygon(aes(y='y')) +
         geom_polygon(aes(y='y+3', alpha='z')) +
         geom_polygon(aes(y='y+6', linetype='factor(z)'),
                      color='brown', fill=None, size=2) +
         geom_polygon(aes(y='y+9', color='z'),
                      fill=None, size=2) +
         geom_polygon(aes(y='y+12', fill='factor(z)')) +
         geom_polygon(aes(y='y+15', size='z'),
                      color='yellow', show_legend=False))

    assert_ggplot_equal(p, 'aesthetics')
