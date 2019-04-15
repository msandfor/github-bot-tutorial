import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
   async with aiohttp.ClientSession() as session:
       gh = GitHubAPI(session, "msandfor", oauth_token=os.getenv("GH_AUTH"))
       await gh.post('/repos/msandfor/snickers/issues',
             data={
                 'title': "Not sure if this is working",
                 'body': "Might have to restart the whole tutorial",
             })

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
