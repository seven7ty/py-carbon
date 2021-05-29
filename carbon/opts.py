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

import enum
from typing import Union
from .utils import *
from .carbon import CarbonError


__all__: tuple = (
    'FontFamily',
    'Theme',
    'CarbonOptions'
)


@enum.unique
class FontFamily(enum.Enum):
    DANK_MONO: str = 'Dank Mono'
    ANONYMOUS_PRO: str = 'Anonymous Pro'
    DROID_SANS_MONO: str = 'Droid Sans Mono'
    FANTASQUE_SANS_MONO: str = 'Fantasque Sans Mono'
    FIRA_CODE: str = 'Fira Code',
    HACK: str = 'Hack'
    IBM_PLEX_MONO: str = 'IBM Plex Mono'
    INCONSOLATA: str = 'Inconsolata'
    IOSEVKA: str = 'Iosevka'
    JETBRAINS_MONO: str = 'Jetbrains Mono'
    MONOID: str = 'Monoid'
    SOURCE_CODE_PRO: str = 'Source Code Pro'
    SPACE_MONO: str = 'Space Mono'
    UBUNTU_MONO: str = 'Ubuntu Mono'


@enum.unique
class Theme(enum.Enum):
    NIGHT_3024: str = '3024 Night'
    A11Y_DARK: str = 'A11y Dark'
    BLACKBOARD: str = 'Blackboard'
    BASE16_DARK: str = 'Base 16 (Dark)'
    BASE16_LIGHT: str = 'Base 16 (Light)'
    COBALT: str = 'Cobalt'
    DUOTONE: str = 'Duotone'
    HOPSCOTCH: str = 'Hopscotch'
    LUCARIO: str = 'Lucario'
    MATERIAL: str = 'Material'
    MONOKAI: str = 'Monokai'
    NIGHT_OWL: str = 'Night Owl'
    NORD: str = 'Nord'
    OCEANIC_NEXT: str = 'Oceanic Next'
    ONE_LIGHT: str = 'One Light'
    ONE_DARK: str = 'One Dark'
    PANDA: str = 'Panda'
    PARAISO: str = 'Paraiso'
    SETI: str = 'Seti'
    SHADES_OF_PURPLE: str = 'Shades of Purple'
    SOLARIZED_DARK: str = 'Solarized (Dark)'
    SOLARIZED_LIGHT: str = 'Solarized (Light)'
    SYNTHWAVE84: str = 'SynthWave\'84'
    TWILIGHT: str = 'Twilight'
    VERMINAL: str = 'Verminal'
    VSCODE: str = 'VSCode'
    YETI: str = 'Yeti'
    ZENBURN: str = 'Zenburn'


@enum.unique
class Language(enum.Enum):
    AUTO: str = 'auto'
    APACHE: str = 'Apache'
    BASH: str = 'Bash'
    PLAINTEXT: str = 'Plain Text'
    C: str = 'C'
    CPP: str = 'C++'
    CSHARP: str = 'C#'
    CLOJURE: str = 'Clojure'
    COBOL: str = 'COBOL'
    COFFEESCRIPT: str = 'CoffeeScript'
    CRYSTAL: str = 'Crystal'
    CSS: str = 'CSS'
    D: str = 'D'
    DART: str = 'Dart'
    DIFF: str = 'Diff'
    DJANGO: str = 'Django'
    DOCKER: str = 'Docker'
    ELIXIR: str = 'Elixir'
    ELM: str = 'Elm'
    ERLANG: str = 'Erlang'
    FORTRAN: str = 'Fortran'
    GHERKIN: str = 'Gherkin'
    GRAPHQL: str = 'GraphQL'
    GO: str = 'Go'
    GROOVY: str = 'Groovy'
    HANDLEBARS: str = 'Handlebars'
    HASKELL: str = 'Haskell'
    HTML_XML: str = 'HTML/XML'
    JAVA: str = 'Java'
    JAVASCRIPT: str = 'JavaScript'
    JSON: str = 'JSON'
    JSX: str = 'JSX'
    JULIA: str = 'Julia'
    KOTLIN: str = 'Kotlin'
    LATEX: str = 'LaTeX'
    LISP: str = 'Lisp'
    LUA: str = 'Lua'
    MARKDOWN: str = 'Markdown'
    MATHEMATICA: str = 'Mathematica'
    MATLAB_OCTAVE: str = 'MATLAB/Octave'
    MYSQL: str = 'MySQL'
    N_TRIPLES: str = 'N-Triples'
    NIM: str = 'Nim'
    OBJECTIVE_C: str = 'Objective C'
    OCAML_FSHARP: str = 'OCaml/F#'
    PASCAL: str = 'Pascal'
    PERL: str = 'Perl'
    PHP: str = 'PHP'
    POWERSHELL: str = 'PowerShell'
    PYTHON: str = 'Python'
    R: str = 'R'
    RISC_V: str = 'RISC-V'
    RUBY: str = 'Ruby'
    RUST: str = 'Rust'
    SASS: str = 'Sass'
    SCALA: str = 'Scala'
    SMALLTALK: str = 'Smalltalk'
    SOLIDITY: str = 'Solidity'
    SPARQL: str = 'SPARQL'
    SQL: str = 'SQL'
    STYLUS: str = 'Stylus'
    SWIFT: str = 'Swift'
    TCL: str = 'TCL'
    TOML: str = 'TOML'
    TURTLE: str = 'Turtle'
    TYPESCRIPT: str = 'TypeScript'
    TSX: str = 'TSX'
    TWIG: str = 'Twig'
    VB_NET: str = 'VB.NET'
    VERILOG: str = 'Verilog'
    VHDL: str = 'VHDL'
    VUE: str = 'Vue'
    XQUERY: str = 'XQuery'
    YAML: str = 'YAML'


class CarbonOptions:
    def __init__(self,
                 code: str,
                 background_color: tuple = (171, 184, 195, 1),
                 drop_shadow: bool = True,
                 shadow_blur_radius_px: int = 68,
                 shadow_offset_y_px: int = 20,
                 export_size: int = 2,
                 font_size_px: int = 14,
                 font_family: FontFamily = FontFamily.HACK,
                 first_line_number: int = 1,
                 language: Language = Language.AUTO,
                 line_height_percent: Union[int, float] = 1.33,
                 show_line_numbers: bool = False,
                 show_window_controls: bool = True,
                 show_watermark: bool = False,
                 horizontal_padding_px: int = 56,
                 vertical_padding_px: int = 56,
                 adjust_width: bool = True,
                 theme: Theme = Theme.SETI,
                 window_theme: str = 'none'):
        self.code: str = code
        self.background_color: tuple = background_color
        self.drop_shadow: bool = drop_shadow
        self.shadow_blur_radius_px: int = shadow_blur_radius_px
        self.shadow_offset_y_px: int = shadow_offset_y_px
        self.export_size: int = export_size
        self.font_size_px: int = font_size_px
        self.font_family: FontFamily = font_family
        self.first_line_number: int = first_line_number
        self.language: Language = language
        self.line_height_percent: Union[int, float] = line_height_percent
        self.show_line_numbers: bool = show_line_numbers
        self.show_window_controls: bool = show_window_controls
        self.show_watermark: bool = show_watermark
        self.horizontal_padding_px: int = horizontal_padding_px
        self.vertical_padding_px: int = vertical_padding_px
        self.adjust_width: bool = adjust_width
        self.theme: Theme = theme
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
            'language': self.language,
            'lineHeight': percent(self.line_height_percent),
            'lineNumbers': self.show_line_numbers,
            'paddingHorizontal': px(self.horizontal_padding_px),
            'paddingVertical': px(self.vertical_padding_px),
            'theme': self.theme,
            'windowTheme': self.window_theme,
            'watermark': self.show_watermark,
            'widthAdjustment': self.adjust_width,
            'windowControls': self.show_window_controls
        }
