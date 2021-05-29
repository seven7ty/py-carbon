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

import io
import os.path
import aiohttp
import aiofiles
from .utils import sanitize_filename
from .opts import CarbonOptions
from typing import Optional, AnyStr

__all__: tuple = (
    'CarbonError',
    'Carbon',
    'CarbonImage'
)


class CarbonImage:
    def __init__(self, _bytes: bytes):
        self.bytes: bytes = _bytes

    async def save(self, filename: str) -> AnyStr:
        async with aiofiles.open(sanitize_filename(filename), 'wb') as fp:
            await fp.write(self.bytes)
        return os.path.realpath(filename)

    async def memorize(self, filename: Optional[str] = None) -> io.BytesIO:
        io_obj: io.BytesIO = io.BytesIO(self.bytes)
        if filename:
            setattr(io_obj, 'name', sanitize_filename(filename))
        return io_obj

    def __bytes__(self) -> bytes:
        return self.bytes


class CarbonError(Exception):
    pass


class Carbon:
    __url__: str = 'https://carbonara.vercel.app/api/cook'

    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        self._ses: aiohttp.ClientSession = session or aiohttp.ClientSession()

    async def gen_carbon_snippet(self, options: CarbonOptions) -> CarbonImage:
        res: aiohttp.ClientResponse = await self._ses.post(self.__url__, json=options.request_format())
        payload: bytes = await res.read()
        if res.status == 200:
            return CarbonImage(payload)
        raise CarbonError(f'Carbonara API Status Code: {res.status}')
