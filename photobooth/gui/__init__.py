#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .GuiState import *
from .GuiPostprocess import *


# Available gui modules as tuples of (config name, module name, class name)
modules = ( ('qt5', 'PyQt5Gui', 'PyQt5Gui'), )


class Gui:

    def __init__(self):

        pass


    def run(self, camera_conn, worker_queue):

        raise NotImplementedError()

