from textwrap import dedent
from crewai import Task
import time


class PeopleTasks:

    @staticmethod
    def research_person_task(agent, person_name, website, misc_information):
        return Task(
            description=dedent(f"""\
                Analyze the provided website {website} and see what information you can find about {person_name}.
                Focus on information about {person_name}. Review the content of each domain thoroughly to gather comprehensive and relevant details. 
                Your analysis should cover personal background, professional achievements, public appearances, and any other notable information available on these sites. 
                {'Additional information to assist your research: ' + misc_information if misc_information else ''}
                """),
            expected_output=dedent(f"""\
                A detailed report containing all relevant information about {person_name} found on the specified websites {website}. 
                The report should be well-organized, segregating information based on personal background, professional life, and other notable aspects. 
                It should also indicate the sources for each piece of information.
                """),
            agent=agent
        )

    @staticmethod
    def research_social_media_task(agent, person_name, social_media_profiles):
        return Task(
            description=dedent(f"""\
                Investigate the following social media profile {social_media_profiles} of {person_name}. 
                Examine posts, interactions, and networks to gather insights into their personal and professional life. 
                Pay special attention to recent activities, posts, public interactions, 
                and any notable changes in their online behavior. 
                Look for patterns or themes in their social media presence that might offer deeper understanding of their interests, 
                opinions, and connections.
                """),
            expected_output=dedent(f"""\
                A comprehensive report on {person_name}'s social media presence, covering the profile {social_media_profiles}. 
                The report should include summaries of recent activities, posts, and notable interactions. 
                It should also analyze their network and any patterns or themes observed in their online behavior. 
                Include direct links to significant posts or interactions, 
                and ensure the information is current and accurately represents the individual's social media activities.
                It should also indicate the sources for each piece of information.
                """),
            agent=agent
        )

    @staticmethod
    def search_web_task(agent, person_name, context):
        return Task(
            description=dedent(f"""\
                Search the web for {person_name}.
                 Use the context provided to ensure the information gathered is about the correct person.
            """),
            expected_output=dedent(f"""\
                A detailed report containing accurate information about {person_name} well-organized and with clear sources for each piece of information.
            """),
            agent=agent,
            context=context
        )

    @staticmethod
    def person_summary_task(agent, person_name, context):
        return Task(
            description=dedent(f"""\
                Create a detailed profile for {person_name} to build a comprehensive and cohesive profile. 
                Ensure the profile captures key aspects of the person's life, including personal background, 
                professional achievements, and online presence. Highlight significant events, accomplishments, 
                and any unique attributes or insights gained from the research.
                """),
            expected_output=dedent(f"""\
                A well-structured, comprehensive profile of {person_name} that synthesizes information from research and social media findings. 
                The profile should be clear, engaging, and informative, providing a holistic view of the person. 
                It should include sections on personal background, career achievements, social media presence, 
                and any other relevant aspects, ensuring a balanced representation of both their personal and professional life. 
                The profile should also contain references to the sources of information used. Formatted in markdown.
                """),
            agent=agent,
            context=context,
            output_file=f"./io/output/{int(time.time())}_{person_name.replace(' ', '_')}_summary.md"
        )
