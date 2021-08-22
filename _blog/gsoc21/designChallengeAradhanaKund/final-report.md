<h1 align="center"> Google Summer of Code 2021 </h1>
<p align="center"><i>with</i> </p>
<h2 align="center"><a href="https://summerofcode.withgoogle.com/organizations/4724093699489792/">Cuneiform Digital Library Initiative (CDLI)</a></h2>

<h2 align="center"><i>Project Report on "<a href="https://summerofcode.withgoogle.com/projects/#5212285703815168">Design Challenge</a>" </i> </h2>

## About the project

The aim of the project was to enhance the UI, UX and accessibility of CDLI Users. Also this project aims to re-unify the design so as to bring more interaction between the  user and the website.

## Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:man_technologist: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) | PR |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- | ---------------------- |
| 1 | :heavy_check_mark: | Redesigning and Implementing the periods page | Implementing periods page for web/tab/mobile view | [#251](https://gitlab.com/cdli/framework/-/issues/251) | [!305](https://gitlab.com/cdli/framework/-/merge_requests/305) |
| 2 | :heavy_check_mark: | Implementing Admin Dashboard | Implementing web/tab/mobile view of admin dashboard | [#75](https://gitlab.com/cdli/framework/-/issues/75) | [!351](https://gitlab.com/cdli/framework/-/merge_requests/351) |
| 3 | :heavy_check_mark: | Resources Page | Implementing web/tab/mobile view of about us and Resources Page | [#209](https://gitlab.com/cdli/framework/-/issues/209) | [!344](https://gitlab.com/cdli/framework/-/merge_requests/344) |
| 4 | :heavy_check_mark: | Add functiionality for no-js and footer styling | Making dropdowns work for no-js and fixing footer discrepancies. | [#214](https://gitlab.com/cdli/framework/-/issues/214) | [!346](https://gitlab.com/cdli/framework/-/merge_requests/346), [!333](https://gitlab.com/cdli/framework/-/merge_requests/333) |
| 5 | :heavy_check_mark: | Accordion styling and accessibility fix. | The old accordions have enhanced styling and accessibility for js as well as no-js users. | [#660](https://gitlab.com/cdli/framework/-/issues/660) | [!361](https://gitlab.com/cdli/framework/-/merge_requests/361), [!364](https://gitlab.com/cdli/framework/-/merge_requests/364) |
| 6 | :heavy_check_mark: | About Us | Implementing web/tab/mobile view of About us. | [#591](https://gitlab.com/cdli/framework/-/issues/591) | [!353](https://gitlab.com/cdli/framework/-/merge_requests/353) |
| 7 | :heavy_check_mark: | Error Page | Improvise and Implement the Error Page | [#334](https://gitlab.com/cdli/framework/-/issues/334) | [!353](https://gitlab.com/cdli/framework/-/merge_requests/353) |
| 8 | :heavy_check_mark: | Single Artifact View | Improvise the Single Artifact View | [#517](https://gitlab.com/cdli/framework/-/issues/517) | [!359](https://gitlab.com/cdli/framework/-/merge_requests/359) |

## Links

- [Proposal](https://drive.google.com/file/d/1IxvKMPuqsF4AeSep5AUcHRAQ_ZxyC1ZN/view)
- [Weekly Blogs](https://github.com/cdli-gh/blog/tree/gh-pages/_blog/gsoc21/designChallengeAradhanaKund/posts)
- [Project Repository](https://gitlab.com/cdli/framework)

## Team

- [Aradhana Kund] - Mentee
- [Émilie Pagé-Perron] - Mentor
- [David Wong] - Mentor
- [Amaan Iqbal] - Mentor

## Technologies

- CakePHP 3
- SASS
- Javascript
- Bootstrap
- HTML

1. ### Redesigned and implemented the periods page
   
    - Redesigned and implemented the responsive and fully accessible layout of the periods page. This provides a better User Interface and User experience to all the users of CDLI.
    - Associated PR ( [!305](https://gitlab.com/cdli/framework/-/merge_requests/305) )
    
      <center>

      | Periods Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 12-59-28](https://user-images.githubusercontent.com/73130056/130346459-db013fac-f8a6-49b3-b2e6-81a8f2f56d13.png) |
      | ![Screenshot from 2021-08-22 13-01-21](https://user-images.githubusercontent.com/73130056/130346562-73458b70-d50d-44c5-a488-3082b5af0b31.png) |
      | Web View |

      </center>
      
       <center>

      | Periods Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-07-18](https://user-images.githubusercontent.com/73130056/130346619-677087ab-3ebb-46bf-8a30-e4d42c12d693.png) |
      | ![Screenshot from 2021-08-22 13-07-43](https://user-images.githubusercontent.com/73130056/130346627-a01becef-c749-4173-aa9c-d978153e9ce1.png) |
      | Tablet and Mobile Screen View |

      </center>
      
2. ### Implemented the Administrative Dashboard
   
    - Implemented the responsive and fully accessible layout of the Administrative Dashboard which contains different sections visible according to the access. This provides a better User Interface and User experience to the admins and editors.
    - Associated PR ( [!351](https://gitlab.com/cdli/framework/-/merge_requests/351) )
    
      <center>

      | Administrative Dashboard |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-26-34](https://user-images.githubusercontent.com/73130056/130347078-bebf596c-d893-4169-a485-cca188ee63e0.png) |
      | ![Screenshot from 2021-08-22 13-25-58](https://user-images.githubusercontent.com/73130056/130347084-900cf14e-780b-491c-bd36-fd521d4f4f92.png) |
      | Web View |

      </center>
      
       <center>

      | Administrative Dashboard |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-28-29](https://user-images.githubusercontent.com/73130056/130347150-d426ef88-8b8e-47e8-b727-badf9215c829.png) |
      | ![Screenshot from 2021-08-22 13-28-54](https://user-images.githubusercontent.com/73130056/130347160-d183b74c-aba6-411b-8b22-6d96a228928f.png) |
      | Tablet and Mobile Screen View |

      </center>

3. ### Implemented the Resources Page
   
    - Implemented the responsive and fully accessible layout of the Resources Page which contains cards on large screen view and accordions for medium and small screens (both js and no-js accessible). This provides a better User Interface and User experience to all the users of CDLI.
    - Associated PR ( [!344](https://gitlab.com/cdli/framework/-/merge_requests/344) )
    
      <center>

      | Resources Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-40-29](https://user-images.githubusercontent.com/73130056/130347430-39c62f5d-cc15-4b77-ae6a-55d45155df63.png) |
      | Web View |

      </center>
      
       <center>

      | Resources Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-41-25](https://user-images.githubusercontent.com/73130056/130347468-072c719f-bd33-42c3-b682-401dae90a450.png) |
      | Tablet and Mobile Screen View |

      </center>
      
4. ### No-js dropdown fix and footer styling discrepancies fix
   
    - Made the dropdowns work for no-js as well. Earlier the dropdowns were working on click for js only. Now the dropdowns work on hover for no-js and on click for js. Also fixed some footer discrepancies.
    - Associated PR ( [!346](https://gitlab.com/cdli/framework/-/merge_requests/346), [!333](https://gitlab.com/cdli/framework/-/merge_requests/333) )
    
      <center>

      | JS and no JS dropdown respectively |
      | :---:	|
      | ![Screenshot from 2021-08-22 13-49-08](https://user-images.githubusercontent.com/73130056/130348085-43e3fc51-20bf-4c96-839b-3e1ee7335018.png) |
      | ![Screenshot from 2021-08-22 14-00-00](https://user-images.githubusercontent.com/73130056/130348097-22784c42-3601-4397-a9f0-99af829af197.png) |
      | On click for js and on hover for no-js |

      </center>
      
       <center>

      | Footer Styling Discrepancy fix |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-06-11](https://user-images.githubusercontent.com/73130056/130348107-c6da6417-8dd7-45be-bc66-e45f9c301363.png) |

      </center>
      
 5. ### Accordion styling and accessibility fix
   
    - Enhanced the styling of accordions with hover effect, extra styling and smooth arrow toggle for both js and no-js. All the accordions of CDLI (Administrative Dashboard accordions, Resources Page accordions, Single Artifact accordions and Search Result accordions) have been updated with enhanced styling and accessibility.
    - Associated PR ( [!361](https://gitlab.com/cdli/framework/-/merge_requests/361), [!364](https://gitlab.com/cdli/framework/-/merge_requests/364) )
    
      <center>

      | Admin Dashboard Accordions |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-21-56](https://user-images.githubusercontent.com/73130056/130348801-4312ee43-84d3-4275-97f9-4b91486227a1.png) |
     
      </center>
      
       <center>

      | Resources Page accordions |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-22-17](https://user-images.githubusercontent.com/73130056/130348793-9d0fc1bc-2821-445c-8993-0e94be86230e.png) |

      </center>
      
      <center>

      | Search Result accordions |
      | :---:	|
      | ![Screenshot from 2021-07-20 23-36-59](https://user-images.githubusercontent.com/73130056/130353181-2967ef12-3007-46ba-87f5-f629408a38a2.png) |

      </center>
      
      <center>

      | Single Artifact accordions |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-25-21](https://user-images.githubusercontent.com/73130056/130348826-1989844c-0557-4af5-b271-745a95de5786.png) |

      </center>

6. ### About Us Page
   
    - Implemented the About Us page with a story timeline which is js and no-js accessible.
    - Associated PR ( [!353](https://gitlab.com/cdli/framework/-/merge_requests/353) )
    
      <center>

      | About Us Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-37-08](https://user-images.githubusercontent.com/73130056/130349451-d6ec5534-2f5b-483f-8d0d-bed86b44ff44.png) |
      | ![Screenshot from 2021-08-22 14-37-27](https://user-images.githubusercontent.com/73130056/130349461-df31f6a4-12f7-403e-80d8-d94fa9d95d11.png) |
      | ![Screenshot from 2021-08-22 14-37-48](https://user-images.githubusercontent.com/73130056/130349469-fb48a936-5c1c-445a-8895-0453a894c25d.png) |
      | Web view |  
   
      </center>
      
      <center>

      | About Us Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 14-38-31](https://user-images.githubusercontent.com/73130056/130349494-94f284ad-ebbd-4226-b07e-aa183f90514c.png) |
      | ![Screenshot from 2021-08-22 14-38-52](https://user-images.githubusercontent.com/73130056/130349497-b11beec5-2fce-4504-8da6-bd16a0f7ef0e.png) |
      | ![Screenshot from 2021-08-22 14-39-39](https://user-images.githubusercontent.com/73130056/130349503-2cc40794-1eb8-4912-8830-3b8d15a55624.png) |
      | Tablet and mobile screen view |  
   
      </center>
      
 7. ### Error Page
   
    - Implemented new design of the Error Pages.
    - Associated PR ( [!353](https://gitlab.com/cdli/framework/-/merge_requests/353) )
    
      <center>

      | Error Page |
      | :---:	|
      | ![Screenshot from 2021-07-12 16-03-36](https://user-images.githubusercontent.com/73130056/130349633-92c0fba0-6775-4f77-bde0-f668822848fc.png) |
   
      </center>
      
 8. ### Single Artifact View Page
   
    - Implemented the new design of Single Artifact View Page, also rendered the data according to the issue description given ([#517](https://gitlab.com/cdli/framework/-/issues/517)).
    - Associated PR ( [!359](https://gitlab.com/cdli/framework/-/merge_requests/359) )
    
      <center>

      | Single Artifact View Page |
      | :---:	|
      | ![Screenshot from 2021-08-22 15-01-27](https://user-images.githubusercontent.com/73130056/130350193-13d77280-559c-4efb-bd53-c1c1a8ee52d9.png) |
      | ![Screenshot from 2021-08-22 15-02-00](https://user-images.githubusercontent.com/73130056/130350198-2b629d9d-0f00-4ad8-96ad-53cda1fdf24b.png) |
      | ![Screenshot from 2021-08-22 15-02-31](https://user-images.githubusercontent.com/73130056/130350202-e20af5e9-ceed-42ea-9297-fd9c61a6b521.png) |
   
      </center>
      
## To Do (Post GSoC)

* Work on providing more content to the Browse and Periods Documentation prepared.
* Work on Additional Objectives which are partially completed.

## Acknowledgement

* I would like to thank my mentors Émilie Pagé-Perron, David Wong and Amaan Iqbal for always supporting me and helping me out to overcome all the challeneges I faced. I would like to thank them for encouraging me to be able to complete my deliverables. This project really helped me enhnace my coding and open source skills. 
* I would like to thank the entire CDLI community for giving me the essence of Open Source in such a cooperative and informative environment. 
* I would finally like to thank Google Summer of Code for providing me with this opportunity and exposing me to a community of like minded people. 
