import argparse
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew
from tasks import PeopleTasks
from agents import PeopleAgents

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate a person profile based research.")
parser.add_argument(
    "--person_name",
    required=True,
    help="The name of the person.")
parser.add_argument(
    "--websites",
    required=True,
    help="Comma seperated list of research domains.")
parser.add_argument(
    "--misc_information",
    required=False,
    help="Comma seperated list of miscellaneous information. e.g. city, age etc.")
parser.add_argument(
    "--social_media_profiles",
    required=False,
    help="Comma seperated list of social media profiles.")

args = parser.parse_args()

# Use arguments
person_name = args.person_name
websites = args.websites
misc_information = args.misc_information
social_media_profiles = args.social_media_profiles

# Rest of your script remains the same
tasks = PeopleTasks()
agents = PeopleAgents()

# Create Agents
researcher_agent = agents.research_agent()
social_media_agent = agents.social_media_agent()
writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Define Tasks for each agent
research_person_task = tasks.research_person_task(researcher_agent, person_name, misc_information, websites)
social_media_task = tasks.research_social_media_task(social_media_agent, person_name, social_media_profiles)
draft_person_profile_task = tasks.draft_person_profile_task(writer_agent, person_name)
review_and_create_profile_task = tasks.review_and_edit_profile_task(review_agent, person_name)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[
        researcher_agent,
        social_media_agent,
        writer_agent,
        review_agent
    ],
    tasks=[
        research_person_task,
        social_media_task,
        draft_person_profile_task,
        review_and_create_profile_task
    ]
)

print('---------- Person Crew Kicking Off ----------')

# Kick off the process
result = crew.kickoff()

print('---------- Person Crew Result ----------')
print(result)
print('---------- Person Crew Complete ----------')
