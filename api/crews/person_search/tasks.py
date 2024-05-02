from textwrap import dedent
from crewai import Task, Agent
import time


class PeopleTasks:

    @staticmethod
    def research_person_task(research_agent: Agent, person_name: str, website: str, misc_information: str):
        return Task(
            description=dedent(f"""\
            Analyze the specified website {website} for comprehensive information on {person_name}. 
            Explore various domains within the site to extract detailed insights on personal background, 
            professional achievements, public appearances, and other notable aspects. 

            {f'Additional guidance for your research: {misc_information}' if misc_information else ''}
            
            Ensure each piece of information is well-sourced. 
            """),
            expected_output=dedent(f"""\
            A Detailed analysis and report on  {person_name}.

            Each piece of information must include a direct link to the source and be formatted in markdown.
            """),
            agent=research_agent,
            output_file=f"./io/output/{int(time.time())}_{person_name.replace(' ', '_')}_{website.replace('https://', '').replace('www', '').replace('/', '_')}_profile.md"
        )

    @staticmethod
    def research_social_media_task(some_agent: Agent, some_profile: str):
        return Task(
            description=dedent(f"""\
            Read the social media profile {some_profile}. Remove empty or non values.
            """),
            expected_output=dedent(f"""\
            Return the information from the social media profile, formatted in json.
            """),
            agent=some_agent,
            output_file=f"./io/output/{int(time.time())}_{some_profile.replace('https://', '').replace('www', '').replace('/', '_')}.json"
        )

    @staticmethod
    def serper_task(web_search_agent: Agent, person_name: str, misc_information: str, context: list[Task]):
        return Task(
            description=dedent(f"""\
            Search the web for {person_name}. 
            Explore various domains within the site to extract detailed insights on personal background, 
            professional achievements, public appearances, and other notable aspects. 

            {f'Additional guidance for your research: {misc_information}' if misc_information else ''}
            
            Ensure each piece of information is well-sourced. 
            """),
            expected_output=dedent(f"""\
            A Detailed analysis and report on  {person_name}.
            
            Each piece of information must include a direct link to the source and be formatted in markdown.
            """),
            agent=web_search_agent,
            context=context,
            output_file=f"./io/output/{int(time.time())}_{person_name.replace(' ', '_')}_serper_search.md"
        )

    @staticmethod
    def person_summary_task(writer_agent: Agent, person_name: str, context: list[Task]):
        return Task(
            description=dedent(f"""\
            Compile and synthesize information from previous research to create a detailed, cohesive profile for {person_name}. 
            
            The profile should cover key areas such as personal background, professional achievements, and online activities. 
            Highlight significant events, notable accomplishments, and unique attributes gleaned from the research.
            
            Ensure the profile integrates insights from various research tasks to provide a complete picture of the individual.
            """),
            expected_output=dedent(f"""\
            Create a comprehensive and well-organized profile of {person_name}, drawing from earlier research and social media analyses. 

            Ensure each piece of information is well-sourced and format the summary in markdown to ensure traceability and credibility of the information. 
            """),
            agent=writer_agent,
            context=context,
            output_file=f"./io/output/{int(time.time())}_{person_name.replace(' ', '_')}_summary.md"
        )
