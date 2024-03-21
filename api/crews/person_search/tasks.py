from textwrap import dedent
from crewai import Task
import time


class PeopleTasks:
    @staticmethod
    def research_person_task(agent, person_name, misc_information, websites):
        return Task(
            description=dedent(f"""\
                Analyze the provided websites {websites} and see what information you can find about {person_name}.
                Focus on information about {person_name}. Review the content of each domain thoroughly to gather comprehensive and relevant details. 
                Your analysis should cover personal background, professional achievements, public appearances, and any other notable information available on these sites. 
                {'Additional information to assist your research: ' + misc_information if misc_information else ''}
                """),
            expected_output=dedent(f"""\
                A detailed report containing all relevant information about {person_name} found on the specified websites {websites}. 
                The report should be well-organized, segregating information based on personal background, professional life, and other notable aspects. 
                It should also indicate the sources for each piece of information.
                """),
            agent=agent
        )

    @staticmethod
    def research_social_media_task(agent, person_name, social_media_profiles):
        return Task(
            description=dedent(f"""\
                Investigate each of the following social media profiles {social_media_profiles} of {person_name}. 
                Examine posts, interactions, and networks to gather insights into their personal and professional life. 
                Pay special attention to recent activities, posts, public interactions, 
                and any notable changes in their online behavior. 
                Look for patterns or themes in their social media presence that might offer deeper understanding of their interests, 
                opinions, and connections.
                """),
            expected_output=dedent(f"""\
                A comprehensive report on {person_name}'s social media presence, covering the profiles {social_media_profiles}. 
                The report should include summaries of recent activities, posts, and notable interactions. 
                It should also analyze their network and any patterns or themes observed in their online behavior. 
                Include direct links to significant posts or interactions, 
                and ensure the information is current and accurately represents the individual's social media activities.
                It should also indicate the sources for each piece of information.
                """),
            agent=agent
        )

    @staticmethod
    def draft_person_profile_task(agent, person_name):
        return Task(
            description=dedent(f"""\
                Create a detailed profile for {person_name} by integrating the data collected from various sources. 
                Use this information and the insights from the social media profiles to build a comprehensive and cohesive profile. 
                Ensure the profile captures key aspects of the person's life, including personal background, 
                professional achievements, and online presence. Highlight significant events, accomplishments, 
                and any unique attributes or insights gained from the research.
                """),
            expected_output=dedent(f"""\
                A well-structured, comprehensive profile of {person_name} that synthesizes information from research and social media findings. 
                The profile should be clear, engaging, and informative, providing a holistic view of the person. 
                It should include sections on personal background, career achievements, social media presence, 
                and any other relevant aspects, ensuring a balanced representation of both their personal and professional life. 
                The profile should also contain references to the sources of information used.
                """),
            agent=agent
        )

    @staticmethod
    def review_and_edit_profile_task(agent, person_name):
        return Task(
            description=dedent(f"""\
                Review the draft profile of {person_name} for accuracy, clarity, and completeness. 
                Check for any factual errors, inconsistencies, or unclear sections in the text. 
                Ensure that the narrative flows logically and is engaging for the reader. 
                Verify that all the information provided is backed up by sources, 
                and that these sources are properly cited within the profile. 
                Suggest improvements or corrections where necessary, 
                focusing on enhancing the quality and reliability of the profile.
                """),
            expected_output=dedent(f"""\
                A detailed and well-structured report for the profile of {person_name}. 
                The report should include any identified errors or inconsistencies, 
                suggestions for improving clarity and narrative flow, and comments on source citations. 
                Highlight specific sections where changes are recommended, 
                and provide clear instructions or revisions for each suggested improvement. 
                The goal is to ensure that the final profile is accurate, well-written, and thoroughly sourced.
                Formatted in markdown.
                """),
            agent=agent,
            output_file=f"./io/output/{int(time.time())}_{person_name.replace(' ', '_')}_draft.md"
        )
