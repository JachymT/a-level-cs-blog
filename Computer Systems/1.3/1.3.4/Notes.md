# HTML
## HTML 
Section from the spec below. HTML is the script web pages are written in, 

`<html>` first line after <!DOCTYPE html>, interprets code as HTML

`<link href="stylesheet.css" rel="stylesheet" type="text/css"` to link to a CSS file

`<head>` websites properties and browser tab area

`<title>` text appearing within the tab

`<body>` main content of webpage

`<h1>` `<h2>` `<h3>` headings in decending size

`<img src="">` including the src (image file source), alt, height and width attributes.

`<a href="">` including the href (link destination) attribute. To create a hyperlink

`<div id="box">` divides a page with the id given

`<form>` to get user inputs

`<input>` where the input is a textbox (i.e. has the attribute type=”text” and another attribute name to identify it) or a submit button (i.e. has the attribute type=”submit”)

`<p>` text goes in here

`<li>` defines a list

`<ol>` ordered elements of a list are added with this

`<ul>` bulleted elemets of a list are added with

`<script>` javascript goes in here

## CSS
section from the spec below. Cascading style sheets are used to describe the style of a webpage. Remeber semi-colons after each element.

inline css:  `<h1 style= "font-size: 18px;">`

external css (can also be in the style tag in the HTML file):

```css
h1{
  font-size: 18px;
}
```

Classes are linked with `.class`

```css
.infoBox{
  background-color: green;
}
```

identifiers (id) are linked with `#id`

```
#menu{
  background-color: #A2441B;
}
```

The following properties can come up

```
background-color      // named colors and hex colors
border-color
border-style
border-width
font-family
font-size
height
width
```

## JavaScript 
Section from the spec below. JS is a scripting language which primarily exists to add interactivity to websites. It is interpreted and not compiled. Can be used to validate client input data. The advantage is that servers don't have to validte the data, it can all be done within the webpage, easing the load on servers.

JavaScript can be used to retrieve inputs. You do not have to know about this, any other JS will be explained in the question

**Outputs**

Changing the attributes of a HTML element:
```js
chosenElement = document.getElementById(“example”);
chosenElement.innerHTML = “Hello World”;
```

Writing directly to the document (overwriting the old document):
```js
document.write(“Hello World”);
```

 Displaying an alert pop-up box:
 ```js
alert(“Hello World”);
```
