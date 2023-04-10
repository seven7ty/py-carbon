import carbon
import asyncio

code = """
defmodule Something do
    def anything() do
        IO.puts "Hello, World"
    end
end
"""  # Any kind of code-block in any language


async def main():
    cb = carbon.Carbon()  # Create a Carbon instance
    opts = carbon.CarbonOptions(code=code)  # Set the options for the image
    image = await cb.generate(opts)  # Generate the image
    await image.save('hello')  # Save the image in png format


asyncio.run(main())
