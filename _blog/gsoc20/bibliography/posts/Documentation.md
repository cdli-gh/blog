

# Documentation

## Link Artifacts to Publications

### Add Artifact-Publication link

There are 3 ways to link artifacts and publications.

1. Add association directly:
For associating any artifact to any publication.
![screencapture-127-0-0-1-2354-admin-artifacts-publications-add-2020-08-26-16_24_36](https://user-images.githubusercontent.com/35206075/91298598-f0064780-e7bd-11ea-86e7-f0a1b4f2f100.png)

2. Add associated artifact to a selected publication:
For associating artifacts for a particular publication. This can be accessed by the admin from the publication view of the selected publication. 
Details for the selected publication are displayed on this page along with a list of associated artifacts.
![screencapture-127-0-0-1-2354-admin-artifacts-publications-add-artifact-1-2020-08-26-16_25_06](https://user-images.githubusercontent.com/35206075/91298560-e086fe80-e7bd-11ea-9931-2b85c4721159.png)

3. Add associated publication to a selected artifact:
For associating publications for a particular artifact.
Few details for the selected artifact are displayed on this page along with a list of associated publications.

Technical details for the add pages:
* Publications are identified using their bibtexkey and suggestions for bibtexkey are provided based on the input.
* Artifacts are identified using their id or P#.

### Edit Artifact-Publication link
The associations listed on the add pages can also be edited. Details for the artifact and publication are provided on the page.

## Authors data pages

### Authors index
Both admin and public index provide same listing of the authors. 
Edit and delete options are available for each entry for the admin.

### Author add
For adding new author entry.

### Author edit
For editing existing author details.

Technical details for add/edit:

* Either `First Name` or `Last Name` have to be provided.
* Selecting `East Asian Order` saves the full author name in the format `last first` while the normal format is `last, first`.
* The editors for the publications are also saved in the authors table.

### Authors public index
Similar to the admin publication index with extra restrictions to prevent the user from accessing sensitive data. 

### Author view page
Both admin and public view pages display the author details along with list of associated data. For public users, sensitive information is not displayed.

## Publications data pages

### Publication index
Both admin and public index provide same listing of the pubications with the same search provided for publication. 
While admin has access to all the data, the public user will only be shown published entries and won't be able to search using private artifact id.
Edit and delete options are available for each entry for the admin.

### Publication add
For adding new publication entry.

### Publication edit
For editing existing publications and the associated artifacts and publications.

Technical details for add/edit:

* `Title` field needs to be provided (doesn't need to be unique).
* `BibTeX Key` needs to be unique and is auto-generated to be a unique value if not provided by the user.
* Authors and editors input fields will have upto 5 suggestions on entering 3 or more characters as input.
* The editors for the publications are also saved in the authors table.

### Publication public index
Similar to the admin publication index with extra restrictions to prevent the user from accessing sensitive data. 

### Publication view page
Both admin and public view pages display the publication citation and designation data along with list of associated data.


## Merge Publications

This feature can be used to clean the publications data by merging duplicates or near duplicates that may result from data conversion from the old database structure or due to other reasons.

The workflow for using the feature is as follows:

### 1. Filtering the publications using the search fields.

  Merge select page:
  ![merge-select](https://user-images.githubusercontent.com/35206075/91346026-e56ba280-e7fd-11ea-9794-32bf243608bc.png)
  
  Publication search elements:
  * Input fields: The publications can be searched using the following fields
    * BibTeX Key: Bibtex key set for the publication.
    * Title: Publication title.
    * Publisher: Search by ame of the publisher for the publication.
    * Author: Author associated to the publication.
    * Entry Type: Entry type of the publication.
    * Journal: Joural name to which the publication is associated.
    * Year: Range of the published year. ('From' denotes the lower range and 'To' denotes the upper range).
  * Search: Once the fields are entered based on the requirement of the user, the results can be obtained by clicking on the search button.
  * Reset: The search input fields and the search results will the reset to the original state.
  
### 2. Selecting publications for merging from the search results.
This can be accessed by the admin from the publication view of the selected publication. This can be accessed by the admin from the publication view of the selected publication. 
  Result list elements:
  * Checkboxes in the select column for the search results: Among the search results, the entries that need be merged are selected by checking them.
  * Merge: Submit the selected entries for merging.
  * Select All: Check all the search results.
  * Reset: Uncheck all the selected entries.

Note: The search results display is limited to 50 results. If the number of results exceeds 50, then a warning will be displayed to the user.

### 3. Editing details of the final merged publication entry.

  Merge page:
  ![merge](https://user-images.githubusercontent.com/35206075/91346018-e3a1df00-e7fd-11ea-80ee-262fcaa764ca.png)

  Elements for finalizing the merge:
  * List of selected publications: List showing details of the publicatiosn selected for merging.
  * Details of the merged publication: Input for all the fields for the merged publication. The fields will be automatically populated with details from the first entry from the selected publications.
  * Artifacts association data: The association data for all the artifacts related to all the selected publications will be displyed as a list where the association details can be edited. The merged publication will have all these artifacts associated to it.
  * Submit: To submit the entered details for creating the merged publication entry and deleting all the selected entries.
