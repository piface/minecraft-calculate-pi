import pifacedigitalio
import monte_carlo
import block_drawer


DEBUG = True

START_BUTTON_INDEX = 0
RESET_BUTTON_INDEX = 1
CLEAR_BUTTON_INDEX = 2


def start(event):
    if DEBUG:
        print('DEBUG:FAKE:Starting Monte Carlo')
    else:
        monte_carlo.start_monte_carlo()
        on_finish()


def reset(event):
    if DEBUG:
        print('DEBUG:FAKE:Resetting Block Drawer')
    else:
        # Turns off the finale relay and restores the minecraft world
        pifacedigital.relays[0].turn_off()
        block_drawer.restore_checkpoint()


def clear(event):
    if DEBUG:
        print('DEBUG:FAKE:Clearing Block Drawer')
    else:
        block_drawer.clear()


def on_finish():
    if DEBUG:
      print('Finished')
    else:
      # Runs after pi has been calculated
      pifacedigital.relays[0].turn_on()



if __name__ == '__main__':
    pifacedigital = pifacedigitalio.PiFaceDigital()
    listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
    listener.register(START_BUTTON_INDEX,
                      pifacedigitalio.IODIR_FALLING_EDGE,
                      start)
    listener.register(RESET_BUTTON_INDEX,
                      pifacedigitalio.IODIR_FALLING_EDGE,
                      reset)
    listener.register(CLEAR_BUTTON_INDEX,
                      pifacedigitalio.IODIR_FALLING_EDGE,
                      clear)
    listener.activate()
