---
layout: page
title: bibliography Eval#3
author: "Ajit"
tags: ["eval","gsoc","gsoc2020","bibliography","eval#3"]
---

## About the project
In order to make CDLI's bibliographic data more useful, this project aims to make features for managing the bibliography and related data for the admin and also to provide a way for the users to browse and view the data.
It mainly deals with the creation of the management pages for this data so that it can be easily handled by the admin and it can be viewed by the users.

## Team
- Ajit Jadhav - Student Developer
- Rune Rattenborg - Mentor
- Sagar - Mentor

## Technologies
- CakePHP 3
- Docker
- Javascript
- JQuery
- HTML
- CSS

## Objectives Accomplished
1. Admin feature for linking publications to associated data like artifacts, authors and editors.
2. Admin feature for managing publications data and public features for viewing the publications data.
3. Admin feature for managing authors data and public features for viewing the authors data.
4. Bulk upload for publications, artifact-publication links, author-publication links and editor-publication links.
5. Documentation for all the work done.

## Contributions
My major contributions during GSoC can be found in the following links

- [Link artifacts and publications](https://gitlab.com/cdli/framework/-/merge_requests/122)
- [Improvements to artifact-publication link feature](https://gitlab.com/cdli/framework/-/merge_requests/153)
- [Link authors to publications and editors to publications](https://gitlab.com/cdli/framework/-/merge_requests/123)
- [Manage Authors Data for admin](https://gitlab.com/cdli/framework/-/merge_requests/128)
- [Authors data public view](https://gitlab.com/cdli/framework/-/merge_requests/131)
- [Creating Bulk upload component and bulk upload for Artifact-Publication links](https://gitlab.com/cdli/framework/-/merge_requests/136)
- [Bulk Upload Authors-Publications and Editors-Publications](https://gitlab.com/cdli/framework/-/merge_requests/143)
- [Publications data management and bulk upload](https://gitlab.com/cdli/framework/-/merge_requests/157)
- [Merge Publications and publications index and view](https://gitlab.com/cdli/framework/-/merge_requests/166)
- [Make the feature design more consistent with the entire framework](https://gitlab.com/cdli/framework/-/merge_requests/182)

A list of all contribution can be found [here](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&author_username=ajit_jadhav).

## Results

### 1. Admin feature for linking associated data to publications like artifacts, authors and editors

Publications have associated data like artifacts, authors and editors that have a many-to-many relation. Features to link them i.e. adding association and related data and also for editing the existing links were created. The linking of artifacts was handled using their id, bibtexkey was used for the publication and the full names for authors and editors. For adding each of the association, 3 ways are provided. 
For example, in case of artifact-publication association:

1. Add association directly:
![screencapture-127-0-0-1-2354-admin-artifacts-publications-add-2020-08-26-16_24_36](https://user-images.githubusercontent.com/35206075/91298598-f0064780-e7bd-11ea-86e7-f0a1b4f2f100.png)

2. Add associated artifact to a selected publication:
![screencapture-127-0-0-1-2354-admin-artifacts-publications-add-artifact-1-2020-08-26-16_25_06](https://user-images.githubusercontent.com/35206075/91298560-e086fe80-e7bd-11ea-9931-2b85c4721159.png)

3. Add associated publication to a selected artifact:
![screencapture-127-0-0-1-2354-admin-artifacts-publications-add-publication-1-2020-08-26-16_25_26](https://user-images.githubusercontent.com/35206075/91298557-df55d180-e7bd-11ea-9c44-f97ebf5e460e.png)

The association data can also be edited.

### 2. Admin feature for managing publications data and public features for viewing the publications data
This involved creation of add, edit and delete functions for the admin for managing the publications. Publications index for viewing all the entries along with search options for filtering through the results are also provided. Also, the publication view contains publication details along with listing of associated data like artifacts, authors and editors. Index and view for public users was also created with display of only published publications and public artifacts along with restrictions on search to make sure that the user is not able get search results using private information.

Publication admin index:
![screencapture-127-0-0-1-2354-admin-publications-2020-08-25-18_47_31](https://user-images.githubusercontent.com/35206075/91299370-1ed0ed80-e7bf-11ea-9890-767c7549e999.png)
Public view also has the same structure with restrictions on search and no options for editing data.

Publication view (admin):
<TBA>
The edit options on view page are only available if the user is admin.

### 3. Admin feature for managing authors data and public features for viewing the authors data
This involved creation of add, edit and delete functions for managing the authors for the admin along with author index for viewing all the entries. Also, publication view was created that contains author details along with listing of associated data like artifacts, authors and editors. Index and view for public users was also created with display of only published publications and public artifacts. These pages have a similar structure to the publication pages.

### 4. Bulk upload for publications, artifacts-publications link, authors-publications link and editors-publications link
For handling bulk upload of data for any of the tables in the database, the Bulk Upload Component was created. It is able to handle bulk upload for most of the database tables with only a few lines of code and proper data formatting in the model. The instruction for using the component for any other tables is provided [here](#).
A CSV file with proper format containing the data is used for the upload. The admin is provided with a validation error report before proceeding with the data save. On proceeding, the data is saved in the database and an error report that can be exported as a CSV file is provided that contains all the entries that could'nt be saved and their errors due to which they couldn't be saved. The exported error report can be used for bulk uploading those entries after fixing the errors.

Validation errors and confirmation for proceeding (in case if validation errors exist):
![Screenshot from 2020-08-20 14-04-53](https://user-images.githubusercontent.com/35206075/91298829-54c1a200-e7be-11ea-84c8-529466af3531.png)

Error report:
![Screenshot from 2020-08-20 14-05-07](https://user-images.githubusercontent.com/35206075/91298835-568b6580-e7be-11ea-8781-19a754f632af.png)

## Bonus Task

### Admin feature for merging publications to clean up publications data

The data conversion from the old flat structure to the new fully associated database leads to duplicates or near duplicates for the publications data. While there is ongoing work for improving the data conversion scripts based on the data patterns, it is very difficult to obtain a perfect data format conversion due to the difference in structure of the data. This feature helps in making the process of cleaning the data easier. The admin can search the publications based on the provided set of criteria and then select the entries for merging and cleaning. Once selected, the publication details along with the artifacts associated to all the selected entries and related association data can be modified and finalized and the publication can be merged.

Search publications for merging:
![screencapture-127-0-0-1-2354-admin-publications-merge-select-2020-08-25-18_49_39](https://user-images.githubusercontent.com/35206075/91299039-a79b5980-e7be-11ea-9b34-73e3b343e4b1.png)

Editing details for the merged publication:
![screencapture-127-0-0-1-2354-admin-publications-merge-2020-08-25-18_55_18](https://user-images.githubusercontent.com/35206075/91299036-a5d19600-e7be-11ea-9094-f10ec96d8bb0.png)

## Conclusion

My project was mostly to design and implement features for managing bibliography related data. The mentors were very helpful and patient while guiding me and the code reviews were very detailed and I was able to learn a lot from them. Some parts were challenging and I was stuck at a them for a while but with the help from the entire CDLI community, I was able to fix them gradually and complete the features.
I learned a lot about development practices and technologies like CakePHP 3.

## Future plan

I would be available to help with further improving my current project or in general with any task that I can help with in case if required. Developing for CDLI has been an enjoyable experience and I plan to be a long-time contributor for CDLI.


 
 



