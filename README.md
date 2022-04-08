# Projects for CS50's Web Programming with Python and JavaScript
**Syllabus**: https://cs50.harvard.edu/web/2020/

## Content
1. Project 0: Search
2. Project 1: Wiki

***

## Project 0: Search

**Video demonstration**: https://www.youtube.com/watch?v=G7krIOm8_bA

**Description**: Website with 3 pages, one for Google Search, one for Image Search and one for Advanced Search. The basic functionality was relatively easy to figure out, the most difficult part was to Style the website with CSS. It uses Flexbox. It's not responsive yet.

**Forms**
- action attribute points to "https://google.com/search"
- name attribute from the input defines the "key" for the type of search
- value attribute from the input defines the text that we want to search
- When the form is submitted, the key-value pairs are concatenated to the url in the action

**CSS Styles**
- The CSS Styles try to resemble the aesthetics from Google

**Files**
- index.html
- imageSearch.html
- advancedSearch.html
- styles.css

***

## Project 1: Wiki

**Video demonstration**: https://www.youtube.com/watch?v=3QKBt80TfT8

**Description**: Wiki web app created with Python and the Django framework.

### Specification
- On the **Index Page** the user can navigate to each entry by clicking on it's title. 
- The user can **Search** entries.
    - A matching query will take the user directly to the resulting page.
    - A partially matching query (the query is a substring of one or more entries's title) will take the user to a **Search Results** page, where he can click any of the results to be redirected to the entry's page.
- The user can create a **New Page**
    - The user can write the content in Markdown syntax
    - If the entry's title already exists, the user is redirected to an Error Page
    - If the entry's title is new, the entry is saved
- The user can **Edit** entries
    - An edit button is available on each entry's page
    - Once the entry is saved, the user is redirected to that entry's page
- **Random Page**: Clicking "Random Page" takes the user to a random entry.

### Version history

#### V1: 2022-April-06
Web app already working correctly, but I've not used redirections at the end of functions like random_page, new_page, edit_page... Instead they just render the page and the content at the end of the functions. This functions often use the "POST" method to get some data, so when the page is reloaded, the data is sent again (like submiting a form). I tried to use **HttpResponseRedirect** and **reverse**, but always got an Error Message from Django. Tomorrow's mission is to fix this and submit the Project! 

#### V2: 2022-April-07
I figured out what the problem is! **HttpResponseRedirect** only accepts the URL, so I need to create it as a string to pass it to that function. To create the string I can use **reverse**, but I wasn't able to get it to work, so I decided to create the strings manually.
Then, **HttpResponseRedirect** should only get an URL, so if I want to send more data, it should be part of the URL. In the cases where I needed to send some data, that's exactly what I did, and I adjusted the **urlpatterns** and the **views** accordingly.

#### Issues
The app is now working correctly, as far as the specification requires. There are some things I wans't able to achieve:
- No session
- Not using the form tools from Django, just manually creating the forms
