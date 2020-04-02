
------------------------------------------------------------------------------------------------------
HFC
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
TFC
------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------
Screening
------------------------------------------------------------------------------------------------------

## System Overview

## User Flows
    - Signup Flow
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
# Architecture


* Do not depend on this file. Too many conflicting and undecided opinions

HFC Community App
Skills / Expertise Screening App

ctsc.forchange.in/volunteer (Design, Mentor)
factly.forchange.in/donate
fdr.forchange.in/donate

mygov.forchange.in/donate

Hack For Change (hackforchange.in) < ForChange (This is for ctsc's purposes only)
    - Problem Statements
    - Projects

* Pointers

- Our mindset should be that the databases are different for HFC and TFC, even though the models and application abstractions are re-usable.

- Something to discuss more
    - HFC Project
        > HFC App (This import Core Models + TFC App)        
        > TFC App (This imports Core Models + Screening App)            
        > Screening App (This import Core Models)
*        > Core Modelling
            > Organization
            > Organization Member

hackforchange.in
toolsforchangein

HFC App (hackforchange.in)
    - Urls
    - fdr.hackforchange.in/volunteer

    Partners < TFC ORg, HFC Orginations < TFC Oganization>, HFC Members < TFC Member

TFC App (toolsforchange.in)
fdr.toolsforchange.in
 - Org specific url's only 

Screening

# Feature Aon For any organization
    This can be use by any non-profit organization to expand their own functionality

Each tool should be clearly abstracted out into an app so that in the future if we need we can extract it out seperately
    - Voluntter Management App
    - Donation Management App
    - Screening App