import carbon
import asyncio

loop = asyncio.get_event_loop()  # Setting up asyncio

code = """
defmodule Something do
    def anything() do
        IO.puts "Hello, World"
    end
end
"""  # Any kind of code-block in any language

options = carbon.CarbonOptions(code)

cb = carbon.Carbon()
image = loop.run_until_complete(cb.generate(options))  # Returns a CarbonImage object
loop.run_until_complete(image.save('something-script'))
