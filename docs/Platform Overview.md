Note(s):
--- Underlying stuff is for future reference

------------------------------------------------------------------------------------------------------
Hack For Change
------------------------------------------------------------------------------------------------------

## Summary
A platform where we can curate and highlight problem statements shared by other non profit organizations and engage the hacker community using the same.

# Goals 
    - Domain Experts to be engaged in submitted problem statements that are relavent to their area of expertise and domain
        - Highlight Problem Statement(s)
	- Engage Developer, Designer and Mentor Community
		- Encouraging continuous contribution
		- Engage institutions as a way contribute, in a more fixed and centralized manner (HFC Chapters)
		- Engage city level, loosely interested people to come together and contribute even if its for a couple of hours on an irregular basis (HFC Centres)

# Domain Overview

	- Partner Organization
		Partner is typically an organization who has been active in the social change (positive change) space for more than 10+ years. Or, a govermental organization / department which is keen to engage the developer community through their problem statements.

		Ex: Non-Governmental Organization (Factly, Foundation For Democratic Reform, Center For Policy Research, Center For Developing Societies),

		Ex: Governmental Organization (GHMC, Meity, Nasscom Foundation)

	- HFC Centre
		Centre a physically fixed  loosely coupled group of contributors who are actively contributing and  involved only part-time. 
		Ex:Hyderabad Centre , Bhubaneswar Centre  

	- HFC Chapter
		The chapter is a  group of contributors who are actively contributing and full-time on behalf of their institution
		Ex: JNTU HFC Chapter , DRIEMS HFC Chapter  

	- Member
		Members can signup to either join a particular chapter or a centre to contribute their coding time or even mentor a whole team of contributors.
		- Contributor (With a different level of expertise, entry-level, intermediate, expert)
		- Mentor (Intermediate, Expert)

	- Problem Statement(s)
		This is a list of problem statement(s) shared with HFC Core team. And HFC Core team will add these problem statements to the platform

	- Project
		This is a project planned as a solution for one or more of the problem statements on the platform.
	- Blog  
		This is a blog post to show all the lastest updates about HackForChange.  
	- Event  
		This is to show all the ongoing and upcoming events related to HackForChange lie hackathons,webinar,bootcamp etc.

# Feature Overview
	- Show all problem statements and their detail
	- List Of HFC Centres, HFC Chapters, Individual contributor leaderboard
	- Highlight the solutions that the community has built under this collaboration (projects)  
	- A blog to show the latest updates from the platform.  
	- An Event engine to show all the ongoing or upcoming HacForChange events lie hackathon,webinar and so on.

# Application Overview
	## Static Pages
		- Home Page
			https://www.Hack.forchange.in/

	## Dynamic Pages
		- Problem Statement List
			/problem-statements
		- Problem Statement Detail
			/problem-statements/:problem-statement-title
		- Focus Area List  
			/focus-areas  
		- Focus Area Detail  
			/focus-areas/:focus-area-title  
		- Project List  
			/projects  
		- Project Detail  
			/projects/:project-name  
		- Community Page  
			/community 
		- Leaderboard (Individual Contribution Leaderboard)  
		- HFC Centre/Chapter Details  
			/:organization-name 
		- Blog List  
			/blog  
		- Blog Detail  
			/blog/:title-name
		- Event List
			/events  
		- Event Detail  
			/events/:event-name

	## Registration / Submission Forms(s)
		- Contributor 
			/chapters/{hfc_chapter}/contributor/signup
			/centres/{hfc_center}/contributor/signup
		- Mentor  
			/mentor/signup  
		- Community Member 
			/community/signup/  
		- Suggest A Problem Statement  
			/problem-statement/suggest/  
		- Event Signup 
			/events/:event-name/signup 


	## Admin Panel  
			/admin
		- Partner Management
			- Partner Team Members (Members)
		- Problem Statement Management
		- HFC Chapter/Centre Management
			- Community Members Management (Candidates)
		- Manage Projects



------------------------------------------------------------------------------------------------------
Screening App
------------------------------------------------------------------------------------------------------

# Summary
	 A rootless screening app that can be used be anybody for screening people  

# Goal(s)
	Goal is to abstract out the screening functionality that can be used by any body in the future, to screen their candidates.

# Domain
	# Candidate
	Candidate is any individual who can be evaluated based on his own interests and skillset.

	# Expertise Areas 
		These are the categories to which a candidate belongs.   
		Ex:Design,Engineering,Management,Marketing  

	# Expertise  
		These are the sub categories for particular categories.  
		Ex:Python,Django comes under the Engineering  
		Digital marketing comes under Marketing  
		Project management comes under Management  

	# Questions  
		All the questions are multiple choice having 4 options from which only one is correct answer.  

	# Question Type	
		Question type are multiple choice.    

# Feature Overview
	- Candidate screening workflow
		- Create a screening
		- Create a screening page where some is actually screened
		- On succeful submittee, say say thankyou

	- Screening should change based on level of expertise a person has
		- Entry level is for 0 to 2+ years of experience  
		- Intermediate is for 3+ to 5+ years of experience people
		- Advanded  is for 10+ to 15+ years of experience  
		- Experty is for 20+ years of exp.

	- Randomized so that not everyone is seeing the same test
	- every screening can be given a passing criteria
	- Admin Panel to manage the questions and the question bank
	- Admin Panel to mange the screenings

# Screening Criteria  
	- Screening is based on the level of expertise  and area of expertise  
	- Every screening consist of 10 questions from the area of expertise 
	- All the questions from different topics under the area of expertise  
	- Qualifying criteria of  screening is 70%   
	- Once screening completes the status of the candidate automatically change from "New" to "Passed" or "Failed" on organization dashboard.  
	- Until the candidate has not attempted the screening the status of screening is "Open".
	- After completion of screening its result will display in the screening result pages. 

# Application Overview
	## Screening 		
		- Screening Page
		- Thank you Page

	## Admin Pages
		- Screenings List
		- Question Types List
		- Question Bank
		- Question Categories
			- Areas
		- Question Sub Categories
