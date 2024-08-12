doc_text_raw = """

Erie Insurance Agents’ Handbook
Requirements Document
Prepared by: Tajmilur Rahman, PhD, Asst. Professor @ Gannon University
December 10th, 2023







Entities
Erie Insurance, Branch, Agency (Primary Agent), Sales Team, Producer, CSR, Account
Project Background
Erie Insurance is the primary entity. It has many branches. Each branch is located in different locations. 
Agency is another entity that works with a branch. Many agencies work with one branch. 
An agency has a primary agent, and many other agents who sell insurance products individually or as a “Sales” team. Within a sales team an agent can be a “Producer”, or a “CSR”. 
An agency is typically identified by the primary agent. Each agent including primary, individual, and agents working within a sales team has an unique ID and they are identified by this ID. 
The unique ID of an agent has the following format: AANNNN 
In this format, A - represents Alphabet, N - represents Number
The first two letters: “AA” represents the state
Agent has the following attributes: 
Agent ID
First Name
Middle Name
Last Name
Preferred Name
Account / Location / Address
Sales Team is a collection of:
Producers (composed of agents)
CSR (composed of agents)
Product is another entity which is sold by the agencies, or individual agents (sales, producers, CSRs) within an agency.
Project Description
Erie Insurance has 18 branches as of today. Each branch organizes their annual board meeting events where they celebrate their performance of the past year and distributes awards to the best performing agents or agencies. Thousands (2200) of agents/agencies (principal agents / executives) may participate in the Annual Board Meeting (ABM) of a branch. Currently the agency's information is shared via pdf or text documents where it takes a lot of manual effort to find out someone in particular in the document.

Erie Insurance needs a mobile application where all the agencies/agents will be accessible by a robust search functionality. The search functionality is the primary feature of this application where a person (agent) can be found by typing any text in the search text-field. 
Besides agent search, Erie Insurance also wants their users of this application to be able to browse and navigate to an event, browse and navigate to an agent manually through branches. 

Figure 1 (a) shows the landing frame of the iOS mobile application where there will be a search bar and two navigator panels i) events, ii) branches. The search bar will be a universal search element throughout the application. Users should be able use the search bar to search for an agent any time while using the app. When users tap on the Events panel, the panel will be expanded listing up all the events. When users tap on the Branches panel, the panel will be expanded listing up all the branches of Erie Insurance. 


		a				  b				     c
Figure 1: a) Landing Frame b) Tap on Events c) Tap on Branches
Project Specifications
Erie Insurance wants an iOS mobile application for V1.0 (MVP) and later on an Android version too.
Agent search is the primary feature of this application.
The search keywords from the search text-field will be looked into the Agent’s Name, Location, Phone Number, Email Address, Description (short bio), and all other information associated with an agent.
All users of the mobile app will have similar access levels and can perform the same functionalities.
Users should be able to browse events or branches from the landing frame. 
Users must login to the app. The Landing Frame in Figure 2 will be launched once the user is successfully logged in.
Each user will have a basic profile page containing a profile picture and other basic details such as affiliation, designation, ID number, location (city, state), fun-fact, hobbies, short bio.
EI Agents’ Handout - Minimum Viable Product (MVP) Requirements
Functional Requirements
Full-text Search: Users would like to type in any fragment of an agent’s name, designation, company, city, description/bio, hobbies, fun-facts, or anything else associated with the user. Search results will appear as a dropdown suggestions list. 
Login: Users must login to the app before he/she can do anything in the app.
If not registered in the app, a link/button will allow users to quickly signup in the app.
Login authentication has to be implemented via two-steps variations technique by sending a text/email to the user.
Once login is successful, the user will be taken to the landing screen (Figure 2 (a)).
Registration: Users must signup before using the app. 
Users can create a user account in the app using his/her Agent ID, email address, and password.
During app signup uploading a profile picture and providing other details is not mandatory. 
Once signup is completed the user will be taken to the login screen. 
Search
Search must be wildcard and full text.
Search results must be linked to user profiles.
Users will be able to type anything in the search text field.
The search keyword will be looked up into the following data in the following order:
First Name
Last Name
Middle Name
Preferred Name
Agency (affiliation)
Designation
Biography or description
Address
Fun-fact
For example: If a keyword typed in is “Thoma” then all agents having their first names starting with “Thoma” will appear first. After that if any agent has their last name starting with “Thoma” will be added in the search result. And so on for middle name, preferred name, agency name, designation, bio, address, and fun-fact. 
Figure 2 (a) shows a search UI mockup.
Profile Page of Agent:
Once a user taps on an agent listed in the search result drop-down list, the user will go to the profile page of the corresponding agent as shown in Figure 3 (b).
Navigate through Events: The landing page contains two panels, i) events and ii) branches. Users can navigate through the events. Once the user taps on the “Event” panel, the user will see the list of different types of events. This is just an expansion of the panel instead of going to a new frame/screen. Similarly, once a user taps on the Branches” panel, users will see the list of branches. 
If a user taps on an event type, for example “Annual Board Meeting”, then the user will be taken to the list of all ABMs sorted by date earliest first. From this screen the user will be able to tap on a particular ABM of a branch. User will then be taken to another screen where the following details will be accessible:
Event Details
Branch Info
Award Info
Reports
Figure 3 shows the event navigation screens.
Navigate through Branches (up to primary agent level): On the other hand, if the user taps on a Branch from the list of branches, for example “Raleigh” then the user will be taken to a screen where details of the Raleigh branch is accessible.
Branches
Agencies
Primary Agent
ID
Account/Location

		a 				     b
Figure 2: a) Agent Search b) User profile navigating from the search result


a			      b				   c

	         d				      e
Figure 3: Event navigation screens starting from a to e.
Non-functional Requirements
Not discussed
Deadlines
UAT & Training: March 1st, 2024
User Acceptance Testing
Data: 
 
V1.0 Release Date: April 10th, 2024
Success Criteria
– MVP v1.0 before April 2024’s (April 11) ABM event.
– At least the following features are completed 
o   Basic search capability – Full-text search
– MVP users are senior leaders
Post-MVP Requirements
Discussed but not confirmed
Mobile App
Connect (may be later)
Social media (may be later)
Gamification (may be later)
Badges
Milestones
Social networking (may be later)
Push notifications (may be later)

Web App / Admin Panel
Features
Users
Data operator
Super user
Use Case
Data Source
 
Server Infrastructure
Database
Web Server
   



"""

expected_requirements = """
    Functional Requirements:
    1. Full-text Search: Users should be able to search for agents by typing any fragment of their name, designation, company, city, description/bio, hobbies, or fun-facts.
    2. Login: Users must login to the app before accessing any features. Login authentication should be implemented using two-step verification.
    3. Registration: Users must sign up before using the app. They can create an account using their Agent ID, email address, and password.
    4. Search: The search functionality should be wildcard and full-text. The search results should be linked to user profiles. Users should be able to search by typing anything in the search text field.
    5. Profile Page of Agent: When a user taps on an agent in the search results, they should be taken to the profile page of that agent.
    6. Navigate through Events: Users should be able to navigate through different types of events. Tapping on an event should display the details of that event.
    7. Navigate through Branches: Users should be able to navigate through different branches. Tapping on a branch should display the details of that branch, including the primary agent and account/location information.
    """

expected_epics = """"{
  "Epics": [
    {
      "User Story": "Users must register to use the app, creating an account with their Agent ID, email address, and password.",
      "Deliverables": {
        "architecture_design": "Design of the user registration module including data flow and interaction with the database.",
        "database_schema_design": "Schema for storing user credentials and profile information securely.",
        "unit_tests": "Tests to ensure user registration handles data correctly and rejects invalid inputs."
      }
    },
    {
      "User Story": "Users must log in with two-step verification before accessing any features.",
      "Deliverables": {
        "architecture_design": "Design of the login process incorporating two-step verification.",
        "unit_tests": "Tests to verify the two-step verification process and login integrity.",
        "user_training_documentation": "Documentation on how users should perform two-step verification during login."
      }
    },
    {
      "User Story": "Users should be able to perform a full-text search by typing any fragment of an agent's name, designation, company, city, description/bio, hobbies, or fun-facts.",
      "Deliverables": {
        "architecture_design": "Design of the search functionality including indexing and query processing.",
        "database_schema_design": "Schema design for efficient storage and retrieval of searchable text attributes.",
        "unit_tests": "Tests to ensure search functionality returns accurate and complete results."
      }
    },
    {
      "User Story": "Search results should be linked to the agent's profile page.",
      "Deliverables": {
        "architecture_design": "Design to ensure search results correctly link to the respective agent's profile page.",
        "unit_tests": "Tests to verify that clicking on search results navigates to the correct agent profile."
      }
    },
    {
      "User Story": "When an agent is selected from the search results, users should be directed to that agent's detailed profile page.",
      "Deliverables": {
        "architecture_design": "Design of the profile access flow from search results.",
        "unit_tests": "Tests to ensure the profile page is accessible and displays correct information from search results."
      }
    },
    {
      "User Story": "Users should be able to navigate and view details of various events and branches.",
      "Deliverables": {
        "architecture_design": "Design of the navigation system for accessing event and branch details.",
        "database_schema_design": "Schema to store and retrieve event and branch details.",
        "unit_tests": "Tests to ensure navigation and data retrieval functions correctly."
      }
    },
    {
      "User Story": "Tapping on an event or branch should display detailed information, including associated agents and location/account details where applicable.",
      "Deliverables": {
        "architecture_design": "Design of detailed information display for events and branches.",
        "unit_tests": "Tests to ensure detailed information is correctly displayed upon user interaction."
      }
    }
  ]
}
"""

expected_tests ="""
{
  "test_cases": [
    {
      "requirement": "User Authentication",
      "test_cases": [
        {
          "description": "Verify that a new user can register with a valid Agent ID, email address, and password.",
          "steps": ["Navigate to the registration page", "Enter valid Agent ID, email, and password", "Submit the registration form"],
          "expected_result": "User is registered and a confirmation message is displayed."
        },
        {
          "description": "Verify that the registration fails with an invalid email format.",
          "steps": ["Navigate to the registration page", "Enter valid Agent ID, invalid email, and password", "Submit the registration form"],
          "expected_result": "Error message is displayed indicating the email format is incorrect."
        },
        {
          "description": "Verify that users can log in with valid credentials and two-step verification.",
          "steps": ["Navigate to the login page", "Enter valid email and password", "Complete the two-step verification process"],
          "expected_result": "User is logged in and directed to the app's main page."
        },
        {
          "description": "Verify that login fails with incorrect password.",
          "steps": ["Navigate to the login page", "Enter valid email and incorrect password", "Attempt to log in"],
          "expected_result": "Error message is displayed indicating the login attempt was unsuccessful."
        }
      ]
    },
    {
      "requirement": "Search Functionality",
      "test_cases": [
        {
          "description": "Verify that users can perform a full-text search by agent name.",
          "steps": ["Navigate to the search page", "Enter an agent's name in the search bar", "Submit the search query"],
          "expected_result": "Search results display profiles matching the agent's name."
        },
        {
          "description": "Verify that wildcard search works for partial agent names.",
          "steps": ["Navigate to the search page", "Enter a partial name with wildcard character", "Submit the search query"],
          "expected_result": "Search results display profiles matching the partial name."
        },
        {
          "description": "Verify that clicking on a search result navigates to the agent's profile page.",
          "steps": ["Perform any search", "Click on one of the search results"],
          "expected_result": "User is redirected to the selected agent's profile page."
        }
      ]
    },
    {
      "requirement": "Agent Profile Access",
      "test_cases": [
        {
          "description": "Verify that users can view all details on an agent's profile.",
          "steps": ["Search and select an agent", "Navigate to the agent's profile page"],
          "expected_result": "All details including contact, events, and branches are displayed on the profile page."
        }
      ]
    },
    {
      "requirement": "Event Navigation",
      "test_cases": [
        {
          "description": "Verify that users can browse through various events.",
          "steps": ["Navigate to the events section", "Browse through the list of events"],
          "expected_result": "All available events are displayed in a list."
        },
        {
          "description": "Verify that detailed information about each event is accessible.",
          "steps": ["Navigate to the events section", "Select an event"],
          "expected_result": "Detailed information about the event is displayed, including related agents and branches."
        }
      ]
    },
    {
      "requirement": "Branch Navigation",
      "test_cases": [
        {
          "description": "Verify that users can explore different branches.",
          "steps": ["Navigate to the branches section", "Browse through the list of branches"],
          "expected_result": "All available branches are displayed in a list."
        },
        {
          "description": "Verify that specific details about each branch are accessible.",
          "steps": ["Navigate to the branches section", "Select a branch"],
          "expected_result": "Details about the branch including primary agent contact and location information are displayed."
        }
      ]
    }
  ]
}
"""
