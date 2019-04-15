import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
   async with aiohttp.ClientSession() as session:
       gh = GitHubAPI(session, "mariatta", oauth_token=os.getenv("GH_AUTH"))
       await gh.patch('/repos/mariatta/strange-relationship/issues/159',
            data={'state': 'closed'},
            )
        

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
