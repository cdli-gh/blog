---
layout: page
title: Journals Management and Display
author: 'Nisheal John'
tags: ['project', 'gsoc', 'gsoc2020', 'journals', 'eval#1', 'week#2']
---

## Project Overview.

I'm <a href="https://in.linkedin.com/in/nishealjohn">Nisheal John</a>, participating in Google Summer of Code 2020 with CDLI.
I've been accepted for the project Journals Management and Display, the project focuses on the publication of various types of articles that CDLI hosts, currently CDLI hosts four articles, two peer-reviewed journals (CDL Journal and CDL Bulletin), the CDL Pre-prints repository and the CDL Notes. For the upload of articles, appropriate designs and workflow need to be developed which includes the development of required routes, controllers, views & tests. The major challenges to this project are the conversion of the editor's article inputs to CDLI's article publications which will be carried out by using latex and Maths libraries. The editors will be uploading the latex file of the article and the dashboard will convert the latex file into the needed HTML content i.e the CDLI web template. Building latex and Math parser is the heart of this project. Further in the project necessary end-to-end & unit testing phases should be established to improve the development workflow and avoid build issues.<br>

<i>Project:</i>
<a target="_blank" href="https://summerofcode.withgoogle.com/projects/#5756188689432576
">GSoC'20</a>,
<a target="_blank" href="https://gitlab.com/cdli/framework"> GitLab</a>
<br>
<i>GSoC'20 Proposal:</i>
<a href="https://docs.google.com/document/d/1RqDL5N3zou7Jr5hd7dXfV4L-Dr6gu0kOevz7tKUzsZ8/edit">Link</a><br>
<i>Contributions to CDLI:</i>
<a href="https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=nishealj
">Link<a><br>
<i>Ongoing work status:</i>
<a href="https://docs.google.com/spreadsheets/d/1G9bFZZEGgC9URRTA15ZaxRsDyZIPjIQr4x13S4bi7xc/edit#gid=0
">Link<a><br>

<b>Mentor: </b> <a target="_blank" href='mailto:lizardcircusus@gmail.com'>David Wong</a>

## GSoC Final Report and Summary.

### Objectives and Deliverables

Objectives are separated in two categories: essential and additional, they are also listed in priority order.

#### Essential Objectives

| \#  | Objectives         | Status | Associated Deliverables                                                         | issue(s) |
| --- | ------------------ | -------- | ------------------------------------------------------------------------------- | -------- |
| 1   | Article CRUD     | Complete|Feature for editors to CRUD different types of articles.                      |  <a target="_blank" href='https://gitlab.com/cdli/framework/-/issues/265'>#265</a>        |
| 2   | Article Conversion |Complete |Backend to convert the editor's uploaded article to CDLI Standards for display. |   <a target="_blank" href='https://gitlab.com/cdli/framework/-/issues/267'>#267</a>       |
| 3   | Article Display    |Complete |Display all the articles at their respective pages and indiviual view for each article.|   <a target="_blank" href='https://gitlab.com/cdli/framework/-/issues/266'>#266</a>       |
| 4   | Schema Migration   | Complete |Make necessary changes to the schema for journals dashboard.                    |          |
| 5   | Article Migration  | Complete |Move old & archived articles to the new architecture.                           |          |
| 6   | Testing            | Complete |Implement necessary testing for the project and sync with CI/CD.                |          |

#### Additional Objectives

| \#  | Objectives             | Associated Deliverables | issue(s) |
| --- | ---------------------- | ----------------------- | -------- |
| 1   | Improvements to CI/CD  | Gitlab CI/CD Pipelines  |          |
| 2   | Initalize unit testing | Framework Testing       |          |

### Timeline

| Week | Objectives                            |Status |Deliverables                                                                                           |
| ---- | ------------------------------------- |------ |------------------------------------------------------------------------------------------------------ |
| 1    | Upload article attributes to database | Complete|CRUD Operations for article attributes and different types of journals.                                |
| 2    | Upload article content to database    | Complete|Controllers to manage authors and article content/HTML to the database |
| 3    | Display varioues types of articles    | Complete|Make Different pages for different types of articles.                                                  |
| 4    | Migration of article                  | Complete|Migrate old CDLI articles to new schema and display                                                    |
| 5    | Testing                               |Complete |Testing Implementations of Milestone 1 i.e Week 1 to week 4                                                                |
| 6    | Convert articles at editor Dashboard. |Complete |Build latex tex to HTML converters.                                           |
| 7    | Convert articles at editor Dashboard. |Complete |Finishing the latex tex to HTML conversion for journals.                                               |
| 8    | Display of article content            |Complete |Display of HTML Content of the journal (Individually)                                                  |
| 9    | Testing                               |Complete |Testing Implementations of Milestone 2 i.e Week 6 to week 8.                                                                |
| 10   | Integration Testing                   |Complete |Testing the data variation to the database with article content and integration with other modules.    |
| 11   | Unit Testing                          |Complete |Initalize unit testing for CDLI Framework and write possible tests journals dashboard                  |
| 12   | Improvements                          |Complete |Manually test the entire journal dashboard, ready the project for submission and document necessary details (CKEditor, pdf2html and tests). |
| 13   | Finishing the project                 |Complete |Testing the project and making release/production ready.                                               |

### Weekly Reports
