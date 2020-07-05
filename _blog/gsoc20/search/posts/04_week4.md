---
layout: page
title: search Eval#1 Week#4
author: "Vedant"
tags: ["week","gsoc","gsoc2020","searchl#1","week#4"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to the fourth weekly blog of GSoC'20 for CDLI. 

### What did you do this week?

The week was quite a productive one as I was able to achieve the deliverables which were expected. The first objective was to create an event in DB to deactivate user with an inactivity period of more than 6 months and successfully added in DB. The Two Factor Guide documentation was added to [MTAAC and CDLI Documentation](https://cdli-gh.github.io/guides/cdli_two_factor_guide.html). Next objective was to use POST request and restrict GET request for logout functionality which is implemented and under review. There was a request to add 'Skip 2FA' to ease the login and register in development mode. The remaining time was used to work on the Access Setup for the framework.

### What is coming up next?

In the upcoming week, I will try to work on the changes suggested for access setup and plan the objectives and schedule for the 2nd phase objectives.

### Did you get stuck anywhere?

After the two reviews for access setup, lack of clarity regarding the Sample Role Page and many other changes were suggested. The changes suggested will require an extra week for its implementation which I'm planning to do during the evaluation period.

### Branch (worked on):  
1. [phoenix/feature/authorization](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authorization)
2. [phoenix/feature/authentication](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authentication)
3. [phoenix/feature/optimize-setup](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/optimize-setup) 

### Issues : 
1. **Closed or worked related to:**
    - [#84](https://gitlab.com/cdli/framework/-/issues/84)
2. **Opened:** 
    - No new issue created during this week. 

### Pull Request : 
1. **Merged (or under review):**
    - [!137](https://gitlab.com/cdli/framework/-/merge_requests/137)
    - [!140](https://gitlab.com/cdli/framework/-/merge_requests/140)
    - [!141](https://gitlab.com/cdli/framework/-/merge_requests/141)
    - [!144](https://gitlab.com/cdli/framework/-/merge_requests/144)  
2. **Reviewed:**
    - [!130](https://gitlab.com/cdli/framework/-/merge_requests/130)

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/22	|  a. WIP : Access setup for Normal User, Editors and Granular access. 	|  
|2   	| Tuesday  	|   2020/06/23	| a. Done with Triggers for inactive users (Objective-A , Week 4). <br> b. Created a guide for 2FA using Google Authenticator. |  
|3   	| Wednesday  	|  2020/06/24 	| a. Created [PR !140](https://gitlab.com/cdli/framework/-/merge_requests/140) for 2FA Guide. <br> b. WIP : Access setup for Normal User.  	|  
|4   	| Thursday  	|   2020/06/25	|  a. WIP : Access setup for Admin. 	|  
|5   	| Friday  	|   2020/06/26	|  a. Added skip for 2FA verification. <br> b. Created [PR !141](https://gitlab.com/cdli/framework/-/merge_requests/141). <br> c. Updated 2FA Guide on	[cdli-gh.github.io](https://cdli-gh.github.io/guides/cdli_two_factor_guide.html).|  
|6   	| Saturday  	|   2020/06/27	|  a. Done with Objective-C : Fix ‘/logout’ functionality. <br> b. Created [PR !144](https://gitlab.com/cdli/framework/-/merge_requests/144).	|  
|7   	| Sunday  	|   2020/06/28	|  a. Done with cleaning of Admin and User side controllers. <br> b. Added skip option for 2FA in development mode.	|  
