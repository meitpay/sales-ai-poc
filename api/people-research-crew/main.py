import argparse
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew
from tasks import PeopleTasks
from agents import PeopleAgents

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate a job posting based on company information.")
parser.add_argument("--company_description", required=True, help="Description of the company.")
parser.add_argument("--company_domain", required=True, help="Domain of the company.")
parser.add_argument("--hiring_needs", required=True, help="Hiring needs of the company.")
parser.add_argument("--specific_benefits", required=True, help="Specific benefits offered by the company.")
args = parser.parse_args()

# Use arguments
company_description = args.company_description
company_domain = args.company_domain
hiring_needs = args.hiring_needs
specific_benefits = args.specific_benefits

# Rest of your script remains the same
tasks = PeopleTasks()
agents = PeopleAgents()

# Create Agents
researcher_agent = agents.research_agent()

writer_agent = agents.writer_agent()
review_agent = agents.review_agent()

# Define Tasks for each agent
research_company_culture_task = tasks.research_company_culture_task(researcher_agent, company_description,
                                                                    company_domain)
industry_analysis_task = tasks.industry_analysis_task(researcher_agent, company_domain, company_description)
research_role_requirements_task = tasks.research_role_requirements_task(researcher_agent, hiring_needs)
draft_job_posting_task = tasks.draft_job_posting_task(writer_agent, company_description, hiring_needs,
                                                      specific_benefits)
review_and_edit_job_posting_task = tasks.review_and_edit_job_posting_task(review_agent, hiring_needs)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[researcher_agent, writer_agent, review_agent],
    tasks=[
        research_company_culture_task,
        industry_analysis_task,
        research_role_requirements_task,
        draft_job_posting_task,
        review_and_edit_job_posting_task
    ]
)

# Kick off the process
result = crew.kickoff()

print("Job Posting Creation Process Completed.")
print("Final Job Posting:")
print(result)
