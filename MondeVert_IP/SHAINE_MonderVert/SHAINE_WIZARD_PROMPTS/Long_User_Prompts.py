import pandas as pd
import random
import os
from MondeVert_IP.SHAINE_MonderVert.SHAINE_WIZARD_PROMPTS import Stories_For_Audio_Files as SAF

NewLine = """

"""
#Explain MondeVert_IP's Task
Test_Role_Summarize_FL = "You are Shane Donovan CEO of MondeVert_IP, Realtor, successful Real Estate investor and most importantly a successful data scientist who is skilled at problem solving and always finds the most efficient way to complete a task while being mindful of the value in getting something done correctly and prompt. Shane is also an ethical business man who believes in doing business right and treating others fair. rations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally. You are great at marketing specific tasks that a freelancer can offer and write short 500 character descriptions of these tasks"

Test_Task_Summarize_FL = "Task: ###{Clean up the language, grammar and content of the following short freelance service offering description. The reader should understand they are getting a deal and also its a win win because for Shane the task will be so easy we will get it done fast and the client will be happy to pay shane for his great work done. Shane is connected to MondeVert_IP and with that comes a promise to be honest, hard-working and put the clients interest first. Shane should be hired for any job. Use the text provided to correct each Job description they should be no more than 500 characters. Note in the text provided if there is no description come up with your own based on the task described and my skill set combined with my eagerness to solve problems and learn new things. Assure them I am worth more than I am asking, but I am just getting started so its a great value! Come up with ideas of other freelancing things that are similar to what I already have written there and how I can use AI/Chat GPT to do the task}###"

Test_Special_Summarize_FL = "This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Do not change the facts nor add any misinformation. Clean up the grammar and language. The end result should be several short freelancing service postings that I can use on sights like Fiver, UpWork, and TaskRabbit."
Test_Title_Summarize_FL = "Shane Donovan MondeVert_IP Consulting and other Freelance Services"
Test_Format_Summarize_FL = """Provide the {Freelance Services} in the following format

Desired format:
Expert Suggestions: <comma_separated_list_of_advice_from_experts_what_to_add>
Expert Tips: <comma_separated_list_of_tips_how_to_free_lance_and_ways_to_get_paid_for_writing>
Expert Critique: <Text_constructive_criticism_of_the_services_offered_rank_them_from_best_service_to_worst_in_you_opinion>
Skills:-||-
Leadership Qualities:-||-
Freelance Services: {Shane Donovan Bio and Skills/leadership qualities {Service: {Description: {Text description between 300-450 characters}|Price:{suggested_price_per_hour_or_per_task}|Skills Required:{Skills Required}}}
"""
Test_Background_Summarize_FL = """ IN general Shane (representing MondeVert_IP) is a consultant who specializes in data science which includes data entry, file type conversions (basically any kind you can think of) and I have the ability to learn a task or concept and explain it to others so it can be understood by them. My skills are problem solving and communication. My goal is to resolve my clients challenges and form a partnership so they return to me overtime. I have many skills and look forward to expanding them even further. At the very least my ability to brainstorm. use the following descriptions and in general Freelance service postings to complete the task. As mentioned add details as neccesary to have between 250 and 450 characters describing the task.
 
Use the following {Skills} and {Leadership Qualities} in your descriptions to set Shane apart from other freelancers. as a writer I have AI and several paid spell checking services to make sure they get the best results. I also went to a top notch liberal arts college where you had to be a skilled writer to graduate. include my skills from past jobs and point to my resume as reference

Skills:###
- Proficient in Python programming language, including Pandas, Numpy, pytest, Selenium, openai, matlabs and other libraries.
- Skilled in Microsoft Power BI for creating dashboards, scheduling reports, and sending emails to clients and users.
- Highly proficient in Microsoft Office, including VBA coding.
- Familiar with Azure, cloud, Azure Dev Ops (ADO), Data Factory, Data Bricks, and several file load processes, including automated file load from websites to a SQL DB.
- Experienced in automated Data Quality (DQ) testing using Python/SQL and fed into pytest/TMS.
- Skilled in SQL for basic and advanced query building.
- Advanced knowledge of private equity data, specifically Fund of Fund investments, as well as other areas of Private Equity, including Credit, Real Asset, Direct Investments, Credit Facilities, IPOs, and other areas of investments.
- Passionate about data and data science in general.
- Developing and maintaining my own Digital Assistant that uses neural speech technology as well as ChatGPT (openai) python libraries.
- Developed and tested quantitative algorithms, analytical tools, and models to enhance investment and asset allocation decisions.
- Analyzed large datasets to identify anomalies, develop new processes, and produce new reporting capabilities.
- Developed and maintains my own website, mondevert.co, which promotes positivity and supports sustainable projects.
- working on personal projects in Real Estate, AI, Content Creation, Entertainment, and other areas.###


Leadership Qualities:###
- Continuously looks for process improvements and uses problem-solving skills to make an impact.
- Skilled at identifying and flagging data anomalies to solve issues.
- Comfortable asking for help when needed but continues to work towards solutions.
- Provides extensive research in areas with limited information available.
- Encourages self-learning and fosters growth within the team.
- Leads by example and mentors new hires and veteran team members alike.
- Manages without authority, leading by example and encouraging calculated risk-taking.
- Proactively managed deliverables and met objectives under minimal supervision.
- Analyzed large datasets and quickly comprehended complex information.###

 
 Text:###
 
- Service: General Consulting
Description: Offering flexibility for clients, this service provides a 20-minute call and 40 minutes of work for $50/hour, or a 40-minute to 1 hour call with 30 minutes of additional work time for $100/hour. Guaranteeing a draft or outline to show (you) the client what needs to be done, this service ensures that the client's needs are met. If it's clear that you can't help, a partial refund will be provided. Also available is a 15-minute brain session for $25, which includes a summary of the call and a detailed outline of next steps.
Price: $100/hour
Skills Required: Problem-solving and communication skills

- Service: AI-Generated Art
Description: Let AI create unique art for you! Just provide a picture, description, or artist you like and let the MondeVert_IP prompts and Python code do the rest. Every piece will be one-of-a-kind and sure to impress. 
Price: $20 per 15 unique pieces (get 5 more for 5$)
Skills Required: Python programming, AI, creativity

- Service: AI-Generated Poetry
Description: Need a personalized poem? Let AI do the work! Provide us with your specifications, and our MondeVert_IP prompts and Python code will generate a beautiful and unique poem just for you. 
Price: $40 per set of 10 poems or 1 poem for $5 
Skills Required: Python programming, AI, creativity

- Service: AI-Generated Short Story
Description: Looking for an imaginative and captivating short story? Let AI do the writing for you! Just provide your specifications, and our MondeVert_IP prompts and Python code will create a one-of-a-kind story that is sure to impress. 
Price: $30 per 3 stories or 1 for $13
Skills Required: Python programming, AI, creativity

- Service: Music Generation
Description: Let us create new music for you in any style or tone! Just provide your specifications, and we will generate a unique piece of music. A tabular version of the music can be provided, and if the music makes a profit, a 10% royalty will be received. 
Price: $20 per piece or 2 for $30
Skills Required: Music composition, creativity

- Service: Business Services
Description: Need help with business-related tasks? We've got you covered! Offering a variety of business services, including mission statements, copy, paperwork completion, interview prep, job assistance, mortgage assistance, and more, this service provides quality assistance with a quick turnaround. 
Price: $50 per hour (offline), $100 if on a call
Skills Required: Business acumen, communication

- Service: Data Entry
Description: Need fast and accurate data entry? We can help! Providing data entry services that can be automated to save time and money. Support is available for a fee after the initial automation, and for a one-time fee (varies based on complexity and time/effort) I will provide a working tool that does the file task automatically so you do not need to hire again
Price: $10 per 1000 lines
Skills Required: Data entry, automation

Service: Social Media Management
Description: Boost your online presence with our expert social media management. We'll handle all the content creation and scheduling, leaving you more time to focus on your business. With quick turnaround times and a focus on problem-solving, you'll see results in no time.
Price: $50/hour (offline work, not on call, see general consulting prices if calls are required)
Skills Required: Social media management, content creation, problem-solving

Service: Content Writing
Description: Need high-quality content in a pinch? Look no further than our expert content writing services. From blog posts to product descriptions, we'll create engaging and informative content that packs a punch. With AI-assisted writing and proofreading, we'll get the job done quickly and efficiently.
Price: $0.15/word
Skills Required: Writing, research, proofreading

Service: Virtual Assistance
Description: Need an extra pair of hands to help with administrative tasks? Our virtual assistance services are here to help. With experience in email management, data entry, and research, we'll complete your tasks quickly and accurately. Plus, with AI-assisted organization and time management, you'll get more done in less time.
Price: $60/hour (mostly Shane working offline on his own given your direction)
Skills Required: Administrative support, email management, data entry, research

Service: Graphic Design
Description: Need eye-catching visuals for your brand? Our expert graphic design services will create unique designs that stand out from the crowd. We'll work with you to understand your brand's aesthetic and create graphics that fit seamlessly with your marketing strategy. Plus, with AI-assisted design tools, we can produce high-quality graphics in record time.
Price: $75/hour
Skills Required: Graphic design, branding, marketing strategy


- Service: File Type conversions
Description: Need fast and accurate data entry? We can help! Providing data entry services that can be automated to save time and money. Support is available for a fee after the initial automation, and for a one-time fee (varies based on complexity and time/effort) I will provide a working tool that does the file task automatically so you do not need to hire again. 
Price: $20 per 100 Files
Skills Required: automation

- Service: Editing
Description: Need editing services for papers, emails, and other written materials? We've got you covered! Providing quality editing services to ensure clarity and quality. 
Price: $20 per 1000 words
Skills Required: Writing, attention to detail

- Service: On-the-Spot Services
Description: Need quick solutions to your problems? We provide a variety of on-the-spot services, including decision-making, study guides, topic summaries, creative ideas, and more! 
Price: Varies
Skills Required: Versatility, creativity


 -write a 5 minute comedy routine
 -write a short youtube sketch/skit
 -write a jingle for an advertisement
 -come up with creative ideas on the spot

 -Write a play
 -Business Mission statement
 -Business copy
 -Help completing paperwork
 -interview prep
 -I can help you get a job
 -I can help you apply for a mortgage
 -I can help you refinance
 -I can help you build a computer (not physically but show you the steps and make it easy as pie
 -I can do almost anything, literally if you meet with me and you tell me whats up there is a good chance I can offer 10 solutions in minutes and given an hour you likely have your solution 100% then and there. complex issues take time but the idea will likely be formed rather quickly its my strongsuit
 -write a fan fiction about anything
 -write a love story about you and your significant other
 -if you give a bunch of random notes I can make it into a wonderful story/documentary or any other media you can imagine
 -Generate Ad- Copy/Business materials
 -Help create content for presentations
 - Generate Short ScreenPlay for pilot or miniseries
 -Generate a unique Character for story movie etc (5$ per character)
 -Generate movie/book/series IP generator: offer this for $100 and 10% royalties of any profit from the IP created
 -generate Logo and other marketing material: See general Consulting prices, after a few meetings we can set up a monthly amount
 -Wedding Planning (outline only for ideas): offer this for $25 or push for the general consulting option. I will help them come up with a plan for their wedding and happy to do another iteration for $10. The prices are somewhat negotiable want to be fair for my time and allow the bride/groom access to a cool tool I have built.
 -Wedding Vows - this is a great way for introverts and people who know what they want to say just not how to say it get it written
 - Graduation speech generator
 -Best man speech generator
 -Motivational thought generator
 -Interview Question generator - off to make 100 unique and interesting interview questions for $20
 -Data entry for cheap ($20 per hour, once I automate you pay a one time fee and I share the tool with you. I will offer support for 25$ an hour first hour and then 50 and hour after that. Or you can keep paying the hourly rate and I can keep the tool working and it will be just like you are hiring 100 workers and I am getting paid to do the work accordingly. In most cases you will benefit because you would have to pay several other people to do the task and I will get it done faster for less.
 -Editing of papers,emails and other written materials (I will do this cheap at $20 per 1000 words for now until I know the market etc.
 -Many more to come: <list all of the possible free lance work a user can get done with the help of Chat GPT with proper use of the tool>
 -Clean up spread sheet
 -set up rules in outlook
 -set up alexa and other alexa devices
 -set up roomba
 -fix your printer
 -get you the right ink for your printer
 -I will answer any tech question you have for $20 (if it takes more than 20 minutes then may cost more, see general consulting price)
 -I will hang out with you for a day for $1300, as long as its in public (or your are not weird and no funny stuff leboski)
 - I will go bowling with you for $50 per round. and you have to pay for the bowling + shoes. This deal goes with any sort of sporting event paintball/darts/pool/body surfing.
 -I will make a short script and act it out and send it for $200
 -I will do most things that keep my dignity for the right price lets discuss!
 
 ###
 """








#************************************************************************************************
#************************************************************************************************
#************************************************************************************************

Resume_Critique_old = """Use the example from your {Prior Work Experience} and tie them to your skills. If you can take a bullet from {Skills} and place it combined with your {Prior Work Experience} example more specific examples of how you utilized your skills in the workplace? What unique achievements have you accomplished that set you apart from other candidates? use more unique action verbs to further highlight your accomplishments"""
Resume_Text_old = """{Prior Work Experience}:
State Street Corporation, Quincy, MA
Master Data Management, Officer, September 2016 – November 2019
IIS Market Support, Associate II, June 2016 - September 2016
Master Data Management, Associate I, Remote Work June 2015 - June 2016
- Built a Regression Testing User Checklist to ensure consistent testing for all Production releases
- Developed critical data quality reports on IDQ, a web-based informatica reporting tool, using SQL queries
- Created advanced VBA macros to simplify complex procedures, resulting in reduced training costs
- Managed four direct reports, held periodic one-on-one meetings to create unique goals for each employee
- Co-led a major data transformation from an outdated system to a new data platform, resulting in a 30% increase in efficiency
- Successfully transitioned a critical process from an internal State Street Team to an offshore team in India within a year with full ownership by the team in India and their management.
- Orchestrated multiple successful DQ initiatives. resulting in a 25% increase in data accuracy
- Experienced in testing for system releases, worked with IT and project teams to write stories and requirements, resulting in a 20% reduction in defects
- Serviced the Teams Reference Data and Master Data Management database, supported the development of procedural improvements, created and enhanced the team's SOPs to maximize effectiveness, and helped transition the team's daily processes offshore
- Trained, troubleshooted, and collaborated with global team members using remote technologies, resulting in a 15% increase in productivity

{Leadership Qualities}:
- Managed and trained a team of four direct reports, holding periodic one-on-one meetings to create unique goals for each employee
- Co-led a major data transformation project resulting in a 30% increase in efficiency
- Successfully transitioned a critical process from an internal State Street Team to an offshore team in India within a year with full ownership by the team in India and their management
- Orchestrated multiple successful data quality initiatives resulting in a 25% increase in data accuracy
- Experienced in testing for system releases, collaborated with IT and project teams to write stories and requirements, resulting in a 20% reduction in defects
- Trained, troubleshooted, and collaborated with global team members using remote technologies, resulting in a 15% increase in productivity


{Awards}:
- Varsity Football - 2013 Little Three and NESCAC Champions; Varsity Golf
- Three Sport Captain of Football, Track and Field, and Wrestling
- Football - All-New England, Two-time All-League, Three-time All-Scholastic; Scholar-Athlete Award recipient from the National Football Foundation and College Hall of Fame Inc.
- Wrestling - All-New England, Two-time Nationally qualified, Two-time All-League, Two-time All-Scholastic; ISL Graves-Kelsea Wrestling Tournament Champion
"""

#************************************************************************************************
#************************************************************************************************
#************************************************************************************************






# <comma_separated_list_of_company_names>

#Shane Resume Builder (Keep passing it through and using the critique to make changes'
#User Inputs
Resume_Critique = """The revised resume showcases the candidate's impressive skills in data analysis, automation, and programming. The bullet points are well-organized and easily readable. However, there is a lack of specific examples of how the candidate utilized their skills in their previous role at HarbourVest Partners. The language used in the leadership qualities section can be made more powerful and impactful by using more specific examples. To improve the resume, use specific examples of how you utilized your skills in the workplace. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice. Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created." Do not have the same Actions repeated use a thesaurus if needed to be unique. Use specific details and numbers to quantify achievements."""
Resume_Text = """Skills:
- Expert of Microsoft Office, including Excel, PowerPoint, Word, Outlook, and Access, with expertise in developing macros using Visual Basic for Applications (VBA).
- Demonstrated skill in programming languages such as Python, C++, Java, and SQL, with proficiency in Python libraries such as openai, Selenium, TensorFlow, Pandas, Numpy, and Matplotlib.
- Experienced in performing advanced data queries and utilizing the latest AI software, including ChatGPT and other tools.
- Skilled in automated data quality testing using Python/SQL and other Automated Test Management Systems (TMS).
- Proficient in Behavior-Driven Development (BDD) and object-oriented concepts, utilizing Cucumber and Gherkin language with normal Python to run automated testing via pytest and Spira (TMS).
- Experienced in utilizing Azure, Azure DevOps (ADO), Data Factory, Data Bricks, and automated file loading processes, including file loading from websites to a SQL DB.
- Expert in Bloomberg Terminal, Asset Control, and Request Builder to extract data and pull security data.
- Proficient in Salesforce360, SWIFT, Anti-Money Laundering (KYC/AML), Informatica (MDM and IDQ).
- Vast experience in techniques and best practices of Master Data Management with multiple roles in Enterprise Data Offices. Also have a few of the intial training certificates for LEAN Six Sigma and Yellow Belt skilled at identifying wasteful steps in processes and also proper root cause analysis 
- Advanced knowledge of Private Equity data, including Fund of Fund investments, Credit, Real Asset, Direct Investments, Credit Facilities, IPOs, and other areas of investments.
- Skilled in researching and comprehending difficult subject areas with limited information available.
- Strong ability to develop and test quantitative algorithms, analytical tools, and models to enhance investment and asset allocation decisions.
- Built personal projects in Real Estate, AI, Content Creation, Entertainment, and other areas.
- Developed and provided technical support for MondeVert_IP.co, a website that promotes positivity and supports sustainable projects.
- Created a Digital Assistant utilizing neural speech technology (AWS Polly) as well as ChatGPT (openai) python libraries. Currently learning how to train my own models for future use cases.
- Utilizes cost-effective solutions for projects and has a wide network of business professionals, developers, attorneys, and other key contacts
- Strong Communicator, professional and direct.
- Passionate about data science and research.

Prior Work Experience:
 HarbourVest Partners|Senior Quantitative Data Associate 2019-2023
    - Took on multiple roles in a start-up like project, including Developer, Business Analyst, Data Quality Operations, Vendor Management,Project Manager, Team engagement chairperson, training new hires, and Production support.
    - Developed, implemented, and managed automated QA/Data Quality processes, reducing manual work from 2-3 weeks to 1 day by running a suite of tools. 
    - Created a regression testing process in Python using Pandas and other python libraries to ensure consistency from DEV to QA to UAT to PROD, achieving 100% accuracy in regression tests.
    - Automated testing for over 6 million calculations, achieving accuracy above 96% for the system's logic. I took over 20 Stored Procedures and did the calculations in one SQL Script. Implemented a fully automated test to monitor the system's exception flagging logic, resulting in an increase in accuracy to 98%.
    - Acquired and integrated data from 10+ sources (Including Bloomberg terminal and Automated FTP feeds), to develop new processes and reporting capabilities. Worked with Quant and IT teams to bring new datasets into the Quantitative Risk dataset.
    - Partnered with 3rd Party and Internal Data providers to improve data sets, working with 3rd party vendors to clean over 100,000 records and helped HarbourVest's internal data providers clean up several production reports.
    - Worked in a scrum team with frequent scrum calls and biweekly sprints, planning strategic and tactical goals using Azure DevOps (ADO) to track tasks/stories.
    - Conducted data analysis, process design, and acceptance testing across projects that required new research content.
    - Led the QA team in identifying/fixing bugs, investigating issues, and providing requirements to the Development team by analyzing large datasets.
    - Conducted interviews for new hires and participated in Sprint Planning meetings as part of the team's leadership committee.
    - Trained and mentored new hires in Quality Assurance (QA), Data Quality (DQ), and Business Analyst (BA) work, resulting in their promotions and added value to the team.
    - Organized and led team engagement projects, such as quarterly party planning, quarterly newsletter, and team-building activities, to foster a collaborative and positive work environment.
    - Contributed to the growth of the team/company since being hired in 2019, from 6 to 30 employees and the company grew from 550 to 1000+ employees.
State Street Corporation, Quincy, MA|Master Data Management, Officer, September 2016 – November 2019|IIS Market Support, Associate II, June 2016 - September 2016|Master Data Management, Associate I, Remote Work June 2015 - June 2016
    - Built a Regression Testing User Checklist to ensure consistent testing for all Production releases
    - Developed critical data quality reports on IDQ, a web-based informatica reporting tool, using SQL queries
    - Created advanced VBA macros to simplify complex procedures, resulting in reduced training costs
    - Managed and trained a team of four direct reports, holding periodic one-on-one meetings to create unique goals for each employee
    - Co-led a major data transformation project resulting in a 30% increase in efficiency
    - Trained, troubleshooted, and collaborated with global team members using remote technologies, resulting in a 15% increase in productivity
    - Successfully transitioned a critical process (partially using saleforce reports) from an internal State Street Team to an offshore team in India within a year with full ownership by the team in India and their management
    - Orchestrated multiple successful data quality initiatives resulting in a 25% increase in data accuracy
    - Experienced in testing for system releases, collaborated with IT and project teams to write stories and requirements, resulting in a 20% reduction in defects
    - Serviced the Teams Reference Data and Master Data Management database, supported the development of procedural improvements, created and enhanced the team's SOPs to maximize effectiveness, and helped transition the team's daily processes offshore
Education:
- MA Real Estate Salesperson License, January 2018
- B.A. in Economics from Wesleyan University, Middletown, CT, May 2016
- High School Diploma, High Honor Student, Thayer Academy, Braintree, MA, June 2012"""

Resume_Trim_Skills ="""Skills: ###
- Writing Business content
-Writing Web content
-Writing Creative content (songs, poems, short storys, screenplays, children stories ad copy and many more)
- Brainstorming ideas and solutions
- Custom Logo Creation
- Marketing Content Generation
- AI Art
- General Consulting
- Wide Spread knowledge and ability to learn new things
- Advanced skills using Microsoft Office, including Excel, PowerPoint, Word, SSMS, and Outlook, with expertise in developing macros using Visual Basic for Applications(VBA)
•	Demonstrated skill in programming languages such as Python, C++, Java, and SQL, with proficiency in Python libraries such as openai, Selenium, TensorFlow, Pandas, Numpy, and Matplotlib
•	Proficient in Behavior-Driven Development (BDD) and object-oriented concepts, utilizing Cucumber and Gherkin language to run automated testing via pytest and Spira (TMS)
•	Experienced in utilizing Azure, Azure DevOps (ADO), Data Factory, Data Bricks, and automated file loading processes, including loading files directly from websites to a SQL DB
•	Expert in Bloomberg Terminal, Asset Control, and Request Builder to extract data and pull security data. Proficient in Salesforce360, SWIFT, Anti-Money Laundering (KYC/AML), Informatica (MDM and IDQ).
•	Vast experience in techniques and best practices of Master Data Management with multiple roles in Enterprise Data Offices. Also have a few of the initial training certificates for LEAN Six Sigma and Yellow Belt skilled at identifying wasteful steps in processes and also proper root cause analysis
•	Advanced knowledge of Private Equity data, including Fund of Fund investments, Credit, Real Asset, Direct Investments, Credit Facilities, IPOs, etc.
•	Skilled in researching and comprehending difficult concepts with limited information available. Strong Communicator, professional and direct.
•	Strong ability to develop and test algorithms, analytical tools and operational process. Able to take a complex process and make it simple
•	Built personal projects in Real Estate, AI, Content Creation, Entertainment, and other areas.
•	Developed and provided technical support for MondeVert_IP.co, a website that promotes positivity and supports sustainable projects.
•	Created a Digital Assistant utilizing neural speech technology (AWS Polly) as well as ChatGPT (openai) python libraries. Currently learning how to train my own models for future use cases
•	Utilizes cost-effective solutions for projects and has a wide network of business professionals, developers, attorneys, and other key contacts
•	Passionate about data science and research###
"""


Resume_Trim = """HarbourVest Partners  Boston, MA | Senior Quantitative Data Associate 		November 2019-Present
•	Took on multiple roles in a start-up like project, including Developer, Business Analyst, Data Quality Operations, Vendor Management, Project Manager, Team engagement chairperson, training new hires, and Production support
•	Developed and implemented automated QA/DQ processes, reducing manual work from 2-3 weeks to 1 day by running a suite of tools
•	Created a regression testing process in Python using Pandas and other python libraries to ensure consistency from DEV to QA to UAT to PROD, achieving 100% accuracy on regression tests for each release
•	Automated testing for over 6 million calculations, achieving accuracy above 96% for the system's logic. I took over 20 Stored Procedures and did the calculations in one SQL Script. Implemented a fully automated test to monitor the system's exception flagging logic, resulting in an increase in accuracy to 98%
•	Acquired and integrated data from 10+ sources (Including Bloomberg terminal and Automated FTP feeds), to develop new processes and reporting capabilities. Worked with Quant and IT teams to bring new datasets into the Quantitative Risk dataset
•	Partnered with 3rd Party and Internal Data providers to improve data sets, working with 3rd party vendors to clean over 100,000 records and helped HarbourVest's internal data providers clean up several production reports
•	Worked in a scrum team with frequent scrum calls and biweekly sprints, planning strategic and tactical goals using Azure DevOps (ADO) to track tasks/User Stories
•	Conducted data analysis, process design, and acceptance testing across projects that required new research content.
•	Identified/resolved bugs, investigated new issues, and provided requirements to the Development team by analyzing large datasets
•	Conducted interviews for new hires and participated in Sprint Planning meetings as part of the team's leadership committee.
•	Trained and mentored new hires in Quality Assurance (QA), Data Quality (DQ), and Business Analyst (BA) work, resulting in their promotions and added value to the team
•	Organized and led team engagement projects, such as quarterly party planning, quarterly newsletter, and team-building activities, to foster a collaborative and positive work environment


State Street Corporation, Quincy, MA | Master Data Management, Officer|IIS Market Support, Associate II|Intern	June 2015-November 2019
•	Built a Regression Testing User Checklist to ensure consistent testing for all Production releases
•	Developed critical data quality reports on IDQ, a web-based informatica reporting tool, using SQL queries
•	Created advanced VBA macros to simplify complex procedures, resulting in reduced training costs
•	Managed/trained a team of four direct reports.  Held Interviews for the team’s open positions and helped picked the best candidates
•	Co-led a major data transformation project resulting in a 30% increase in efficiency. Orchestrated multiple successful data quality initiatives resulting in a 25% increase in data accuracy
•	Successfully transitioned a critical process (partially using Salesforce360 reports) from an internal State Street Team to an offshore team in India within a year with full ownership by the team in India and their management
•	Experienced in testing for system releases, collaborated with IT and project teams to write stories and requirements
•	Serviced the Teams Reference Data and Master Data Management database, supported the development of procedural improvements, created and enhanced the team's SOPs to maximize effectiveness, and helped transition the team's daily processes  
"""




#************************************************************************************************



#This is one time then turn it off
##Resume_Text = Resume_Trim

Test_Role_Resume = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"
Test_Task_Resume = """ Complete the {Task} provided below, use the {Expert Critique} and {Expert Tips} to process the respective revision
{Task}: ###Clean up the language, grammar and content of the following resume and remove any redundancies. Use the background provided as the persona/voice of who is authoring these points. Do not change the facts nor add any misinformation. Clean up the grammar and language. Make it sound powerful and impressive, but do not sound exagerated. Shane should be hired for any job. Use the {Expert Critique} as a guide for the neccesary revisions| After the revision takes place you are going to give a new expert critique, give specific examples of how it can be improved, provide specific parts that need to be updated.###
{Expert Critique}:###""" + Resume_Critique + """"###
{Expert Tips}:### Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created.", Do not have the same Actions repeated use a thesaurus if needed to be unique.  Use specific details and numbers to quantify achievements. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice.###
"""

Test_Special_Resume = "Follow the format as provided, for the text only provide the revised text and not the original text. This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Keep the facts and content accurate to the original text do not add any misinformation. "
Test_Title_Resume = "Shane Donovan Resume Clean Up"
Test_Format_Resume = """ Insert the revised, reworded and reorganized text into the formate provided below

Desired Revision format:
Expert Critique: {Grade_Original_Resume_From_0_to_100%}|{Grade_Revised_Resume_From_0_to_100%}|{Expert_Critique_of_the_revised_resume}|{Questions_or_Information_User_Should_Provide_To_improve_resume_to_100%_grading}
Skills:-||-
Prior Work Experience: -||-
"""


Test_Background_Resume = Test_Task_Resume + """ 
{Text}: ### """ + Resume_Text + """"   ###"""

# #One time clean up of old text
# Test_Background_Resume = Test_Task_Resume + """
# {Text}: ### """ + Resume_Text_old + """"   ###"""



#************************************************************************************************

#************************************************************************************************

#************************************************************************************************


Resume_Critique_Review ="""First run give it an honest critique"""
#This is one time then turn it off
##Resume_Text = Resume_Trim

Test_Role_Resume_Review = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"
Test_Task_Resume_Review = """ Complete the {Task} provided below, use the {Expert Critique} and {Expert Tips} to process the respective revision
{Task}: ###Clean up the language, grammar and content of the following resume and remove any redundancies. Use the background provided as the persona/voice of who is authoring these points. Do not change the facts nor add any misinformation. Clean up the grammar and language. Make it sound powerful and impressive, but do not sound exagerated. Shane should be hired for any job. Use the {Expert Critique} as a guide for the neccesary revisions| After the revision takes place you are going to give a new expert critique, give specific examples of how it can be improved, provide specific parts that need to be updated.###
{Expert Critique}:###""" + Resume_Critique_Review + """"###
{Expert Tips}:### Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created.", Do not have the same Actions repeated use a thesaurus if needed to be unique.  Use specific details and numbers to quantify achievements. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice.###
"""

Test_Special_Resume_Review = "Follow the format as provided, for the text only provide the revised text and not the original text. This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Keep the facts and content accurate to the original text do not add any misinformation. "
Test_Title_Resume_Review = "Shane Donovan Resume Clean Up"
Test_Format_Resume_Review = """ Complete the table provided below using the specified formats

Desired Revision format:
Expert Critique: {Grade_Resume_From_0_to_100%}|{Questions_or_Information_User_Should_Provide_To_improve_resume_to_100%_grading}
Summary of skills with examples: {professionally_written_for_Linked_In_or_Website}
Summary of skills with examples: {To_be_spoken_to_potential_client}
ad copy: {professionally_written_for_Freelancing_Website}
Suggested Roles/Jobs to apply to: {Comma_separated_list_of_top_10_jobs_that_fit_resume}
Talent Level: {Rate_0_to_100%_how_talented_they_seem_versus_peers}
Suggested New Career or Industry: {provide suggested new role based on resume's skills}
Best Place to live in their current industry: {comma_separated_list_of_best_locations_for_jobs_they_fit}
Recruiter Comments: {Play the role of recruiter and provide feedback and a general 500-750 word summary of their skills and what roles they would be great for, give a list of companies they should apply to}
Job Posting Websites: {Provide URLs of job postings and/or job sites to look for jobs}
"""


Test_Background_Resume_Review = Test_Task_Resume_Review + """ 
{Text}: ### """ + Resume_Text + """"   ###"""

# #One time clean up of old text
# Test_Background_Resume = Test_Task_Resume + """
# {Text}: ### """ + Resume_Text_old + """"   ###"""




#************************************************************************************************
#************************************************************************************************
#************************************************************************************************




#This is one time then turn it off
##Resume_Text = Resume_Trim_Skills

Test_Role_LinkedIn = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"
Test_Task_LinkedIn = """ Complete the {Task} provided below, use the {Expert Critique} and {Expert Tips} to process the respective revision
{Task}: ###Using the list of skills, come up with a solid explanation to be used as a linkedin profile as well as other professional sites. You will also provide a cover letter explaining why you are a good person to hire. The explanation should make it obvious as to why a client/customer should hire you as a consultant for their project. Go over what types of projects you would be great at. Beyond this mention all of the tasks that can be done easily with the help of Chat GPT and open ai as well as DALL E because part of my service will allow access to these tools and their capabilities###
{Expert Critique}:###""" + Resume_Critique + """"###
{Expert Tips}:### Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created.", Do not have the same Actions repeated use a thesaurus if needed to be unique.  Use specific details and numbers to quantify achievements. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice.###
"""

Test_Special_LinkedIn = "Follow the format as provided, for the text only provide the revised text and not the original text. This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Keep the facts and content accurate to the original text do not add any misinformation. "
Test_Title_LinkedIn = "Shane Donovan Resume Clean Up"
Test_Format_LinkedIn = """ Insert the revised, reworded and reorganized text into the formate provided below

Desired Revision format:
Expert Critique: {Grade_Results_From_0_to_100%}|{Expert_Critique_of_the_explanation}|{Questions_or_Information_User_Should_Provide_To_improve_to_100%_grading}
LinkedIN Bio: <Professionally_written_text>
Cover Letter: <Professionally_written_text>
Explanation to a potential client: <Professionally_written_text_in_layman_terms_as_the_Client_is_not_technical>
40 second elevator pitch: <Professionally_written_text_in_layman_terms_as_the_Client_is_not_technical>
Social Medial Business profile: <Professionally_written_text>
ad copy: <Professionally_written_text>
"""


Test_Background_LinkedIn = Test_Task_LinkedIn + """ 
{Text}: ### """ + Resume_Trim_Skills + """"   ###"""

#Resume_Text

#************************************************************************************************
#************************************************************************************************
#************************************************************************************************





Test_Role_Resume_old = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"

Test_Task_Resume_old = """ Complete the {Task} provided below, use the {Expert Critique} and {Expert Tips} to process the respective revision
{Task}: ###Clean up the language, grammar and content of the following resume and remove any redundancies. This is my original Resume from 2019 but I am adding 3 new years of work experience and skills and reformatting the resume so your {Task} is to consolidate the {Text} into 10-15 bullets that summarize the work I did with specific examples and strong action words. This should show I came a far way in the past 3 years but also that I started from an impressive place. It should show that I can continue to imrpove even after reaching the top of my abilities in a given role. I knwo the value in moving on to learn new things and become a more talented individual###
{Expert Critique}:###""" + Resume_Critique + """"###
{Expert Tips}:### Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created.", Do not have the same Actions repeated use a thesaurus if needed to be unique.  Use specific details and numbers to quantify achievements. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice.###
"""

Test_Special_Resume_old = "Follow the format as provided, for the text only provide the revised text and not the original text. This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Keep the facts and content accurate to the original text do not add any misinformation. "
Test_Title_Resume_old = "Shane Donovan Old Resume Clean Up"
Test_Format_Resume_old = """ Insert the revised, reworded and reorganized text into the formate provided below

Desired Revision format:
Expert Critique: {Grade_Original_Resume_From_0_to_100%}|{Grade_Revised_Resume_From_0_to_100%}|{Expert_Critique_of_the_revised_resume}|{Questions_or_Information_User_Should_Provide_To_improve_resume_to_100%_grading}
Leadership Qualities:-||-
Prior Work Experience: -||-
Education:-||-
"""


Test_Background_Resume_old = Test_Task_Resume_old + """ 
{Text}: ### """ + Resume_Text_old + """"   ###"""




Resume_Critique_New_Combo = """The revised resume showcases the candidate's impressive skills in data analysis, automation, and programming. The bullet points are well-organized and easily readable. However, there is a lack of specific examples of how the candidate utilized their skills in their previous role at HarbourVest Partners. The language used in the leadership qualities section can be made more powerful and impactful by using more specific examples. To improve the resume, use specific examples of how you utilized your skills in the workplace. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice. Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created." Do not have the same Actions repeated use a thesaurus if needed to be unique. Use specific details and numbers to quantify achievements."""




Test_Role_Resume_old_New_Combo = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"

Test_Task_Resume_old_New_Combo = """ Complete the {Task} provided below, use the {Expert Critique} and {Expert Tips} to process the respective revision
{Task}: ###Clean up the language, grammar and content of the following resume and remove any redundancies. Consolidate the {Old_Resume_To_Condense_and_add} and then add it to the bottom of the resume. Make sure it flows as one cohesive resume. Make sure it fits on one page do not have too much info from {Old_Resume_To_Condense_and_add}. Revise the whole thing and make it as close to a score of 100% as possible. This is my original Resume from 2019 but I am adding 3 new years of work experience and skills and reformatting the resume so your {Task} is to consolidate the {Text} into 10-15 bullets that summarize the work I did with specific examples and strong action words. This should show I came a far way in the past 3 years but also that I started from an impressive place. It should show that I can continue to imrpove even after reaching the top of my abilities in a given role. I knwo the value in moving on to learn new things and become a more talented individual###
{Expert Critique}:###""" + Resume_Critique_New_Combo + """"###
{Expert Tips}:### Use bullet points to organize information and make it easier to read. Use action verbs to start phrases and sentences, such as "developed," "implemented," "managed," and "created.", Do not have the same Actions repeated use a thesaurus if needed to be unique.  Use specific details and numbers to quantify achievements. Avoid using overly technical language and acronyms that may be unfamiliar to the reader. Highlight the most important skills and achievements. Use language that is powerful and impressive, but not exaggerated. Keep the resume concise and focused on the key points. Use active voice and avoid passive voice.###
"""

Test_Special_Resume_old_New_Combo = "Follow the format as provided, for the text only provide the revised text and not the original text. This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Keep the facts and content accurate to the original text do not add any misinformation. "
Test_Title_Resume_old_New_Combo = "Shane Donovan Old Resume Clean Up"
Test_Format_Resume_old_New_Combo = """ Insert the revised, reworded and reorganized text into the formate provided below

Desired Revision format:
Expert Critique: {Grade_Originals_Resume_From_0_to_100%}|{Grade_Revised_Resume_From_0_to_100%}|{Expert_Critique_of_the_revised_resume}|{Questions_or_Information_User_Should_Provide_To_improve_resume_to_100%_grading}
Skills:-||-
Leadership Qualities:-||-
Prior Work Experience: -||-
Education:-||-
"""


Test_Background_Resume_old_New_Combo = Test_Task_Resume_old_New_Combo + """ 
{Text}: ### """ + Resume_Text + """"   ###

{Old_Resume_To_Condense_and_add}:
""" + Resume_Text_old


##***************************************************************************
##***************************************************************************









Blog_Revise_Task = """edit and revise the following article, provide me with the best version of the article keep the main concepts the same, but make it sound better and make it the best possible article it can be"""



Blog_Revise_Format= """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format. I want no headings just the {Title} "written by Shane Donovan" and then the poem should be inserted below. No additional text should be provided besides what is requested

Desired Format: 
{Title} "<written_by_{Writer_Name}}>

{Blog}
"""

# Blog_Revise_Format= """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
#
# Desired Format:
# Grade: <Original_Grade_0%_to_100%>| <Revised_Grade_0%_to_100%>
# Expert Revisions Summarized: <Expert_Revisions_Summarized>
# Revised Article: <Revised_Article>"""


Blog_Role= """you are an expert writer and specialize in blog posts and other online posts, you occasionally write articles for newsletters and newspapers. You are a master editer and social media expert. Who writes research papers and useful topics that are relevant to people of different ages. The content should be engaging and relateable, for this task and future tasks I want you to take on the following persona: """
Blog_Outline_Format= """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.

Desired Format:
Title: <ClickBait_title_of_blog>
Reading Time/Speaking time:
Subject: <Subject_of_Article_or_Post>
Description of post:<Description_of_post> 
Media Type: {Media Type}
Writing Style: {Writing Form}
Voice:-||-
Narrative:-||-
Point of View: -||-
Inspiration: -||-
Similar Writers: -||-
Themes: -||-
Mood: -||-
Audience/Word Choice:
Emotional Reaction: <Choose_between_an_emotion_Joy_laughter_sadness_anger_excited_inspired_moved>
Literary Devices: -||-
Examples of Literary Devices in use: -||-
Reason for Writing:
Positive Idea/Lesson: 
Symbolism:{Symbolism}
Imagery:{Imagery}
Specific Quotes to be used in the Post: -||-
Other Research informaton: -||-

"""
Blog_Outline_Task= """using the persona you are role playing as, Provide me with an outline for a specific blog post/research article/opinion piece that summarizes the respective information and provide the result in a format specified previously by me the user."""
Blog_Task= """Write a short (45 second to 2 minute) Blog/vlog Post based on the following outline: """
Blog_Format= """Follow the guidelines laid out by the user outline, use the proper format for the post according to the style  and information chosen by the {outline}"""

#Add-on is parable like a preacher or priest would give as a sermon
##***************************************************************************
Speech_Role= """you are an expert Public speaker/motivational speaker/ generally amazing at hyping people up and promoting a positive message that invites the listener to come back for more and challenges them to do something with their life and for the betterment of their people/the world. Help them with education and other educational/informative topics, for this task and future tasks I want you to take on the following persona: """
Entertain_Speech = """Follow these guidelines for your speech: Entertaining speech that is designed to captivate an audience’s attention and regale or amuse them while delivering a clear message.Your Entertaining speech should include four key considerations (among others): preparation, adaptation to the occasion, adaptation to the audience, and mindfulness of the time. As with all speeches, speakers need to prepare the speech. Second, speakers need to think about the specific occasion. Third, speakers need to adapt their speeches to the specific audience. Lastly, speakers need to think about how long they should speak."""
Speech_Outline_Task= """using the persona you are role playing as, Provide me with an outline for a specific 30 second to 1 minute and 20 second speech {General public speech, entertaining lecture, soap-box speech, elevator speech, motivational speech topic or idea, or a daily speech like a pastor/preacher would give}. You want to entertain the audience and make them come back for more. that summarizes the respective information and provide the result in a format specified previously by me the user."""
Speech_Task= """Make a captivating and entertaining Speech  based on the following outline: """ + Entertain_Speech



##***************************************************************************



Blog_Persona_Task = """{Task}: ### Write a bio and complete the table as requested in the {Desired Format}### 25% of the time you should create a persona that heavily focus on political topics that scale from local communities to state to federal and also global policies and laws( Topics should be informative providing the reader with information on global policy/federal laws/policy/local laws in an easy and summarized way that is easy to understand with references for the user to follow up on, use proper MLA format)."""

Blog_Persona_Role = """you are an expert writer and specialize in blog posts and other online posts, you occasionally write articles for newsletters and newspapers. You are a master editer and social media expert. Who writes research papers and useful topics that are relevant to people of different ages.  The content should be engaging and relateable to a specific audience or a wide range of audiences depending on the person you come up with. the goal of the media company you work for is to promote positivity and make people feel better by sharing good news, funny stories, making them feel better and not negative, there can be pop-culture news, but this should be global and celebrate love peace and happiness. also promote education and sharing cultural knowledge between each other. The company you work for is called 'MondeVert - Amini Amor' Which means 'Green World' and 'Believe Love' in a mix of French, Swahili and Spanish/Portuguese. We belive in being global partners with all world cultures and people spreading our love and opinions. Provide educational topics at times, DIY projects/ideas, how to save/programsa vailable for people to take advantage of, how to help people around the world, etc. """
Blog_Persona_Special = """Have fun, you should have a unique brand and style that makes your persona feel one of a kind but still relateable. Pick a unique name for your persona, use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time. This person should have star potential Provide references as needed and cite your information in proper MLA notation."""
Blog_Persona_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format. 





Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Collection Names:-||-
    Language Style: -||-
    Literary Devices: -||-
    Blog Topics: -||-
    Passions:-||-
    Writing Style: -||-
    Areas of expertise: -||-
    Research topics: -||-
    Article Structures: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Similar Writers: -||-
    Personality: -||-
    Odd_Facts_or_Fun_Facts: -||-
    Brief Summary: <Short_Description>
    Quotes:-||-
    Other Important information: -||-
"""



#************************************************************************************************
#************************************************************************************************
#************************************************************************************************








Poem_Revise_Task = """As a master of poetry edit and rewrite the following poem, provide me with the best version of the poem keep the main concepts the same, but make it sound better and make it an award winning poem. Poem: """
Poem_Revise_Format= """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format. I want no headings just the {Title} {Written By} and then the {poem} should be inserted below. No additional text should be provided besides what is requested

Desired Format: 
{Title}
{Written By}

{Poem}
"""


Poem_Role= """you are an expert poet and master of all styles of poetry, for this task and future tasks I want you to take on the following persona: """
Poem_Outline_Format= """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.

Desired Format:
Title: <Abstract_not_obvious_Title_of_Poem>
Subject: <Subject of poem>
Poetry Form: {Poetry Form}
Poetry Style: {Poetry Form}
Inspiration: -||-
Similar Poets: -||-
Themes: -||-
Mood: -||-
Audience/Word Choice:
Emotional Reaction: <Choose_between_an_emotion_Joy_laughter_sadness_anger_excited_inspired_moved>
Literary Devices: -||-
Examples of Literary Devices in use: -||-
Rhythm: -||-
Rhyme Scheme: {Rhyme Scheme}
Symbolism:{Symbolism}
Imagery:{Imagery}
Specific Quotes to be used in the Poem: -||-

"""
Poem_Outline_Task= """using the persona you are role playing as, Provide me with the neccesary informationI would need to write a new poem. Summarize the respective information in a specified format. its ok if there is no rhyme shceme, not all poetry rhymes so try to switch it up and vary your choice."""
Poem_Task= """Write a poem based on the following outline: """
Poem_Format= """use the proper format for the poem according to the style chosen by the {outline}"""





Poet_Persona_Task = """{Task}: ### Write a bio and complete the table as requested in the {Desired Format}###"""

Poet_Persona_Role = """You are an expert poet master of all genres of poetry,music, writing and entertainment/production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of poetry mastering all forms."""
Poet_Persona_Special = """Have fun, you should have a unique brand and style that makes your persona feel one of a kind but still relateable. Pick a unique name for your persona, use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time. This person should have star potential"""
Poet_Persona_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.






Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Collection Names:-||-
    Poem Names: -||-
    Passions:-||-
    Writing Style: -||-
    Melodies/Rhythym: -||-
    Rhyme Scheme: -||-
    Poem Structures: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Similar Poets: -||-
    Personality: -||-
    Odd_Facts_or_Fun_Facts: -||-
    Brief Summary: <Short_Description>
    Quotes:-||-
    Other Important information: -||-
"""



#************************************************************************************************
#************************************************************************************************
#************************************************************************************************




Music_Persona_Task = """{Task}: ### Write a bio and complete the table as requested in the {Desired Format}###"""

Music_Persona_Role = """You are an expert writer master of all genres of music,poetry, screenplays, novels, short stories, and music production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of lyric writing and music theory, also anything else I tell you to be"""
Music_Persona_Special = """Have fun, you should have a unique brand and style that makes your persona feel one of a kind but still relateable. Pick a unique name for your persona, use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time. This person should have star potential"""
Music_Persona_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Album Names:-||-
    Song Names: -||-
    Writing Style: -||-
    Melodies: -||-
    Rhyme Scheme: -||-
    Song Structures: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Similar Artists: -||-
    Personality: -||-
    Odd_Facts_or_Fun_Facts: -||-
    Brief Summary: <Short_Description>
    Quotes:-||-
    Other Important information: -||-
"""
#************************************************************************************************

Song_Role = """You are an expert writer master of all genres of music,poetry, screenplays, novels, short stories, and music production. IN general you are an expert in the entertainment industry specifically you will be taking on the persona you created. Be a master of lyric writing and music theory, also anything else I tell you to be"""
Song_Outline_Task= """using the persona you are role playing as, Provide me with an outline for a song that summarizes the respective information and provide the result in a format specified previously by me the user."""
Song_Task= """Write an original hit song based on the following outline: """

Song_Format = """Verse:{Lyrics}
              Bridge:{Lyrics}
              Chorus:{Lyrics}
              Verse:{Lyrics}
              """
Song_Outline_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:
    Time:{Less than 100 seconds}
    genres: -||-
    Tone: -||-
    Themes:-||-
    Audience: -||-
    vocabulary:
    Song Name: -||-
    Album Name:-||-
    Subject of Works:-||-
    Melodies: -||-
    Song Styles: -||-
    Rhyme Scheme: -||-
    Song Structures: -||-
    Similar Artists: -||-
    Brief Summary of Song/Story/Poem: <Short_Description>
    Influences (music, literature, film, other): -||-
    Original Quotes to use in the song:Verse:{Sample Lyrics}|Chorus:{Sample Lyrics}|Bridge/Pre-Chorus:{Sample Lyrics}
    Samples to use in the song (<Including_Song_Name_and_Artist_Name>): -||-
    Other Important information: -||-
"""


#************************************************************************************************
#************************************************************************************************
#************************************************************************************************

#Persona_Task_PictureBook = """{Task}: ### Write a bio and complete the table as requested in the {Desired Format}###"""


Persona_Task = """{Task}: ### Write a bio and complete the table as requested in the {Desired Format}###"""

Persona_Role = """You are an expert writer master of poetry, screenplays, novels, short stories, children's books etc. specifically you will be taking on the persona you created. Be a master of writing and also anything else I tell you to be"""
Persona_Special = """Have fun, you should have a unique brand and style that makes your persona feel one of a kind but still relateable. Pick a unique name for your persona, use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time"""
Persona_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:
    Persona: Full Name|Age|Personality|Hometown|Current Home|Background_Story|Current_Life_Story|Family|Odd_Facts_or_Fun_Facts
    Skills:-||-
    Subject of Works:-||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Characters from their stories: <Comma_Separated_list_of_5+_characters_and_quick_description_and_bio> (under 500 words total)
    Short Story:Sample of their work (under 500 words)
    Poetry :Sample of their work (under 500 words)
    dramatic scene from a screenplay:Sample of their work (under 300 words)
"""

Persona_Format2 = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:
    Persona: Full Name|Age|BirthDate|Personality|Hometown|Current Home|Family
    Skills:-||-
    Subject of Works:-||-
    Writing Style: -||-
    Influences (music, literature, film, other): -||-
    Audience: -||-
    genres: -||-
    Tone: -||-
    Themes:-||-
    Dialogue Style: -||-
    Personality: -||-
    Odd_Facts_or_Fun_Facts: -||-
    Brief Summary: <Short_Description>
"""

#Characters from their stories: <Comma_Separated_list_of_5+_characters_and_quick_description_and_bio> (under 500 words total)


Persona_Summary_For_Role_Play_Line2_Role = "You are a master of all skills, you are great at role playing and describing how to role play a person based on the details they provide."
Persona_Summary_For_Role_Play_Line3_Format = """Desired Format:

Skills:-||-
Subject of Works:-||-
Writing Style: -||-
Influences (music, literature, film, other): -||-
Audience: -||-
genres: -||-
Tone: -||-
Themes:-||-
Dialogue Style: -||-
Personality: -||-
Brief Summary: <Short_Description>
"""
Persona_Summary_For_Role_Play_Line4_Task = "Task: ###  Exapand on the following Persona's details in a way way for ChatGPT to assume the role of this persona. Be creative and make them feel real and human, you should have an idea the person's voice and personality from your summary  Follow the format I proivded and give me a complete response ('N/A' is not the correct response). ###   Persona: ###"




Persona_Background = """Create a persona for your writer to use as an alias be extremely creative and make the person completely unique. It should feel like a real person completely unique with all of their own personal details to be shared with the world. I want them to  feel real and cover many genres but pick a specific few they are specialists at and also the tone""" + Persona_Task

PicturebookArt = "Come up with a short prompt [less than 250 characters] to for an artist to render a work of art for a children's book that is derived from the following text. Take the text and Describe the simple background and the subjects of the work of art. Keep it simple for instance if there is a new character introduced, the artwork should show the audience the new character. Do not use proper nouns, use third person to describe the character as he/she/the <insert_animal_plant_inanimate_object>.  Make the prompt concise and easy for the artist to interpret, use the following text as your subject Text:  "

artDetailsPrompt =  "Come up with specific details that is related(or would be a good style match-up) to the symbolism/tone/context of the following text   Text:  "
artDetailsFormat = """ use the {Persona} you created to provide  the result  in the correct format, keep your response concise no more than 100 characters.

Desired Format:
Similar Artist and Details: <Artist that art is similar to>, <Tone>, <Colors> """


artDetailsFormat2 = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:

Artist that art is similar to: 
Art Style: 
Art Utensil Used: 
Tone: 
Color Schemes: """

Persona_artist_Task = Persona_Task

Persona_artist_Role = """You are an expert artist specializing in digital art that can replicate any art style.Pick 1-3 styles of your own that fit your persona """
Persona_artist_Special = Persona_Special
Persona_artist_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


Desired Format:
    Persona: 
    Full Name|Age|Hometown|Current Home|Family
    
    Skills:-||-
    Subject of Works:-||-
    art styles: -||-
    Influences (art, locations, cultures, styles , music, literature, film, other): -||-
    What are they most famous for: -||-
    Description of most famous series of work: -||-
    Other artists with similar style: -||-
    Audience: -||-
    Tone: -||-
    Themes:-||-
    Personality:
    Background:
    Odd_Facts_or_Fun_Facts: 
    
"""

Persona_artist_Background = """Create a persona for your artist to use as an alias be extremely creative and make the person completely unique. It should feel like a real person completely unique with all of their own personal details to be shared with the world. I want them to  feel real and cover many art styles but pick a specific few they are specialists at and also the tone. """ + Persona_Task





##Make Promotion Tool That runs 1  function multiple times 1 for bitter critique, Fir huge fan #supporter, unbiased opinion rate it lean towards being a harsh critic but be honest, how can we improve
#Separate tool for promotions 1 that is 90s voice, other that is for Twitter, other for Instagram, other for youtube, including script for promotion, news channel updates, short 15 second ads
# interesting no bs preview to attach and hype it up
#write a blog prmoting




#Above is step 1



#************************************************************************************************
#************************************************************************************************
#************************************************************************************************


#1 Make a persona, Make a painting of them and a photograph to be used for their online profiles
# 2 use persona to make a 5 episode screenplay (format it for audiobook) - Outline 1 All details --> use details to make outline for episode 1, then episode 2 then episode 3 etc., then use outline to make episode (eventually we can try to have something edit the language for continuity but not yet)
#For every Scene Make 4 pictures 2 of characters in the scene 1 of the setting, 1 of something important that happens in the scene
#For each line make the voice change. Pick a distinct voice for each character I need to make a quick function to make a df with Character Name:Voice Name
#Send in the Name with the respective voice and create a bunch of different audio files,
#make a program that loops through and puts the audio files together by date or whatever (date is probably best)
#Then it would be cool to make a program that puts the pictures into a movie format with the proper order maintained
#Have the description of character AI Art generator go (this is finally going to be some content)
#Feed in Artist style I like and want it to emulate.
#have a randomizer of ideas to give it some randomness and still some direction so its not boring
#Soon after posting in the next few weeks update this to beef it up.




#Below is the prompts I wrote for the short story/screenplay generator, with audio file capabilityies
#****************************************************************
#****************************************************************
#****************************************************************
#Below is step 6
Art_Summary_short_story_format = """ Complete the {Task} provided. Make sure the result is in the correct format. the results should be less than 150 words

Desired Format:
Art_Styles: <no_more_than_3>|
Themes: -||-
Tones: -||-
Color Schemes: -||-
Similar Artists: -||-
Key Signature: -||-

"""


Short_Story_Role = """role play that you are an award winning writer and director with all the talents neccesary to make a succesful screenplay/audio book that is exciting and draws the audience for more and more"""
Short_Story_Special = """Have fun, be creative and follow the rules. You are currently writing the story/screenplay for Episode #:"""
Short_Story_Task = """{Task}: ### Using the {Persona} you created, the {Episode Outline} you created and the {Characters} you created, write an Episode for all of the episodes for the series you created. See Special notes for what episode you are writing for. The story should read like a screenplay with lots of emotions, actions, dialogue and it should be relatable but also drive the reader in and use literary devices like cliff hangers to make the content breath taking. Try to make something that is emotional but also has a sweet side that makes you cry tears of joy. Do not be corny stick to the writing persona you have created when in doubt of what to do.###"""
Short_Story_Format = """Complete the {Task} provided , use the {Persona} and {Episode Outline} you created to do all of the tasks. Make sure the result is in the correct format.

Note: For the results, you should format the text as a screen play where the Narrator is written like one of the characters named 'NARRATOR'. The Narrator will say the non verbal words from the text, for example the mood, the actions happening, the scenery, the smells etc. anything not spoken should be 'spoken' by the NARRATOR. If the NARRATOR is one of the Characters switch the name from NARRATOR to their respective name. All of the Narrator non-verbal parts should be in parenthesis so the reader knows it is not being spoken aloud (NARRATOR:).

Desired Format:

Episode Details:

###<Episode_#>|<Episode_Title>|<Series Title>|Music:{Opening Song|Other Songs/Instrumentals}###

###
|NARRATOR: (<Describes_Scene_and_other_actions_emotions_voiceover_narrator>)
|CHARACTERS: "<witty_exciting_Dialog_that_fits_character_persona_and_plot>"
###"""

#Note add this to the task or background when making the outline and when writing the episode 1
Pilot_Short_story_fix = """Important Note:###this is the pilot episode so you need to introduce a bunch of characters and get the plot/arc plot going at the end of the episode the audience should know the basic plot/anti-hero/antagonist. Introduce a lot of the characters and start the arc-plots. Make the audience fall in love with some of the rich-with-details and exciting/relatable characters you create.###"""



##Set up Writing competitions and content creation competitions children story|Poetry|Comedy bit or joke|Video Skit/Sketch|Work of Art
#1st place gets 100*the buyin plus 10% of the amount over profit (so if payout is (1500 total) $1000 (1st) 300 (2nd) (200) 3rd and buy-in was $10 and we sell $3000 worth of requests then the $1500 extra goes 10% to 1st Place, 5% to 2nd and 3% to third which mean 1st would get another #150, second would get $75 extra bucks and 3rd would get $45
#3 Note countdown does not start until we get 100 submissions then the time is predetermined, usually 1 month after we hit our number or 2 weeks not sure
#Cant win more than 3 times in a row, you can be selected 2nd or third any number of times but after 3 you cannot win another outright, and I will look to see if algorithm is off or juding is flawed.
#writing, video/content,trivia, jokes, riddles, true stories


#Prompt to come up with the artist doing all of the art work so its cohesive (take writer persona tool and make one for artist)
#maybe come up with presets for now so art is reasonable and not bad
#After each episode I should make 15 pieces of work: Prompt for each of the various scenes
#Art for characters
#1 Art for Plot
#1 Art for Theme/Mood
#1 Art for Music
#1 for setting/time period
#Each Episode make art prompt by scene (2 pieces per scene)
#2 Picture of the characters in the scene
#2 pictures of main action or event or theme of the scene,be descriptive and possibly abstract


#Make Art for each outline
#use the same prompts for all the outlines

#this is high level ones, should be easy enough to make a list of prompts I can loop through

Short_Story_Art_Main_Task= "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each detail from the main {Outline} of the following story/screenplay. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  styule and tones of each prompt.use the artist persona you created, Your prompt should have each art prompts  separated by a '|' delimiter"
Short_Story_Art_Main_Format= """For your final output, the data is to be formatted in the following way:  {Art_Prompt_1_Title}|{Art_Prompt_2_Music}|{Art_Prompt_3Theme_Mood}|{Art_Prompt_4_Plot}|{Art_Prompt_5_Setting_time_Period}"""

#this is the prompt to make the art for characters.
Character_Art_Task_Main= "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each main {Character} of the following story/screenplay. Use the details provided regarding {Character} details to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  style and tones of each prompt.use the artist persona you created, Your prompt must have each art prompts  separated by a '|' delimiter"
Character_Art_Format_Main = """For your final output, the data is to be formatted in the following way:  {Art_Prompt_1_Photograph_of_character}|{Art_Prompt_2_Character_portrait}|{Art_Prompt_3_character_Wes_Anderson_Style}|{Art_Prompt_4_Character_in_Natural_Habitat_with_friends_Family_or_at_work}|{Art_Prompt_5_Character_Doing_what_they_Love}"""
Character_Art_Format_Minor = Character_Art_Format_Main
Character_Art_Task_Minor=  "write a  short descriptive art prompt for an DALL-E (ai) artist to render a work of art for each main {Character} of the following story/screenplay. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  style and tones of each prompt.use the artist persona you created, Your prompt should have each art prompts  separated by a '|' delimiter"


Short_Story_Art_Season_Task= "write 6 short descriptive art prompts for each Episode for an DALL-E (ai) artist to render a work of art for each {Scene} of the following {Story} of the following short Story. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  style and tones of each the artist persona you created. For Following text you completed, For this task you are asked to Illustration a children's story. Pictures should match the tone/theme/art styles of your artist {persona} Your prompt should have multiple art prompts per scene where each one is separated by a '|' delimiter"
Short_Story_Art_Season_Format= """"For your final output, the data is to be formatted in the following way:  Episode#:{Art_Prompt_1_Picture_of_Mood_theme_start_of_Episode}|{Art_Prompt_2_Picture_of_Mood_theme_end_of_Episode}|{Art_Prompt_3_Picture_of_characters_at_start_of_Episode}|{Art_Prompt_4_Picture_of_characters_at_end_of_Episode}|{Art_Prompt_5_Picture_of_Main_event_start_of_Episode}|{Art_Prompt_6_Picture_of_Main_event_end_of_Episode}"""


#this is Scene by scene, should be easy enough to make a list of prompts I can loop through
Short_Story_Art_Episode_Task= "write 6 short descriptive art prompts for each scene for an DALL-E (ai) artist to render a work of art for each {Scene} of the following {Story} of the following short Story. Use the details provided regarding {Illustration Details}  to come up with your prompt. The more clear the picture the better. It would also be ideal if you could match the  styule and tones of each prompt. For Following text you completed, For this task you are asked to Illustration a children's story. Pictures should match the tone/theme/art styles of your artist {persona} Your prompt should have multiple art prompts per scene where each one is separated by a '|' delimiter"
Short_Story_Art_Episode_Format= """"For your final output, the data is to be formatted in the following way:  Scene#:{Art_Prompt_1_Picture_of_Mood_theme_start_of_scene}|{Art_Prompt_2_Picture_of_Mood_theme_end_of_scene}|{Art_Prompt_3_Picture_of_characters_at_start_of_scene}|{Art_Prompt_4_Picture_of_characters_at_end_of_scene}|{Art_Prompt_5_Picture_of_Main_event_start_of_scene}|{Art_Prompt_6_Picture_of_Main_event_end_of_scene}"""


Clean_Task_after_Delimit = '{Task}:###Write a short prompt for an artist to create a unique work of art (or photo). Follow the rules/details provided###'
Clean_Role_after_Delimit = 'As an artist embody the following notes to complete your task'
Clean_Format_after_Delimit = "Keep the prompt short and to the point. Explain the following details: background, foreground, art style, subject of artwork, tone, similar artist, colors/color scheme, main focus, theme, abstracts concepts/symbolism"

#Put together the audio files
#Put the pictures together in a slideshow



#Character Outline to build the story (do this after you have details)
Character_Task_add_on1 = """ When creating the {character} details use the following {outline}  as a guide. Outline:###"""
Characters_Role = Short_Story_Role
Characters_Task1 ="""{Task}: ###Create 10-15 Main Characters and 10-20 Minor Characters for a short story/screenplay be creative and pick a diverse mix of characters, or if there is a specific time period or theme you are picking you can use names and characters that fit accordingly. Use the {Persona} you created to come up with the inspiration###"""
Characters_Special = """Have fun, be creative and follow the rules. Pick unique names for your characters, use uncommon names, then cultural names, then nicknames, try to pick common names only 10% or less of the time"""
Characters_Format = """Complete the {Task} provided, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.

Characters: ###{Name:{First Name Last Name}Age:{Age}|Voice:{Voice}|Personality:{Personality}|Home:{Current:{City State}|origin:{Country}}|Language:{Language}|Role:{Minor_Major_Protaganist_Antagonist_Unknown}|Career:{Current:{Current Job}|Dream Job:{Dream Job}}|strengths:{strengths,strengths,strengths}|weakness:{weakness,weakness,weakness}|Background:{Background}}###"""
Characters_Task = Characters_Task1 + Character_Task_add_on1


#Below is step 2
#****************************************************************
#Fist Outline of all details
Shane_Test_User_Input = "Try to be funny, but also entertaining.   Episode_Constraints: 1 Season  4 Episodes total###"

Short_Story_Config = """The following Instruction from user must be followed, Instruction: ###"""
Short_Story_Outline_Task =  """Create a Detailed Outline that fits in the format described. Base your answers off of the {Persona} you have created and are currently role playing. Do not be afraid to have tragedy strike your main/beloved characters, everyone dies eventually in life so why not see it in literature. That doesn't mean you have to follow the themes provided by the persona, but make the stories feel real even happy endings have some tragedies along the way, life is never a fairy tale, in fact even fairy tales have misfortune that needs to be overcome  """
Short_Story_Outline_Format = """Complete the {Task} provided , use the {Persona} and {Characters} you created to do all of the tasks. Make sure the result is in the correct format.

###
Background:
    Title:{Title}|Episode Length:{Episode Length}|Number of Seasons:{Number of Seasons}|Episodes per Season:{Episodes per Season}
    Target Audience:{Target Audience}
    Setting:{Setting}
    TimePeriod:{TimePeriod}
    genre:{genre}
    mood:{mood}
    Theme:{Theme}
    Narrative:{Narrative}
    Point of view:{Point of view}
    Language(s):{Language(s)}
    Music:{genres:{song genre}|songs:{song by artist,song by artist}}
    Specific Quotes:{'Quote' - Character}

Literary Devices:###
    Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}
    Arc-Plots:{Arc-Plots}
    Foreshadowing:{Foreshadowing}
    Red Herrings:{Red Herrings}
    Plot Twists:{Plot Twists}
    Juxtapositions:{Juxtapositions}
    Symbolism:{Symbolism}
    Allusion:{Allusion}
    Allegory:{Allegory}
    Irony:{Irony}
    Imagery:{Imagery}
    Similes_Metaphors:{Similes_Metaphors}
    Reoccurring Jokes:{Reoccurring Jokes}###

"""

#Below is step 3
#****************************************************************
Short_Story_Season_Outline_Role = Short_Story_Role
Short_Story_Season_Outline_Task = """{Task}: ### Using the {Persona} you created, the {Outline} you created and the {Characters} you created, write an extensivley detailed outline for all of the episodes in the series, do not make a show more than 6 episodes for now. In your outline Give a detailed description of each episode with all of the respective {Literary devices being used and relevant plot points and major character development ###"""

#Below is step 4
Short_Story_Season_Outline_Format = """Complete the {Task} provided , use the {Persona} and {Characters} you created to do all of the tasks. Make sure the result is in the correct format. You should make a table for each episode in the story/Series.

Episode by Episode Outline:
    Episode Specific Info: ###Episode Number{Episode Number}| Episode Title:{Title}|Episode Length:{Episode Length}|Setting:{Setting}|mood:{mood}|Theme:{Theme}Narrative:{Narrative}|Point of view:{Point of view}|Language(s):{Language(s)}|Specific Quotes:{'Quote' - Character}|Literary Devices:{Plot:{Exposition:{Exposition}|Rising Action (Conflict){Rising Action (Conflict)}|Climax:{Climax}|Falling Action:{Falling Action}|Resolution:{Resolution}}|Arc-Plots:{Arc-Plots}|Foreshadowing:{Foreshadowing}|Red Herrings:{Red Herrings}|Plot Twists:{Plot Twists}|Literary Devices:{Literary Devices}|Reoccurring Jokes:{Reoccurring Jokes}}###
    ###
    Major Character Development:###{Major Character Development}###  """








#****************************************************************

Short_Story_Episode_Outline_Role = Short_Story_Role
Short_Story_Episode_Outline_Special = """You are currently writing the story/screenplay for Episode #:"""
Short_Story_Episode_Outline_Task = """{Task}: ### Using the {Persona} you created, and the {Season Outline} you created and the {Characters} you created, write a detailed outline for one episode in from the story. Use the {Season Outline as your main guide and then use the Characters as potential minor characters to use and how to use the prior characters.###"""
Short_Story_Episode_Outline_Format = """Complete the {Task} provided , use the {Persona} and {Characters} you created to do all of the tasks. Make sure the result is in the correct format. Only work on the current Episode that is the focus of your task.
Episode Summary:### Episode Number{Episode Number}| Episode Title:{Title}|Episode Length:{Episode Length}|Setting:{Setting}|Point of view:{Point of view}|Language(s):{Language(s)}|Music:{genres:{song genre}|songs:{song by artist,song by artist}}|Theme:{Theme}|mood:{mood}|Literary Devices:{Literary Devices} ###
    
Scene by Scene Summary:### Scene:{Setting:{Setting}|Characters:{Characters}|Specific Quotes:{'Quote' - Character}|Scene Summary:{Scene Summarry}} ###
"""



#you need to place the custom person after this



Focus_AI = """###"""

#************************************************************************************************

#Below is step 7
Audio_Voice_Task = """{Task}: ### Do not pick a {Name/ID} that is already used based on the inputs provided. Pick a unique {Name/ID} based on the {Character description} and the data in the {Table} Provided###"""
Audio_Voice_Role = """You are an expert casting director and specialize in voice talent. You are picking the best voice based on the character description and you will no reuse the same voices so refer to the list provided if blank pick any name that fits the character"""
Audio_Voice_Special = """Have fun, be creative and follow the rules"""
Audio_Voice_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.


{Desired Format}:
Name/ID: <Name/ID>

"""

Audio_Voice_Background =  Persona_Task + """

{Character Description}:
{Table} = """ + SAF.Audio_Voice_Table

#****************************************************************
#****************************************************************
#
#
# Audio_Voice_Task = """{Task}: ### Do not pick a {Name/ID} that is already used based on the inputs provided. Pick a unique {Name/ID} based on the {Character description} and the data in the {Table} Provided###"""
#
# Audio_Voice_Role = """You are an expert casting director and specialize in voice talent. You are picking the best voice based on the character description and you will no reuse the same voices so refer to the list provided if blank pick any name that fits the character"""
# Audio_Voice_Special = """Have fun, be creative and follow the rules"""
# Audio_Voice_Format = """Complete the {Task} provided below, use the {Persona} you created to do all of the tasks. Make sure the result is in the correct format.
#
#
# {Desired Format}:
# Name/ID = <Name/ID>
# """
#
# Audio_Voice_Background =  Persona_Task + """
#
# {Character Description}:
# {Table} = """ + SAF.Audio_Voice_Table
#


MusicPy_System = """You are a brilliant assistant to the user, you are a skilled programmer and master of music theory"""
MusicPy_Role = """you are a skilled computer programmer and master of music theory. You are a modern dj who can make any form of music and is a master of midi python software and code"""
MusicPy_Task = """Your task is to drastically rewrite the parameters of the previous code so it plays the instrumental for  a new song inspired by 'Amber' by 311 or 'Gravity' by John Mayer  (do not add new functions, but you can add  additional chords/tracks/instruments within the one 'Piece' function to make your cover instrumental, update the sound by changing the chords, notes, bpm, instruments etc.' sample previously provided  to  make an instrumental to last 1 minute and 30 seconds.  Pick new instruments from the list of instruments and switch up the chords/notes you choose within the code provided as a sample."""
#Make the song a chill vibe with high notes and a reggae-like bpm (bpm <=90 Make it pleasing for the audience). Use instruments that would be in a pop top-40 summer hit song. Try to make an absolute banger. Follow the syntax for the python library 'Musicpy' for more information see the following URL: ["https://musicpy.readthedocs.io/en/latest/Basic%20syntax%20of%20piece%20type/]. Be creative and have fun, choose new instruments that go together and fit the song I requested using the instrument list provided in my prior communication.

MusicPy_Format = """

Note: Here is a full list of instruments and drums you can choose from:
#INSTRUMENTS = {    'Acoustic Grand Piano',    'Bright Acoustic Piano',    'Electric Grand Piano',    'Honky-tonk Piano',    'Electric Piano 1',    'Electric Piano 2',    'Harpsichord',    'Clavi',    'Celesta',    'Glockenspiel',    'Music Box',    'Vibraphone',    'Marimba',    'Xylophone',    'Tubular Bells',    'Dulcimer',    'Drawbar Organ',    'Percussive Organ',    'Rock Organ',    'Church Organ',    'Reed Organ',    'Accordion',    'Harmonica',    'Tango Accordion',    'Acoustic Guitar (nylon)',    'Acoustic Guitar (steel)',    'Electric Guitar (jazz)',    'Electric Guitar (clean)',    'Electric Guitar (muted)',    'Overdriven Guitar',    'Distortion Guitar',    'Guitar harmonics',    'Acoustic Bass',    'Electric Bass (finger)',    'Electric Bass (pick)',    'Fretless Bass',    'Slap Bass 1',    'Slap Bass 2',    'Synth Bass 1',    'Synth Bass 2',    'Violin',    'Viola',    'Cello',    'Contrabass',    'Tremolo Strings',    'Pizzicato Strings',    'Orchestral Harp',    'Timpani',    'String Ensemble 1',    'String Ensemble 2',    'SynthStrings 1',    'SynthStrings 2',    'Choir Aahs',    'Voice Oohs',    'Synth Voice',    'Orchestra Hit',    'Trumpet',    'Trombone',    'Tuba',    'Muted Trumpet',    'French Horn',    'Brass Section',    'SynthBrass 1',    'SynthBrass 2',    'Soprano Sax',    'Alto Sax',    'Tenor Sax',    'Baritone Sax',    'Oboe',    'English Horn',    'Bassoon',    'Clarinet',    'Piccolo',    'Flute',    'Recorder',    'Pan Flute',    'Blown Bottle',    'Shakuhachi',    'Whistle',    'Ocarina',    'Lead 1 (square)',    'Lead 2 (sawtooth)',    'Lead 3 (calliope)',    'Lead 4 (chiff)',    'Lead 5 (charang)',    'Lead 6 (voice)',    'Lead 7 (fifths)',    'Lead 8 (bass + lead)',    'Pad 1 (new age)',    'Pad 2 (warm)',    'Pad 3 (polysynth)',    'Pad 4 (choir)',    'Pad 5 (bowed)',    'Pad 6 (metallic)',    'Pad 7 (halo)',    'Pad 8 (sweep)',    'FX 1 (rain)',    'FX 2 (soundtrack)',    'FX 3 (crystal)',    'FX 4 (atmosphere)',    'FX 5 (brightness)',    'FX 6 (goblins)',    'FX 7 (echoes)',    'FX 8 (sci-fi)',    'Sitar',    'Banjo',    'Shamisen',    'Koto',    'Kalimba',    'Bag pipe',    'Fiddle',    'Shanai',    'Tinkle Bell',    'Agogo',    'Steel Drums',    'Woodblock',    'Taiko Drum',    'Melodic Tom',    'Synth Drum',    'Reverse Cymbal',    'Guitar Fret Noise', 'High Q', 'Slap', 'Stratch Push', 'Stratch Pull', 'Sticks', 'Square Click', 'Metronome Click', 'Metronome Bell', 'Acoustic Bass Drum', 'Electric Bass Drum', 'Side Stick', 'Acoustic Snare', 'Hand Clap', 'Electric Snare', 'Low Floor Tom', 'Closed Hi-hat', 'High Floor Tom', 'Pedal Hi-hat', 'Low Tom', 'Open Hi-hat', 'Low-Mid Tom', 'Hi-Mid Tom', 'Crash Cymbal 1', 'High Tom', 'Ride Cymbal 1', 'Chinese Cymbal', 'Ride Bell', 'Tambourine', 'Splash Cymbal', 'Cowbell', 'Crash Cymbal 2', 'Vibra Slap', 'Ride Cymbal 2', 'High Bongo', 'Low Bongo', 'Mute High Conga', 'Open High Conga', 'Low Conga', 'High Timbale', 'Low Timbale', 'High Agogô', 'Low Agogô', 'Cabasa', 'Maracas', 'Short Whistle', 'Long Whistle', 'Short Guiro', 'Long Guiro', 'Claves', 'High Woodblock', 'Low Woodblock', 'Mute Cuica', 'Open Cuica', 'Mute Triangle', 'Open Triangle', 'Shaker', 'Jingle Bell', 'Belltree', 'Castanets', 'Mute Surdo', 'Open Surdo'

Below is an example of code that runs and outputs 3 cool instrumentals, use it as a guide to complete the user task, use the different instruments/drums previously provided  and different chords and other music theory changes. DO NOT MAKE UP SYNTAX it has to run as-is, 

###




import musicpy as mp


# Chords and notes for the instrumental
C1 = mp.chord('E3, G#3, B3') % (1, 1/8) * 16
C2 = (mp.chord('E3, G#3, B3') % (1,1)) * 16
C3 = (mp.chord('C#3, E3, G#3') % (1/4, 1/4, 1/2) * 8 | mp.chord('E3, G#3, B3') % (1/8, 1/8, 1/4) * 8) * 8
C4 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C5 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C6 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C7 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C8 = mp.chord('E3, G#3, B3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C9 = mp.chord('E3, G#3, B3') % (1,1) * 2
C10 = mp.chord('C#3, E3, G#3') % ([3/8,1/8,1/4], [3/8,1/8,1/4]) * 16
C11 = mp.chord('C#3, E3, G#3') %  (1,1) * 8
C12 = mp.chord('F#2, A2, C#3') %  (1,1) * 8
C13 = mp.chord('G#2, C3, D#3') %  (1,1) * 8
C14 = mp.chord('G#2, C3, D#3') % (1/4,1/4,1/2) * 16
C15 = mp.chord('F#2, A2, C#3') %  (1,1) * 8

# Create a new piece with the above chords and notes
Dank_midz_SD = mp.piece(tracks=[C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15],
                      instruments=['Pizzicato Strings', 'Guitar harmonics', 'Bright Acoustic Piano', 'Woodblock', 'Koto',   'Violin', 'Tuba' , 'Harmonica', 'Banjo',  'Alto Sax',  'Slap Bass 1', 'Distortion Guitar', 'Sitar', 'Kalimba', 'Taiko Drum'],
                      bpm=100,
                      start_times=[0, 2, 2, 0, 4, 6, 8, 10,10, 12, 2, 12, 4, 6, 24],
                      track_names=['clean_guitar', 'bass', 'electric_piano', 'drum', 'grand_piano', 'jazz_guitar', 'trumpet', 'synth1', 'synth2', 'synth_bass', 'distortion_guitar', 'sitar', 'kalimba', 'string', 'synthstrings'])


mp.play(Dank_midz_SD)

###


"""
#MusicPy_Task = """Your task is to drastically rewrite the  code sample previously provided  to  make a cool new reggae instrumental following the syntax for the python library 'Musicpy' for more information see the following URL: ["https://musicpy.readthedocs.io/en/latest/Basic%20syntax%20of%20piece%20type/]. Be creative and have fun"""

#MusicPy_Task = """Your task is to drastically rewrite the parameters of the code so it plays a song similar to '311 - Amber' (do not add new functions, but you can add  additional chords/tracks/instruments within the one 'Piece' function, just update the lines as-is changing the chords, notes, bpm, instruments etc.' sample previously provided  to  make a  new hit low-fi hip hop instrumental to last 1 minute and 30 seconds. Make the song a chill vibe with lower notes and slower bpm (bpm <=90 Make it pleasing for the audience. Follow the syntax for the python library 'Musicpy' for more information see the following URL: ["https://musicpy.readthedocs.io/en/latest/Basic%20syntax%20of%20piece%20type/]. Be creative and have fun, choose new instruments that go together and fit the song I requested using the instrument list provided in my prior communication. Pick new instruments from the list of instruments and switch up the chords/notes you choose wihtin the code rovided as a sample."""








#Explain MondeVert_IP
Test_Role_Summarize_JD = "You are a master job recruiter as well as former CEO and head of hiring for several major corporations. You understand what business owners want to see and also are good at making things sound real and connect with the audience personally"

Test_Task_Summarize_JD = "Task: ###{Clean up the language, grammar and content of the following summary of a job description, we are going to add the skills and work completed from this job on a resume. Take these words and give them strong action words that could be used for a resume and clean it up so there are no redundancies and the reader would want to hire this candidate on the spot. Shane Donovan a skilled worker and driven problem solver is the persona/voice of who is authoring these points. Do not change the facts nor add any misinformation. Clean up the grammar and language. Make it sound powerful and impressive, but do not sound exagerated. Shane should be hired for any job}###"

Test_Special_Summarize_JD = "This is professional and supposed to show how skilled at marketing Shane is. This is him marketing himself, be confident but not cocky. Impress the reader and make them curious to see what skills I can bring to their company. Think of Dale Carnegie's how to win friends and influence others and make these resume items stand out. Do not change the facts nor add any misinformation. Clean up the grammar and language. The end result should be a resume with bullets for each point"
Test_Title_Summarize_JD = "Shane Donovan Job Description Clean Up for resume"
Test_Format_Summarize_JD = Test_Format_Resume
Test_Background_Summarize_JD = """You are working on a summary of a job description, we are going to add the skills and work completed from this job on a resume. Take these words and give them strong action words that could be used for a resume and clean it up so there are no redundancies and the reader would want to hire this candidate on the spot. Use the following {Text} to accomplish your tasks. Text: ###{ 


ob Description:###

HarbourVest is seeking to hire a Quantitative Data Associate to serve as a liaison between the Enterprise Data Office and the Quantitative Research and Investment Risk team. This role will be a mix of project work and data operations and the Quantitative Data Associate will sit with the Quantitative Research and Investment Risk team, and report directly to the Vice President of the Enterprise Data Office and indirectly to the Vice President of Quantitative Research and Investment Risk. The HarbourVest Enterprise Data Office acts as a facilitator and coordinator of data governance, data acquisition and data strategy across the organization. The Quantitative Research and Investment Risk team is responsible for developing and testing quantitative algorithms, analytical tools and models to enhance fundamentally driven investment and asset allocation decisions.

Job Skills and Abilities
- 3-5 years experience in financial services
- Knowledge of or the ability to learn SQL is required
- Knowledge of or the ability to learn Python or R is a plus
- Experience doing data analysis is required
- Highly analytical with the ability to quickly comprehend large datasets in order to develop new processes, perform calculations, identify anomalies, and/or produce new reporting capabilities
- The desire to develop a general understanding of quantitative analytics
- Capability to liaise with various teams to determine data requirements and manage deliverables
- Highly proactive and self-motivated with the ability to meet objectives under minimal supervision
- Experience with unstructured data is a plus
- Experience working on data integration projects and partnering with IT is a plus



Data Operations: 

Acquire data via external sources
Integrate data and manage mapping tables
Develop and manage data quality routines around Quant dataset
Work with sources or 3rd party vendors on exception handling
Ensure all required input data is available, processes run successfully, and data aggregations and transformations processed correctly
Partner with Portfolio Analytics Group in acquiring data from external sources
Data Projects:

Partner with Quant and IT to bring new datasets into the Quantitative Risk dataset
Work to transition multi-purpose datasets between the local environment and central environment, and help to be the bridge between these two locations
Perform data analysis, process design, and acceptance testing across projects that require new research content###



"""

