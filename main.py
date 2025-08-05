from AI_interview import team_Config, interview
import asyncio

async def main():
    job_position = input("Enter the job position you want to prepare for: ")  # User input
    team = await team_Config(job_position)

    async for message in interview(team):
        print('-' * 70)
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
