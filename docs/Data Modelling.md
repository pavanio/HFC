Note(s):

* items are still under debate
Any "text" field is assumed to be styleable using markup/plugins

# HFC Core
    
    ## Problem Statement | problem_statements

    Attribute | Type | DB Name
    ---|---|---

    Title | String | title | required
    Summary | Text | summary | required
    Background Information |Text | background_info | required
    Related Links |String |related_link | required
    Proposed Solution | Text | proposed_solution | required
    Submitted By Which Partner | id | partner_id | required
    Status | String | status|  required | Possible Values: "New / Open", "Work In Progress", "Resolved"

    ## Partner Information | partners    
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    Name | String | name | required | Ex:factly
    Website |String  | website | required |  Ex: http://www.factly.in/
    Partner Brief | Text| partner_desc| required |  Ex: Factly is a Hyderabad based fact checking organization focused on fake news         detection and educaition
    Partner Type |String| type| required | Possible Values: "Non Governmental Organization, Governmental Organization, Private               Organization"
    Contact Phone Number | String |phone_number | optional 
    Contact Email | String | email | required
    Logo | Image | logo | optional
    Primary Contact Name | String | primary_contact_name | required | Ex: Rakesh Dubbudu
    Primary Contact Number| String | primary_contact_number| required |Ex: +91 8888, We should be able to accept international numbers       as well
    Primary Contact Email | String | primary_contact_email | required 

    ## Member | members**
    |attribute| type | db column name | examples, possible values, assumptions | required / optional
        
    Name | String | name | required
    Email | String | email | required  
    Mobile | String | mobile |  required 
    Member Type | String |type | Ex: Contributor, Mentor| required    
    Github Profile | String |github_profile | required
    LinkedIn Profile String | linkedin_profile | required
    HFC Organization | integer | organization_id |required |  Ex: 2 
    HFC Organization Type | String | organination_type | required | "Chapter"
    *Assigned Project | integer | project_id| Ex: 1 | optional
    *Screening Status | integer | screening_score

    ## HFC Organization (Chapter or a Center) | organizations
    |attribute| type | db column name | examples, possible values, assumptions | required / optional
    
    Organization Name | String |organization_name |  required | Ex:JNTU, GRIET 
    Website Link | String | website | Ex:JNTU Website link| optional
    Co-ordinator Name | String | coordinator_name | required
    Co-ordinator Email | String |coordinator_email | required
    Co-ordinator Mobile | String | coordinator_mobile | required
    Organization Type | String| type | Possible Values: "Center, Chapter" | required

    ## Project | projects
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    Name | String | name | required 
    Project Link | String | project_link| required | Ex: Github link
    Project Description | Text | project_desc | required
    Website Link | String | website_link | required
    Goal | Text | goal | required 
    *Funded By | String | funded_by | Ex: "Facebook, Github, Microsoft"

# Screening App
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

