"""
Program entrpoint
"""

import panel as pn
import holoviews as hv

from panel.theme import Native
hv.extension('bokeh')
hv.extension('floatpanel')
pn.config.design = Native
template = pn.template.FastGridTemplate(title='HOLOPRIME')

# Modularity
## PARAMETERS


## ACTIVITIES


# Layout
## MAIN

## SIDEBAR




# Serve
pn.serve(
    template
)