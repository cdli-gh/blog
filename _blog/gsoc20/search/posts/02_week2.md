---
layout: page
title: search Eval#1 Week#2
author: "Vedant"
tags: ["week","gsoc","gsoc2020","search","eval#1","week#2"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to the second weekly blog of GSoC'20 for CDLI. 

### What did you do this week?

At the start of this week, the final code for Objective-B (Bad Password check) was pushed in MR [!115](https://gitlab.com/cdli/framework/-/merge_requests/115) and successfully merged after review.

The Objective-C (Password retrieval functionality) was implemented as planned and I improvised by adding 2FA to make it more secure before the user sets a new password, implemented after discussion with my mentor.  

The upcoming objective of Role-based access system required the restructuring of the current Database tables which affected the Authentication system. It was the priority task to update code so that framework won't break. The Authentication code was updated according to the new DB structure.

### What is coming up next?

The upcoming week will aim at achieving combined objectives planned for Week 2 and 3.

### Did you get stuck anywhere?

Few docker containers have restricted internet access for security purpose from which arose a problem while attempting to set up email configuration for the password retrieval functionality.  The backend is ready and tested except the email functionality, which will be addressed in buffer week.

### Branch (worked on): 
1. [phoenix/feature/authentication](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authentication) 
2. [phoenix/feature/authorization](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authorization) 

### Issues : 
1. **Closed or worked related to:**
    - [#211](https://gitlab.com/cdli/framework/-/issues/211)
2. **Opened:** 
    - [#245](https://gitlab.com/cdli/framework/-/issues/245) 
    - [#247](https://gitlab.com/cdli/framework/-/issues/247) 
    - [#248](https://gitlab.com/cdli/framework/-/issues/248) 
    - [#249](https://gitlab.com/cdli/framework/-/issues/249) 

### Pull Request : 
1. **Merged (or under review):**
    - [!115](https://gitlab.com/cdli/framework/-/merge_requests/115)
    - [!119](https://gitlab.com/cdli/framework/-/merge_requests/119) 
    - [!120](https://gitlab.com/cdli/framework/-/merge_requests/120)
2. **Reviewed:**
    - [!117](https://gitlab.com/cdli/framework/-/merge_requests/117)
    - [!121](https://gitlab.com/cdli/framework/-/merge_requests/121) 
    - [!125](https://gitlab.com/cdli/framework/-/merge_requests/125)  


## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/08	|  a. Done with Bad Password Check. <br> b. WIP: Password Retrieval.	|  
|2   	| Tuesday  	|   2020/06/09	| a. WIP: Password Retrieval |  
|3   	| Wednesday  	|  2020/06/10 	| a. Password retrieval almost done. (Except the email functionality). <br> b. Configuring Email Settings for forgot Password.	|  
|4   	| Thursday  	|   2020/06/11	|  a. Integrating 2FA verification before creating new password from reset link. 	|  
|5   	| Friday  	|   2020/06/12	|  a. Done with Password retrieval with 2FA verification. (except sending email) PR [!119](https://gitlab.com/cdli/framework/-/merge_requests/119) <br> b. Updating Authentication with new DB structure.	|  
|6   	| Saturday  	|   2020/06/13	| a. Created PR [!120](https://gitlab.com/cdli/framework/-/merge_requests/120).  <br> b. Reviewed pending pull requests.	|  
|7   	| Sunday  	|   2020/06/14	|  a. Modified Authentication based on new role (table) structure.	<br> b. Created PR [!129](https://gitlab.com/cdli/framework/-/merge_requests/129). |  
