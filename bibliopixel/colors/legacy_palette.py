from . import make
from . import palette

def pop_legacy_palette(kwds, *color_defaults):
    """
    Older animations in BPA and other areas use all sorts of different names for
    what we are now representing with palettes.

    This function mutates a kwds dictionary to remove these legacy fields and
    extract a palette from it, which it returns.
 """
    new_palette = kwds.pop('palette', None)
    return palette.Palette(colors = new_palette)
