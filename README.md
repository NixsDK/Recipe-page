# Frontend Mentor - Recipe page solution

This is a solution to the [Recipe page challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/recipe-page-KiTsR8QQKm). Frontend Mentor challenges help you improve your coding skills by building realistic projects. 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

**Note: Delete this note and update the table of contents based on what sections you keep.**

## Overview

### Screenshot

![Desktop layout](assets/images/Screenshot%202025-07-11%20162710.png)  
![Ingredients section](assets/images/Screenshot%202025-07-11%20162852.png)  
![Instructions section](assets/images/Screenshot%202025-07-11%20162943.png)  
![Nutrition section](assets/images/Screenshot%202025-07-11%20162959.png)  
![Mobile view](assets/images/Screenshot%202025-07-11%20163016.png)

### Links

- Solution URL: [Add solution URL here](https://your-solution-url.com)
- Live Site URL: [Add live site URL here](https://your-live-site-url.com)

## My process

### Built with

- Semantic HTML5
- CSS3
- Flexbox
- Mobile-first design
- Manual responsiveness (no frameworks)
- https://www.w3schools.com
- https://css-tricks.com


### What I learned

While building this project, I learned the importance of semantic HTML structure and how Flexbox behaves differently on 
mobile when switching flex-direction. I also learned how nesting elements like <h4> inside a .value div can override 
inherited styles — and why it's better to use CSS for styling rather than semantic tags for appearance.
To see how you can add code snippets, see below:

```html
<div class="row">
  <div class="label">Calories</div>
  <div class="value">277kcal</div>
</div>
<div class="row">
  <div class="label">Carbs</div>
  <div class="value">0g</div>
</div>
<div class="row">
  <div class="label">Protein</div>
  <div class="value">20g</div>
</div>
<div class="row">
  <div class="label">Fat</div>
  <div class="value">22g</div>
</div>
```css
.row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom:  1rem;
}
.prep-time {
  background-color: hsl(330, 100%, 98%);
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
}

.prep-time h2 {
  color: hsl(332, 51%, 32%);
}
```

### Continued development

I want to improve my confidence with Flexbox alignment on different screen sizes and explore more semantic HTML like
when to use <section>, <main>, and <article>. I also plan to practice using Google Fonts more intentionally.

### Useful resources

- [Example resource 1](https://developer.mozilla.org/en-US/docs/Web/CSS/flex) - Helped me understand how to align .row content on small screens.
- [Example resource 2](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) - Used this to troubleshoot spacing between .label and .value.


## Author

- Frontend Mentor - [@yourusername](https://www.frontendmentor.io/profile/NixsDK)



## Acknowledgments

This project was done solo pretty simple project, looked for ideas online how to make the design.


