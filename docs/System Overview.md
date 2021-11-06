------------------------------------------------------------------------------------------------------
Highlevel System Overview
------------------------------------------------------------------------------------------------------
- We are designing Screeing App, Tools For Change, Hack For Change as 3 different levels of app abstraction that way, we can expose TFC for public consumption. And also, the underlying Screening app is built in a modular way so that it can repurposed in the future if needed.

------------------------------------------------------------------------------------------------------
HFC
------------------------------------------------------------------------------------------------------
Hack For Change system only has the necessary features only specific to hack for change.

Webpages in this module are accessible through https://www.hackforchange.in

------------------------------------------------------------------------------------------------------
Screening
------------------------------------------------------------------------------------------------------
Screening App has the barebones screening invitation and the screening submission and screening managment, which is used by TFC for screening purposes.

We can choose to extract this out in the future if we want this to be a standalone app.

Web pages in the module are rootless. 

Ex: If the imporing module is volunteer the screenig url will be under volunteer name space.
If the importing module is under employee url will be under employee name space.
