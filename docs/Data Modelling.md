Note(s):

* items are still under debate  
Any "text" field is assumed to be styleable using markup/plugins  
attribute | type | db column name | examples, possible values, assumptions | required / optional


------------------------------------------------------------------------------------------------------
HFC Modelling
------------------------------------------------------------------------------------------------------

## HFC Community Organization (Chapter or a Centre) | community_organizations
    Note: Our community organizations are not TFC Orgnizations, these are just loosely/tightly coupled group of developers. So we dont want to give our tfc features to these groups
    
    Organization Name | String | organization_name |  required | Ex:JNTU, GRIET
    Organization Type | String| type | Possible Values: "Center, Chapter" | required
    Website Link | String | website | Ex:JNTU Website link| optional
    Logo | String | logo | Ex: College Centre / City chapter logo | not required
    Co-ordinator Name | String | coordinator_name | required  
    Co-ordinator Email | String | coordinator_email | required  
    Co-ordinator Mobile | String | coordinator_mobile | required  
    Project | Many to many | project | not required  
    City | String | city | not required   
    is public | Boolean | is_public | not required   

## HFC Community Organization Member | community_members** (*This is a subclass of candidate in ScreeningApp)
    Name | String | name | required  
    Email | String | email | required    
    Mobile | String | mobile |  required   
    Member Type | String |type | Ex: Contributor, Mentor| required
    Github Profile | String | coder_profile | required  
    LinkedIn Profile String | linkedin_profile | required  
    HFC Organization | integer | organization_id |required |  Ex: 2   
    *Assigned Project | integer | project_id| Ex: 1 | optional  
    *Screening Status | integer | screening_score  
    Years of Experience | String | years_of_experience | required  
    Image | String | image | not required  
    Commit | String | commit | not required  
    Avatar Url | String | avatar_url | not required  
    Project | Many to many | project | not required  

## Project | projects
    Name | String | name | required   
    Project Link | String | project_link| required | Ex: Github link  
    Project Icon | String | project_icon | not required    
    Project Overview | Text | project_overview | required  
    Website Link | String | website_link | not required  
    Goal | Text | goal | not required  
    Project Slug | String | project_slug | not required   

## Problem Statement | problem_statements
    Problem Statement | String | problem_statement | required  
    Overview | Text | overview | required  
    Background Information |Text | background_info | required  
    Related Links |String |related_link | not required  
    Proposed Solution | Text | proposed_solution | not required  
    Submitted By Which Partner | id | partner_id | not required  
    Status | String | status|  required | Possible Values: "Draft", "New / Open", "Work In Progress", "Resolved"  
    Issue Areas | String |issue_area | required | EX:"open gov","democracy"  

## Partner Information | partners (TFC Orgs are submodels or TFC Orgs)
    This is a subclass of TFC Organizations Ex: Factly / Foundation For Democratic Reforms

## Issue Area | Focus Area
    Issue Area | String | issue_area | required 
    Issue Sub Header | String | issue_sub_header | not required   
    Issue Brief | Text| issue_brief| not required  
    issue_overview | Text | issue_overview | not required  
    Context | Text| issue_brief| not required  
    Tehnology Intervention | Text | technology_intervention | not required
    Related Information | URL | related_information | not required  
    Issue Area Slug | Text | issue_area_slug | not required  

## Project_Partners | project_partners
    Partner Association | id | partner_id | required
    Project Association | id | project_id | required
    Project Involvement | String | project_involvement | required | Possible Values:"Funding","Execution","Adoption/Promotion"

## Organization | organizations (Governmental/ Non-Governmental organization)
    Name | String | name | required | Ex:factly
    Website |String  | website | required |  Ex: http://www.factly.in/  
    Organization Brief | Text| organization_brief| required |  Ex: Factly is a Hyderabad based fact checking organization focused on fake news detection and educaition
    Contact Phone Number | String | phone_number | required 
    Contact Email | String | email | required
    Logo | Image | logo | required
    City | String | city | required
    Focus Area | String | focus_area | required | EX:"open gov","democracy"   
    
    * Not asked during signup
    State | String | state | required
    subdomain | String | subdomain | Automatically generated based on organization abbreviation, which can changed by the admin later.
    thankyou_template | String | thankyou_template | Automatically generated the first time, the organization will have option to edit it later.
    UPI Identifier | String | upi_id | Ex: factly@okhdfcbank

## Donation Intents | donation_intents
    Organization Association | integer| organization_id | 
    Intent Amount | float | intent_amount | Ex: 100.00, 500.00, 1000.00
    Intent Frequency | string | intent_frequency | Ex: One Time, Monthly, Quarterly, Annually
    Donor First Name | string | first_name
    Donor Last Name | string | last_name 
    Donor Email | string | donor_email
    Donor Phone Number | string | donor_mobile
    Donor Comment | text | comments
    Donor Anonymity | string | donor_anonymity | Ex: Yes / No    
    Subscription

## Platform Donation Requests (Jobs)
    Donor Full Name | string | donor_fullname
    Donor Phone Number | string | donor_mobile
    Donation Request Amount | float | request_amount
    Status | string | status | Ex: Open, Raised, Full-filled
    
------------------------------------------------------------------------------------------------------
Screening App Models (Should be usable by volunteers/non-volunteers as well)
------------------------------------------------------------------------------------------------------

## Candidate | candidates
    Name | String | name | required
    Email | String | email | required  
    Contact Number | String | contact_number | required  
    Gender | String | gender | not required  
    D.0.B | Datefield | dob |  not required 
    Highest Education | String | highest_education | Possible Values: "Intermediate, Bachelors, Masters" |required  
    Profession | String | profession | Ex: Design, Engineering, Management, Operations, HR,  etc. (This should be populated form area of category from category table)  
    Area of Expertise (Skills) | String | area_of_expertise | Ex: For Contributer "Python, CSS, HTML, Databases", For Mentor "Project Management| required  
    Level of Expertise | String | level_of _expertise | Possible Values: "Entry Level, Intermediate, Advanced, Expert" | required  
    
## Expertise Areas | expertise_areas
    Expertise Area Id | Integer | expertise_area_id
    Area Of Expertise (Profession) | String | area_of_expertise | Ex: Design, Engineering
    
## Expertise | expertise     
    Expertise Id | Integer | expertise_id
    Expertise Name | String | expertise | required | Ex: Python, Ruby, HTML, CSS, Java,
    Expertise Area Mapping | integer | expertise_area_id  
    is published | Boolean | is_published 
    
## Question Bank | questions
    Question | Text | question | required 
    type | String | qtype | Possible Values: "Multiple Choice, Yes/No"
    Option 1 | Text | option_1 | required when type is multiple choice
    Option 2 | Text | option_2 | required when type is multiple choice
    Option 3 | Text | option_3 | required when type is multiple choice
    Option 4 | Text | option_4 | required when type is multiple choice
    yes / no | String | yes_no | Possiblie Valaues: "YES, NO"
    Answer | String | answer | required  
    Question Image | Image | question_image | not required  
    Area Of Expertise Mapping | integer | expertise_area_id | required  (Is mapped with candidate/volunteers profession)  
    Expertise Mapping | integer | expertise_id | required (Is mapped with candidate/volunteers area of expertise) 
    Question Level Mapping | integer | level | entry, intermediate, advanced, expert | required (Is mapped with candidate/volunteers level_of_expertise)   
    Topic | String | topic | required | Ex: ORM, DOM Model, CSS Animations etc.  

## Screening with lots of questions | screenings_questions
    Screening Association | integer | screening_id | required  
    Question Association | integer | question_id | required  
    Candidates Answer | String | candidates_answer 
    Correct Answer | String | correct_ans | required  
    Answers Correctness | Boolean | answer_correctness | Ex: True, False

## Many to Many Screening | screenings
    
    Screening UUID | String | screening_uuid | Ex: SCRNGSMTY01, SCRNGSMTY02 so on which is auto generated whenever you create the record
    Candidate association | integer | candidate_id
    Screening association | id | screening_id
    Status | String | Possible Values: "New, Closed, Passed, Failed" 
    Screening Result | String | screening_result | Possible Values:60%,50%,  
    Created On | Date | created_on | not required 
    First Reminder Date | Date | first_reminder_date | not required 
    Second Reminder Date | Date | second_reminder_date | not required 
    Third Reminder Date | Date | third_reminder_date | not required  

------------------------------------------------------------------------------------
Blog Models
-------------------------------------------------------------------------------------
## Post  
    Title | String | title | required  
    Body | Text | body | required  
    Author | String | author | not required  
    Image | Image | image | not required  
    Created on | Date | created_on | not required  
    Status | String | status | Possible values :"Draft,Published" | required
    Keywords | Text | keywords | required  

--------------------------------------------------------------------------------------------
Event Models  
------------------------------------------------------------------------------------------------
## Event Type  
    Category | String | category | required  
## Event  
    Title | String | title | required  
    Start Date | Date | start_date | not required 
    End Date | Date | end_date | not required  
    Description | Text | description | not required   
    Agenda | Text | agenda | not required  
    Status | String | status | Possible Values: "Draft,Published" | required  
    Event Type | Id | event_type_id | required  
    Email confirmation | Text | email_confirmation | not required  
    Registartion | String | registration | not required  
    logo | Image | logo | not required  
    Banner | Image | banner | not required  
    Banner Color | String | banner_color | Possible Values:"Dark,Light" | not required  

