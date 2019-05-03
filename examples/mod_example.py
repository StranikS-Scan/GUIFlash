# -*- coding: utf-8 -*-

from gambiter import g_guiFlash
from gambiter.flash import COMPONENT_TYPE, COMPONENT_ALIGN
from gambiter.utils import LOG_NOTE

from gui import InputHandler
from gui.shared.utils.key_mapping import getBigworldNameFromKey


g_guiFlash.createComponent('testSprite', COMPONENT_TYPE.PANEL, {'x': -500, 'y': 25, 'drag': True, 'border': True, 'alignX': COMPONENT_ALIGN.RIGHT, 'alignY': COMPONENT_ALIGN.TOP})

g_guiFlash.createComponent('testSprite.testImage', COMPONENT_TYPE.IMAGE, {'image': '../maps/icons/tooltip/resourceTooltip.png', 'width': 250, 'height': 130, 'alpha': 0.7, 'tooltip': 'Tooltip Image'})

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, <br /> sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, <br /> quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. <br /> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. <br /> Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

text = 'World of Tanks'

props = {'text': text,
         'x': 20,
         'y': 100,         
         # 'width': 100,
         # 'height': 50,
         'multiline': True,
         'wordWrap': True,
         'hAlign': COMPONENT_ALIGN.RIGHT,
         'vAlign': COMPONENT_ALIGN.BOTTOM,
         'drag': True,
         # 'limit': False,
         'border': True,
         # 'background': True,
         'tooltip': 'Tooltip Text'}

g_guiFlash.createComponent('testSprite.testText', COMPONENT_TYPE.LABEL, props)


def onhandleKeyEvent(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_F10':
        g_guiFlash.updateComponent('testSprite', {'index': 1})
        LOG_NOTE('guiFlash [UPDATE] testSprite: index - 1')
    if key == 'KEY_F11':
        g_guiFlash.updateComponent('testSprite', {'index': 10})
        LOG_NOTE('guiFlash [UPDATE] testSprite: index - 10')
    if key == 'KEY_F12':
        g_guiFlash.updateComponent('testSprite', {'index': 100})
        LOG_NOTE('guiFlash [UPDATE] testSprite: index - 100')
    return None

InputHandler.g_instance.onKeyDown += onhandleKeyEvent