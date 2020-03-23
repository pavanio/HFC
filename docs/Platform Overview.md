# Overview
A platform where we can curate and highlight problem statements shared by other non profit organizations and engage the hacker community using the same.

# Goals
- Show all problem statements and their detail
- Engage developer, desinger community in the best way possible
- Highlight the solutions that the community has built under this collaboration

- Problem Statement List Page, Problem Statement Detail Page
	- Admin Panel to Create Partners
	- Admin Panel to create problem statements on partners behalf

- Builing Online Communities
	- Leaderboard
		- HFC Centres
		- HFC Chapters	
		
		- Contributors
			- Contributor Page / Contributor Detail
	- Signup
		- Contributor
		- Mentor

# Domain Overview

- Partner Organization
	Partner is typically an organization who have been active in the social change (posittive change) space for more than 10+ years. 
	Ex: Factly, Foundation For Democratic Reform, Center For Policy Research, Center For Developing Societies

- Member
	Members can signup to either join a particular chapter or a centre to contributue their coding time or even mentor a whole team of contributors.
	- Contributor (With different level of expertise, entry level, intermediate, expert)
	- Mentor (Intermediate, Expert)

- HFC Centre
	Centre a physically fixed group of contributors who are actively contributing full-time on behalf of their institution
	Ex: JNTU HFC Center, GRIET Center

- HFC Chapter
	Chapter is a loosely coupled group of contributors who are involved only part-time
	Ex: City Chapters (Hyderabad Chapter)

- Problem Statement(s)
	This is a list of problem statement(s) shared with HFC Core team. And HFC Core team will add these problem statements to the platform

- Project
	This is a project planned as a solution for one or more of the problem statements on the platform.

# Application Overview

	## Features

		- Admin Panel / CMS
			- Manage Partner (s)
			- Manage Problem Statement(s)
			- Manage Member(s)
			- Manage HFC Chapter(s)
			- Manage HFC Center(s)
			- Manage Projects(Solutions)

		- Static Pages
			- Home

		- Dynamic Pages
			- List of Problem Statements
			- Problem Statement Detail
			- Leaderboard Page
				- HFC Centers
				- HFC Chapters
				
				- Contributor Wise

		- Sigup Forms
			- Contributor
			- Mentor

		- Screening Form
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




