---
layout: page
title: Project Title
author: "Developer Name"
tags: ["eval","gsoc","gsoc2021","projectHashTag","eval#2"]
---
 
 
This post contains the report for the entire project. For more information on the project, see the [project index page](https://cdli-gh.github.io/blog/gsoc20/bibliography/index).

 
## About the project
In order to make CDLI's bibliographic data more useful, this project aims to make features for managing the bibliography and related data for the admin and also to provide a way for the users to browse and view the data.
It mainly deals with the creation of the management pages for this data so that it can be easily handled by the admin and it can be viewed by the users.

## Team
- Ajit Jadhav - Student Developer ([LinkedIn](https://www.linkedin.com/in/ajitjjadhav/))
- Rune Rattenborg - Mentor ([Website](https://katalog.uu.se/profile/?id=N18-1120), [LinkedIn](https://www.linkedin.com/in/rune-rattenborg/))
- Sagar - Mentor ([LinkedIn](https://www.linkedin.com/in/sagar-sehgal/))

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
My major contributions during GSoC can be found in the following links:

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
Add association for any artifact using its artifact id (or P#) and any publication using its bibtexkey along with the other associated data fields.

2. Add associated artifact to a selected publication:
Through the publication view page, the admin can access feature for associating artifacts to the publication. Selected publication information and list of associated artifacts are provided.

3. Add associated publication to a selected artifact: Similarly, the admin can access feature for associating publications to the artifact. Selected artifact information and list of associated publications are provided.


The association data can also be edited using the edit page that contains both the artifact and publication information for the selected association. Selected artifact information and list of associated publications are provided.

Edit page with the information of the artifact and publication for the selected publication along with the input fields:

<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91659976-d41de100-eaf0-11ea-9f19-87922d89582a.png" style="border: 2px solid black" width="1000" />
</div>
 
The add pages have a similar design with their respective elements.

#### Pull Requests

- [Link artifacts and publications](https://gitlab.com/cdli/framework/-/merge_requests/122)
- [Improvements to artifact-publication link feature](https://gitlab.com/cdli/framework/-/merge_requests/153)
- [Link authors to publications and editors to publications](https://gitlab.com/cdli/framework/-/merge_requests/123)

### 2. Admin feature for managing publications data and public features for viewing the publications data
This involved creation of add, edit and delete functions for the admin for managing the publications. Publications index for viewing all the entries along with search options for filtering through the results are also provided. Also, the publication view contains publication details along with listing of associated data like artifacts, authors and editors. Index and view for public users were also created with display of only published publications and public artifacts along with restrictions on search to make sure that the user is not able get search results using private information.

Publications index (admin):
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91660069-7fc73100-eaf1-11ea-8f15-699660bc7788.png" style="border: 2px solid black" width="1000" />
</div>

Public index also has the same structure with restrictions on search and no options for editing data.

Publication view:
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91660070-8190f480-eaf1-11ea-85c7-849334566b1f.png" style="border: 2px solid black" width="1000" />
</div>

The edit options on view page are only available if the user is admin.

#### Pull Requests

- [Publications data management and bulk upload](https://gitlab.com/cdli/framework/-/merge_requests/157)
- [Merge Publications and publications index and view](https://gitlab.com/cdli/framework/-/merge_requests/166)
- [Public Publications index](https://gitlab.com/cdli/framework/-/merge_requests/190)

### 3. Admin feature for managing authors data and public features for viewing the authors data
This involved functions for managing the authors for the admin along with author index for viewing all the entries. Also, author view was created that contains publications details. Similarly, index and view pages for public users were also created. These pages have a similar structure to the publication pages.

#### Pull Requests

- [Manage Authors Data for admin](https://gitlab.com/cdli/framework/-/merge_requests/128)
- [Authors data public view](https://gitlab.com/cdli/framework/-/merge_requests/131)
- [Authors data validation fix](https://gitlab.com/cdli/framework/-/merge_requests/155)


### 4. Bulk upload for publications, artifact-publication associations, author-publication associations and editor-publication associations
For handling bulk upload of data for any of the tables in the database, the Bulk Upload Component was created. It is able to handle bulk upload for most of the database tables with only a few lines of code and proper data formatting in the model.

A CSV file in the required format containing the data is used for the upload. The admin is provided with a validation error report before proceeding with the data save. On proceeding, the data is saved in the database and an error report that can be exported as a CSV file is provided that contains all the entries that could'nt be saved and their errors due to which they couldn't be saved. The exported error report can be used for bulk uploading those entries after fixing the errors.

Validation errors and confirmation for proceeding (in case if validation errors exist):
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91661473-f23c0f00-eaf9-11ea-965e-b99c25657b29.png" style="border: 2px solid black" width="1000" />
</div>

Error report:
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91661478-f36d3c00-eaf9-11ea-91bf-0b7890caedd2.png" style="border: 2px solid black" width="1000" />
</div>

#### Pull Requests

- [Creating Bulk upload component and bulk upload for Artifact-Publication links](https://gitlab.com/cdli/framework/-/merge_requests/136)
- [Bulk Upload Authors-Publications and Editors-Publications](https://gitlab.com/cdli/framework/-/merge_requests/143)
- [Publications data management and bulk upload](https://gitlab.com/cdli/framework/-/merge_requests/157)
- [Improvements to bulk upload](https://gitlab.com/cdli/framework/-/merge_requests/191)


## Bonus Task

### Admin feature for merging publications to clean up publications data

The data conversion from the old flat structure to the new fully associated database leads to duplicates or near duplicates for the publications data. While there is ongoing work for improving the data conversion scripts based on the data patterns, it is very difficult to obtain a perfect data format conversion due to the difference in structure of the data. This feature helps in making the process of cleaning the data easier. The admin can search the publications based on the provided set of criteria and then select the entries for merging and cleaning. Once selected, the publication details along with the artifacts associated to all the selected entries and related association data can be modified and finalized and the publication can be merged.

Search publications for merging:
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91299039-a79b5980-e7be-11ea-9b34-73e3b343e4b1.png" style="border: 2px solid black" width="1000" />
</div>

Editing details for the merged publication:
<div style="text-align:center">
    <img src="https://user-images.githubusercontent.com/35206075/91299036-a5d19600-e7be-11ea-9094-f10ec96d8bb0.png" style="border: 2px solid black" width="1000" />
</div>

#### Pull Requests

- [Merge Publications and publications index and view](https://gitlab.com/cdli/framework/-/merge_requests/166)

## Conclusion

My project was mainly to design and implement features for managing bibliography related data.
The CDLI database holds the worldwide canonical text catalogue for cuneiform texts of more than 300,000 records from the earliest part of human history. This project will enable the CDLI admin and users to improve the data quality and interoperability of the CDLI database that will be of critical relevance to the scholarly community working with cuneiform sources.

The mentors were very helpful and patient while guiding me and the code reviews were very detailed and I was able to learn a lot from them. Some parts were challenging and I was stuck at a them for a while but with the help from the entire CDLI community, I was able to fix them gradually and complete the features.
I learned a lot about development practices and technologies like CakePHP 3 throughout my project.

## Future plan

I enjoyed contributing to CDLI for developing their framework. Considering that there is still room for more development related to my project and the entire framework as a whole, I would like to help with the development in the future. I would be available to help with further improving my current project or in general with any task that I can help with in case if required. Developing for CDLI has been an enjoyable experience and I plan to be a long-time contributor for CDLI.

 



