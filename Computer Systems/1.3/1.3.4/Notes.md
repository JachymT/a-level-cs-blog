# Web Technologies

## Search Engine Indexing
When using a search engine, information is retrieved from the search engines index. Allows for fast and relevant information access.

### Web crawlers
crawls through all webpages on the WWW using **hyperlinks** to go to an subsequent web pages Data like metadata, contents, and the url is saved to a huge index of webpages. 

### Metatags
They are keywords relating to the content. Exist in the header tag and are not vissible to the user. Improve the chances of discovery and help the webcrawler decide on the category of the page.

## Page Rank Algorithm
Used to order pages by usefulness, relevance and authority, based on the pagerank of pages linking to it

![image](https://user-images.githubusercontent.com/72783315/165080503-b9be8d08-ed2f-4364-abfd-d1c424935e79.png)

- **PR(A)** is the PageRank of page A 
- **PR(Tn)** is the PageRank of pages Tn which link to page A
- **d** is the damping factor (start by assuming that it is 0.85). The dampening factor is how likely a user is to stop following hyperlinks, or that a website may be accessed directly by url, or how long it will take to get to that webpage.
- **C(Tn)** is the number of outbound links on page Tn, including the link to page A

**inbound links** - external links pointing to a page :point_right: :point_left:

**outbound links** - links on a page pointing to external pages :point_left: :point_right:

Start by assuming the rank of each page is 1 and then iterate untill they sum to the total number of pages. Use the algorithm for all pages to page n. In reality this can be thousands of iterations. 

During an iteration dont change the inputs for each page rank, eg iteration 1: A=1, B=1, C=1...

### factors that can affect web page rank
- domain name
- quality of inbound links
- umber of inbound links
- domain age
- key words
- magnitude of updates
- keyword density

## Server and client side processing
