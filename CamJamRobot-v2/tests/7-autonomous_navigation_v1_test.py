from unittest.mock import MagicMock, call
import threading
from gpiozero import LED
from ..src.7-autonomous_navigation_v1 import right_led_blink, is_near_obstacle, move_backwards, turn_right
import ..src.7-autonomous_navigation_v1

def test_right_led_blink(monkeypatch):
    # Mock LEDs
    led1 = MagicMock(spec=LED)
    led2 = MagicMock(spec=LED)
    led3 = MagicMock(spec=LED)
    led4 = MagicMock(spec=LED)

    # Mock 





def test 
    