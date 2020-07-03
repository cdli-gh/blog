---
layout: page
title: search Eval#1
author: "Vedant"
tags: ["eval","gsoc","gsoc2020","searchl#1"]
---

## Summary

The first phase of GSoC was quite a busy one. The main focus of this phase was to improve the authentication and authorization of the framework. Starting with the Authentication part, the main challenge was to make every user set up and verify two-factor authentication (2FA). Then moving to the authorization part, this is a complicated part of the framework as the approach to use generalized set up for web pages according to the user roles but the complexity increases if the role-based restriction is within the web page rather than the whole web page. This issue is currently in discussion with other contributors and will be addressed in buffer week.

The remaining small objectives related to the enhancement and security were implemented like disabling the user account after a specific period of inactivity, restricting logout using a GET request,  Forgot password functionality, etc.


## Objectives and Deliverables

Most of the objectives and deliverables were successfully accomplished.

| Sr. No. | Objectives | Deliverables  |
| --- | ---------- | ------------- |
| 1       | Two Factor Authentication (2FA) | Enforced 2FA for Login & Register. | 
| 2       | Password Strength Checker | Check if the user password is secure and not commonly used one. | 
| 3       | Implement Password Retrieval | Forgot password functionality is successfully set up except for the mail server which will be addressed in buffer week. | 
| 4       | Access control page | Admin can now set up additional roles for other users. | 
| 5       | Access Setup for Public, Granular and Admin roles | For now, the public and admin side roles are set up. Granular Access will be addressed in buffer week. | 
| 6       | Triggers for inactive users | Users with an inactivity period more than 6 months will be deactivated. | 
| 7       | 2FA Google Authenticator Guide | Two Factor Guide is added on [MTAAC and CDLI Documentation](https://cdli-gh.github.io/guides/cdli_two_factor_guide.html). | 
| 8       | Fix ‘/logout’ functionality | Logout now accepts POST requests and restricts the GET requests. | 

## Learning and Success

Data security is a vital part of any project. When building a project, it is important to realise the data requirement of specific functionality and discarding the additional data.

Currently, two-factor authentication is an additional security layer for traditional password-based authentication. But in the future, there is a possibility of user don't have to remember password and use the dynamically generated password which will be more secure and hard to predict.

So the important part is to properly store and manage the data according to the functionality requirement.


## Difficulties

The main difficulty is the clarity on setting up of role-based access which will get more complicated as the project expands. Although for now with the known functionalities, we can set up a generalized method for all pages but complications may arise in future.

## Plan update

Considering Phase-1 objectives and deliverables, I was able to accomplish 80% of deliverables and the remaining 20% will be completed during the 1st evaluation period or will be shifted to buffer week if additional time is required.

And on upcoming objectives for the next phase, I'll be discussed with my mentor and start to work from next week onwards.

