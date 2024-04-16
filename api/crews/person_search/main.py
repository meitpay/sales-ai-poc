import argparse
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew
from tasks import PeopleTasks
from agents import PeopleAgents
from crewai_tools.tools import SerperDevTool, WebsiteSearchTool

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate a person profile based research.")
parser.add_argument(
    "--person_name",
    required=True,
    help="The name of the person.")
parser.add_argument(
    "--websites",
    required=False,
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

website_agents = {}
some_agents = {}

# Create Agents
search_agent = agents.research_agent([SerperDevTool()])
writer_agent = agents.writer_agent()

# Define Tasks for each agent

all_agents = []
all_tasks = []

if social_media_profiles:
    for index, profile in enumerate(social_media_profiles.split(',')):
        profile = profile.strip()
        some_agents[f'social_media_agent_{index}'] = agents.social_media_agent([WebsiteSearchTool(profile)])
        current_agent = some_agents[f'social_media_agent_{index}']
        all_agents.append(current_agent)
        all_tasks.append(tasks.research_social_media_task(current_agent, person_name, profile))

if websites:
    for index, website in enumerate(websites.split(',')):
        website = website.strip()
        some_agents[f'researcher_agent{index}'] = agents.social_media_agent([WebsiteSearchTool(website)])
        current_agent = some_agents[f'researcher_agent{index}']
        all_agents.append(current_agent)
        all_tasks.append(tasks.research_person_task(current_agent, person_name, website, misc_information))

all_agents.append(search_agent)
all_agents.append(writer_agent)

search_task = tasks.search_web_task(search_agent, person_name, all_tasks)
all_tasks.append(search_task)
write_report_task = tasks.person_summary_task(writer_agent, person_name, all_tasks)
all_tasks.append(write_report_task)

# Instantiate the crew with a sequential process
crew = Crew(agents=all_agents, tasks=all_tasks)

# Kick off the process
result = crew.kickoff()
