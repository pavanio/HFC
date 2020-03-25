* items are still under debate

# Problem Statement | problem_statements

    Attribute | Type | DB Name
    ---|---|---

    id | integer | id
    Title | String | title
    Summary | Text | summary
    Background Information
    Related Links
    Proposed Solution
    Partner Information | id | partner_id
    Status | String | status| Possible Values: "New / Open", "Work In Progress", "Resolved"

# Partner Information | partner
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    id | integer | id | 
    Name | String | name | factly
    Website | | | http://www.factly.in/
    Partner Brief ||| Ex: Factly is a Hyderabad based fact checking organization focused on fake news detection and educaition
    Contact Phone Number
    Contact Email
    Logo
    Primary Contact Name ||| Rakesh Dubbudu
    Primary Contact Number||| +91 8888, We should be able to accept international numbers as well
    Primary Contact Email


# Member
    |attribute| type | db column name 
    
    id 
    *project |||project_id|
    *Member Type | String ||Ex: Contributor, Mentor|
    Name | String
    Email 
    Mobile
    Github link
    LinkedIn Link
    HFC Center/Chapter Name
    Level Of Expertise
# HFC Center
    |attribute| type | db column name 
    
    id |integer
    Center Name |String
    Website Link |
    Center Co-ordinator Name |
    Co-ordinator Email
    Co-ordinator Mobile
    Project |project_name
# HFC Chapter
    |attribute| type | db column name 
    
    id |integer
    Chapter Name |String
    Project |project_name
    
    

# Project    
    |attribute| type | db column name | context, examples, possible values, assumptions
    
    id | integer | id | 
    Name |    
    Project Link | Github link
    Website Link |




