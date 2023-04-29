# Code in Spec
## HTML 
**Section from the spec below**. HTML is the script web pages are written in:

to link to a CSS file
```html
<link href="stylesheet.css" rel="stylesheet" type="text/css">
``` 

`<head>` websites properties and browser tab area

`<title>` text appearing within the tab

`<body>` main content of webpage

`<h1>` `<h2>` `<h3>` headings in decending size

`<img src="">` including the src (image file source), alt, height and width attributes. **Does not need a closing tag**

`<a href="">` including the href (link destination) attribute. Creates a hyperlink

`<div id="box">` divides a page with the id given

`<form>` to get user inputs

`<input>` where the input is a textbox (i.e. has the attribute type=”text” and another attribute name to identify it) or a submit button (i.e. has the attribute type=”submit”)

`<p> </p>` text goes in here 

`<script> </script>` javascript goes in here 

```html
<ul>
  <li> text </li> <!-- Unordred list item -->
</ul>

<ol>
  <li> text </li> <!-- Ordered list item -->
</ol>
```

**Not in the spec:**

```html
<b> Bold text </b>        <!-- These can be inside <p> tags -->
<i> Italic text </i>
<u> Underlined text </u>
```

## CSS
section from the spec below. Cascading style sheets are used to describe the style of a webpage. Remeber semi-colons after each element.

### inline css

`<h1 style= "font-size: 18px;">`

disadvantages:
- slower access time as css needs to be reloaded for each page
- css needs to be rewritten for each web page

### external css (linked css file)

```css
h1{
  font-size: 18px;
}
```

advantages:
- easier to maintain and add new content - css will follow he same rules
- css links to every page and so gives a consistent look
- only a single change needs to be made to change the font on all webpages 

### Classes
Linked with `.class` , Classes can be linked to **multiple elements**

```html
<div class="infoBox">
```

```css
.infoBox{
  background-color: green;
}
```

### Identifiers (id)
Linked with `#id` , Identifiers can only be linked to a **single element**

```html
<div id="menu">
```

```css
#menu{
  background-color: #A2441B;
}
```

### The following properties can come up

```css
background-color      /* named colors and hex colors */
border-color
border-style
border-width
font-family           /* affects text */
font-size
color
height
width
```

## JavaScript 
Section from the spec below. JS is a scripting language which primarily exists to add interactivity to websites, by embeding it into HTLM. It is interpreted and not compiled. Can be used to validate client input data. The advantage is that servers don't have to validte the data, it can all be done within the webpage, easing the load on servers.

JavaScript can be used to retrieve inputs, but any input code will be explained in the Question

**Outputs**

Changing the attributes of a HTML element:
```js
chosenElement = document.getElementById("menuText");
chosenElement.innerHTML = "Hello World";
```

Writing directly to the document (overwriting the old document):
```js
document.write(“Hello World”);
```

 Displaying an alert pop-up box:
 ```js
alert(“Hello World”);
```
