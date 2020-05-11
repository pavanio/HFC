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

## HFC Community Organization Member | community_members** (*This is a subclass of candidate in ScreeningApp)
    Name | String | name | required  
    Email | String | email | required    
    Mobile | String | mobile |  required   
    Member Type | String |type | Ex: Contributor, Mentor| required      
    Github Profile | String | coder_profile | required  
    LinkedIn Profile String | linkedin_profile | required  
    HFC Organization | integer | organization_id |required |  Ex: 2   
    HFC Organization Type | String | organination_type | required | "Chapter"  
    *Assigned Project | integer | project_id| Ex: 1 | optional  
    *Screening Status | integer | screening_score 

## Project | projects
    Name | String | name | required   
    Project Link | String | project_link| required | Ex: Github link  
    Project Icon | String | project_icon  
    Project Description | Text | project_desc | required  
    Website Link | String | website_link | required  
    Goal | Text | goal | required  
    *Funded By | String | funded_by | Ex: "Facebook, Github, Microsoft"  

## Problem Statement | problem_statements
    Title | String | title | required  
    Summary | Text | summary | required  
    Background Information |Text | background_info | required  
    Related Links |String |related_link | required  
    Proposed Solution | Text | proposed_solution | required  
    Submitted By Which Partner | id | partner_id | required  
    Status | String | status|  required | Possible Values: "Draft", "New / Open", "Work In Progress", "Resolved"
    Partner Association | id | partner_id | required |   

## Partner Information | partners (TFC Orgs are submodels or TFC Orgs)
This is a subclass of TFC Organizations Ex: Factly / Foundation For Democratic Reforms

------------------------------------------------------------------------------------------------------
TFC Modelling
------------------------------------------------------------------------------------------------------

## Organization | organizations (Governmental/ Non-Governmental organization)
    Name | String | name | required | Ex:factly
    Website |String  | website | required |  Ex: http://www.factly.in/
    Organization Brief | Text| organization_brief| required |  Ex: Factly is a Hyderabad based fact checking organization focused on fake news detection and educaition
    Contact Phone Number | String | phone_number | required 
    Contact Email | String | email | required
    Logo | Image | logo | required
    Address | Text | address | required  
    City | String | city | required  
    State | String | state | required  
    Zip | String | zip | required  
    
    * Not asked during signup
    subdomain | String | subdomain | Automatically generated based on organization abbreviation, which can changed by the admin later.
    thankyou_template | String | thankyou_template | Automatically generated the first time, the organization will have option to edit it later.
    UPI Identifier | String | upi_id | Ex: factly@okhdfcbank
    
## Member (Team Members) | team_members
    Name | String | member_name | required | Ex: Rakesh Dubbudu
    Email | String | member_email | required
    Phone Number | String | member_phone_number| required |Ex: +91 8888, We should be able to accept international numbers as well
    Password | String | password | required
    Invitation Auth Token | String | auth token | Created and sent in the email link, On password setup, auth token is cleared, if the auth token is nil, the email link will expire.
    *role | String | role | Possible: "Primary Contact(Admin) / Member"

## Volunteer Information | volunteers (This is a subclass of the candidate model)
    Name | String | name | required 
    *Mobile | String | mobile| required
    Email | String | email | Required
    Gender | String | gender | required
    Age | integer | age | required
    Address | Text | address | required  
    City | String | city | required
    State | String | state | required
    Zip | String | zip | required
    
    Education | String | education | required    
    Availability | String | availability | required | Ex: 0 - 10hours, 10 - 20hours, 20 - 30hours, 30 - 40hours per week
    Current Occupation | String | current_occupation | required | Ex: Student, Working Professional, Govenment Official
    Years Of Experience | String | years_of_experience | required | "No Experience, 1+ years, 2+ years, 3+ years, 5+ years, 10+years, 15+years, 20+ years"
    Profession | String | profession | Ex: Design, Engineering, Management etc.

## Volunteer Screening
    Subclass of ScreeningApp screening
    Organizations should be able to choose the size of a screening

## Donation Request Raised | donation_requests
    Ogranization Association | integer| organization_id | 
    Donation Request | float | donation_request | Ex: 100.00, 500.00, 1000.00
    
------------------------------------------------------------------------------------------------------
Screening App Models
------------------------------------------------------------------------------------------------------

## Candidate | candidates
    Name | String | name | required
    Email | String | email | required
    Level of Expertise | String | level_of _expertise | Possible Values: "Entry Level, Intermediate, Advanced, Expert" | required
    Area of Expertise (Skills) | String | area_of_expertise |Ex: For Contributer "Python, CSS, HTML, Databases", For Mentor "Project Management
    | required
    
## Expertise Areas | expertise_areas
    Expertise Area Id | Integer | expertise_area_id
    Area Of Expertise | String | area_of_expertise | Ex: Design, Engineering
    Category Of Expertise | String | category_of_expertise | required | Ex: Python, HTML, CSS etc
    
## Expertise | expertise     
    Expertise Id | Integer | expertise_id
    Expertise Name | String | expertise | required | Ex: ORM, DOM Model, CSS Animations etc.
    
## Question Bank | questions
    Question | Text | question | required 
    type | String | type | Possible Values: "Multiple Choice, Yes/No"
    Option 1 | Text | option_1 | required when type is multiple choice
    Option 2 | Text | option_2 | required when type is multiple choice
    Option 3 | Text | option_3 | required when type is multiple choice
    Option 4 | Text | option_4 | required when type is multiple choice
    yes / no | String | yes_no | Possiblie Valaues: "YES, NO"
    Answer | String | answer | required
    Area Of Expertise Mapping | integer | expertise_area_id | required
    Expertise Mapping | integer | expertise_id | required

## Screening with lots of questions | screenings_questions
    Screening Association | integer | screening_id
    Question Association | integer | question_id
    Candidates Answer | String | candidates_answer
    Answers Correctness | Boolean | answer_correctness | Ex: True, False

## Many to Many Screening | screenings
    Screeing id
    Screening UUID | String | screening_uuid | Ex: SCRNGSMTY01, SCRNGSMTY02 so on which is auto generated whenever you create the record
    Candidate association | integer | candidate_id
    Screening association | id | screening_id
    *Status | String | Possible Values: "New, Closed, Passed, Failed"
