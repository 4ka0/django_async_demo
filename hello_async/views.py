import asyncio
import random
from time import sleep
from typing import List

import httpx
from django.http import HttpResponse


# Helpers

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


async def smoke(smokables: List[str] = None, flavor: str = "Sweet Baby Ray's") -> List[str]:
    """ Smokes some meats and applies the Sweet Baby Ray's """

    for smokable in smokables:
        print(f"Smoking some {smokable}...")
        print(f"Applying the {flavor}...")
        print(f"{smokable.capitalize()} smoked.")

    return len(smokables)


async def get_smokables():
    print("Getting smokeables...")

    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning smokeable")
        return [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]


async def get_flavor():
    print("Getting flavor...")

    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

        print("Returning flavor")
        return random.choice(
            [
                "Sweet Baby Ray's",
                "Stubb's Original",
                "Famous Dave's",
            ]
        )


def oversmoke() -> None:
    """ If it's not dry, it must be uncooked """
    sleep(5)
    print("Who doesn't love burnt meats?")


async def upper_case(input_text):
    print("Converting to upper case ...")
    return input_text.upper()


async def title_case(input_text):
    print("Converting to title case ...")
    return input_text.title()


# Views

async def index(request):
    return HttpResponse("Hello, async Django!")


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(), get_flavor()])
    total = await asyncio.gather(*[smoke(results[0], results[1])])
    return HttpResponse(f"Smoked {total[0]} meats with {results[1]}!")


async def format_text(request):
    input_text = "this is sample text"
    results = await asyncio.gather(*[upper_case(input_text), title_case(input_text)])
    return HttpResponse(f'Ouput = "{results[0]}" and "{results[1]}"')


async def burn_some_meats(request):
    oversmoke()
    return HttpResponse("Burned some meats.")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
