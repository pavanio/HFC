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
TFC
------------------------------------------------------------------------------------------------------
Tools For Change is built as a underlying app, that can support other organizations with the voluntereing, fundraising tools that we ourselves would need.

    - Every Partner Organization that comes through HFC has all the features provided by TFC available to them.
    - Ex: Every Patner Organizaation created under hfc will have dedicated home like ex: http://factly.forchange.in
    - This would allow the partner organization to better engage their community as well
    - May be in the future we can give them a way directly to submit problem statements to HFC

Webpages in this module are accessible thorugh https://www.forchange.in domain only

------------------------------------------------------------------------------------------------------
Screening
------------------------------------------------------------------------------------------------------
Screening App has the barebones screening invitation and the screening submission and screening managment, which is used by TFC for screening purposes.

We can choose to extract this out in the future if we want this to be a standalone app.

Web pages in the module are rootless. 

Ex: If the imporing module is volunteer the screenig url will be under volunteer name space.
If the importing module is under employee url will be under employee name space.