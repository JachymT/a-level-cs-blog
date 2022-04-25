# Web Technologies

## Search Engine Indexing
When using a search engine, information is retrieved from the search engines index. Allows for fast and relevant information access.

### Web crawlers
crawls through all webpages on the WWW using **hyperlinks** to go to an subsequent web pages Data like metadata, contents, and the url is saved to a huge index of webpages. 

### Metatags
They are keywords relating to the content. Exist in the header tag and are not vissible to the user. Improve the chances of discovery and help the webcrawler decide on the category of the page.

## Page Rank Algorithm
Used to order pages by usefulness, relevance and authority

![image](https://user-images.githubusercontent.com/72783315/165080503-b9be8d08-ed2f-4364-abfd-d1c424935e79.png)

- **PR(A)** is the PageRank of page A 
- **PR(Ti)** is the PageRank of pages Ti which link to page A
- **d** is the damping factor (start by assuming that it is 0.85). The dampening factor is how likely a user is to stop following hyperlinks, or that a website may be accessed directly by url, or how long it will take to get to that webpage.
- **C(Ti)** is the number of outbound links on page Ti

Start by assuming the rank of each page is one and then iterate untill they sum to 

**inbound links** - external links pointing to a page

**outbound links** - links on a page pointing to external pages

### factors that can affect web page rank
- domain name
- quality of inbound links, number of inbound links, domain age, key words, magnitude of updates, keyword density

## Server and client side processing
