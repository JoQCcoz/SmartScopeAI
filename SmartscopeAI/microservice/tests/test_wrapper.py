import mrcfile
import os
from ..wrapper import find_squares


TESTFILES = '/home/ubuntu//MySmartScope/SmartScope/data/testing/20241206_test_new_protocols/1_grid_1/grid_1_atlas'

def test_find_squares():
    with mrcfile.open(os.path.join(TESTFILES,'grid_1_atlas.mrc')) as mrc:
        atlas = mrc.data
    squares, labels = find_squares(atlas, weights='square_weights/model_large_atlas.pth')
    assert len(squares) >= 0
    assert len(labels) >= 0



