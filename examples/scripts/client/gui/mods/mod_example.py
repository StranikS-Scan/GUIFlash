# -*- coding: utf-8 -*-

from gui import InputHandler
from gui.shared.utils.key_mapping import getBigworldNameFromKey
from gui.mods.gambiter import g_guiFlash, utils
from gui.mods.gambiter.flash import COMPONENT_TYPE, COMPONENT_ALIGN
from gui.mods.gambiter.utils import LOG_NOTE

utils.IS_DEBUG = True

#Создаём передвигаемую панель, на которой разместим картинку и текст  
g_guiFlash.createComponent('testSprite', COMPONENT_TYPE.PANEL, \
                           {'x': -500, 'y': 25, 'drag': True, 'border': True, 'alignX': COMPONENT_ALIGN.RIGHT, 'alignY': COMPONENT_ALIGN.TOP})
#Cоздаём картинку на панели, которая будет подложкой
g_guiFlash.createComponent('testSprite.testImage', COMPONENT_TYPE.IMAGE, \
                           {'image': '../maps/icons/tooltip/resourceTooltip.png', 'width': 250, 'height': 130, 'alpha': 0.7, 'tooltip': 'Tooltip Image'})
#Создаём текстовое поле на панели с html-форматированием и тенью
g_guiFlash.createComponent('testSprite.testText', COMPONENT_TYPE.LABEL, \
                           {'text': '<font face="Tahoma" size="20" color="#0000FF">This is the text field in the <b>first line</b> \nand this is the <i>second line</i>.</font>', \
                            'x': 20, 'y': 100, 'isHtml': True, 'multiline': True, 'wordWrap': True, 'tooltip': 'Tooltip Text', \
                            'shadow': {'distance': 0, 'angle': 135, 'color': 0x101010, 'alpha': 0.60, 'blurX': 1, 'blurY': 1, 'strength': 1, 'quality': 1}})

#Меняем динамически параметры отображения
def onFlashChange(event):
    key = getBigworldNameFromKey(event.key)
    if key == 'KEY_NUMPAD0':
        g_guiFlash.updateComponent('testSprite', {'index': 10})
        LOG_NOTE('guiFlash [UPDATE] testSprite: index = 10')
    elif key == 'KEY_NUMPAD1':
        g_guiFlash.updateComponent('testSprite', {'index': 0})
        LOG_NOTE('guiFlash [UPDATE] testSprite: index = 0')
    elif key == 'KEY_NUMPAD2':
        g_guiFlash.updateComponent('testSprite', {'visible': False})
        LOG_NOTE('guiFlash [UPDATE] testSprite: visible = False')
    elif key == 'KEY_NUMPAD3':
        g_guiFlash.updateComponent('testSprite', {'visible': True})
        LOG_NOTE('guiFlash [UPDATE] testSprite: visible = True')

InputHandler.g_instance.onKeyDown += onFlashChange