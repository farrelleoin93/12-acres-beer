## Contents

- [User Stories](#user-stories)
- [Manual Testing](#manual-testing)
- [Automated Testing](#auto-testing)
- [Responsiveness](#responsiveness)
- [Bugs](#bugs)

### As an unregistered user I want the ability to...
**easily navigate the site so that I can find what I am looking for**

- The navbar has clear and descriptive words so that the user will be able to easily navigate through the website.

**search for beers so that I can quickly find beers that I am interested in**
- The user can enter any word into the seach bar in the navbar and they will be redirected to the beers page. This page will only display beers that contain the queried word in their name and/or description.

**filter beers so that I can find specific types of beer**
- On the beers page their are buttons at the top labeled: All beers, Ale, Lager and Stout, if the user clicks one of these buttons only the relevant beers are displayed.

**read details about each beer so that I can see if it is the type of beer tha I want**
- If the user clicks on a specific beer on the beers page they are brought to a beer details page where they can read about the beer, see the alcohal percentage, reviews and more.

**see what pubs and shops sell the beers so that I can have another way to buy them other than the website**
- On the find our beers page the user can click one of two buttons (Off-licenses or Bars and Restaurants). When they click a button markers appear on the Google maps feature showing them the location of either te off-licences or bars that stock 12 Acres beer.

**access contact details so that I can get in touch with 12 Acres**
- The Contact us page is available to all users of the website. On this page the user enters their details and message into a form and an email is sent to 12 Acres from their email account.

**easily register an account so that I can use the site easier in the future**
- The sign up page is easily accessible from the navbar and contains a small straight forward form for the user to fill in their details. They then just need to confirm there email address by clicking on a link that can be found in their email inbox.

### As a registered user I want the ability to...
**log in and log out of my profile account so that my personal information will be safe**
- Log in and log out links can be easily accessed from the navbar.

**store my details for later so that I can avoid having to fill in my details each time**
- Each user has a profile page where they can fill in and save their personal information if they wish to.

**leave a review so that I can inform future users about the beer**
- If the user is registered they can leave a review for a beer via a form on the beer details page. If they are not registered they can not.

**update my details so that I can update address and other details in case they change**
- This can be easliy done via the form on the user's profile page.

**store my order history so that I can access my previous orders**
- When a registered user orders something the order details are automatically saved to their profile page.

**review my purchase at the checkout so that I can decide whether to add or edit the order before confirming**
- On the checkout page where the user fills in their information an order summary is displayed so that the user can easily review the order details.

**Make secure payments so that I can ensure that my payments are securely handled**
- Stripe provides the security for payments.

**receive email confirmation of my order so that I can confirm that my order was sucessful.**
- Once an order is successfully made a confirmation email is sent to the email address provided by the user.

### As site admin/superuser I want the ability to...
**add new beers to the website so that I can continuously make new beers available**
- An add beer page is easily accssible to the superuser via the navbar

**edit existing beers so that I can update the website**
- The admin/superuser can access an edit beer form via an edit button on all beer details pages.

**delete existing beers so that I can delete beers that 12 Acres do not make anymore**
- The admin/superuser can delete a beer by clicking on a delete button on the beer detail page.

**create blogs so that I can inform users about any developments at the company**
- An add blog page is easily accssible to the superuser via the navbar

**update blog entries so that I can update users on any developments at the company**
- The admin/superuser can access an edit blog form via an edit button on all blog posts.

**delete blog posts so that I can remove blog posts**
- A delete button is located on each blog post.

## <a name="manual-testing">Manual Testing</a>

The following tests have been carried out without issue:


**Top navbar**

- Confirm clicking the 12 Acres logo in the top navbar directs the user to the home page.
    - CHECK

- Confirm that entering a word into the search box brings the user to the beers page and only beers containing the relevant word are displayed.
    - CHECK

- Confirm that cicking the bag icon brings the user to the shopping bag page.
    - CHECK

- Reduce the screen size to mobile and tablet screen sizes to confirm that the search bar collapses into a search icon.
    - Check


#### If user is not logged in
- Confirm that the "Register" option in the "My Account" dropdown menu brings the user to the "Sign Up" page.
    - CHECK

- Confirm that the "Login" option in the "My Account" dropdown menu brings the user to the "Sign In" page.
    - CHECK


#### If user is logged in
- Confirm that the "Logout" option in the "My Account" dropdown menu brings the user to the "Sign Out" page.
    - CHECK

- Confirm that the "Profile" option in the "My Account" dropdown menu brings the user to their "Profile" page.
    - CHECK


#### If admin/superuser is logged in
- Confirm that the "Add Beer" option in the "My Account" dropdown menu brings the user to the "Add Beer" page.
    - CHECK

- Confirm that the "Add Blog" option in the "My Account" dropdown menu brings the user to the "Add Blog" page.
    - CHECK

- Confirm that the "Profile" option in the "My Account" dropdown menu brings the user to their "Profile" page.
    - CHECK

- Confirm that the "Logout" option in the "My Account" dropdown menu brings the user to the "Sign Out" page.
    - CHECK


**Bottom navbar**
- Confirm that all the navigation links bring the user to the relevant pages.
    - CHECK

- Reduce the screen size to mobile and tablet screen sizes to confirm that the navigation links collapse into a burger menu.
    - Check


**Home page**
- Confirm that the "Shop" button brings the user to the beers page.
    - CHECK


**Beers page**
- Confirm that all beers are displayed by default.
    - CHECK

- Confirm that clicking on the buttons filters the beers by the appropriate beer type.
    - CHECK

- Confirm that clicking on a beer brings the user to the beer details page for that beer.
    - CHECK


**Beer details page**
- Confirm that the plus and minus buttons adjust the quantity properly.
    - CHECK

- Confirm that the quantity can not go below one or above 99.
    - CHECK

- Confirm that the "Add to bag" button adds the beer with the correct quantity to the shopping bag and that a toas appears showing this.
    - CHECK

- Confirm that the "Buy more beer" button brings the user back to the beers page.
    - CHECK

- Confirm that a site admin/superuser  can edit a beer via an edit button and associated edit page.
    - CHECK

- Confirm that a site admin/superuser can delete a beer via a delete button in the beer details section and that after deleting a beer the user is brought to the beers page.
    - CHECK

- Confirm that the bag icon in the navbar updates its price when a beer is added to the bag.
    - CHECK

- Confirm that a registered user can leave a review of the beer.
    - CHECK

- Confirm that an unregistered user can not leave a review of the beer.
    - CHECK

- Confirm that a registered user can not leave a review of the beer if they have already done so.
    - CHECK

- Confirm that the average rating of the beer in the star rating section updates upon a new review being added or an existing review being deleted.
    - CHECK

- Confirm that a registered user can edit of their own reviews via an edit button and associated page.
    - CHECK

- Confirm that a site admin/superuser can delete a review via a delete button in the footer of the review.
    - CHECK


**Shopping bag page**
- Confirm that all beers that have been added to the bag are present.
    - Check

- Confirm that the minus and plus buttons adjust the quantity properly while also updating the subtotal and grand total.
    - Check

- Confirm that the delivery threshold is working properly.
    - Check

- Confirm that the "Keep Shopping" button brings the user back to the beers page.
    - CHECK

- Confirm that the "Checkout" button brings the user to the chechout page.
    - CHECK


**Checkout page**
- Confirm that the order summary details are correct.
    - CHECK

- Confirm that if the user adds correct information and stripes example card details and clicks on the "Complete Order" button that the loading overlay appears before bringing the user to the checkout success page.
    - CHECK

- Confirm that if the user is signed in a checkbox appears beneath the details so that the user can save their details to their profile page.
    - CHECK

- Confirm Stripe webhooks successfully processed the order
    - CHECK

- Confirm that the "Keep Shopping" button brings the user back to the beers page.
    - CHECK


**Checkout success page**
- Confirm that the order details on the receipt are correct.
    - CHECK

- Confirm that the use receives an order confirmation email.
    - CHECK

- Confirm that the use receives an order confirmation email.
    - CHECK


**Find our beers page**
- Confirm that an empty Google map square is centeres on Ireland
    - CHECK

- Confirm that if a user clicks on a button markers appear on the map and the buttons background colour changes so that the user knows which button is in affect
    - CHECK

- Confirm that if a user clicks on a marker that an info box displays information about the location.
    - CHECK


**Blog page**
- Confirm that the blog page displays all blog posts.
    - CHECK

- Confirm that site admin/superuser can delete blogs via a delete button
    - CHECK

- Confirm that site admin/superuser can edit blogs via an edit button and the associated page
    - CHECK


**Contact us page**
- Confirm that if a user submits a valid form that an email is sent to the site owner.
    - CHECK


**Profile page**
- Confirm that the users details are already populated in the form if the user ticked the save button on the checkout page.
    - CHECK

- Confirm that the user can update their details by making a change and clicking the update button.
    - CHECK

- Confirm that if the user clicks the "Your orders" button that the details section is hidden and replaced by the orders section.
    - CHECK

- Confirm that the order details and user details are correct.
    - CHECK


**Footer**
- Confirm that if the user enters their email in the newsletter section that their email is added to the newsletter database and that a toast appears confirming that it was successful.
    - CHECK

- Confirm that if an existing email is entered in the newsletter box that an error toast appears notifying the user.
    - CHECK

- Confirm that the userr clicks one of the social icons that the relevant website opens in a new tab.
    - CHECK


**Forms**
- Confirm that if a user enters in valid details to any of the forms that the form will not submit.
    - CHECK

- Confirm that if required fields have not been filled in the form will not submit.
    - CHECK


**Toasts**
- Confirm that the user recieves toasts in all expected situations
    - CHECK


**Responsiveness**
- Confirm that all pages are visually appealling on phone, tablet and dektop screensizes.
    - CHECK


## <a name="auto-testing">Automated Testing</a>
[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Lighthouse audit summary for both desktop and mobile:

**Home page**

- Performance: **95%**
- Accessibility: **88%**
- Best Practices: **87%**
- SEO: **100%**

**Beers page**

- Performance: **96%**
- Accessibility: **89%**
- Best Practices: **87%**
- SEO: **100%**

**Beer detail page**

- Performance: **96%**
- Accessibility: **87%**
- Best Practices: **87%**
- SEO: **100%**

**Add/edit beer page**

- Performance: **97%**
- Accessibility: **81%**
- Best Practices: **87%**
- SEO: **100%**

**Bag page**

- Performance: **97%**
- Accessibility: **86%**
- Best Practices: **87%**
- SEO: **100%**

**Find our beers page**

- Performance: **90%**
- Accessibility: **86%**
- Best Practices: **87%**
- SEO: **100%**

**Blog page**

- Performance: **97%**
- Accessibility: **80%**
- Best Practices: **87%**
- SEO: **100%**

**Add/edit blog page**

- Performance: **96%**
- Accessibility: **81%**
- Best Practices: **87%**
- SEO: **100%**

**Blog detail page**

- Performance: **96%**
- Accessibility: **79%**
- Best Practices: **87%**
- SEO: **100%**

**Contact us page**

- Performance: **96%**
- Accessibility: **81%**
- Best Practices: **87%**
- SEO: **100%**


**Validators**

- [W3C - HTML](https://validator.w3.org/) a couple of duplicate id's errors appeared on the shopping bag page and the edit beer/blog pages. These errors are common and are essential to function of the site.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/) - 0 errors **PASS**
- [JS Hint](https://jshint.com/) - 0 errors - **PASS**
- [Pep8 Online](http://pep8online.com/) - 0 errors - **PASS**



## <a name="responsiveness">Responsivenss</a>

The site has been designed with a mobile-first philosophy and is supported by [Bootstrap](https://getbootstrap.com/), has been tested at all stages of development using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).


### Browsers

Tested on:

- Chrome
    - no issues
- Edge
    - no issues
- Firefox
    - no issues
- Safari (iOS)
    - no-issues

### Screen sizes

Tested with Chrome DevTools using profiles for the following devices, accounting for minimum screen widths of 320px:

- Galaxy S5
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

... and also using the responsive profiles of:

- Mobile S (320px)
- Mobile M (375px)
- Mobile L (425px)
- Tablet (768px)
- Laptop (1024px)
- Laptop L (1440px)

Real world testing on:

- Oppo a42
- iPhone SE
- iPhone x
- Acer Aspire
- Macbook

## <a name="bugs">Bugs</a>

### Resolved

- Bug: blog page was giving a 404 error
- Solution: changed url from path('slug:slug' ...) to path(blog_detail/slug:slug) and placed the add_blog url above the blog_detail rather than beneath

- Bug: The focus psuedo class was not working on the buttons in the profile page.
- Solution: This was fixed by adding tabindex="1" to each button element.

- Bug: I got the error "undefined name DATABASES"
- Solution: Fixed typo and by replacing "DATABASES -" with "DATABASES ="

- Bug: NoReverseMatch at /blog/
- Solution: Added slug field to form as no slug was being added for blog posts

- Bug: Beer image was not showing in the bag app.
- Solution: Changed code from src="{{ beer_product.image.url }}" to src="{{ item.beer_product.image.url }}"