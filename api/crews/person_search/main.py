import argparse
import os
import time

from dotenv import load_dotenv

load_dotenv()

from crewai import Crew
from tasks import PeopleTasks
from agents import PeopleAgents
from crewai_tools.tools import SerperDevTool, ScrapeWebsiteTool

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
    "--linkedin_profile",
    required=False,
    help="LinkedIn Profile.")
parser.add_argument(
    "--twitter_profile",
    required=False,
    help="Twitter Profile.")
parser.add_argument(
    "--facebook_profile",
    required=False,
    help="Facebook Profile.")

args = parser.parse_args()

# Use arguments
person_name = args.person_name
websites = args.websites
misc_information = args.misc_information
linkedin_profile = args.linkedin_profile
twitter_profile = args.twitter_profile
facebook_profile = args.facebook_profile

# Initialise agents and tasks
tasks = PeopleTasks()
agents = PeopleAgents()

# List of Agents and Tasks
all_agents = []
all_tasks = []

if linkedin_profile:
    linkedin_agent = agents.some_agent()
    all_agents.append(linkedin_agent)
    all_tasks.append(tasks.research_social_media_task(linkedin_agent, linkedin_profile))

if twitter_profile:
    twitter_agent = agents.some_agent()
    all_agents.append(twitter_agent)
    all_tasks.append(tasks.research_social_media_task(twitter_agent, twitter_profile))

if facebook_profile:
    facebook_agent = agents.some_agent()
    all_agents.append(facebook_agent)
    all_tasks.append(tasks.research_social_media_task(facebook_agent, facebook_profile))

if websites:
    for website in websites.split(','):
        website = website.strip()
        scraper_agent = agents.research_agent([ScrapeWebsiteTool(website_url=website)])
        all_agents.append(scraper_agent)
        all_tasks.append(tasks.research_person_task(scraper_agent, person_name, website, misc_information))

# Serper (google search api response)
serper_agent = agents.research_agent([SerperDevTool()])
all_agents.append(serper_agent)
serper_task = tasks.serper_task(serper_agent, person_name, misc_information, all_tasks)
all_tasks.append(serper_task)

# Writer
writer_agent = agents.writer_agent()
all_agents.append(writer_agent)
write_report_task = tasks.person_summary_task(writer_agent, person_name, all_tasks)
all_tasks.append(write_report_task)

log_path = os.path.join(os.path.dirname(__file__), '..', '..', 'io', 'output', f"{int(time.time())}_log.txt")

# Instantiate the crew with a sequential process
crew = Crew(agents=all_agents, tasks=all_tasks, verbose=True, output_log_file=log_path)

# Kick off the process
result = crew.kickoff()
