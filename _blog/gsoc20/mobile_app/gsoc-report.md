# Google Summer of Code 2020: Final Project Report

This is an outline of the work done from June to August 2020 under the [Cuneiform Digital Library Initiative (CDLI)](https://cdli.ucla.edu/), as part of Google Summer of Code 2020 program.

## Project Overview

The **Revamp CDLI tablet apps (Apple and Android)** project aims to recreate the existing CDLI tablet app using Flutter, Google's open-source UI software development kit, and provide a web admin interface for the mobile app data entry and management inside the CDLI framework. Besides its existing components, the new mobile application offers additional features for a highly-customized UX.

### Team

**Student developer:** Anila Hoxha

**Mentor:** M. Willis Monroe

## Work Done 

### Milestones

- [x] Recreate the existing CDLI tablet app using Flutter. 
- [x] Implement additional app features for a highly-customized UX. 
- [x] Provide a web admin interface for the mobile app data entry and management. 
- [x] Display the entries in the web with the same functionalities as in the mobile app.

### Contributions

The code I've written for the revamped mobile apps: [Source Code](https://github.com/anila-a/cdli-tablet-app) : [List of Commits](https://github.com/anila-a/cdli-tablet-app/commits/master)

My contributions to the CDLI framework repository:

  - Add cdli tablet feature to admin panel: [!154](https://gitlab.com/cdli/framework/-/merge_requests/154) : [List of Commits](https://gitlab.com/cdli/framework/-/merge_requests/154/commits)
  - Add instructions for framework installation on WSL 2 backend: [!179](https://gitlab.com/cdli/framework/-/merge_requests/179) (Merged) : [List of Commits](https://gitlab.com/cdli/framework/-/merge_requests/179/commits)

**Tools and Technologies used:** Flutter, CakePHP, Docker, Bootstrap

### Results

#### Mobile app

To watch the CDLI tablet app demo video, click [here](https://drive.google.com/file/d/1Bq09m2OeLeuMyPTsHOtFYWRPYYAp6cK-/view?usp=sharing).

<p float="left">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_1.jpg" alt="Splash Screen" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_2.jpg" alt="Page Layout" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_3.jpg" alt="Sliding Up Panel" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_4.jpg" alt="Dashboard" width="225" height="400">
</p>

<p float="left">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_5.jpg" alt="Grid Layout" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_6.jpg" alt="List Layout" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_7.jpg" alt="Help & Feedback" width="225" height="400">
  <img src="https://github.com/cdli-gh/blog/blob/gh-pages/_blog/gsoc20/mobile_app/img/Screenshot_8.jpg" alt="Search" width="225" height="400">
</p>

#### Web admin interface

To watch the admin interface demo video, click [here](https://drive.google.com/file/d/1KeBs4PmL-rrZJnEcRdPraN7KEjOPF609/view?usp=sharing).

### Weekly Reports

All reports written in the coding period:

| Month      | #1            | #2  | #3  | #4  | #eval  |
| :--------: |:-------------:| :-----: | :-----: | :-----: | :-----: |
| **June**   | [week 1](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/01_week1)  | [week 2](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/02_week2)  | [week 3](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/03_week3)  | [week 4](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/04_week4)  | [eval 1](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/05_eval1)  |
| **July**   | [week 5](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/06_week5)  | [week 6](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/07_week6)  | [week 7](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/08_week7)  | [week 8](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/09_week8)  | [eval 2](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/10_eval2)  |
| **August** | [week 9](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/11_week9)  | [week 10](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/12_week10)  | [week 11](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/13_week11)  | [week 12](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/14_week12)  | [eval 3](https://cdli-gh.github.io/blog/gsoc20/mobile_app/posts/15_eval3)  |

## Future Work

Points of possible improvement / resumed work in the project include:

- Connect the app to the new API.
