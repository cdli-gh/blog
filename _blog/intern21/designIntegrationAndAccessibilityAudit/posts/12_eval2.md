---
layout: page
title: Second Evaluation
author: "Mohit Sharma"
tags: ["eval","intern","intern2021","designIntegrationAndAccessibilityAudit","eval#2"]
---

## Summary
In phase 2, I’ve develop Add and Edit form for Posting with regex validation in Artifact ID and develop Add and Edit form for Staff with Image upload feature for Staff members. Setup Accessibility tests in pipelines using pa11y-ci and Gitlab CI/CD and also provide script to run the same tests locally. Finally, I’ve successfully finished all the deliverables of the project. It was challenging at all the instances but I managed to tackle all of it. It was a great experience and I’m looking forward to contributing more to CDLI


## Objectives and Deliverables
| \# | Objectives         | Associated Deliverables                                             | issue(s) | Status |
| --- | ------------------ | ------------------------------------------------------------------- | -------- | -------- |
| 1 | Posting Page | Develop Add and Edit pages for Posting and Check for it's Accessibility | [#464](https://gitlab.com/cdli/framework/-/issues/464) | Completed |
| 2 | Staff Page | Develop Add and Edit pages for Staff page with image upload feature for staff members | [#484](https://gitlab.com/cdli/framework/-/issues/484) | Completed |
| 4 | Accessibility Tests | Setup Automated Accessibility Tests in pipelines | [#600](https://gitlab.com/cdli/framework/-/issues/600), [#164](https://gitlab.com/cdli/framework/-/issues/164) | Completed |



## Learning and Success
After completing my 3 month internship with CDLI. I got to learn about CI/CD pipelines, docker, Cakephp,  Bootstrap, Sass and improve my existing skills of Php, Javascript and CSS.

## Difficulties
Setting up Pa11y-CI in a docker container was the major challenge for phase 2 as pa11y-ci default headleass chrome (puppeteer) is not working in docker container so we have to use chromium browser which is another headless chrome and then configure it with Pa11y-CI, Regex validation in posting forms and image upload in staff forms are also challenging featues to implement.
