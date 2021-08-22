<h1 align="center" > Google Summer of Code 2021 </h1>
<p align="center"><i>with</i> </p>
<h2 align="center"><a href="https://summerofcode.withgoogle.com/organizations/4724093699489792/">Cuneiform Digital Library Initiative (CDLI)</a></h2>
<h2 align="center"> Final Report of my GSoC'21 Project </h2>

<br/>
GSoC CDLI Logo

<h1> Journal Open Review Workflow And Integration </h1>

## About the project

This project focuses on creating a functional pipeline which will consist of open submission and open review process before publishing articles in our CDLI journals dashboard. To implement  open journals in the system,  an appropriate workflow needs to be developed which is intended to be carried out using https://pkp.sfu.ca/ojs/ojs_download/ software. OJS(Open Journal System) is an open source solution to managing and publishing scholarly journals online. OJS is a highly flexible editor-operated journal management and publishing system. In addition to this, we intend to make further integration in the CDLI journals dashboard and display the endorsement of reviewers with published articles.

## Links

- [Project Proposal](https://docs.google.com/document/d/1Bq1Be4UYaF08vBwasERpx2kiWuiVPWdkSEHBM-owUx4/edit#heading=h.rti1bbjk8idf)
- [Project Weekly Blogs](https://cdli-gh.github.io/blog/gsoc21/journalsOpenReviewWorkflowAndIntegration/index)
- [Contributions to CDLI](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=apoorva1509)

## Mentor: 
<a href='mailto:nisheal.work@gmail.com'>Nisheal John</a>

## Technologies

- CakePHP 3
- Javascript
- Docker
- HTML
- SCSS
- PKP/OJS

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | Issues |
| --- | --- | ----------------------------- | ---------------------------------------------- | ---- |
| 1 | :heavy_check_mark: | Integrating ojs Docker Container in the framework | Downloading ojs software and creating a docker container for it | - |
| 2 | :heavy_check_mark:| Ojs workflow for submission and review of articles | Creating a workflow for open submission and open review of articles | - | 
| 3 | :heavy_check_mark:  |  Ojs Datbase Connection | Setup ojs connection and create relations between ojs models | - |
| 4 |  :heavy_check_mark: | Write command script to move ojs submissions to cdli | Command script that will run hourly and move reviewed ojs submissions to cdli database  | -  | 
| 5 |  :heavy_check_mark: | Designing single article view | Remove header from latex convertor and design single article web view page |  - |
| 6 | :heavy_check_mark: |Displaying reviewers endorsements | Develop review page to display reviewers endorsements on article web page | - |

## Milestone 1 

In particular the work done in milestone 1 was

- Written dockerfile to create ojs container consisting ojs submodule
- Updated CDLI journals index to create a link between CDLI journals dashboard and ojs dashboard
- Finalized single article web view design with Somil Jain
- Wrote Readme file for deploying ojs and running ojs container

### PRs Involved

- [Created docker container for ojs](https://gitlab.com/cdli/framework/-/merge_requests/313)
- [Created a direct link between CDLI journals and ojs](https://gitlab.com/cdli/framework/-/merge_requests/599)
- [Readme file for running ojs locally ](https://gitlab.com/cdli/framework/-/merge_requests/348)
- [Created different fields for year of submission and article number ](https://gitlab.com/cdli/framework/-/merge_requests/291)

### Summary

## Milestone 2

The work done in Milestone 2 was

- Creating a workflow for open submission and open review of articles in ojs
- Creating a test submission in ojs with complete open review process
- Implementing single article web view design 
- Remove header from latex convertor

Along with this we even discussed the final workflow to be followed to integrate ojs submissions in CDLI journals dashboard and publish them.

### PR Involved

- [Implement single article web view ](https://gitlab.com/cdli/framework/-/merge_requests/368)

### Summary


## Milestone 3

The work done in this milestone is:

- Created command script to move reviewed ojs submissions to CDLI journals dashboard and prepopulate the CDLI database
- Update Journals admin index to add ojs reviewed submissions to CDLI database
- Display reviewers endorsements on single article web view page
- Access all the revisions of the submission from single article web view
- Testing Ojs

### PR Involved

- [Workflow to move ojs submissions to CDLI](https://gitlab.com/cdli/framework/-/merge_requests/374)

### Summary


## To Do (Post GSoC)

- Citations for articles
- Fix author picker
- Filter draft and published articles
- ORCHID Integration
- [Create single article web view navbar for no-js users](https://gitlab.com/cdli/framework/-/issues/682)
- [Download button for html source code of journals](https://gitlab.com/cdli/framework/-/issues/662)
- [Write specific error for missing entity while adding article](https://gitlab.com/cdli/framework/-/issues/683) 
- [Create field for keywords in journals dashboard](https://gitlab.com/cdli/framework/-/issues/626)

## Summary

## Learning/Success

## Takeaways

## Acknowledgements
