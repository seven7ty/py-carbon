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

__all__: tuple = (
    'rgba',
    'percent',
    'px',
    'size',
    'sanitize_filename'
)


def rgba(r: int, g: int, b: int, a: float) -> str:
    return f'rgba({r}, {g}, {b}, {a})'


def percent(num: Union[int, float]) -> str:
    if isinstance(num, float):
        num: int = int(num * 100)
    return f'{num}%'


def px(num: int) -> str:
    return f'{num}px'


def size(num: int) -> str:
    return f'{num}x'


def sanitize_filename(filename: str) -> str:
    if not filename.endswith('.png'):
        if '.' in filename:
            return filename[:filename.rindex('.', 1)] + '.png'
        return filename + '.png'
