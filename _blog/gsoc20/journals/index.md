---
layout: page
title: Journals
author: 'Nisheal'
tags: ['project', 'gsoc', 'gsoc2020', 'journals', 'eval#1', 'week#2']
---

## Journals Management & Display.

I'm <a href="https://in.linkedin.com/in/nishealjohn">Nisheal John</a>, participating in Google Summer of Code 2020 with CDLI.
This project focuses on the publication of various types of journals that CDLI hosts, currently CDLI hosts four journals, two peer-reviewed journals (CDL Journal and CDL Bulletin), the CDL Pre-prints repository and the CDL Notes. For the upload of articles, appropriate designs and workflow need to be developed which includes the development of required routes, controllers, views & tests. The major challenges to this project are the conversion of the editor's article inputs to CDLI's article publications which will be carried out by using latex and Maths libraries. Further in the project necessary end-to-end & unit testing phases should be established to improve the development workflow and avoid build issues.<br>

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

<b>Mentor: </b> <a target="_blank" href='mailto:lizardcircusus@gmail.com'>David Wong</a>

### Objectives and Deliverables

Objectives are separated in two categories: essential and additional, they are also listed in priority order.

#### Essential Objectives

| \#  | Objectives         | Associated Deliverables                                                         | issue(s) |
| --- | ------------------ | ------------------------------------------------------------------------------- | -------- |
| 1   | Article upload     | Feature for editors to upload different types of articles.                      |          |
| 2   | Article Conversion | Backend to convert the editor's uploaded article to CDLI Standards for display. |          |
| 3   | Article Display    | Display different types of CDLI articles to publictions.                        |          |
| 4   | Schema Migration   | Make necessary changes to the schema for journals dashboard.                    |          |
| 5   | Article Migration  | Move old & archived articles to the new architecture.                           |          |
| 6   | Testing            | Implement necessary testing for the project and sync with CI/CD.                |          |
| 7   |                    |

#### Additional Objectives

| \#  | Objectives             | Associated Deliverables | issue(s) |
| --- | ---------------------- | ----------------------- | -------- |
| 1   | Improvements to CI/CD  | Gitlab CI/CD Pipelines  |          |
| 2   | Initalize unit testing | Framework Testing       |          |
| 3   |                        |                         |          |

### Tentative timeline

| Week | Objectives                            | Deliverables                                                                                           |
| ---- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1    | Convert articles at editor Dashboard. | Implementation of CKEditor and latex pdf to HTML converters.                                           |
| 2    | Convert articles at editor Dashboard. | Finishing the latex pdf to HTML conversion for journals.                                               |
| 3    | Upload article attributes to database | CRUD Operations for article attributes and different types of journals.                                |
| 4    | Upload article content to database    | Controllers to manage authors and article content/HTML to the database                                 |
| 5    | Testing                               | Testing Implementations of Milestone 1.                                                                |
| 6    | Display varioues types of articles    | Make Different pages for different types of articles.                                                  |
| 7    | Migration of article                  | Migrate old CDLI articles to new schema and display                                                    |
| 8    | Display of article content            | Display of HTML Content of the journal (Individually)                                                  |
| 9    | Testing                               | Testing Implementations of Milestone 2.                                                                |
| 10   | Integration Testing                   | Testing the data variation to the database with article content and integration with other modules.    |
| 11   | Unit Testing                          | Initalize unit testing for CDLI Framework and write possible tests journals dashboard                  |
| 12   | Improvements                          | Manually test the entire journal dashboard, build few left out things and ready the project submission |
| 13   | Finishing the project                 | Testing the project and making release/production ready.                                               |
