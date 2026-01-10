# Firmable API Documentation

> **Generated via Copy-Button Detection**
---

## Firmable home page

Overview
Welcome

Firmable API is your gateway to Australia and NZ’s #1 sales intelligence platform.

Firmable combines Australia and New Zealand’s B2B database with over 10 million contacts at 1.5 million companies with rich buying signals and AI agents. Firmable gives you instant access to Australian and Kiwi decision makers.
New to Firmable?
⌘I
x
linkedin
Powered by

---

## API Reference

Overview
Welcome

Firmable API is your gateway to Australia and NZ’s #1 sales intelligence platform.

Firmable combines Australia and New Zealand’s B2B database with over 10 million contacts at 1.5 million companies with rich buying signals and AI agents. Firmable gives you instant access to Australian and Kiwi decision makers.
New to Firmable?
⌘I
x
linkedin
Powered by

---

## New to Firmable?

Overview
New to Firmable?
Firmable’s AI powered sales intelligence platform gives you:
Access to over 1.5 million Australian and New Zealand B2B companies and over 10 million people.
Accurate and detailed profiles with localised information, including ABNs/ NZBNs, industry segments, tech stacks, and more.
Extensive mobile and email coverage.
Dedicated local support in your time zone.
Welcome
Creating API keys
⌘I
x
linkedin
Powered by

---

## Creating API keys

Overview
Creating API keys

General information about Firmable API

Create your Firmable API key
Once you have created your API key, you can view, copy and delete and recreate a new key. You will pass this key to authenticate your requests to the Firmable API.
New to Firmable?
Authentication
⌘I
x
linkedin
Powered by

---

## Authentication

Overview
Authentication

How to authenticate your requests to Firmable’s API

​
Bearer Token
When requesting resources, you will need your Firmable key — you will find it in the Dashboard. Here’s how to add the key to the request header using cURL:
Copy
curl https://api.firmable.com/company/... \
  -H "Authorization: Bearer fbl_xxx"

Always keep your root safe and reset it if you suspect it has been compromised.
Creating API keys
HTTP Methods
⌘I
x
linkedin
Powered by

#### 💻 Code Samples
**Block 1 (bash)**
```bash
curl https://api.firmable.com/company/... \
  -H "Authorization: Bearer fbl_xxx"

```

---

## HTTP Methods

Overview
HTTP Methods

General information about Firmable API

​
GET
GET methods are used for reading data. Filtering, sorting, or pagination is done via query parameters.
Copy
curl "https://api.firmable.com/company?ln_slug=company_slug" \
  -H "Authorization: Bearer <FIRMABLE_API_KEY>"

Authentication
Rate Limits
⌘I
x
linkedin
Powered by

#### 💻 Code Samples
**Block 1 (bash)**
```bash
curl "https://api.firmable.com/company?ln_slug=company_slug" \
  -H "Authorization: Bearer <FIRMABLE_API_KEY>"

```

---

## Rate Limits

Overview
Rate Limits

Rate limits for Firmable API

50 requests per second per API key.
HTTP Methods
Company Enrichment
⌘I
x
linkedin
Powered by

---

## GET
Company Enrichment

Enrichment APIs
Company Enrichment

Returns company information

GET
/
company
Try it
Authorizations
​
Authorization
stringheaderrequired

Bearer authentication header of the form Bearer <token>, where <token> is your auth token.

Query Parameters
​
id
string

The Firmable ID of the company (example: f000000117274)

​
ln_slug
string

The LinkedIn slug of the company (example: smec)

​
ln_url
string

LinkedIn URL of the company (example: https://www.linkedin.com/company/smec/)

​
fqdn
string

FQDN of the company (example: smec.com)

​
abn
string

ABN of the company (example: 47065475149)

​
website
string

Website of the company (example: https://www.smec.com)

Response
200
application/json

Company response

​
id
string

The Firmable ID of the company.

Example:

"f0000067890"

​
name
string

The name of the company.

Example:

"The name of the company."

​
website
string

The company's website URL.

Example:

"https://www.example.com"

​
fqdn
string

The fully qualified domain name of the company's website.

Example:

"firmable.com"

​
description
string

A detailed description of the company.

Example:

"CommBank offers personal banking, business solutions, institutional banking, company information, and more"

​
tagline
string

A brief tagline or slogan for the company.

Example:

"We are a team of 1000 people"

​
linkedin
string

The company's LinkedIn handle.

Example:

"commbank"

​
au_employee_count
integer | null

The number of employees in Australia.

Example:

1000

​
year_founded
integer

The year the company was founded.

Example:

2000

​
hq_location
string | null

The headquarters location of the company.

Example:

"Wallan"

​
hq_country
string

The country of the company's headquarters.

Example:

"Australia"

​
company_size
string

The size category of the company.

Example:

"1000+"

​
company_type
string

The type of company (e.g., Private, Public).

Example:

"Public company"

​
abn_operation_status
string

The operational status of the company's ABN.

Example:

"active"

​
locations
string[]

The locations associated with the company.

Example:
["Sydney", "Melbourne"]
​
industries
string[]

The industries associated with the company.

Example:
["Finance", "Tech"]
​
revenue
string

The company's revenue, if available.

Example:

">$1B+"

​
phones
string[]

List of phone numbers associated with the company.

Example:
["0450 600 0000"]
​
emails
string[]

List of email addresses associated with the company.

Example:
["email@example.com"]
​
social_media
object

Social media profiles of the company.

Show child attributes

​
industry_codes
object

Various industry classification codes for the company.

Show child attributes

​
keywords
string[]

Keywords associated with the company.

Example:
["Finance", "Tech"]
​
org_registers
object

Information about organizational registers.

Example:
{ "vc": "VCs & Investors" }
​
states
string[]

Additional state information about the company.

Example:
["NSW", "VIC"]
​
nextGen
object

Next-generation data about the company.

Show child attributes

Rate Limits
People Enrichment
⌘I
x
linkedin
Powered by

#### 💻 Code Samples
**Block 1 (default)**
```default
curl --request GET \
  --url https://api.firmable.com/company \
  --header 'Authorization: Bearer <token>'
```

**Block 2 (default)**
```default
{
  "id": "f0000067890",
  "name": "The name of the company.",
  "website": "https://www.example.com",
  "fqdn": "firmable.com",
  "description": "CommBank offers personal banking, business solutions, institutional banking, company information, and more",
  "tagline": "We are a team of 1000 people",
  "linkedin": "commbank",
  "au_employee_count": 1000,
  "year_founded": 2000,
  "hq_location": "Wallan",
  "hq_country": "Australia",
  "company_size": "1000+",
  "company_type": "Public company",
  "abn_operation_status": "active",
  "locations": [
    "Sydney",
    "Melbourne"
  ],
  "industries": [
    "Finance",
    "Tech"
  ],
  "revenue": ">$1B+",
  "phones": [
    "0450 600 0000"
  ],
  "emails": [
    "email@example.com"
  ],
  "social_media": {
    "twitter": "username",
    "youtube": "username",
    "facebook": "username",
    "linkedin": "username",
    "instagram": "username"
  },
  "industry_codes": {
    "abn": "1234567890",
    "acn": "1234567890",
    "sic": "1234567890",
    "duns": "1234567890",
    "naics": "1234567890",
    "anzsic": "1234567890"
  },
  "keywords": [
    "Finance",
    "Tech"
  ],
  "org_registers": {
    "vc": "VCs & Investors"
  },
  "states": [
    "NSW",
    "VIC"
  ],
  "nextGen": {
    "technographics": {
      "Software Development": [
        "PostgreSQL",
        "Java"
      ],
      "Finance & Accounting": [
        "Visa",
        "Pace"
      ]
    },
    "website": "https://www.example.com",
    "social_media": {
      "youtube": {
        "profile_name": "profile_name",
        "handle": "handle",
        "followers": 100,
        "verified": true,
        "videos": 100,
        "likes": 100,
        "views": 100,
        "subscribers": 100,
        "following": 100,
        "joined": "2021-01-01"
      },
      "instagram": {
        "profile_name": "profile_name",
        "handle": "handle",
        "followers": 100,
        "verified": true,
        "videos": 100,
        "likes": 100,
        "views": 100,
        "subscribers": 100,
        "following": 100,
        "joined": "2021-01-01"
      },
      "linkedin": {
        "profile_name": "profile_name",
        "handle": "handle",
        "followers": 100,
        "verified": true,
        "videos": 100,
        "likes": 100,
        "views": 100,
        "subscribers": 100,
        "following": 100,
        "joined": "2021-01-01"
      },
      "facebook": {
        "profile_name": "profile_name",
        "handle": "handle",
        "followers": 100,
        "verified": true,
        "videos": 100,
        "likes": 100,
        "views": 100,
        "subscribers": 100,
        "following": 100,
        "joined": "2021-01-01"
      }
    },
    "reviews_rating": {
      "ceo_approval": "4.5",
      "total_reviews": 100,
      "rating": {
        "ceo_approval_rating": "4.5",
        "career_opportunities_rating": "4.5",
        "compensation_and_benefits_rating": "4.5",
        "culture_and_values_rating": "4.5",
        "diversity_and_inclusion_rating": "4.5",
        "senior_management_rating": "4.5",
        "work_life_balance_rating": "4.5"
      },
      "overall_rating": "4.5",
      "employee_rating_id": "fp000000067890",
      "recommend_to_friend": 232,
      "url": 4.5
    },
    "id": "f0000067890",
    "web_traffic": {
      "summary": {
        "avg_visit_duration": "<string>",
        "total_web_visitors": 123,
        "bounce_rate": 123,
        "pages_per_visit": 123
      },
      "traffic_share": {
        "countries": {},
        "organic": 123,
        "paid": 123
      },
      "marketing_channels_distribution": {
        "Direct": 123,
        "Referrals": 123,
        "Search": 123,
        "Social": 123,
        "Mail": 123
      }
    }
  }
}
```

**Block 3 (default)**
```default
["Sydney", "Melbourne"]
```

**Block 4 (default)**
```default
["Finance", "Tech"]
```

**Block 5 (default)**
```default
["0450 600 0000"]
```

**Block 6 (default)**
```default
["email@example.com"]
```

**Block 7 (default)**
```default
{ "vc": "VCs & Investors" }
```

**Block 8 (default)**
```default
["NSW", "VIC"]
```

---

## GET
People Enrichment

Enrichment APIs
People Enrichment

Returns people information

GET
/
people
Try it
Authorizations
​
Authorization
stringheaderrequired

Bearer authentication header of the form Bearer <token>, where <token> is your auth token.

Query Parameters
​
id
string

The unique identifier for a person in the Firmable system. (example: fp000000067890)

​
ln_slug
string

The LinkedIn slug of the person. (example: chathchw)

​
ln_url
string

The full LinkedIn URL of the person (example: https://www.linkedin.com/in/chathchw/)

​
work_email
string

Work email of the person (example: ******@firmable.com)

​
personal_email
string

Personal email of the person (example: ******@gmail.com)

Response
200
application/json

People response

​
id
string

The Firmable ID of the person.

Example:

"fp000000067890"

​
name
string

The full name of the person.

Example:

"John Doe"

​
first_name
string

The first name of the person.

Example:

"John"

​
last_name
string

The last name of the person.

Example:

"Doe"

​
middle_name
string | null

The person's middle name (if available).

Example:

"M"

​
headline
string

A brief professional headline.

Example:

"Unlimited C-Suite Partner"

​
description
string | null

A detailed description of the person.

Example:

"I am a finance manager at a bank"

​
position
string | null

The person's current job position.

Example:

"Chief Marketing Officer"

​
current_company
object

Details about the person's current company.

Show child attributes

​
time_in_current_role
string

Duration in the current role.

Example:

"Jan '23 - Present"

​
month_joined
number

The month when the person joined their current role.

Example:

2

​
year_joined
integer | null

The year when the person joined their current role.

Example:

2002

​
emails
object

Show child attributes

​
phones
object[]

List of phone numbers with additional details.

Show child attributes

​
linkedin
string

LinkedIn profile handle.

Example:

"https://www.linkedin.com/in/person_slug"

​
social_media
object

Social media profiles and statistics.

Show child attributes

​
location
string[]

The person's location information.

Example:
["Sydney", "Melbourne"]
​
department
string

The person's department information.

Example:

"Marketing"

​
seniority
string

Information about the person's seniority level.

Example:

"C-Suite / Partner"

​
gender
string

Information about the person's gender.

Example:

"Female"

​
skills
string[] | null

List of professional skills.

Example:
["Finance", "Tech"]
​
education
object

List of educational qualifications.

Show child attributes

​
keywords
string[] | null

Keywords associated with the person (if available).

Example:
["Finance", "Tech"]
​
secondary_position
object[] | null

Show child attributes

Company Enrichment
People Search
⌘I
x
linkedin
Powered by

#### 💻 Code Samples
**Block 1 (default)**
```default
curl --request GET \
  --url https://api.firmable.com/people \
  --header 'Authorization: Bearer <token>'
```

**Block 2 (default)**
```default
{
  "id": "fp000000067890",
  "name": "John Doe",
  "first_name": "John",
  "last_name": "Doe",
  "middle_name": "M",
  "headline": "Unlimited C-Suite Partner",
  "description": "I am a finance manager at a bank",
  "position": "Chief Marketing Officer",
  "current_company": {
    "id": "f0000067890",
    "name": "Company Name",
    "size": "11 - 50",
    "website": "https://www.example.com",
    "industry": [
      "Finance",
      "Tech"
    ],
    "linkedin": "person_slug",
    "main_phones": [
      "0450 600 0000"
    ],
    "other_phones": [
      "0450 600 0000"
    ],
    "mobile_phones": [
      "0450 600 0000"
    ]
  },
  "time_in_current_role": "Jan '23 - Present",
  "month_joined": 2,
  "year_joined": 2002,
  "emails": {
    "personal": [
      {
        "value": "email@gmail.com",
        "deliverability": "Deliverable"
      }
    ],
    "work": [
      {
        "value": "email@gmail.com",
        "deliverability": "Deliverable"
      }
    ]
  },
  "phones": [
    {
      "value": "0450 600 0000",
      "is_dnd": false
    }
  ],
  "linkedin": "https://www.linkedin.com/in/person_slug",
  "social_media": {
    "linkedin": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    },
    "github": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    },
    "twitter": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    },
    "facebook": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    },
    "youtube": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    },
    "pintrest": {
      "handle": 100,
      "connections": "username",
      "followers": 100,
      "stars": 100
    }
  },
  "location": [
    "Sydney",
    "Melbourne"
  ],
  "department": "Marketing",
  "seniority": "C-Suite / Partner",
  "gender": "Female",
  "skills": [
    "Finance",
    "Tech"
  ],
  "education": {
    "field": "Computer Science",
    "degree": "University of Sydney",
    "date_range": "University of Sydney",
    "school_name": "University of Sydney"
  },
  "keywords": [
    "Finance",
    "Tech"
  ],
  "secondary_position": [
    {
      "company_id": "f000000120808",
      "company_name": "Firmable",
      "company_size": "1 - 100",
      "company_website": "https://firmable.com",
      "company_linkedin": "company-slug",
      "company_industry": "Financial Services",
      "cleaned_position": "Marketing Principal",
      "month_joined": 11,
      "year_joined": "2022",
      "time_in_current_role": "Nov '22 - Present",
      "seniority": "Other",
      "department": "Marketing"
    }
  ]
}
```

**Block 3 (default)**
```default
["Sydney", "Melbourne"]
```

**Block 4 (default)**
```default
["Finance", "Tech"]
```

---

## POST
People Search

Enrichment APIs
People Search

Search for people by id, company id, position, seniority, and department

POST
/
people
/
search
Try it
​
Description
Search for people by company id, position, seniority, and department.
Please pass ids for seniority and department as listed below.
​
Acceptable seniority and department ids
​
Seniority:
1: Board Member / Company Director
2: Owner / Founder
3: C-Suite / Partner
4: VP/Director / Head of
5: Manager
6: Other
7: No Data Available
​
Department:
1: General Management
2: Sales
3: Trades
4: Operations
5: Engineering & Technical
6: Human Resources
7: Customer Service
8: Medicine & Healthcare
9: Research & Analysis
10: Legal
11: Marketing
12: Education & Training
13: Consulting
14: Finance
15: Product
16: Other
17: No Data Available
Authorizations
​
Authorization
stringheaderrequired

Bearer authentication header of the form Bearer <token>, where <token> is your auth token.

Query Parameters
​
selectedCountry
string

The country to search against. (example: AU)

​
companyId
string

The unique identifier for a company in the Firmable system. (example: f000000117274)

​
position
string

The position of the person. (example: Software Engineer)

​
seniority
string

The seniority of the person. (example: Senior)

​
department
string

The department of the person. (example: Engineering)

​
from
string

The offset to start the search from. (example: 0)

​
size
string

The size of the search results. (example: 10)

Response
200
application/json

People search response

​
person_id
string

The Firmable ID of the person.

Example:

"f000000117274"

​
position
string

The position of the person.

Example:

"Software Engineer"

​
company_name
string

The name of the company the person works for.

Example:

"Senior"

​
linkedin
string

LinkedIn profile handle.

Example:

"person_slug"

​
has_email
boolean

Whether the person has an email address.

Example:

true

​
has_personal_email
boolean

Whether the person has a personal email address.

Example:

true

​
has_phone
boolean

Whether the person has a phone number.

Example:

true

​
has_dnd_phone
boolean

Whether the person number is a DND number.

Example:

true

​
has_mobile
boolean

Whether the person has a mobile number.

Example:

true

People Enrichment
⌘I
x
linkedin
Powered by

#### 💻 Code Samples
**Block 1 (default)**
```default
curl --request POST \
  --url https://api.firmable.com/people/search \
  --header 'Authorization: Bearer <token>'
```

**Block 2 (default)**
```default
[
  {
    "person_id": "f000000117274",
    "position": "Software Engineer",
    "company_name": "Senior",
    "linkedin": "person_slug",
    "has_email": true,
    "has_personal_email": true,
    "has_phone": true,
    "has_dnd_phone": true,
    "has_mobile": true
  }
]
```

---
