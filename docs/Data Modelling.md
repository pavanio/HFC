Note(s):

* items are still under debate
Any "text" field is assumed to be styleable using markup/plugins

# Problem Statement | problem_statements

    Attribute | Type | DB Name
    ---|---|---

    Title | String | title
    Summary | Text | summary
    Background Information
    Related Links
    Proposed Solution
    Submitted By Which Partner | id | partner_id
    Status | String | status| Possible Values: "New / Open", "Work In Progress", "Resolved"

# Partner Information | partners
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    Name | String | name | factly
    Website | | | http://www.factly.in/
    Partner Brief ||| Ex: Factly is a Hyderabad based fact checking organization focused on fake news detection and educaition
    Partner Type |String| type| Possible Values: "Non Governmental Organization, Governmental Organization, Private Organization"
    Contact Phone Number
    Contact Email
    Logo
    Primary Contact Name ||| Rakesh Dubbudu
    Primary Contact Number||| +91 8888, We should be able to accept international numbers as well
    Primary Contact Email

# Member | members
    |attribute| type | db column name | examples, possible values, assumptions | required / optional
        
    Name | String
    Email 
    Mobile
    Member Type | String |type | Ex: Contributor, Mentor| required    
    Github Profile
    LinkedIn Profile
    HFC Organization | integer | organization_id | Ex: 2 
    HFC Organization Type | String | organination_type | "Chapter"
    Level Of Expertise |String| level_of_expertise | Possible Values: "Entry Level, Intermediate, 
    Advanced, Expert" | required
    Areas Of Expertise | String | areas_of_expertise | Ex: For Contributer "Python, CSS, HTML, Databases", For Mentor "Project Management, " | required
    *Screening Status | String | status | Possible Values: "Passed, On Hold, Open"
    *Assigned Project |integer| project_id| Ex: 1 | optional

# HFC Organization (Chapter or a Center) | organizations
    |attribute| type | db column name | examples, possible values, assumptions | required / optional
    
    Organization Name | String | 
    Website Link | String | website ||
    Co-ordinator Name | String | coordinator_name
    Co-ordinator Email
    Co-ordinator Mobile
    Organization Type | String| type | Possible Values: "Center, Chapter"

# Project | projects
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    Name | 
    Project Link | Github link
    Project Description |
    Website Link | 
    Goal | Text | goal | 
    *Funded By | String | funded_by | Ex: "Facebook, Github, Microsoft"