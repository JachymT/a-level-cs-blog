# Web Technologies

## Client-server architecture

![image](https://user-images.githubusercontent.com/72783315/165905951-aefd0e4d-af1b-4906-82eb-0c08619118f7.png)

Most services on the internet use this model. Providers of resources are designated as **servers** and make responses to requests made by **clients**. Resources may be web pages, files, emails and other communications. A server or client is not determined by hardware as most devices can be both, such as a laptop running a FTP and a web server. 

A web server is always listening and anticipating requests, without it the resources for the website cannot be accessed.

A web browser is a client service, that makes reqeuests to the right server in a format that matches, and then waits for a response.

## Client side processing
The processing that happen on the users local device. Most webpages use some client side processing. Client side scripting can be done with javascript and those Scripts are interpreted in the browser. Cookies are an example of client side data. Using an old version of a browser can let malicious websites use vunerabilites.

**Advantages**
- Immediate response
- Quick execution
- Reduced load on the server
- Used for validating forms
- Used for controlling the look of a website and creating interative, personalised features.

![image](https://user-images.githubusercontent.com/72783315/165909418-2f4db4a5-9be1-4095-bd23-36e0700c098c.png)

## Server-side processing
The processing that happen on a server. Databases are servers that can be accessed by backend scripts such as PHP, SQL, ASP.net and Python. Server side scripts are processed entirely on the server and cannot be viewed by the client

**Advantages**
- can perform large calculations
- not browser dependent
- theremore more secure

![image](https://user-images.githubusercontent.com/72783315/165909571-ea8631f6-b7ba-4d19-944f-dc6b06edfac8.png)

(notes from isaac)[https://isaaccomputerscience.org/concepts/net_internet_client_server_model?examBoard=all&stage=all]

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
