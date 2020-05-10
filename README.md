
# CDLI Blog 

This is the CDLI blog which would be used as a eview system for monitoring the progress of the projects currently active in CLDI Labs.

## How to add a new program?

Create a new folder for a new folder in `_blog` folder. Furhter, in order mantain the template, an easy hack would be to just make a copy of an existing folder and then modify it content.

For eg:- 
If you want to add a new pragram like `intern20`. So for that, make a copy of an existing folder like `gsoc20`. And then the projects inside could be modified further as per the projects inside.

All the programs would be listed on the home page of the Blog. In order to update what is displayed on the home page regarding the program, you will have to update the `_blog/<program_name>/index.md` file. 

For eg:- 

For the GSoC 2020 program, the front matter of `_blog/gsoc20/index.md` looks like this:- 

```
---
title: GSOC 2020
layout: page
author: ""
tags:  ["gsoc","gsoc2020"]
---
```

*title* : The title of the page. The title would be displayed on the top of the page. Furhter the same title would be shown on the Home page.

*layout* : Always keep it to "page" only.

*author* :  The name of Author. Please keep the name inside quotes(\"\").If more than 1 authors, make it a list ["author1","author2"].

*tags* : These are the tags that would be assigned to the page. Please assign the tags accordingly, bcz based on the tags, the pages would be shown in the **Tags** tab.

## How to add a new project inside a program?

Assuming that the program name would be `gsoc20` and I want to add a new project into this program. Assume the new project name is `testing`.

So, for this we would have to add a new folder named `_blog/gsoc20/testing`. In order to prevent any error, the best way, is to make a copy of any other folder in `_blog/gsoc20/`. Like a copy of `_blog/gsoc20/api` could be made and then it could be renamed to `testing`.

Now, every project has the following structure:-

```
_blog/gsoc20/testing/
├── index.md
└── posts
   ├── 01_week1.md
   ├── 02_week2.md
   ...
```

Here the `index.md` file contais the info about the project . Furhter it also links to all the blogs published during the project.

Further, more info about `index.md` would be  

For the GSoC 2020 program, the front matter of `_blog/gsoc20/testing/index.md` should look like this:- 

```
---
title: "testing"
layout: page
author: "<Your Name>"
tags: ["project","gsoc", "gsoc20"]
---
```

*title* : The title of the page. The title would be displayed on the top of the page. Furhter the same title would be shown on the previous page where the projects of the program are listed.

*layout* : Always keep it to "page" only.

*author* :  The name of Author. Please keep the name inside quotes(\"\").If more than 1 authors, make it a list ["author1","author2"].

*tags* : These are the tags that would be assigned to the page. Please assign the tags accordingly, bcz based on the tags, the pages would be shown in the **Tags** tab.

## How to Write Blogs for the program?

So, if you have been assigned a project for a program, for that there would be having a folder for you in the `_blog/<program_name>/<project_name>`.

Various blogs pages have already been made in the folder.

```
_blog/<program_name>/<project_name>
├── index.md
└── posts
   ├── 01_week1.md
   ├── 02_week2.md
   ├── 03_week3.md
   ├── 04_week4.md
   ├── 05_eval1.md
   ├── 06_week5.md
   ├── 07_week6.md
   ├── 08_week7.md
   ├── 09_week8.md
   ├── 10_eval2.md
   ├── 11_week9.md
   ├── 12_week10.md
   ├── 13_week11.md
   ├── 14_week12.md
   └── 15_eval3.md
```

Here the `<project_name>/index.md` contains the summary of the complete project. This can be seen as a final report which would be written at the end of the program summarizing the complete project. But don't forget to fill the front matter of the `<project_name>/index.md`. The front matter of should look like this:- 
```
---
title: "<project_name>"
layout: page
author: "<your_name>"
tags: ["project","gsoc", "gsoc20"]
---
```

*title* : The title of the page. The title would be displayed on the top of the page. Furhter the same title would be shown on the previous page where the projects of the program are listed.

*layout* : Always keep it to "page" only.

*author* :  The name of Author. Please keep the name inside quotes(\"\").If more than 1 authors, make it a list ["author1","author2"].

*tags* : These are the tags that would be assigned to the page. Please assign the tags accordingly, bcz based on the tags, the pages would be shown in the **Tags** tab.

All the blogs posted in the `<project_name>/posts` would be shown at the bottom of the project page. These blogs would be displayed in the order of filename therefore, they have been numbered.

In the current system, we have 2 types of blogs in the `<project_name>/posts` section i.e. `eval` and `week`. 

- `week` blogs must have tags  `[ "week","week#n","eval#m"]` where `n` is the week number and `m` is the eval number that week comes into. This page conatins the compiled work done every week in form of a report. Further, it must contain, a small summary of every day work which was done. 

- `eval` blogs must have tags `["eval","gsoc","gsoc2020","eval#m"]` where m is the eval number. This contains the compiled report of the work done in a month. 

