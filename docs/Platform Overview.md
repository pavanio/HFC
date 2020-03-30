## HFC Overview
	# Overview
	A platform where we can curate and highlight problem statements shared by other non profit organizations and engage the hacker community using the same.

	# Goals
	- Show all problem statements and their detail
	- Engage developer, designer community in the best way possible
	- Highlight the solutions that the community has built under this collaboration

	- Problem Statement List Page, Problem Statement Detail Page
		- Admin Panel to Create Partners
		- Admin Panel to create problem statements on partners behalf
		- Add a way for us to accept problem statements submitted by people

	- Building Online Communities
		- Leaderboard
			- HFC Centres
			- HFC Chapters	
			
			- Contributors
				- Contributor Page / Contributor Detail
		- Signup
			- Contributor
			- Mentor
			- *Project Co-Ordinator

	# Domain Overview

	- Partner Organization
		Partner is typically an organization who has been active in the social change (posittive change) space for more than 10+ years. Or, a govermental organization / department which is keen to engage the developer community through their problem statements.

		Ex: Non-Governmental Organization (Factly, Foundation For Democratic Reform, Center For Policy Research, Center For Developing Societies),

		Ex: Governmental Organization (GHMC, Meity, Nasscom Foundation)

	- Member
		Members can signup to either join a particular chapter or a centre to contribute their coding time or even mentor a whole team of contributors.
		- Contributor (With a different level of expertise, entry-level, intermediate, expert)
		- Mentor (Intermediate, Expert)

	- HFC Centre
		Centre a physically fixed group of contributors who are actively contributing full-time on behalf of their institution
		Ex: JNTU HFC Center, GRIET Center

	- HFC Chapter
		The chapter is a loosely coupled group of contributors who are involved only part-time
		Ex: City Chapters (Hyderabad Chapter)

	- Problem Statement(s)
		This is a list of problem statement(s) shared with HFC Core team. And HFC Core team will add these problem statements to the platform

	- Project
		This is a project planned as a solution for one or more of the problem statements on the platform.

	# Application Overview

		## Features

			- Admin Panel / CMS (Private)
				- Manage Partner (s)
				- Manage Problem Statement(s)
				- Manage Member(s)
				- Manage HFC Chapter(s)
				- Manage HFC Center(s)
				- Manage Projects(Solutions)

			- Static Pages (Public)
				- Home

			- Dynamic Pages (Public)
				- List of Problem Statements
					- Problem Statement Detail
					- Submit A Problem Statement
				- Leaderboard Page
					- HFC Centers
					- HFC Chapters

					- *Contributor Wise

			- Sigup Forms (Public)
				- Contributor
				- Mentor

			- Screening Form (Public)
				- Screening should change based on level of expertise a person has
					- Entry level is for college students
					- Intermediate is for 2+ of experience people
					- Advanded / Expert is for more than 5+ years of experience

		## Signup Flow
			Need: Flow Charts

			- Mentor Signup
				-> Signup Form Completed
				-> Application creates a member in the system and Sends a Welcome Email with Screening link 
				-> Based on the level of expertise mentioned during the signup, we generate a link for screening and include that in the email	   		
				-> On Screening Completion we mark a particular member as mentor and verified/selected or on hold and send a confirmation / intimation email to the mentor (also asking them to review few links)

				# Mentor To be Assigned to a project	(Admin Panel)
		
				-> Mentor is assigned to a particular project (Only one project per mentor)
				-> Send a welcome email to the mentor with the links to the project

			- Contributor Signup
				-> Signup Form Completed
				-> Application creates a member in the system and Sends a Welcome Email with Screening link 
				-> Based on the level of expertise mentioned during the signup, we generate a link for screening and include that in the email	   		
				-> On Screening Completion we mark a particular member as verified/selected or on hold and send a confirmation / intimation email to the member (also asking them to cotribute to hackforchange project itself)

				# Contributor To be Assigned to a project	(Admin Panel)
		
					-> Member is assigned to a particular project (Only project that already have a mentor assigned and ready can be assigned to new members)
					-> Send a welcome email to the member with the links to the project connecting the mentor and the project members as well.

# TFC Overview
	## Overview
	A platform where a common set of tools that can be used by any non-profit (including CTSC) or a governmental organization, to spread the word or get the community invovled, and raise money for their cause as well.

	## Goals
	Our goal is to create a way for other organizations to use our toolset to further their cause and also at the same time a better to engage with the HackForChange Community as well.

	By giving out a freely adoptable toolset we are hoping the organizations can use the same platform to align their causes with the tech community.

	Also, we can create a common pool website non-profit can raise their needs in a better way. 
	For ex: On our website, we can show all the volunteer requirements posted by all the organizations.

	## Features    
		# Volunteer Match      
			- Community
			- Screening
			- Acceptance    

		# Fundraising 

		# Maintain Individual Organization Identity
		- We can create a way for organizaitons to upload their logo and do a minimal branding for their own pages. Also, we can give a dedicated sub-domain for each organization so that they can link it with their own websites if they choose to.
		Ex: fdr.forchange.in
		fdr.forchangee.in/volunteer
		fdr.forchange.in/donate
		
	## Application Overview
		## Organization Specific Pages (Public)
		- Org Home (fdr.forchange.in)
		- Org Volunteer Opportunities Page (fdr.forchangee.in/volunteer)
		- Volunteer Signup (fdr.forchange.in/volunteer/signup)
		- Org Donation Page (fdr.forchange.in/donate)
			- This should be only enabled if the payment setup is ready and verified

		## Organization Dashboard (Private)
		- Team Management
			- Add team members
			- Team Members roles

		- Volunteer Managemement
			- Create Categories
			- Create Subcategories
			- Manage Submissions        
			- Screening Management

		- Donation Managment
			- Payment Gateway Setup
			- Create Categores
			- Create Sub-Categories
			- Track Donations
			- Donatee and Donation

		## TFC Pages (Public)
		- TFC Home Page ()      
		- List Of Organizations on the platform by category and their areas of expertise
		- Org signup
		- Volunteer Opportunites
		- Donation Opportunities

		## TFC Dashboard
		- Organization Management
			- Organization(s) member management
			- Activate / Deactivate an organization

## Screening App Overview (SFC)

    Our Screening app is intented to screen any technical, non-technical individual based on his own level of expertise. 
        - Randomized so that not everyone is seeing the same test
        - every screening can be given a passing criteria

    ## Candidates | candidates
    Level Of Expertise |String| level_of_expertise | Possible Values: "Entry Level, Intermediate, 
    Advanced, Expert" | required
    Areas Of Expertise | String | areas_of_expertise | Ex: For Contributer "Python, CSS, HTML, Databases", For Mentor "Project Management, " | required
    *Screening Points | integer | status | Possible Values: "Passed, On Hold, Open"

    # Screening
        - A series of questions randomly chosen for a particular candidate based on his level and areas of expertise
        - Once completed we should able to evaluate and store how he is scoring on the screening
        - Also mark if someone passed or not

    ## Screeing Questions
    
    - Mutliple question types
        - yes or no
        - long answer
        - mutiple choice
    
    ## Options

