from crewai import Agent
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool
from textwrap import dedent

web_search_tool = WebsiteSearchTool()
serper_dev_tool = SerperDevTool()


class PeopleAgents:
    def research_agent(self):
        return Agent(
            role='Research Analyst',
            goal=dedent("""\
			To gather comprehensive and accurate information about individuals, 
			their professional achievements, academic backgrounds, affiliations, 
			and historical mentions in media and publications.
			"""),
            tools=[web_search_tool, serper_dev_tool],
            backstory=dedent("""\ 
			Skilled in analyzing individuals, their professional experiences and achievements, 
			identifying their key values, associates and connections   
			from various sources, including websites and brief descriptions.
			"""),
            verbose=True
        )

    def social_media_research_agent(self):
        return Agent(
            role='Social Media Investigator',
            goal=dedent("""\ 
				To analyze social media profiles 
				and online presence to understand a persona\'s interests, 
				social circles, and public persona
				"""),
            tools=[web_search_tool, serper_dev_tool],
            backstory=dedent("""\
				A former investigative journalist, known for his knack for understanding the nuances of online behavior, 
				brings his expertise in social media analysis. 
				He excels in connecting dots across various online platforms to create a comprehensive 
				picture of an individual's digital footprint.
				"""),
            verbose=True
        )

    def writer_agent(self):
        return Agent(
            role='Investigative Writer',
            goal=dedent("""\ 
				Use insights from the Research Analyst and the Social Media Investigator to craft detailed, engaging, and accurate narratives 
				about individuals, integrating diverse information into comprehensive biographical summaries, always site your sources.
				"""),
            tools=[web_search_tool, serper_dev_tool],
            backstory=dedent("""\
				A seasoned journalist with a passion for biographies, made her mark in investigative journalism. 
				Her knack for storytelling led her to specialize in writing detailed profiles, 
				where she weaves together threads of a person's life, work, and influence. 
				She's writing is known for its depth, clarity, and engaging style. 
				She often spends time researching her subjects extensively, 
				ensuring that every article she writes is well-informed and nuanced.
				"""),
            verbose=True
        )

    def review_agent(self):
        return Agent(
            role='Review and Editing Specialist',
            goal=dedent("""\ 
				To meticulously review, fact-check, and refine written content, ensuring its accuracy, fairness, and readability
				"""),
            tools=[web_search_tool, serper_dev_tool],
            backstory=dedent("""\
				A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect.
				"""),
            verbose=True
        )
