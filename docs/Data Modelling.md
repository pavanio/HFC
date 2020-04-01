Note(s):

* items are still under debate  
Any "text" field is assumed to be styleable using markup/plugins  
attribute | type | db column name | examples, possible values, assumptions | required / optional


------------------------------------------------------------------------------------------------------
HFC Modelling
------------------------------------------------------------------------------------------------------

## HFC Organization (Chapter or a Center) | organizations
    Organization Name | String | organization_name |  required | Ex:JNTU, GRIET   
    Organization Type | String| type | Possible Values: "Center, Chapter" | required  
    Website Link | String | website | Ex:JNTU Website link| optional  
    Co-ordinator Name | String | coordinator_name | required  
    Co-ordinator Email | String | coordinator_email | required  
    Co-ordinator Mobile | String | coordinator_mobile | required  

## HFC Member | members**
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

## Partner Information | partners (TFC Orgs are submodels or TFC Orgs)
This is a subclass of TFC Organizations  
|attribute| type | db column name | context, examples, possible values, assumptions

------------------------------------------------------------------------------------------------------
TFC Modelling
------------------------------------------------------------------------------------------------------

## Organization | organization (Governmental/ Non-Governmental organization)
    Name | String | name | required | Ex:factly
    Website |String  | website | required |  Ex: http://www.factly.in/
    Organization Brief | Text| partner_desc| required |  Ex: Factly is a Hyderabad based fact checking organization focused on fake news detection and educaition
    Contact Phone Number | String |phone_number | required 
    Contact Email | String | email | required
    Logo | Image | logo | required
    Address | Text | address | required  
    City | String | city | required  
    State | String | state | required  
    Zip | String | zip | required  
    subdomain | String | subdomain | Automatically generated based on organization abbreviation, which can changed by the admin later.

    * Payment Gateway Modelling
    
## Member (Team Members) | team_members
    User Name | String | user_name | required
    Password | String | password | required
    Name | String | primary_contact_name | required | Ex: Rakesh Dubbudu
    Number| String | primary_contact_number| required |Ex: +91 8888, We should be able to accept international numbers as well
    Email | String | primary_contact_email | required
    *role | String | role | Possible: "Primary Contact / Admin"

## Volunteer Information | volunteers (This is a subclass of the candidate model)    
    Name | String | name | required 
    Mobile | String | mobile| required 
    Email | String | email Required    
    Gender | String | gender | required
    Address | Text | address | required  
    City | String | city | required
    State | String | state | required  
    Zip | String | zip | required  
    Highest Education | String | highest_education | required   
    Availability | String | availability | required | Ex:Immidiate , within 24 hour etc.  
    Profession | String | profession | required | Ex:Engineer, Doctor etc  
    
    
    

## Donation(*)  

## Payment Setup | payment_setup  
    Organization Name | String | organization_name | required
    Organization Merchant Key | String | organization_merchant_key | required  
    Organization Merchant Salt | String | organization_merchant_salt | required  
## Payment History | payment_history  
    Payment Id | String | payment_id | required | (payment id coming from Payment Gateway)  
    Organization Id | Integer | organization_id | required  
    Donor Name | String | donor_name | required  
    Donor Email | String | donor_email | required  
    Donation Amount | Integer | donation_amount | required  
    
    
  

## Volunteer Categories | volunteer_category 
    Category Id | Integer | category_id  | required  
    Category Name | String | category_name | required    
## Volunteer Sub Categories | volunteer_sub_category  
    Sub Category Id | Integer | sub_category_id  | required  
    Sub Category Name | String | Sub_category_name  | required  
        



------------------------------------------------------------------------------------------------------
Screening App Models
------------------------------------------------------------------------------------------------------

## Candidate | candidate    
    Name | String | name | required
    Email | String | email | required
    Level of Expertise | String | level_of _expertise | Possible Values: "Entry Level, Intermediate, Advanced, Expert" | required
    Area of Expertise (Skills) | String | area_of_expertse |Ex: For Contributer "Python, CSS, HTML, Databases", For Mentor "Project Management
    | required
    
## Category | category     
    Categoer Id | Integer | category_id
    Category Name | String | category_name | required | Ex:Python, HTML,CSS etc
    
## Sub Category | category     
    Sub Category Id | Integer | category_id
    Sub Category Name | String | category_name | required | Ex:Python, HTML,CSS etc
    
## Question Bank | questions    
    Question | String | question | required
    type | String | type | Possible Values: "Multiple Choice, Yes/No, Descriptive"    
    Option 1 | String | option_1 | required when type is multiple choice
    Option 2 | String | option_2 | required when type is multiple choice
    Option 3 | String | option_3 | required when type is multiple choice
    Option 4 | String | option_4 | required when type is multiple choice
    yes / no | String | yes_no | Possiblie Valaues: "YES, NO"
    Answer | String | answer | required
    Category Mapping | integer | category_id | required
    Sub Category Mapping | integer | sub_category_id | required
    
## Screening with lots of questions | screenings
    Screening Association | integer | screening_d
    Question Association | integer | question_id
    Candidates Answer | String | candidates_answer    

## Many to Many Screening | candidates_screenings
    Candidate association | integer | candidate_id
    Screening association | id | screening_d
    Status | String | Possible Values: "New, Closed, Passed, Failed"


    
