## Test Results

Below are the results from our manual testing of key functionalities across the application.

### General Navigation & Header

| Element                                  | Expected Outcome                                                                                  | Pass/Fail |
|------------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Main Logo Link**                       | Clicking the logo redirects to the products page (`{% url 'products' %}`).                        | Pass      |
| **Home Link**                            | Clicking "Home" redirects to the home page (`{% url 'home' %}`).                                   | Pass      |
| **Products Dropdown – Category Links**   | Clicking a category link filters products by that category.                                       | Pass      |
| **Products Dropdown – Sort Options**     | Clicking sort options sorts products accordingly (e.g., by price ascending/descending, rating).    | Pass      |
| **My Account Dropdown (Not Logged In)**  | Displays "Login" and "Register" links that redirect to the respective pages.                      | Pass      |
| **My Account Dropdown (Logged In)**      | Displays "My Profile and My Orders", "Logout", "Edit Profile", "Delete Account", and "Change Password" links. | Pass      |
| **Search Bar**                           | Entering a query and submitting redirects to the products page with matching results.             | Pass      |
| **Privacy Policy Link**                  | Clicking the link opens the privacy policy page.                                                 | Pass      |
| **Facebook Icon**                        | Clicking the icon opens the business Facebook page in a new tab.                                   | Pass      |
| **Newsletter Form**                      | Submitting a valid email registers the subscriber and displays a success message.                 | Pass      |

---

### Home Page

| Element                          | Expected Outcome                                                                                  | Pass/Fail |
|----------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Categories Links**             | Clicking a category link redirects to the products page and filters products by that category.    | Pass      |
| **Down Arrow Link**              | Clicking the down arrow scrolls or redirects to the "About" section of the home page.             | Pass      |

---

### Product Page

| Element                              | Expected Outcome                                                                                  | Pass/Fail |
|--------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Product Image**                    | Clicking the product image redirects to the product detail page.                                  | Pass      |
| **Product Edit Link**                | Clicking the edit link (admin) redirects to the edit product page.                                | Pass      |
| **Product Delete Link**              | Clicking the delete link removes the product from the database.                                   | Pass      |

---

### Product Detail Page

| Element                              | Expected Outcome                                                                                  | Pass/Fail |
|--------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Product Image**                    | Clicking the image opens a larger view or a new tab with the image.                               | Pass      |
| **Favorites Icon**                   | Toggling the icon adds/removes the product from the favorites list.                               | Pass      |
| **Review Submission Form**           | Submitting the review form adds the review and displays a success message.                        | Pass      |
| **Review Edit/Delete Links**         | Clicking these links redirects appropriately to edit/delete the review.                         | Pass      |

---

### Checkout & Payment

| Element                              | Expected Outcome                                                                                  | Pass/Fail |
|--------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Add to Bag Button**                | Clicking the button adds the specified quantity of the product to the shopping bag.               | Pass      |
| **Shopping Cart Icon**               | Clicking the cart icon redirects to the shopping bag page.                                       | Pass      |
| **Secure Checkout Button**           | Clicking the checkout button redirects to a secure Stripe-hosted payment page.                     | Pass      |
| **Payment Success**                  | After successful payment, a success message is displayed and the order status updates to "Paid".     | Pass      |
| **Payment Cancel**                   | If payment is cancelled, an error message is displayed and the order status updates to "Cancelled".  | Pass      |

---

### User Account & Reviews

| Element                              | Expected Outcome                                                                                  | Pass/Fail |
|--------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| **Registration Form**                | Submitting the registration form creates a new account and saves the shipping address for checkout. | Pass      |
| **Login/Logout Functionality**       | Users can log in and out; appropriate success messages are displayed.                             | Pass      |
| **Profile Update Form**              | Submitting the profile update form updates user information and shows a success message.            | Pass      |
| **Delete Account**                   | Confirming account deletion removes the account and displays a confirmation message.                | Pass      |
| **Review Edit/Delete**               | Users can edit or delete their reviews with changes reflected immediately.                        | Pass      |

---

*Note: "Pass" indicates that the expected behavior was observed during testing.*

