Gotcha(s)
  Word signup is to say that the registration form is public. 
  Word creation means we are creating them either programmtically during runtime or through admin panel
------------------------------------------------------------------------------------------------------
HFC Flows
------------------------------------------------------------------------------------------------------

# Partner Creation (Admin Panel) 

# Problem Statement Creation

# HFC Center Creation (Admin Panel)

# HFC Member Signup (Invitation Link) (Member can only join the centre that he has been invited to)
Ex: www.hackforchange.in/jntu-hfc-centre/signup/{invitation_token}

# HFC Contributor Public Signup (Contributer has to pick a city chapter)
Ex: www.hackforchange.in/contributer/signup

# HFC Mentor Public Signup (Mentors should be able to mentor any project, we will assign them projects)
Ex: www.hackforchange.in/mentor/signup

# Sumbit A Problem Statement (Public Flow)

# Project Creation (Admin Panel)

# Project Assignment (Admin Panel)

# HFC Screeing Flow (3 types, for student, for contributor, for mentor)

    ## Contributor Screening Flow
    
        1. Admin Panel Login
        2. Trigger/Create Screening From Admin Panel

------------------------------------------------------------------------------------------------------
TFC Flows
------------------------------------------------------------------------------------------------------

## Organization Signup Flow
    -

## Organization Login Flow

    - Login Screen
    - Dashboard

## Organization Settings Flow


## Member Creation / Invitation (This one is only on member invitation)

## Member Invitation Flow
    - 

    Ex: Link
    https://factly.hackforchange.in/member/activate/{auth_token}

## Member Signup Flow (Through Invitation Link)
    - 

## Volunteer Requirement Management

## Volunteer Signup (This is a public signup)
   Note: Send a thankyou note based on the template in the organization.

------------------------------------------------------------------------------------------------------
Screening Flows
------------------------------------------------------------------------------------------------------

## Screening Invitation (On Creation email is sent)
    - Ends with rendering screeing form
    - Load the screening form, with the answers that he has already given.

## Screening Review & Submit

Stage 1: Answer & Hit Proceed Button
    - Now save all the answers in the database, This will still keep the screen as open
STage 2: Review their answers and hit submit,
    - This will mark the screening as closed.
