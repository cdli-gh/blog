---
layout: page
title: search Eval#1 Week#1
author: "Vedant"
tags: ["week","gsoc","gsoc2020","search","eval#1","week#1"]
---
## Week Summary

<!-- A complete report of the work done during the week must be written here.  -->

Namaste 🙏 ,    
Welcome to the first weekly blog of GSoC'20 for CDLI. 

### What did you do this week?

This week's main focus was to improve the Authentication for the framework. The two-factor authentication (2FA) was already set up but the main objective was to enforce the user to set up or verify 2FA and then authenticate the user. The initial implementation discussed was to create a middleware layer which seems to be a safe option, but unless you experiment or explore other methods (may be simple or complex) there no learning. That's when I found an alternative implementation and proceeded with my mentor's approval. So the result was that the user cannot access the account until he has set up 2FA or verified 2FA. 

The next objective implemented is the bad password check. The user's password is checked against the most commonly used or leaked passwords and is prompted to set a secure password during registration.

### What is coming up next?

The upcoming week will accommodate the remaining Objective-C (Password retrieval functionality) for Week 1 and objectives planned for Week 2.

### Did you get stuck anywhere?

Not as such hindrance but due to change in implementation and improving the use case coverage for security reason of 2FA, it took time more than expected and caused a bit change in plan for Objective-C. 

### Branch (worked on): 
1. [phoenix/feature/authentication](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authentication) 

### Issues : 
1. **Closed or worked related to:**
    - [#4](https://gitlab.com/cdli/framework/-/issues/4) 
    - [#107](https://gitlab.com/cdli/framework/-/issues/107)    
2. **Opened:** No new issue opened during this week.

### Pull Request : 
1. **Merged (or under review):**
    - [!115](https://gitlab.com/cdli/framework/-/merge_requests/115)
2. **Reviewed:** No PR reviewed during this week.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| a. Explored Auth and its configuration options. <br>b. Tried to enforce 2FA using AppController. |  
|2   	| Tuesday  	|   2020/06/02	|  a. Continued to test enforcing 2FA using AppController. <br> b. Created basic Middleware layer to enforce 2FA.|  
|3   	| Wednesday  	|  2020/06/03 	|  a. Restructuring TwoFactor Controller. |  
|4   	| Thursday  	|   2020/06/04	|  a. Login + Two Factor Completed <br> b. Register + Two Factor (WIP) 	|  
|5   	| Friday  	|   2020/06/05	|  a. Register + Two Factor (Restructured)	|  
|6   	| Saturday  	|   2020/06/06	| a. Done with Objective-A of this week. PR [#115](https://gitlab.com/cdli/framework/-/merge_requests/115) under review. <br> b. Researched more about salt and hashes for passwords. <br> c. Started Implementation for Objective-B.	|  
|7   	| Sunday  	|   2020/06/07	| a. Implementation of bad password check.	<br> b. Researched Forget password functionality in CakePhp. <br> c. Started Implementation for Objective-C. |  
