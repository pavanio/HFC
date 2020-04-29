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
		- Engage institutions as a way contribute, in a more fixed and centralized manner (HFC Centers)
		- Engage city level, loosely interested people to come together and contribute even if its for a couple of hours on an irregular basis (HFC Chapters)

# Domain Overview

	- Partner Organization
		Partner is typically an organization who has been active in the social change (posittive change) space for more than 10+ years. Or, a govermental organization / department which is keen to engage the developer community through their problem statements.

		Ex: Non-Governmental Organization (Factly, Foundation For Democratic Reform, Center For Policy Research, Center For Developing Societies),

		Ex: Governmental Organization (GHMC, Meity, Nasscom Foundation)

	- HFC Centre
		Centre a physically fixed group of contributors who are actively contributing full-time on behalf of their institution
		Ex: JNTU HFC Center, GRIET HFC Center

	- HFC Chapter
		The chapter is a loosely coupled group of contributors who are involved only part-time
		Ex: City Chapters (Hyderabad Chapter)

	- Member
		Members can signup to either join a particular chapter or a centre to contribute their coding time or even mentor a whole team of contributors.
		- Contributor (With a different level of expertise, entry-level, intermediate, expert)
		- Mentor (Intermediate, Expert)

	- Problem Statement(s)
		This is a list of problem statement(s) shared with HFC Core team. And HFC Core team will add these problem statements to the platform

	- Project
		This is a project planned as a solution for one or more of the problem statements on the platform.

# Feature Overview
	- Show all problem statements and their detail
	- List Of HFC Centres, HFC Chapters, Individual contributor leaderboard
	- Highlight the solutions that the community has built under this collaboration (projects)

# Application Overview
	## Static Pages
		- Home Page

	## Dynamic Pages
		- Problem Statement List
		- Project List
		- HFC Centers
		- HFC Chapters
		- Leaderboard (Individual Contribution Leaderboard)

	## Registration / Submission Forms(s)
		- Contributor
		- Mentor		
		- Suggest A Problem Statement

	## Admin Panel
		- Partner Management
		- Problem Statement Management
		- HFC Chapter Management
		- HFC Centre Management
		- Manage Projects

------------------------------------------------------------------------------------------------------
Tools For Change (TFC)
------------------------------------------------------------------------------------------------------

# Summary
TFC in a generic application, which can be used by any organization (for-profit or non-profit) to engage the community and also raise money for their cause. This becomes a placeholder for adding any common tools that can be used by organizations like CTSC.

# Goal(s)
	- A way for orgnizations to seek volunteers and screen them
	- Raise donation requests on organizations behalf

# Domain Overview
	# Organization
	Organization is any governmental or non-governmental organization that can signup for an account on our platform and use our tools for change for their cause.

	# Volunteer
	Volunteer is any individual who is willing to contribute their time and skills towards their cause of choice by working closely with any organization

	# Donation
	Donation is money contribution towards any particular organizations cause or for core operations.

# Feature Overview
	- Organizations should be able to signup and login
	- Organizations should be able to manage their own volunteer requrirements and volunteer registrations
	- Organizations should be able to accept donations and review the same across their own specific needs
	- That means organiztion(s) should be able to specify their needs, and people can select a need and select a comfortable amount that they can donate	
	- We end our process by taking them to a page, where we are sending a request to the user for the donatoin amount on their upi app.

# Application Overview
	## Global Static Pages
		- Home Page 
			https://www.forchange.in/

	## Gloabal Dynamic Pages
		- Org List
			https://www.forchange.in/orginizations
			
			- By cause etc. (Somethign like a Filter or a tag or a label) 
				https://www.forchange.in/orginizations/{label}
		
		- Organization Registration
			https://www.forchange.in/organizations/signup

	# Organization Pages (Subdomain level)
		- Org Home Page
			https://factly.forchange.in

		- Org Donation Request Page
			https://factly.forchange.in/donate

		- Organization Login
			https://factly.forchange.in/login

		- Organization Volunteer Signup
			https://factly.forchange.in/volunteer

		- Volunteer Screning
			https://factly.forchange.in/volunteer/screening/:screning_id

	## Organization Dashboard (Private, Only when somebody is logged in)
		- Org Dashboard
			https://factly.forchangein/dashboard

		- Org profile management
			- Basic Profile
			- UPI Details

		- Team Management
			- Member List page
				https://factly.forchange.in/members
			
			- Organization Member Magement
				https://factly.forchange.in/members/new
				https://factly.forchange.in/members/:member_id/edit
				
				- Activate a member
				https://factly.forchange.in/members/activate/:invitation_token
					After activation we clear the invitation_token
				
				- Set password first time after activation, secon	
				https://factly.forchange.in/members/:member_id/set_password

		- Volunteer Management (Applications)
			- List / Detail
		
		- Donation Request Management (Donations)
			- List / Detail / Metrics etc

		- Volunteer Requrements
		
		- Donation Requirements

	## Admin Panel
		https://www.forchange.in/admin

		- Organization Management
			- Create an organization manually
			- Metrics

		- Member Management at orginzation level
			List members
				Members, activation status
		
		- Volunteer Management
			- Metrics

		- Donation Management
			- Metrics

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

	# Category

	# Sub-Category

	# Questions

	# Question Type	

# Feature Overview
	- Candidate screening workflow
		- Create a screening
		- Create a screening page where some is actually screened
		- On succeful submittee, say say thankyou

	- Screening should change based on level of expertise a person has
		- Entry level is for college students
		- Intermediate is for 2+ of experience people
		- Advanded / Expert is for more than 5+ years of experience

	- Randomized so that not everyone is seeing the same test
	- every screening can be given a passing criteria
	- Admin Panel to manage the questions and the question bank
	- Admin Panel to mange the screenings

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
