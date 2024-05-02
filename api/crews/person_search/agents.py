from crewai import Agent
from textwrap import dedent
from crewai_tools.tools import FileReadTool
from tools.some_tool import SocialMediaProfileTool

person_report_tool = FileReadTool(
    file_path='./io/templates/person_report_example.md',
    description='A tool to read the report example file.'
)


class PeopleAgents:
    @staticmethod
    def research_agent(tools):
        return Agent(
            role='Research Analyst',
            goal=dedent("""\
            To gather comprehensive and accurate information about individuals, 
            their professional achievements, academic backgrounds, affiliations, 
            and historical mentions in media and publications.
            """),
            tools=tools,
            backstory=dedent("""\
            Skilled in analyzing individuals, their professional experiences and achievements, 
            identifying their key values, associates and connections from various sources.
            """)
        )

    @staticmethod
    def some_agent():
        return Agent(
            role='Social Media Analyst',
            goal=dedent("""\
            Get accurate information about individuals on social media.
            """),
            tools=[
                SocialMediaProfileTool.search_linkedin,
                SocialMediaProfileTool.search_twitter,
                SocialMediaProfileTool.search_facebook
            ],
            backstory=dedent("""\
            An expert in analyzing individuals on social media.
            """)
        )

    @staticmethod
    def writer_agent():
        return Agent(
            role='Biography Writer',
            goal=dedent("""\
            Craft a detailed, engaging, and accurate narratives about the given person, 
            integrating diverse information into comprehensive biographical summaries, always site your sources.
            """),
            tools=[person_report_tool],
            backstory=dedent("""\
             A seasoned journalist with a passion for biographies and person profiling, 
             known for its depth, clarity, and engaging style.
             Specializes in ensuring that every article she writes is well-informed and nuanced
             """)
        )
