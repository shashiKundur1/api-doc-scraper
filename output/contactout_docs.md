# API Documentation

## Introduction

Welcome to ContactOut's API. Find anyone's email & phone number 10x faster with the most powerful sales and recruitment intelligence software available.

---

## Authentication

To authorize, use this code:

ContactOut uses API keys to allow access to the API. You can request an API key by booking a meetinghere.

ContactOut expects the API key to be included in all API requests to the server in a header that looks like the following:

token : <YOUR_API_TOKEN>

People Search API: 60 requests per minute

Contact Checker APIs: 150 requests per minute

Other APIs: 1000 requests per minute

### Code Samples
**curl**
```
Copy to Clipboard# With shell, you can just pass the correct header with each requestcurl"https://api.contactout.com"\-H"authorization: basic"-H"token: <YOUR_API_TOKEN>"
```

---

## LinkedIn Profile API

---

## from LinkedIn URL

Get profile details for a single linkedin profile URL. The input only accepts LinkedIn regular URLs, not Sales Navigator or Talent / Recruiter LinkedIn products.

This API allows you to retrieve various details such as email addresses, phone numbers, work experience, education, skills, and more associated with a LinkedIn profile.

The above command returns JSON structured like this:

Empty Results

GET https://api.contactout.com/v1/linkedin/enrich?{profile=}

Consumes 1 email credit if email is found and 1 phone credit if phone number is found.

Consumes 1 search credit ifprofile_onlyis set to true or if there is no contact information available for the requested profile.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profile | string, URL encoded, required | The fully formed URL of the LinkedIn profile. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| profile_only | boolean, optional, default: false | If set to true, returns the profile data without contact information. |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | Contains profile details related to the URLurl- The URL of the LinkedIn profile.email- An array of email addresses associated with the profile.work_email- An array of work email addresses associated with the profile.personal_emailAn array of personal email addresses associated with the profile.phone- An array of phone numbers associated with the profile.github- An array of GitHub usernames associated with the profile.twitter- An array of Twitter usernames associated with the profile.full_name- The full name of the profile owner.headlineThe headline or job title of the profile owner.industry- The industry in which the profile owner works.company- An object containing information about the current company of the profile owner, including name, URL, website, and headquarters location.location- The location of the profile owner.summary- A summary or description of the profile owner's professional background.experience- An array of objects containing details about the profile owner's work experience, including start and end dates, job title, description, and company LinkedIn URL.education- An array of objects containing details about the profile owner's education, including institution name, major, start and end dates, degrees, and profile URL.skills- An array of skills associated with the profile owner.certifications- An array of objects containing the certifications of the profile. Includes details like certification name, company, authority, license number and date.publications- An array of objects containing the publications of the profile. Includes details like publication name, description and date.projects- An array of objects containing the project details of the profile. Includes details like the project title, description, start date/month and end date/month.followers- The number of LinkedIn followers the profile has.job_function- The functional area of the profile owner's current role (e.g., Engineering, Marketing, Sales).seniority- The seniority level of the profile owner's current role (e.g., Entry Level, Manager, Vice President).work_status- The current employment status of the profile owner ("open_to_work"ornull).profile_picture_url- The URL of the profile picture of the profile owner.updated_at- The date and time when the profile was last updated. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"  https://api.contactout.com/v1/linkedin/enrich?profile=https://www.linkedin.com/in/example-person"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"url":"https://www.linkedin.com/in/example-person","email":["email1@example.com","email2@gmail.com"],"work_email":["email1@example.com"],"personal_email":["email2@gmail.com"],"phone":["+1234567891"],"github":["github_name"],"twitter":["twitter_username"],"full_name":"Example Person","headline":"Manager, Business Operations & Marketing at OBM","industry":"Broadcast Media","company":{"name":"Legros, Smitham and Kessler","url":"https://www.linkedin.com/company/legros-smitham-and-kessler","linkedin_company_id":12345678,"domain":"legros.com","email_domain":"legros.com","overview":"Legros, Smitham and Kessler is a publicly traded healthcare company specializing in pharmaceuticals, biotechnology, and medical devices. Founded in 2007 and headquartered in the United States, they are committed to advancing medical innovation and improving patient outcomes.","type":"Public Company","size":50,"country":"United States","revenue":6101000,"founded_at":2007,"industry":"Healthcare","headquarter":"535 Kuhic Gardens Apt. 044","website":"http://www.legros.com","logo_url":"https://images.contactout.com/companies/voluptates","specialties":["Healthcare","Medical","Pharmaceuticals","Biotechnology","Medical Devices"],"locations":["426 Lyda Unions, 551, Janniefort, New Hampshire, 56941-1470, Nicaragua","308 Cassandra Harbor Apt. 751, 78817, Darionburgh, Louisiana, 18743, Timor-Leste"]},"location":"Bermuda","languages":[{"name":"English","proficiency":"Full professional proficiency"}],"country":"United States","summary":"An experienced professional with over 19 years in Marketing (digital, print, radio, television), Communications, Content Creation, Copy Writing, Website Maintenance, Social Media Exploitation, Relationship Building, Business Development, Business Operations, Training and Leadership.\\n","experience":[{"start_date":"20204","end_date":"202112","title":"Manager, Business Operations & Marketing","summary":"Established in 1936, OBMI is a global master planning, architecture and design firm, with a rich history of shaping the architectural landscape of Bermuda. Within the firm, I support the OBMI Bermuda office on a multi-faceted level. My commitment to relationship building & client management, together with my passion and proficiency in marketing & communications, allows me to be an integral member of the team. Currently, my mandates include:Marketing\tLead all marketing initiatives for the OBMI Bermuda office\tCreation all print and digital ads for the local market\tCreate, design and execute the quarterly newsletter\tCopy & creative of OBMI Bermuda articles for local and international publication\tManage Google My Business content\tOversee see all aspects of the OBMI Bermuda website\tCapture and analyze various metrics to identify areas of enhancement\tExplore industry trends, best practices and innovative marketing solutions for potential adoptionBusiness Operations\tProject management\tClient relationship management\tVendor & consultant management\tOffice administration\tPrimary point of contact for Bermuda office\tCollaborate with corporate office in Miami on marketing & company-wide initiatives/roll-outs","locality":"Hamilton, Bermuda","company_name":"OBM International","linkedin_url":"https://www.linkedin.com/company/obm-international","start_date_year":2020,"start_date_month":4,"end_date_year":2021,"end_date_month":12,"is_current":false}],"education":[{"field_of_study":"Journalism","description":null,"start_date_year":"2002","end_date_year":"2004","degree":"Journalism","school_name":"George Brown College"}],"skills":["Digital Marketing","Content Creation","Business Development","Project Management","Client Relationship Management"],"certifications":[{"name":"Project Management Professional (PMP)","authority":"Project Management Institute","license":"12345678","start_date_year":2018,"start_date_month":1,"end_date_year":2024,"end_date_month":1}],"publications":[{"url":"https://example.com/publication1","title":"The Future of Digital Marketing","description":"An in-depth analysis of emerging trends in digital marketing and their impact on business growth.","publisher":"Marketing Monthly","authors":["Example Person","Co-Author Name"],"published_on_year":2022,"published_on_month":5,"published_on_day":10}],"projects":[{"title":"Website Redesign Project","description":"Led a team of designers and developers to completely revamp the company's website, resulting in a 40% increase in user engagement.","start_date_year":2019,"start_date_month":6,"end_date_year":2020,"end_date_month":2}],"followers":1000,"job_function":"Design","seniority":"Manager","work_status":"open_to_work","profile_picture_url":"https://images.contactout.com/profiles/ca33f14227b1e5d3a1d53b0b5ca36fc8","updated_at":"2024-01-01 00:00:00"}}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":[]}
```

---

## from email address

Get profile details for a single email address. The match rate is typically higher with a personal email address as they change less frequently.

For work emails, if the domain is from a past employer, the API checks previous work experience to ensure accurate identification.

The above command returns JSON structured like this:

Empty Results

GET https://api.contactout.com/v1/email/enrich?{email=}

Includinginclude=work_emailmay increase the response time as real-time verification happens on the email provided to ensure the quality of data.

Consumes 1 email credit if email is found and 1 phone credit if phone number is found.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| email | string, required | Email Address |
| include | string, optional | Data to be returned. Currently supportwork_email |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | object containing all profile details associated with the email address. Also includes phone number if available.email- The user's personal email address.workEmail- The user's work email address. (if include=work_email in request)workEmailStatus- The status of the work email address, whether it's verified or unverifiedfullName- The full name of the user.headline- The job title or professional headline of the user.industry- The industry in which the user works.linkedinUrl- The LinkedIn profile URL of the user.profilePictureUrl- The profile picture URL of the user.confidenceLevel- Confidence level in the accuracy of the profile information.altMatches- Alternative matches or suggestions related to the user's profile.phone- The user's phone number.twitter- The user's Twitter handle.github- The user's GitHub username.company- An object containing information about the user's current company.name- The name of the user's company.url- The LinkedIn URL of the company.website- The website URL of the company.headquarter- Location of the company's headquarters.locations- An array containing details of the company's locations.location- The current location of the user.summary- A brief summary of the user's professional experience and skills.experience- An array containing details of the user's work experience.education- An array containing details of the user's educational background.skills- An array containing the user's skills and expertise.certifications- An array of objects containing the certifications of the profile. Includes details like certification name, company, authority, license number and date.publications- An array of objects containing the publications of the profile. Includes details like publication name, description and date.projects- An array of objects containing the project details of the profile. Includes details like the project title, description, start date/month and end date/month.followers- The number of LinkedIn followers the profile has.updatedAt- The date and time when the profile was last updated. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/email/enrich?email=0getfisher@gmail.com"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"email":"0getfisher@gmail.com","workEmail":"work-email@obm-international.com","workEmailStatus":"Verified | Unverified","fullName":"Bobbi Singh","headline":"Manager, Business Operations & Marketing at OBM International","industry":"Broadcast Media","linkedinUrl":"https://www.linkedin.com/in/bobbisingh","profilePictureUrl":"https://images.contactout.com/profiles/ca33f14227b1e5d3a1d53b0b5ca36fc8","confidenceLevel":"","altMatches":[],"phone":" +61.438347437","twitter":"","github":"","company":{"name":"OBM International","url":"https://www.linkedin.com/company/obm-international","website":"http://obm.international","linkedin_company_id":12345678,"domain":"obm.international","email_domain":"obm.international","overview":"OBM International is a global master planning, architecture and design firm, with a rich history of shaping the architectural landscape of Bermuda. Founded in 1936 and headquartered in the United States, they are committed to advancing medical innovation and improving patient outcomes.","type":"Public Company","size":50,"country":"United States","revenue":6101000,"founded_at":1936,"industry":"Healthcare","headquarter":"HQ","logo_url":"https://images.contactout.com/companies/voluptates","specialties":["Healthcare","Medical","Pharmaceuticals","Biotechnology","Medical Devices"],"locations":[{"city":"Miami","line1":"123 Business Ave","line2":"Suite 100","state":"Florida","country":"United States","postalCode":"33101","description":"Headquarters"},{"city":"Hamilton","line1":"456 Front Street","line2":"","state":"","country":"Bermuda","postalCode":"HM 12","description":"Regional Office"}]},"location":"Bermuda","languages":[{"name":"English","proficiency":"Full professional proficiency"}],"summary":"An experienced professional with over 19 years in Marketing (digital, print, radio, television), Communications, Content Creation, Copy Writing, Website Maintenance, Social Media Exploitation, Relationship Building, Business Development, Business Operations, Training and Leadership.\\n","experience":[{"start_date":"20204","end_date":"202112","title":"Manager, Business Operations & Marketing","summary":"Established in 1936, OBMI is a global master planning, architecture and design firm, with a rich history of shaping the architectural landscape of Bermuda. Within the firm, I support the OBMI Bermuda office on a multi-faceted level. My commitment to relationship building & client management, together with my passion and proficiency in marketing & communications, allows me to be an integral member of the team. Currently, my mandates include:Marketing\tLead all marketing initiatives for the OBMI Bermuda office\tCreation all print and digital ads for the local market\tCreate, design and execute the quarterly newsletter\tCopy & creative of OBMI Bermuda articles for local and international publication\tManage Google My Business content\tOversee see all aspects of the OBMI Bermuda website\tCapture and analyze various metrics to identify areas of enhancement\tExplore industry trends, best practices and innovative marketing solutions for potential adoptionBusiness Operations\tProject management\tClient relationship management\tVendor & consultant management\tOffice administration\tPrimary point of contact for Bermuda office\tCollaborate with corporate office in Miami on marketing & company-wide initiatives/roll-outs","locality":"Hamilton, Bermuda","company_name":"OBM International","linkedin_url":"https://www.linkedin.com/company/obm-international","start_date_year":2020,"start_date_month":4,"end_date_year":2021,"end_date_month":12,"is_current":false}],"education":[{"field_of_study":"Journalism","description":null,"start_date_year":"2002","end_date_year":"2004","degree":"Journalism","school_name":"George Brown College"}],"skills":["Digital Marketing","Content Creation","Business Development","Project Management","Client Relationship Management"],"certifications":[{"title":"Project Management Professional (PMP)","authority":"Project Management Institute","license":"12345678","start_date_year":2018,"start_date_month":1,"end_date_year":2024,"end_date_month":1}],"publications":[{"url":"https://example.com/publication1","title":"The Future of Digital Marketing","description":"An in-depth analysis of emerging trends in digital marketing and their impact on business growth.","publisher":"Marketing Monthly","authors":["Example Person","Co-Author Name"],"published_on_year":2022,"published_on_month":5,"published_on_day":10}],"projects":[{"title":"Website Redesign Project","description":"Led a team of designers and developers to completely revamp the company's website, resulting in a 40% increase in user engagement.","start_date_year":2019,"start_date_month":6,"end_date_year":2020,"end_date_month":2}],"followers":1000,"jobFunction":"Design","seniority":"Vice President","workStatus":"open_to_work","updatedAt":"2024-01-01 00:00:00"}}
```

**javascript**
```
Copy to Clipboard{"status_code":404,"message":"Not Found"}
```

---

## People Enrich API

Get profile details using a combination of data points such as name, email, phone, LinkedIn URL, company information, education, and location. This endpoint provides flexible enrichment by allowing you to provide multiple identifying parameters to find and enrich a person's profile.

By default, this endpoint returns profile information without contact details. To include contact information such as email addresses and phone numbers, you must specify theincludeparameter with the desired contact types.

The above command returns JSON structured like this:

Empty Results

POST https://api.contactout.com/v1/people/enrich

Primary Parameters:

Name Parameters:

Secondary Parameters(required when using name parameters):

Include Parameters:

Parameter Requirements:To return a match, the API requires:• One primary identifier (linkedin_url,email, orphone)OR• A combination of name (e.g.full_name, orfirst_name+last_name) plus at least one secondary parameter (company,location, oreducation)

Contact Information:By default, this endpoint returns profile data without contact information. To receive email addresses or phone numbers, you must include the appropriate values in theincludeparameter.

Consumes 1 search credit if a profile was found.

Consumes 1 email credit if email is found and 1 phone credit if phone number is found.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| linkedin_url | string, optional | LinkedIn profile URL |
| email | string, optional | Email address |
| phone | string, optional | Phone number |
| Parameter | Type | Description |
| full_name | string, optional | Full name of the person |
| first_name | string, optional | First name (must be used with last_name) |
| last_name | string, optional | Last name (must be used with first_name) |
| Parameter | Type | Description |
| company | array, optional, max:10 | Array of company names |
| company_domain | array, optional, max:10 | Array of company domains |
| education | array, optional, max:10 | Array of educational institutions |
| location | string, optional | Location/city |
| job_title | string, optional | Job title |
|  |  |  |
| Parameter | Type | Description |
| include | array, optional | Data to include:work_email,personal_email,phone |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | Object containing all profile details associated with the provided parameters.email- The user's personal email address.workEmail- The user's work email address (if include=work_email in request).workEmailStatus- The status of the work email address, whether it's verified or unverified.fullName- The full name of the user.headline- The job title or professional headline of the user.industry- The industry in which the user works.linkedinUrl- The LinkedIn profile URL of the user.profilePictureUrl- The profile picture URL of the user.confidenceLevel- Confidence level in the accuracy of the profile information.altMatches- Alternative matches or suggestions related to the user's profile.phone- The user's phone number.twitter- The user's Twitter handle.github- The user's GitHub username.company- An object containing information about the user's current company including name, URL, website, headquarters, locations, and other company details.location- The current location of the user.summary- A brief summary of the user's professional experience and skills.experience- An array containing details of the user's work experience.education- An array containing details of the user's educational background.skills- An array containing the user's skills and expertise.certifications- An array of objects containing the certifications of the profile.publications- An array of objects containing the publications of the profile.projects- An array of objects containing the project details of the profile.followers- The number of LinkedIn followers the profile has.jobFunction- The functional area of the user's current role (e.g., Engineering, Marketing, Sales).seniority- The seniority level of the user's current role (e.g., Entry Level, Manager, Vice President).workStatus- The current employment status of the user ("open_to_work"ornull).updatedAt- The date and time when the profile was last updated. |


### Code Samples
**curl**
```
Copy to Clipboardcurl-XPOST"https://api.contactout.com/v1/people/enrich"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"\--data'{
  "full_name": "Jane Doe",
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@gmail.com",
  "phone": "+14155552671",
  "linkedin_url": "https://linkedin.com/in/janedoe",
  "company": ["paypal", "stripe"],
  "company_domain": "http://stripe.com",
  "job_title": "Product Manager",
  "location": "San Francisco, CA",
  "education": ["University of Melbourne"],
  "include": ["work_email", "personal_email", "phone"]
}'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"url":"https://www.linkedin.com/in/example-person","email":["email1@example.com","email2@gmail.com"],"work_email":["email1@example.com"],"personal_email":["email2@gmail.com"],"phone":["+1234567891"],"github":["github_name"],"twitter":["twitter_username"],"full_name":"Example Person","headline":"Manager, Business Operations & Marketing at OBM","industry":"Broadcast Media","company":{"name":"Legros, Smitham and Kessler","url":"https://www.linkedin.com/company/legros-smitham-and-kessler","linkedin_company_id":12345678,"domain":"legros.com","email_domain":"legros.com","overview":"Legros, Smitham and Kessler is a publicly traded healthcare company specializing in pharmaceuticals, biotechnology, and medical devices. Founded in 2007 and headquartered in the United States, they are committed to advancing medical innovation and improving patient outcomes.","type":"Public Company","size":50,"country":"United States","revenue":6101000,"founded_at":2007,"industry":"Healthcare","headquarter":"535 Kuhic Gardens Apt. 044","website":"http://www.legros.com","logo_url":"https://images.contactout.com/companies/voluptates","specialties":["Healthcare","Medical","Pharmaceuticals","Biotechnology","Medical Devices"],"locations":["426 Lyda Unions, 551, Janniefort, New Hampshire, 56941-1470, Nicaragua","308 Cassandra Harbor Apt. 751, 78817, Darionburgh, Louisiana, 18743, Timor-Leste"]},"location":"Bermuda","languages":[{"name":"English","proficiency":"Full professional proficiency"}],"country":"United States","summary":"An experienced professional with over 19 years in Marketing (digital, print, radio, television), Communications, Content Creation, Copy Writing, Website Maintenance, Social Media Exploitation, Relationship Building, Business Development, Business Operations, Training and Leadership.\\n","experience":[{"start_date":"20204","end_date":"202112","title":"Manager, Business Operations & Marketing","summary":"Established in 1936, OBMI is a global master planning, architecture and design firm, with a rich history of shaping the architectural landscape of Bermuda. Within the firm, I support the OBMI Bermuda office on a multi-faceted level. My commitment to relationship building & client management, together with my passion and proficiency in marketing & communications, allows me to be an integral member of the team. Currently, my mandates include:Marketing\tLead all marketing initiatives for the OBMI Bermuda office\tCreation all print and digital ads for the local market\tCreate, design and execute the quarterly newsletter\tCopy & creative of OBMI Bermuda articles for local and international publication\tManage Google My Business content\tOversee see all aspects of the OBMI Bermuda website\tCapture and analyze various metrics to identify areas of enhancement\tExplore industry trends, best practices and innovative marketing solutions for potential adoptionBusiness Operations\tProject management\tClient relationship management\tVendor & consultant management\tOffice administration\tPrimary point of contact for Bermuda office\tCollaborate with corporate office in Miami on marketing & company-wide initiatives/roll-outs","locality":"Hamilton, Bermuda","company_name":"OBM International","linkedin_url":"https://www.linkedin.com/company/obm-international","start_date_year":2020,"start_date_month":4,"end_date_year":2021,"end_date_month":12,"is_current":false}],"education":[{"field_of_study":"Journalism","description":null,"start_date_year":"2002","end_date_year":"2004","degree":"Journalism","school_name":"George Brown College"}],"skills":["Digital Marketing","Content Creation","Business Development","Project Management","Client Relationship Management"],"certifications":[{"name":"Project Management Professional (PMP)","authority":"Project Management Institute","license":"12345678","start_date_year":2018,"start_date_month":1,"end_date_year":2024,"end_date_month":1}],"publications":[{"url":"https://example.com/publication1","title":"The Future of Digital Marketing","description":"An in-depth analysis of emerging trends in digital marketing and their impact on business growth.","publisher":"Marketing Monthly","authors":["Example Person","Co-Author Name"],"published_on_year":2022,"published_on_month":5,"published_on_day":10}],"projects":[{"title":"Website Redesign Project","description":"Led a team of designers and developers to completely revamp the company's website, resulting in a 40% increase in user engagement.","start_date_year":2019,"start_date_month":6,"end_date_year":2020,"end_date_month":2}],"followers":1000,"job_function":"Design","seniority":"Manager","work_status":"open_to_work","profile_picture_url":"https://images.contactout.com/profiles/ca33f14227b1e5d3a1d53b0b5ca36fc8","updated_at":"2024-01-01 00:00:00"}}
```

**javascript**
```
Copy to Clipboard{"status_code":404,"message":"Not Found"}
```

---

## Contact Info API - Single

---

## from LinkedIn Profile

Get contact details for a single LinkedIn profile. Requesting real-time work_emails viaemail_type=workmay increase the response time. This endpointdoes notprovide real-time verifiedwork_emailby default. If you need it in the response, you must pass the additional argument:email_type.

The API does not support LinkedIn URLs from Sales Navigator or Recruiter because they can vary and change.Common URLs include:https://www.linkedin.com/sales/...https://www.linkedin.com/talent/...

The above command returns JSON structured like this:

Empty Results

GET https://api.contactout.com/v1/people/linkedin?{profile=&include_phone=}

Ifemail_typeis not specified in the request, the response includes both personal and work emails. However, real-time verification is only performed whenemail_type=workis explicitly included, which may yield more work email results but can increase response time.

Consumes 1 email credit if email is found and 1 phone credit if phone number is found (andinclude_phoneis set totrue).

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profile | profile: (string, URL encoded, required) | The fully formed URL of the LinkedIn profile. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| include_phone | boolean, optional, Defaults to false | If set to true, it will include phone information in the response and deduct phone credits. |
| email_type | string, optional | email_type=personal— Returns only personal emailsemail_type=work— Returns only work emailsemail_type=personal,work— Returns both personal and work emailsemail_type=none— Returns no emails and consumes no email creditsBy default, both personal and work emails are returned. |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. |
| profile | object | An object containing contact details for the LinkedIn profile.url- The URL of the LinkedIn profile.email- An array of email addresses associated with the profile.work_email- An array of work email addresses.work_email_status- A dictionary indicating the verification status of work emails.personal_email- An array of personal email addresses.phone- An array of phone numbers associated with the profile.github- An array of GitHub usernames associated with the profile. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/linkedin?profile=https://www.linkedin.com/in/example-person&include_phone=true"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"url":"https://www.linkedin.com/in/example-person","email":["email1@example.com","email2@gmail.com"],"work_email":["email1@example.com"],"work_email_status":{"email1@example.com":"Verified | Unverified"},"personal_email":["email2@gmail.com"],"phone":["phone number 1"],"github":["github_name"]}}
```

**javascript**
```
Copy to Clipboard{"status_code":404,"message":"Not Found"}
```

---

## Contact Info API - Bulk

---

## V1 Bulk ContactInfo

Get contact details for a batch of 30 LinkedIn Profiles per API call

The above command returns JSON structured like this:

If no contact info found

POST https://api.contactout.com/v1/people/linkedin/batch

Consumes 1 email credit per profile if email is found

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profiles | Array, required, max:30 | An array of LinkedIn profile URLs. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profiles | object | An object containing multiple LinkedIn profiles and their associated email addresses. Each profile URL serves as a key in theprofilesobject, and the associated value is an array containing the email addresses associated with that LinkedIn profile. |


### Code Samples
**curl**
```
Copy to Clipboardcurl'https://api.contactout.com/v1/people/linkedin/batch'\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'{
    "profiles": [
        "https://linkedin.com/in/example-person-1",
        "https://linkedin.com/in/example-person-2",
        "https://linkedin.com/in/example-person-3"
    ]
}'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profiles":{"https://linkedin.com/in/example-person-1":["email1@example.com","email2@example.com","email3@example.com"],"https://linkedin.com/in/example-person-2":["email1@domain.com"],"https://linkedin.com/in/example-person-3":["email1@website.com"]}}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profiles":{"https://linkedin.com/in/example-person-1":[],"https://linkedin.com/in/example-person-2":[],"https://linkedin.com/in/example-person-3":[]}}
```

---

## V2 Bulk ContactInfo

Improves upon v1 by incorporating ContactOut's real-time work email finder. If no work email is found in ContactOut's database, the system attempts to guess and verify one in real-time.

This API enables users to retrieve contact details asynchronously through a background job process. Upon initiating the request, ajob_uuidis returned, which can be used to retrieve the resultsThe user can then retrieve the results in 2 ways:Callback URL:If an optionalcallback_urlis provided in the request parameters, we send a POST request to that URL with the results once the job is complete.Direct Request:Users can call the following endpoint at any time using thejob_uuidobtained from the initial request:GET https://api.contactout.com/v2/people/linkedin/batch/{job_uuid}

The above command returns JSON structured like this:

To get the contact information

The above command returns JSON structured like this:

POST https://api.contactout.com/v2/people/linkedin/batch

GET https://api.contactout.com/v2/people/linkedin/batch/{job_uuid}

Consumes 1 email credit per profile if email is foundConsumes 1 phone credit per profile ifinclude_phoneis true and phone number is found

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| callback_url | String, optional | A URL where the results will be posted once the enrichment operation is completed. |
| profiles | Array, required, Max:1000 | An array of LinkedIn profile URLs. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| include_phone | Boolean, optional, default: false | If set to true, phone numbers will be included in the response if available. Requires phone credits. |
| Field | Type | Description |
| uuid | string | The unique identifier for the email lookup request. This uuid can be used to call the endpoint anytime and retrieve resultsGET https://api.contactout.com/v2/people/linkedin/batch/{uuid} |
| status | string | The status of the email lookup request (e.g., "SENT" indicating the request has been sent) |
| result | object | An object containing multiple LinkedIn profiles and their associated contact information.emails- An array of all email addresses associated with the LinkedIn profile.personal_emails- An array of personal email addresses associated with the LinkedIn profile.work_emails- An array of work email addresses associated with the LinkedIn profile.phones- An array of phone numbers associated with the LinkedIn profile (ifinclude_phoneis true). |


### Code Samples
**curl**
```
Copy to Clipboardcurl'https://api.contactout.com/v2/people/linkedin/batch'\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'{
    "callback_url": "https://api.contactout.com/enrich-test-callback-endpoint",
    "profiles": [
        "https://linkedin.com/in/example-person-1",
        "https://linkedin.com/in/example-person-2",
        "https://linkedin.com/in/example-person-3"
    ],
    "include_phone": true
}'
```

**javascript**
```
Copy to Clipboard{"status":"QUEUED","job_id":"96d1c156-fc66-46ef-b053-be6dbb45cf1f"}
```

**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v2/people/linkedin/batch/96d1c156-fc66-46ef-b053-be6dbb45cf1f"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"data":{"uuid":"96d1d610-f163-484e-a433-3006c862c14d","status":"SENT","result":{"https://www.linkedin.com/in/example-person-1":{"emails":["email1@example.com"],"personal_emails":[],"work_emails":["email1@example.com"],"phones":["+1234567890"]},"https://www.linkedin.com/in/example-person-2":{"emails":["email2@example.com","email2@gmail.com"],"personal_emails":["email2@gmail.com"],"work_emails":["email2@example.com"],"phones":[]},"https://www.linkedin.com/in/example-person-3":{"emails":["email3@example.com","email3@gmail.com"],"personal_emails":["email3@gmail.com"],"work_emails":["email3@example.com"],"phones":["+0987654321"]}}}}
```

---

## Company information from domains

Get company information based on given input domains.

The above command returns JSON structured like this:

Empty Results

POST https://api.contactout.com/v1/domain/enrich

Does not consume credits

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| domains | array, required, max:30 | An array of domain names. Each domain should be in a valid format, for ex:example.com |
| Field | Type | Description |
| status_code | integer | HTTP status code indicating the success or failure of the request. |
| companies | object | An object containing information about the company associated with the provided domain.company_domain- The domain name of the company, serving as the key for the company object.li_vanity-LinkedIn vanity URL for the company.name- Name of the company.domain- Domain name of the company.description- Brief description of the company.website- URL of the company's website.logo_url- URL of the company's logo image.type- Type of the company (e.g., Privately Held, Public).headquarter- Headquarters location of the company.country- Country where the company is located.size- Size of the company (e.g., number of employees).founded_at- Year the company was founded.locations- Array containing locations where the company operates.city- City of the location.country- Country of the location.isPrimary- Indicates if this location is the primary one.industry- Industry in which the company operates.specialties- Specialties or areas of expertise of the companyrevenue- Revenue of the company. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/domain/enrich"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'{
    "domains": [
        "test.com"
    ]
}'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"companies":[{"contactout.com":{"li_vanity":"https://www.linkedin.com/company/test","name":"Test","domain":"test.com","description":"This company specializes in innovative software solutions to streamline business operations and enhance productivity.","website":"http://test.com","logo_url":"https://images.contactout.com/companies/328ffa89a83a83042329f8181b7fbfaf","type":"Privately Held","headquarter":"San Francisco, US","country":"United States","size":89,"founded_at":2015,"locations":["San Francisco, US"],"industry":"Computer Software","specialties":[],"revenue":"$5.4M"}}]}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"companies":[]}
```

---

## People Search API

Get profiles matching the search criteria.

The above command returns JSON structured like this:

Whendetailed_experienceordetailed_educationare set totrue, the response returns structured data for their corresponding fields:

No matching profiles

POST https://api.contactout.com/v1/people/search

Few input parameters mentioned in the table above can accept boolean equations as input. Check the "Accepts Boolean" column to know which input fields can accept boolean equations. You can use boolean equations to filter based on a specific criteria.

e.g. If you are looking for profiles who have the skills ReactJS and Python, but not Java, you can format the skills parameter as:{ "skills": ["(ReactJS AND Python) NOT Java"] }. Always add brackets to ensure the boolean logic is applied correctly.

The same logic will apply for the rest of the mentioned paramters.

The supported boolean operators are:

ORANDNOT

Response contains the meta information and the matching list of profiles. Each profile contains the information like title, headline, company details, experience, skills etc. It also lists the contact availability and contact information fields.

For customizing the output fields, use the below command with list of fields to be returned in the output:

The above command returns JSON structured like this:

Consumes 1 search credit for each profile returned.

Consumes 1 email/phone credit for every profile where email/phone info is found, ifreveal_info=trueis specified.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Accepts Boolean |
| name | text | No |
| job_title | array, max:50 | Yes |
| job_function | array, max:50 | No |
| seniority | array, max:50 | No |
| current_titles_only | boolean, default: true | No |
| include_related_job_titles | boolean, default: false | No |
| match_experience | string, default: current | No |
| skills | array, max:50 | Yes |
| education | array, max:50 | Yes |
| location | array, max:50 | No |
| company | array, max:50 | No |
| company_filter | string, default:current | No |
| current_company_only | boolean, default: true | No |
| domain | array, max:50 | No |
| industry | array, max:50 | Yes |
| keyword | text | Yes |
| company_size | array | No |
| years_of_experience | array | No |
| years_in_current_role | array | No |
| page | integer | No |
| data_types | array | No |
| reveal_info | boolean, default: false | No |
| detailed_experience | boolean, default: false | No |
| detailed_education | boolean, default: false | No |
| exclude_companies | array | No |
| exclude_job_titles | array | No |
| Parameter | Type | Description |
| contact_info | array | Returns an array containing contact information including email and phone numbers |
| contact_availability | array | Returns an array determining whether the profile contains the contact information |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/search"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'
  {
    "page": 1,
    "name": "John Smith",
    "job_title": [
      "Vice President",
      "VP Of Product"
    ],
    "exclude_job_titles": [
      "Sales"
    ],
    "current_titles_only": false,
    "include_related_job_titles": false,
    "job_function": ["design"],
    "seniority": ["vice president"],
    "skills": [
      "Network Security",
      "Networking"
    ],
    "education": [
      "Doctorate Degree",
      "Vertapple University"
    ],
    "location": [
      "Sydney, Australia"
    ],
    "company": [
      "ContactOut"
    ],
    "company_filter": "both",
    "exclude_companies": [
      "Google"
    ],
    "match_experience": "current",
    "domain":[
      "https://contactout.com"
    ],
    "industry": [
      "Computer Software",
      "Computer Networking"
    ],
    "keyword": "Computer Networking",
    "company_size": [
      "1_10",
      "11_50"
    ],
    "years_of_experience": [
      "6_10",
      "10"
    ],
    "years_in_current_role": [
      "8_10",
      "10"
    ],
    "current_company_only": false,
    "data_types" : [
      "personal_email",
      "work_email",
      "phone"
    ],
    "reveal_info" : true,
    "detailed_experience": false,
    "detailed_education": false
  }
'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":45},"profiles":{"https://linkedin.com/in/at-JqjtXv":{"li_vanity":"at-JqjtXv","full_name":"Llewellyn Ruecker","title":"Research Assistant","headline":"Research Assistant at Legros, Smitham and Kessler","company":{"name":"Legros, Smitham and Kessler","url":"https://www.linkedin.com/company/legros-smitham-and-kessler","domain":"legros.com","email_domain":"legros.com","overview":"Legros, Smitham and Kessler is a publicly traded healthcare company specializing in pharmaceuticals, biotechnology, and medical devices. Founded in 2007 and headquartered in the United States, they are committed to advancing medical innovation and improving patient outcomes.","type":"Public Company","size":50,"country":"United States","revenue":6101000,"founded_at":2007,"industry":"Healthcare","headquarter":"535 Kuhic Gardens Apt. 044","website":"http://www.legros.com","logo_url":"https://images.contactout.com/companies/voluptates","specialties":["Healthcare","Medical","Pharmaceuticals","Biotechnology","Medical Devices"],"locations":["426 Lyda Unions, 551, Janniefort, New Hampshire, 56941-1470, Nicaragua","308 Cassandra Harbor Apt. 751, 78817, Darionburgh, Louisiana, 18743, Timor-Leste"]},"location":"Faheybury","country":"United States","industry":"Dr. Trenton Hane III","experience":["Research Assistant at Legros, Smitham and Kessler in 2014 - Present"],"education":["Doctorate Degree at Vertapple University in 2017 - 2021"],"skills":["Research","Algorithms","Budget Planning","Storage","Requirements Gathering","Coding"],"summary":"An experienced professional with over 19 years in Marketing (digital, print, radio, television), Communications, Content Creation, Copy Writing, Website Maintenance, Social Media Exploitation, Relationship Building, Business Development, Business Operations, Training and Leadership.","languages":[{"name":"English","proficiency":"Full professional proficiency"}],"certifications":[{"name":"Project Management Professional (PMP)","authority":"Project Management Institute","license":"12345678","start_date_year":2018,"start_date_month":1,"end_date_year":2024,"end_date_month":1}],"publications":[{"url":"https://example.com/publication1","title":"The Future of Digital Marketing","description":"An in-depth analysis of emerging trends in digital marketing and their impact on business growth.","publisher":"Marketing Monthly","authors":["Example Person","Co-Author Name"],"published_on_year":2022,"published_on_month":5,"published_on_day":10}],"projects":[{"title":"Website Redesign Project","description":"Led a team of designers and developers to completely revamp the company's website, resulting in a 40% increase in user engagement.","start_date_year":2019,"start_date_month":6,"end_date_year":2020,"end_date_month":2}],"followers":1000,"updated_at":"2023-03-31 00:00:00","profile_picture_url":"https://images.contactout.com/profiles/ca33f14227b1e5d3a1d53b0b5ca36fc8","job_function":"Design","seniority":"Manager","work_status":"open_to_work","contact_availability":{"personal_email":true,"work_email":true,"phone":true},"contact_info":{"emails":["test@gmail.com","email1@example.com"],"personal_emails":["test@gmail.com"],"work_emails":["email1@example.com"],"work_email_status":{"email1@example.com":"Verified | Unverified"},"phones":["+123456789"]}}}}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":45},"profiles":{"https://linkedin.com/in/at-JqjtXv":{//otherfields..."experience":[{"title":"Research Assistant","summary":"Conducting research on machine learning algorithms and data analysis.","locality":"San Francisco, CA","company_name":"Legros, Smitham and Kessler","start_date_year":2014,"start_date_month":3,"end_date_year":null,"end_date_month":null,"is_current":true,"linkedin_url":"https://www.linkedin.com/company/legros-smitham-and-kessler","logo_url":"https://images.contactout.com/companies/legros-logo.png"}],"education":[{"field_of_study":"Computer Science","description":"Specialized in Machine Learning and Artificial Intelligence","start_date_year":"2017","end_date_year":"2021","degree":"Doctorate Degree","school_name":"Vertapple University","url":"https://www.linkedin.com/school/vertapple-university/"}]}}}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":0},"profiles":[]}
```

**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/search"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'
  {
    "page": 1,
    "name": "John Smith",
    "output_fields" : [
        "title",
        "li_vanity"
    ]
  }
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":0},"profiles":{"https://linkedin.com/in/at-JqjtXv":{"li_vanity":"at-JqjtXv","title":"Research Assistant","contact_availability":{"personal_email":true,"work_email":true,"phone":true},"contact_info":{"emails":[],"personal_emails":[],"work_emails":[],"work_email_status":[],"phones":[]}}}}
```

---

## People Count API

Get the total count of profiles matching the search criteria.

The above command returns JSON structured like this:

POST https://api.contactout.com/v1/people/count

This endpoint accepts the same parameters as thePeople Search API, except forpage,data_types, andreveal_info.

Response contains the total count of profiles matching the search criteria.

Does not consume credits

Only available to paid users

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| status_code | integer | HTTP status code of the response |
| total_results | integer | Total number of profiles matching the search criteria |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/count"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'
  {
    "job_title": [
      "Vice President",
      "VP Of Product"
    ],
    "company": [
      "ContactOut"
    ],
    "location": [
      "Sydney, Australia"
    ]
  }
'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"total_results":100000}
```

---

## Decision Makers API

Get profiles of key decision makers within a specified company.

The above command returns JSON structured like this:

GET https://api.contactout.com/v1/people/decision-makers?{domain=&name=&linkedin_url=&reveal_info=}

This endpoint requiresat least oneof the following three parameters:linkedin_url,domain, orname. The endpoint accepts any combination of these parameters to identify the most relevant company match.

Response contains the meta information and the matching list of profiles. Each profile contains the information like title, headline, company details, experience, skills etc. It also lists the contact availability and contact information fields.

Consumes 1 search credit for each profile returned.

Consumes 1 email/phone credit for every profile where email/phone info is found, ifreveal_info=trueis specified.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| linkedin_url | string, optional | The fully formed URL of the company's LinkedIn profile. URL must begin with http and must contain linkedin.com/company/. Accepts both the numeric or string version of the URL, e.g.https://linkedin.com/company/contactoutorhttps://linkedin.com/company/27090845 |
| domain | string, optional | The domain name of the company's website, e.g. example.com |
| name | string, optional | The name of the company |
| page | integer, optional | Provides results for the given page |
| reveal_info | boolean, default: false | If set to true,contact_infowill contain the emails and phone numbers of the profile and credits will be charged |
| Field | Type | Description |
| contact_info | array | Returns an array containing contact information including email and phone numbers |
| contact_availability | array | Returns an array determining whether the profile contains the contact information |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/decision-makers?reveal_info=true&linkedin_url=https://linkedin.com/company/contactout"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":8},"profiles":{"https://www.linkedin.com/in/rob-liu":{"full_name":"Rob Liu","li_vanity":"robliu","title":"CEO / Founder","headline":"Founder at Contactout","company":{"name":"ContactOut","website":"http://contactout.com","domain":"contactout.com","email_domain":"contactout.com","headquarter":"San Francisco, US","size":96,"revenue":10000,"industry":"Computer Software"},"location":"Singapore","industry":"Computer Software","experience":["CEO / Founder at ContactOut in 2015 - Present","Limited Partner at Blackbird in 2020 - Present","Limited Partner at Hustle Fund in 2021 - Present","Visiting Partner at Iterative in 2023 - Present"],"education":["UNSW in 2008 - 2011"],"skills":["Start-ups","Entrepreneurship","Online Advertising","Social Media Marketing","Digital Marketing","Web Analytics","Digital Media","Project Management","Laravel","Test Driven Development"],"updated_at":"2024-04-03 17:15:14","profile_picture_url":"https://images.contactout.com/profiles/ca33f14227b1e5d3a1d53b0b5ca36fc8","job_function":"Design","seniority":"Manager","contact_availability":{"work_email":true,"personal_email":true,"phone":true},"contact_info":{"emails":["test@gmail.com","email1@example.com"],"personal_emails":["test@gmail.com"],"work_emails":["email1@example.com"],"work_email_status":{"email1@example.com":"Verified"},"phones":["+123456789"]}}}}
```

---

## Company Search API

Get company profiles matching the search criteria.

The above command returns JSON structured like this:

No matching company profiles

POST https://api.contactout.com/v1/company/search

Consumes 1 search credit for each company returned.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Accepts Boolean |
| name | array, max:50 | No |
| domain | array, max:50 | No |
| size | array | No |
| hq_only | boolean | No |
| location | array, max:50 | No |
| industries | array, max:50 | No |
| min_revenue | integer | No |
| max_revenue | integer | No |
| year_founded_from | integer, min:1985 | No |
| year_founded_to | integer, max: current year | No |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| companies | array | Contains company profile details that matched the search.name- Name of the company.url- The LinkedIn URL of the company.domain- Domain name of the company.email_domain- Email domain of the company.overview- Brief description of the company.type- Type of the company (e.g., Privately Held, Public).size- Size of the company (e.g., number of employees).country- Country where the company is located.revenue- Revenue of the companyfounded_at- Year the company was founded.industry- Industry in which the company operates.headquarter- Headquarters location of the company.website- URL of the company's website.location- The location of the company.logo_url- The URL of the company logo.specialties- Specialties or areas of expertise of the company.locations- Array containing locations where the company operates. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/company/search"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'
  {
    "page": 1,
    "name": ["ContactOut"],
    "domain": ["contactout.com"],
    "size": ["1_10"],
    "hq_only": false,
    "location": ["United States"],
    "industry": ["Software"],
    "min_revenue": 1000000,
    "max_revenue": 50000000,
    "year_founded_from": 2000,
    "year_founded_to": 2024
  }
'
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":1},"companies":[{"name":"ContactOut","url":"https://linkedin.com/company/contactout","domain":"contactout.com","email_domain":"contactout.com","overview":"At ContactOut, we pride ourselves on being the most accurate contact data intelligence tool out there. Find emails and phone numbers for 350M professionals, including B2B data for 40M companies.\n\nOur platform is trusted by 1.4M sales, marketing, and recruitment professionals in over 76% of Fortune 500 companies like Google, Microsoft and Netflix.\n\nOur key features are designed with users in mind, so you can easily:\n1) Find quality prospects fast all in one place with our Search Portal\n2) Supercharge your LinkedIn prospecting with our Chrome Extension\n3) Personalize and automate their outbound messaging with our Email Campaign\n\nOur platform is the perfect way to take your business to the next level. With our powerful tools and accurate data, you'll be able to reach more prospects than ever before and see real results.\n\nTry for free today at www.contactout.com","type":"Privately Held","size":96,"country":"United States","revenue":10000000,"founded_at":2015,"industry":"Computer Software","headquarter":"San Francisco, California","website":"http://contactout.com","location":"San Francisco US","logo_url":"https://images.contactout.com/companies/328ffa89a83a83042329f8181b7fbfaf","specialties":["Lead Generation","Recruitment","Computer Software"],"locations":["San Francisco, US"]}]}
```

**javascript**
```
Copy to Clipboard{"status_code":200,"metadata":{"page":1,"page_size":25,"total_results":0},"companies":[]}
```

---

## Email to LinkedIn API

Get LinkedIn profile url for a given email

The above command returns JSON structured like this:

Empty Results

GET https://api.contactout.com/v1/people/person?{email=}

Consumes 1 email credit if profile is found.

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| email | string, required | Email Address |
| Field | Type | Description |
| status_code | integer | HTTP status code indicating the success or failure of the request. |
| profile | object | An object containing basic information about the user's profile.email (string)- Email address associated with the user's profile.linkedin (string)- LinkedIn profile URL of the user. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/person?email=terry@gmail.com"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"email":"terry@gmail.com","linkedin":"https://www.linkedin.com/in/terry"}}
```

**javascript**
```
Copy to Clipboard{"status_code":404,"message":"Not Found"}
```

---

## Contact Checker API

---

## Personal Email Checker

Get personal email availability status for a single Linkedin profile

The above command returns JSON structured like this:

GET https://api.contactout.com/v1/people/linkedin/personal_email_status?{profile=}

Does not consume credits

Only available to paid users

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profile | profile: (string, URL encoded, required) | The fully formed URL of the LinkedIn profile. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | Contains personal email availability status for a single LinkedIn profile.email- returns true if personal email is present |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/linkedin/personal_email_status?profile=https://www.linkedin.com/in/example-person"\--header"authorization: basic"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"email":true}}
```

---

## Work Email Checker

Get work email availability status for a single LinkedIn profile

The above command returns JSON structured like this:

GET https://api.contactout.com/v1/people/linkedin/work_email_status?{profile=}

Does not consume credits

Only available to paid users

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profile | profile: (string, URL encoded, required) | The fully formed URL of the LinkedIn profile. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/. |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | Contains work email availability status for a single LinkedIn profile.email- returns true if work email is presentemail_status- returns whether the email is verified or unverified. |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/linkedin/work_email_status?profile=https://www.linkedin.com/in/example-person"\--header"authorization: basic"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"email":true,"email_status":"Verified | Unverified | null"}}
```

---

## Phone Number Checker

Get phone availability status for a single LinkedIn profile

The above command returns JSON structured like this:

GET https://api.contactout.com/v1/people/linkedin/phone_status?{profile=}

Does not consume credits

Only available to paid users

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| profile | profile: (string, URL encoded, required) | The fully formed URL of the LinkedIn profile. URL must begin withhttpand must containlinkedin.com/in/orlinkedin.com/pub/ |
| Field | Type | Description |
| status_code | integer | The HTTP status code of the response. Indicates the success or failure of the API request. |
| profile | object | Contains phone number availability status for a single LinkedIn profile.phone- returns true if phone number is present |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/people/linkedin/phone_status?profile=https://www.linkedin.com/in/example-person"\--header"authorization: basic"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"profile":{"phone":true}}
```

---

## Email Verifier API

---

## Single

Verify the deliverability of an email address

The above command returns JSON structured like this:

GET https://api.contactout.com/v1/email/verify?{email=}

statusreturns the status of the email address. Below are the possible values

valid: the email address is valid.invalid: the email address is not valid.accept_all: the email address is valid but any email address is accepted by the server.disposable: the email address comes from a disposable email service provider.unknown: we failed to verify the email address.

Consumes 1 “verifier” credit if result is eithervalid,invalidoraccept_all

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| email | string, required | Email Address |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/email/verify?email=foo@bar.com"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"data":{"status":"valid"}}
```

---

## Bulk

Verify the deliverability for a batch of 100 email addresses in bulk.

The above command returns JSON structured like this:

To get the data

The above command returns JSON structured like this:

POST https://api.contactout.com/v1/email/verify/batch

GET https://api.contactout.com/v1/email/verify/batch/{job_uuid}

Consumes 1 “verifier” credit per email if result is eithervalid,invalidoraccept_all

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| callback_url | String, optional | A URL where the results will be posted once the bulk email verification operation is completed. |
| emails | Array, required, Max:1000 | An array of email addresses |
| Field | Type | Description |
| uuid | string | The unique identifier associated with the email verification request. |
| status | string | The status of the email verification process. "DONE": Indicates that the email verification process has been completed. |
| result | object | An object containing the results of the email verification process, indexed by email addresses.Below are the possible values for verification statusvalid- the email address is valid.invalid- the email address is not valid.accept_all- the email address is valid but any email address is accepted by the server.disposable- the email address comes from a disposable email service provider.unknownwe failed to verify the email address. |


### Code Samples
**curl**
```
Copy to Clipboardcurl'https://api.contactout.com/v1/email/verify/batch'\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"--data'{
    "callback_url": "https://api.contactout.com/enrich-test-callback-endpoint",
    "emails": [
        "test1@gmail.com",
        "test2@contactout.com",
        "test3@yahoo.com"
    ]
}'
```

**javascript**
```
Copy to Clipboard{"status":"QUEUED","job_id":"96d1c156-fc66-46ef-b053-be6dbb45cf1f"}
```

**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/email/verify/batch/96d1c156-fc66-46ef-b053-be6dbb45cf1f"\--header"Content-Type: application/json"\--header"Accept: application/json"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"data":{"uuid":"992d8707-aa77-4499-92e4-cf3579c1d384","status":"DONE","result":{"test1@gmail.com":"valid","test2@contactout.com":"accept_all","test3@gmail.com":"invalid"}}}
```

---

## API Usage Stats

Get API stats for the given period.

GET https://api.contactout.com/v1/stats?period=2023-04

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Parameter | Type | Description |
| period | string, YYYY-MM format, defaults to current month | Accepts month in YYYY-MM format, which returns the stats of the given month |


---

## Postpaid

The above command returns JSON structured like this:

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Key | Type | Description |
| count | integer | Successful API requests that used an email credit |
| quota | integer | Allowed email credit usage before either overage is charged or key is disabled until next period |
| remaining | integer | Calculated asquota - count |
| over_quota | integer | Overages on email credit usage(only applicable to some users) |
| phone_count | integer | Successful API requests that used a phone credit |
| phone_quota | integer | Allowed phone credit usage before either overage is charged or key is disabled until next period |
| phone_remaining | integer | Calculated asphone_quota - phone_count |
| phone_over_quota | integer | Overages on phone credit usage (only applicable to some users) |
| search_count | integer | Successful API requests that used a search credit |
| search_quota | integer | Allowed search credit usage before either overage is charged or key is disabled until next period |
| search_remaining | integer | Calculated assearch_quota - search_count |
| search_over_quota | integer | Overages on search credit usage (only applicable to some users) |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/stats?period=2023-04"\--header"authorization: basic"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"period":{"start":"2023-04-01","end":"2023-04-31"},"usage":{"count":100,"quota":200,"remaining":100,"over_quota":0,"phone_count":500,"phone_quota":1000,"phone_remaining":500,"phone_over_quota":0,"search_count":100,"search_quota":200,"search_remaining":100,"search_over_quota":0}}
```

---

## Prepaid

The above command returns JSON structured like this:

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Key | Type | Description |
| count | integer | Successful API requests that used an email credit |
| quota | integer | Prepaid Email credits remaining |
| phone_count | integer | Successful API requests that used a phone credit |
| phone_quota | integer | Prepaid Phone credits remaining |
| search_count | integer | Successful API requests that used a search credit |
| search_quota | integer | Prepaid Search credits remaining |


### Code Samples
**curl**
```
Copy to Clipboardcurl"https://api.contactout.com/v1/stats?period=2023-04"\--header"authorization: basic"\--header"token: <YOUR_API_TOKEN>"
```

**javascript**
```
Copy to Clipboard{"status_code":200,"period":{"start":"2023-04-01","end":"2023-04-31"},"usage":{"count":100,"quota":200,"phone_count":500,"phone_quota":1000,"search_count":100,"search_quota":200}}
```

---

## Errors

ContactOut APIs returns the following error codes:

### Parameters
| Name | Type | Description |
|------|------|-------------|
| Error Code | Message | Message |
| 400 | Bad credentials or invalid headers | Bad credentials or invalid headers |
| 401 | Bad request or invalid input | Bad request or invalid input |
| 403 | You're out of credits, please email your sales manager | You're out of credits, please email your sales manager |
| 403 | No access to endpoint | No access to endpoint |
| 429 | Rate limit reached. Check headerretry-after: <time_in_seconds>for when rate limit will reset | Rate limit reached. Check headerretry-after: <time_in_seconds>for when rate limit will reset |


---

## Frequently Asked Questions

You can view answers for some of the most commonly asked questionshere.

---
