from . animation import Animation
from . circle import Circle
from . game import BaseGameAnim
from . matrix import BaseMatrixAnim
from . cube import BaseCubeAnim
from . off import Off
from . sequence import Sequence
from . strip import BaseStripAnim
from . receiver import BaseReceiver
from . tests import StripChannelTest, MatrixChannelTest, MatrixCalibrationTest


# DEPRECATED
strip_test = StripChannelTest
matrix_calibration = MatrixCalibrationTest
matrix_test = MatrixChannelTest
from . off import OffAnim
from . animation import BaseAnimation
from . circle import BaseCircleAnim
