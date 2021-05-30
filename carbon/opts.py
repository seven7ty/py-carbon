# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2021 wulf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Union
from .utils import *
from .errors import CarbonError


__all__: tuple = ('CarbonOptions',)


class CarbonOptions:
    def __init__(self,
                 code: str,
                 background_color: tuple = (171, 184, 195, 1),
                 drop_shadow: bool = True,
                 shadow_blur_radius_px: int = 68,
                 shadow_offset_y_px: int = 20,
                 export_size: int = 2,
                 font_size_px: int = 14,
                 font_family: str = 'hack',
                 first_line_number: int = 1,
                 language: str = 'auto',
                 line_height_percent: Union[int, float] = 1.33,
                 show_line_numbers: bool = False,
                 show_window_controls: bool = True,
                 show_watermark: bool = False,
                 horizontal_padding_px: int = 56,
                 vertical_padding_px: int = 56,
                 adjust_width: bool = True,
                 theme: str = 'seti',
                 window_theme: str = 'none'):
        self.code: str = code
        self.background_color: tuple = background_color
        self.drop_shadow: bool = drop_shadow
        self.shadow_blur_radius_px: int = shadow_blur_radius_px
        self.shadow_offset_y_px: int = shadow_offset_y_px
        self.export_size: int = export_size
        self.font_size_px: int = font_size_px
        self.font_family: str = font_family
        self.first_line_number: int = first_line_number
        self.language: str = language
        self.line_height_percent: Union[int, float] = line_height_percent
        self.show_line_numbers: bool = show_line_numbers
        self.show_window_controls: bool = show_window_controls
        self.show_watermark: bool = show_watermark
        self.horizontal_padding_px: int = horizontal_padding_px
        self.vertical_padding_px: int = vertical_padding_px
        self.adjust_width: bool = adjust_width
        self.theme: str = theme
        self.window_theme: str = window_theme
        if len(self.background_color) != 4:
            if len(self.background_color) == 3:
                self.background_color = (*self.background_color, 1)
            else:
                raise CarbonError(
                    f'background_color expects an RGB(A) tuple with a length of 3 or 4, not {len(self.background_color)}')

    def request_format(self) -> dict:
        return {
            'code': self.code,
            'backgroundColor': rgba(*self.background_color),
            'dropShadow': self.drop_shadow,
            'dropShadowBlurRadius': px(self.shadow_blur_radius_px),
            'dropShadowOffsetY': px(self.shadow_offset_y_px),
            'exportSize': size(self.export_size),
            'fontSize': px(self.font_size_px),
            'fontFamily': str(self.font_family),
            'firstLineNumber': self.first_line_number,
            'language': str(self.language),
            'lineHeight': percent(self.line_height_percent),
            'lineNumbers': self.show_line_numbers,
            'paddingHorizontal': px(self.horizontal_padding_px),
            'paddingVertical': px(self.vertical_padding_px),
            'theme': str(self.theme),
            'windowTheme': str(self.window_theme),
            'watermark': self.show_watermark,
            'widthAdjustment': self.adjust_width,
            'windowControls': self.show_window_controls
        }
