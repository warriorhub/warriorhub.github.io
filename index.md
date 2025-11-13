# WarriorHub: UH Mānoa Event Scheduler

## Table of contents

* [Overview](#overview)
* [Team](#team)
* [Our Github](#our-github)
* [Deployment](#deployment)
* [User Guide](#user-guide)
* [Developer Guide](#developer-guide)
* [Community Feedback](#community-feedback)
* [Development History](#development-history)
* [Continuous Integration](#continuous-integration)
* [Example enhancements](#example-enhancements)

## Overview

WarriorHub is a web application that will provide UH Mānoa students to browse on-campus events all in one place. With WarriorHub, students will no longer have to search across multiple websites and calenders to find events that interests them. Now students may experience the campus life to the fullest and stay informed about activities that they enjoy. Users will be able to browse, search, and filter events that are most relevant to them. The web application will allow three types of users: students, admins, and organizers.

* Students can browse and RSVP for events
* Organizers can create and manage events
* Admins will validate new events, manage event quality, and organizer accounts

WarriorHub will illustrate a variety of technologies useful to ICS software engineering students that include and not limited to:

* React
* React Bootstrap
* Nextjs
* HTML and CSS

---

### The Problem

Currently, UH Mānoa has several different event calendars with varying functionality, which are all disconnected from each other.  
For instance, Hamilton Library has its own calendar with events such as trivia night and board game night; however, these events are not advertised on the [UH Mānoa Events Calendar](https://www.hawaii.edu/calendar/manoa/2025/11/5).  

Moreover, events cannot be filtered by category, often leaving users with inefficient visualizations. This results in students having to check multiple sites to find relevant events, which leads to lower attendance.

---

### The Solution

We will implement a mass event scheduler. This will allow various organizations to input their events on a singular website, allowing for efficiency and ease of use.  

---

## Team

WarriorHub is designed, implemented, and maintained by:

* Sakura Takahashi (<sakuraet@hawaii.edu>)
* Jiayi Lu (<liujiayi@hawaii.edu>)
* Kacy Kuniyoshi (<kacykuni@hawaii.edu>)
* Jordan Wong (<jordanww@hawaii.edu>)
* Alicia Luck (<luckmana@hawaii.edu>)

---

### Team Contract

Our team's code of conduct can be found in the [Team Contract](https://docs.google.com/document/d/1tgecXyrKeLgYMAdy3Xhf0NZaTgcaG1QSbqhRyxEmIIQ/edit?usp=sharing)

---

## Our GitHub

- View our organization on GitHub [here](https://github.com/warriorhub)
- View our WarriorHub application src code on Github [here](https://github.com/warriorhub/warriorhub)
- View our github.io home page [here](https://warriorhub.github.io/)

---

## Deployment

Our running application is [here](https://github.com/warriorhub/warriorhub). It is currently not working.

## User Guide

This section provides a walkthrough of the WarriorHub user interface and its capabilities.

---

### Approach

This app will create an organized platform to present UH Mānoa–specific events in a unified student interface, with three role options.  

The app will include three roles:

1. **Users:** Students log in with their UH email, set event and location preferences, and view customized recommendations.  
2. **Organizers:** Event planners can upload and manage events related to their department, hall, or organization.  
3. **Admins:** Oversee organizer accounts, approve or edit events, and ensure quality control.  

Organizers will manage all event details such as:

* Time
* Location
* Topic
* RSVP options

Users will be able to include their preferences, like their favorite event and their specific residence hall. This will allow the app to show more content relevant to them and give accurate recommendations.

---

### Use Cases

#### Users Searching for Events

1. User signs up with UH credentials.
2. Navigates to the Calendar page.
3. Selects interests and receives recommended events; irrelevant events are hidden.
4. Toggles filters (event type, size, location).
5. Views RSVP or interest indicators for signed-in users.
6. RSVPs to events and receives reminder notifications.

#### User Hosting an Event

1. User logs in with Organizer credentials.
2. Navigates to Create an Event page.
3. Fills in event details:
   * Date, time, and location
   * Category and summary
   * Flyers or website links
   * Sponsor and ticketing information
4. Optionally provides an external calendar link to import events.

#### Admin Editing the Page

1. Logs in with Admin credentials.
2. Visits the page with admin-only edit tools visible.
3. Documents and implements approved edits or changes.

---

### Landing Page Mockup

Anyone visiting the site should have access to the landing page. It should show the application name on the top right, navbar on the top, filters to search for events in the header, and two carousels showing images of upcoming events. The landing page is presented to users when they visit the top-level URL to the site.
<p align="center">
  <img src="images/LandingPageMockup.png" alt="WarriorHub Welcome Page" width="100%">
</p>

---

### Sign In and Sign Up Page Mockup

Click on the “Login” button in the upper right corner of the navbar, then select “Sign in” to go to the following page and login.

Alternatively, you can select “Sign up” to go to the following page and register as a new user.

<p align="center">
  <img src="images/sign_in_page.png" alt="Sign In / Sign Up Page" width="100%">
</p>

---

### Event Search Page Mockup

Anyone visiting the site can also search through the events in the database through the search page. They have the option of searching by category or location location, or by typing in search terms.

<p align="center">
  <img src="images/search_page_mockup.png" alt="Event Search Page" width="100%">
</p>

---

### User Home Page Mockup

When a user signs up or logs in, they can click on the “MyEvents” link in the navbar and be taken to a list of events they have signed up for notifications for. This includes upcoming events as well as past events.

---

### Admin Home Page Mockup

When an admin signs up or logs in, they can click on the “MyEvents” link in the navbar and be taken to a list of all events.
They can then have permission to add/delete/edit the event via the [Add / Delete / Edit Event Page](#Add/Delete/Edit-Event-Page-Mockup).

---

### Organizer Home Page Mockup

When an organizer signs up or logs in, they can click on the “MyEvents” link in the navbar and be taken to a list of all events they have created.
They can then have permission to add/delete/edit their events via the [Add / Delete / Edit Event Page](#Add/Delete/Edit-Event-Page-Mockup).

---

### Add / Delete / Edit Event Page Mockup

Once you are logged in, you can define new projects with the Edit Project page:

1. **Users:** Can add/delete/edit their own archieved events in their "My Events" page.
2. **Organizers:** Can upload and manage events related to their organization in their "My Events" page.
3. **Admins:** Can add/delete/edit any/all events in their "My Events" page to ensure quality control.  

---

### Calendar Page Mockup

Features of the Calendar Page

* Calendar showing a month at a time
* Events for that month
* Ability to view events on specific days

---

### Event Detail Page Mockup

Features of the Event Detail Page

* Navigation Bar
* Organizer form to request to post an event
  * Attributes to help categorize the event
  * Image upload for thumbnails and supporting images
  * Description of the event
  * Request for submission
* Footer

---

### Contact Us / About Us Page Mockup

Anyone using the application can view this page to see the members behind the creation of this application. An overview of our goal is at the top and a collection of our pictures are below.

Users can contact us through this page. Each of our names redirects to opening an email with our respective hawaii.edu email address. Users who are event organizers can contact us to request a higher level of permissions to create and post events.

---

### (Optional) Campus Map Page Mockup

TBD

---

### (Optional) User / Admin / Organizer Profile Page Mockup

Features of the Profile Page

* View user profile
* Edit user profile

---

## Developer Guide

TBD

---

### Installations

TBD

---

## Community Feedback

TBD

## Development History

The development process for WarriorHub follows Issue Driven Project Management practices: 

- Development consists of a sequence of Milestones.
- Each Milestone is specified as a set of tasks.
- Each task is described using a GitHub Issue, and is assigned to a single developer to complete.
- Tasks should typically consist of work that can be completed in 2-4 days.
- The work for each task is accomplished with a git branch named “issue-XX”, where XX is replaced by the issue number.
- When a task is complete, its corresponding issue is closed and its corresponding git branch is merged into master.
- The state (todo, in progress, complete) of each task for a milestone is managed using a GitHub Project Board.

The following sections document the development history of WarriorHub.

---

### Project Milestones

Here are our goals throughout this project, separated into Milestones. They can also be found on our organization's Github.

[Project Milestone 1](https://github.com/orgs/warriorhub/projects/1): WIP

Project Milestone 2: TBD

Project Milestone 3: TBD

---

### Milestone 1: Mockup Development 

The goal of Milestone 1 was to create a set of HTML pages providing a mockup of the pages in the system.

Milestone 1 was managed using [WarriorHub GitHub Project Board M1](https://github.com/orgs/warriorhub/projects/1): 

<p align="center">
  <img src="images/project_milestone1.png" alt="Project Milestone 1" width="100%">
</p>

---

### Milestone 2: TBD

---

### Milestone 3: TBD

---

## Continuous Integration

TBD

## Example Enhancements

Additional planned features include:

* Notify students via email and SMS reminders of upcoming events that they have RSVPed for and notifying similar events that are coming up that they might be interested in..
* Map viewing showing the location of nearby events.  
* System for reviews on events, allowing RSVP students to give anonymous feedback of the event after they have attended.
* Allow users to ‘like’ certain events that would give the program better suggestions on what kind of events a user would like to attend for personalized reccomendations.
* Engagement points for people who attend events and reward badges for users to unlock. (i.e “Athletics Fan”, “Music Jammer”, “Foodie”, etc.)
