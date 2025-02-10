# Boutique-Ecommerce

![Home Page](/images/responsive.png)

## Table of Contents
1. [About the Project](#about-the-project)
2. [Objectives](#objectives)
3. [Project Overview](#project-overview)
4. [User Stories & Project Management](#user-stories--project-management)
5. [Built With](#built-with)
6. [Database Model](#database-model)
7. [Bugs Resolved](#bugs-resolved)
8. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
9. [Screenshots](#screenshots)
10. [Wireframes](#wireframes)
11. [SEO & Marketing](#seo--marketing)
12. [Testing, Code Quality & Coverage](#testing-code-quality--coverage)
13. [Accessibility](#accessibility)
14. [Deployment Guide](#deployment-guide)
15. [Future Enhancements](#future-enhancements)
16. [Acknowledgements](#acknowledgements)
17. [References](#references)

---

## About the Project

Boutique-Ecommerce is a user-friendly online store designed to provide a seamless shopping experience. Customers can explore a variety of products, manage their profiles, and make purchases with ease. The platform also includes an admin panel for managing inventory, users, and orders efficiently.

---

## Objectives

- Deliver a simple yet powerful e-commerce platform.
- Allow customers to browse, search, and purchase products effortlessly.
- Provide administrators with tools to manage the store effectively.
- Ensure the platform is fully responsive across all devices.

---

## Project Overview

This Django project is organized into several apps, each handling a specific set of features:

### Authentication (`authenticate` app)
- **Features:**
  - Manages user login, logout, registration, password changes, profile editing, and account deletion.
  - Uses custom forms (e.g., `SignUpForm`, `EditProfileForm`) along with Django’s built-in authentication system.
- **Tests:**
  - Comprehensive tests ensure that all authentication views function as expected.

### Home (`home` app)
- **Features:**
  - Contains the homepage and a contact page.
  - The contact page includes a form for sending emails via Django’s email system.
- **Tests:**
  - Tests verify that the homepage and contact page render correctly and that the form works properly.

### Newsletter (`newsletter` app)
- **Features:**
  - Allows users to subscribe to the newsletter.
  - Sends a welcome email upon subscription.
  - Prevents duplicate subscriptions and validates email addresses.
- **Tests:**
  - Tests ensure proper handling of subscriptions and email validations.

### Store (`store` app)
- **Features:**
  - Enables users to browse products, view detailed product pages, and submit reviews.
  - Provides admin functionality to add, update, or delete products.
  - Integrates with Stripe for payment processing.
  - Manages orders and processes refund requests.
  - Uses Cloudinary for handling product images.
- **Models & Validations:**
  - **Category:** Organizes products into groups.
  - **Product:** Manages product details, including stock and price validations.
  - **Review:** Allows users to rate and comment on products.
  - **Order:** Tracks order details and statuses.
  - **Refund:** Handles refund requests and tracks their status.
- **Tests:**
  - Extensive tests cover forms, model validations, and view functionality.

### User Registration & Seamless Checkout
Our registration process is designed for convenience. When users sign up, they’re asked to enter their shipping address so that during checkout their delivery details are already saved. This approach:
- Simplifies checkout by eliminating the need to re-enter shipping information.
- Enhances the overall user experience.
- Saves time and reduces friction during the ordering process.

---

## User Stories & Project Management

We used GitHub Projects as our project management tool to track user stories via a Kanban board. This helped us focus on specific tasks and monitor project progress.

- **View the board [here](https://github.com/users/BadrAlioui/projects/9).**

#### Sprint1
![Sprint1](/images/sprint1.png)

#### Sprint2
![Sprint2](/images/sprint2.png)

#### Sprint3
![Sprint3](/images/sprint3.png)

#### Sprint4
![Sprint4](/images/sprint4.png)

---

## Built With

- **Python** – Backend logic and data handling.
- **Django** – Rapid and robust web framework.
- **HTML5** – Semantic structure.
- **CSS3** – Responsive styling.
- **JavaScript** – Interactive elements.
- **PostgreSQL** – Production database.
- **Bootstrap** – Modern, responsive UI.

---

## Database Model

The database model was designed using [drawsql](https://drawsql.app/). We use SQLite3 during development and PostgreSQL in production.

![Database Model](/images/database_model.png)

---

## Bugs Resolved

### 1. IP Address Mismatch on Heroku
- **Problem:** Deployment failures due to an "IP address mismatch" error.
- **Solution:** Removed `django_heroku.settings(locals())` from `settings.py` to prevent conflicts.
- **Outcome:** Deployment now works flawlessly.

### 2. Media Files Not Persisting on Heroku
- **Problem:** Uploaded images were lost due to Heroku’s ephemeral file system.
- **Solution:** Integrated Cloudinary for external storage:
  - Installed `django-cloudinary-storage`
  - Configured Cloudinary in `settings.py`
- **Outcome:** Media files are now permanently stored and reliably served.

### 3. CSS Not Loading Locally
- **Problem:** CSS files were not loading on `localhost` because the `collectstatic` command had not been run.
- **Solution:** Ran:
  ```bash
  python manage.py collectstatic```


---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- PostgreSQL
- A modern web browser

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-link>
    ```

2. Navigate to the project folder:
    ```bash
    cd boutique-ecommerce
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with these keys:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `STRIPE_KEYS` (optional)
    - `CLOUDINARY_KEYS` (optional)

5. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

---

## Screenshots

### Home Page
![Home Page](/images/home_page.png)

### Contact Page

![Contact Page](/images/Screenshot_contact_page.png)

### Product Page

![Product Page](/images/products_page.png)

### Product Detail

![Product Detail Page](/images/screenshot_product_detail.png)

### Payment Page

![Product Page](/images/payment_product.png)

### Login Page

![Product Page](/images/screenshot_login_page.png)

### Edit Profile Page
![Edit Profile Page](/images/edit_profile_page.png)


---

## wireframes

![wireframes](/images/wireframe-boutique.png)

## SEO Strategy

### Keyword Research
- **Short-tail keywords**:
  - "Online fashion store"
  - "Affordable clothing"
- **Long-tail keywords**:
  - "Where to buy trendy slim-fit jeans"
  - "Elegant crop tops for women"

### On-Page SEO
- **Meta Tags**: Descriptive tags for better search engine visibility.
- **Clean URLs**: Easy-to-read and SEO-friendly URLs.
- **Alt Text**: Descriptive alt attributes for images.
- **Optimized Headings**: Structured headings for better content readability.

---

## Marketing Strategy

### Search Engine Optimization (SEO)

To boost our search engine rankings on Google, we performed extensive keyword research using tools like Google Keyword Planner and SEMrush. We identified keywords that represent our brand, "Boutique VitaleVibes," and current fashion trends, integrating them into meta tags and throughout our website content.

**Targeted Keywords:**
- Boutique VitaleVibes
- Trendy fashion online
- Affordable stylish clothes
- Modern e-commerce fashion
- Shop latest trends online
- Sustainable fashion

These keywords are continuously monitored using analytics tools to ensure our content remains relevant and drives organic traffic.

### Business Model

**Company Description:**  
Boutique VitaleVibes is a B2C online store dedicated to offering trendy and affordable fashion products. Our mission is to provide a seamless shopping experience with a carefully curated collection, secure payment options, and exceptional customer service.

**Customers:**  
Our target audience includes fashion-forward millennials and Gen Z, as well as families who value style and affordability. These customers are constantly seeking the latest trends and value a user-friendly online shopping experience.

**Competitors:**  
We face competition from:
- Niche online boutiques that focus on specific fashion trends.
- Large online retailers offering a wide range of fashion items.
- General marketplaces where finding a curated and unique collection can be challenging.

### SWOT Analysis

- **Strengths:**
  - A carefully curated selection of trendy and affordable fashion items.
  - A user-friendly, responsive website with a seamless shopping experience.
  - Robust order management and secure payment processing.
- **Weaknesses:**
  - As a newer brand, we are still building market recognition.
  - A limited marketing budget compared to established competitors.
- **Opportunities:**
  - Growing consumer interest in sustainable and ethically sourced fashion.
  - Increasing online shopping trends among younger consumers.
  - Opportunities for collaboration with fashion influencers and bloggers.
- **Threats:**
  - Intense competition from well-established brands and large online retailers.
  - Potential challenges in supply chain management and shipping logistics.
  - Rapid changes in fashion trends that could impact our inventory.

### Marketing Strategy

Given our limited marketing budget, Boutique VitaleVibes focuses on cost-effective strategies that maximize our reach:
- **Social Media Engagement:**  
  We maintain an active presence on Facebook and Instagram, sharing updates, new arrivals, behind-the-scenes content, and engaging with our community.
- **Newsletter Campaigns:**  
  We encourage visitors to subscribe to our newsletter, offering exclusive discounts, style tips, and early access to new collections, thereby fostering customer loyalty.
- **Influencer Collaborations:**  
  Partnering with fashion influencers and bloggers helps us expand our reach, build credibility, and attract new customers.
- **Word of Mouth:**  
  We leverage customer reviews and testimonials to build trust and encourage organic sharing of our brand.
- **Content Marketing:**  
  Through regular blog posts, style guides, and fashion tips, we provide valuable content that not only enhances user engagement but also improves our SEO performance.

By continuously monitoring our marketing efforts and refining our strategies, we aim to increase our online visibility and drive sustainable growth for Boutique VitaleVibes.

---

### **Facebook Page for Boutique VitaleVibes**

As part of my content marketing strategy, I created a dedicated Facebook page to promote Boutique VitaleVibes's products and engage with my target audience. This page serves as a platform to showcase the latest offers, share updates, and drive traffic to the website.

#### **Purpose of the Facebook Page:**
- **Brand Visibility**: Boost awareness of Boutique VitaleVibes among a broader audience.
- **Engagement**: Interact directly with customers through posts, comments, and messages.
- **Promotion**: Announce new product launches, special discounts, and seasonal offers.
- **Traffic Generation**: Redirect visitors to the website for a seamless shopping experience.

#### **Key Features:**
- **Content Posts**: Sharing high-quality images and descriptions of featured products.
- **Call-to-Action**: Encouraging users to visit the e-commerce store for exclusive offers.
- **Customer Interaction**: Responding promptly to inquiries and building trust with the audience.

![home-page](/images/page1-facebook.png)

![home-page2](/images/page2-facebook.png)

By integrating Facebook into my marketing strategy, I aim to connect with potential customers where they are most active and strengthen Boutique VitaleVibes's online presence.


## Testing

### Automated Testing

- **HTML Validation**: No errors detected.
- **CSS Validation**: Passed with clean code.
- **Python Testing**: High test coverage using Django’s test framework.

### Manual Testing

- User workflows, including registration, login, and profile management, tested successfully.
- Products and categories load correctly with accurate filtering and sorting.

---


---

## Code Quality

### Python Code Example
![Python Code Example](/images/python_code_example.png)

Sometimes, scripts may contain more characters than expected, but I’m leaving it that way for an improved experience for advanced users

### JavaScript Code Example
![JavaScript Code Example](/images/javascript_code_example.png)

### HTML Code Examples

#### Test Home Page Html

![HTML Home Page](/images/home_page_html.png)

#### Test Login Page Html

![HTML Login Page](/images/validator_login.png)

#### Test Delete Profile Html

![HTML Edit Profile](/images/validator_delete_account.png)

#### Test Edit Profile Html

![HTML Edit Profile](/images/validator_edit_profile.png)

#### Register Page

![HTML Register Page](/images/Screenshot_register_page.png)


#### Product Page

![HTML Register Page](/images/Screenshot_validator_product_page.png)

### Product Detail Page

![HTML Register Page](/images/Screenshot_validator_product_detail.png)

### Add Product Page

![HTML Register Page](/images/Screenshot_validator_add_product.png)

#### Test Home Page Html

![HTML Home Page](/images/home_page_html.png)

#### Test Login Page Html

![HTML Login Page](/images/validator_login.png)

#### Test Delete Profile Html

![HTML Edit Profile](/images/validator_delete_account.png)

#### Test Edit Profile Html

![HTML Edit Profile](/images/validator_edit_profile.png)

#### Register Page

![HTML Register Page](/images/Screenshot_register_page.png)


#### Product Page

![HTML Register Page](/images/Screenshot_validator_product_page.png)

#### Product Detail Page

![HTML Register Page](/images/Screenshot_validator_product_detail.png)

#### Delete Product Page

![HTML Register Page](/images/Screenshot_validator_delete_product.png)

#### Update Product Page

![HTML Register Page](/images/Screenshot_validator_edit_product.png)

#### Update Review Page

![HTML Register Page](/images/Screenshot_validator_edit_review.png)

#### Delete Review Page

![HTML Register Page](/images/Screenshot_validator_delete_review.png)

#### Request Fund Page

![HTML Register Page](/images/Screenshot_validator_request_refund.png)

#### Request Status Page

![HTML Register Page](/images/Screenshot_validator_request_status.png)

---

### CSS Code Example
![CSS Code Example](/images/css_code_example.png)


---

### Test Coverage

We’ve built a robust suite of tests to catch bugs early and ensure our code works as expected. Our current overall test coverage is **84%**, meaning that 84% of our code is exercised during testing.

**What This Means:**

- **Strong Coverage in Key Areas:**  
  Many core features—like authentication views, forms, and essential utility functions—are tested extensively (mostly 90% or above). This gives us confidence in their reliability.

- **Fully Tested Modules:**  
  Several parts of the application, including our models, migrations, and some helper modules, are 100% covered by tests.

- **Areas for Improvement:**  
  Some files, such as `store/views.py` (with 40% coverage), show opportunities for adding more tests. We’re committed to improving these areas as the project evolves.

By continuously monitoring and enhancing our test coverage, we strive to maintain high code quality and ensure that our project remains stable and maintainable as new features are added.

here’s the HTML coverage report:
![HTML Coverage](/images/coverage_report.png)


## Accessibility

Lighthouse tests ensured high accessibility scores:

- **Mobile Accessibility**: Scored above 90%.

![mobile](/images/mobile_lighthouse.png)

- **Desktop Accessibility**: Scored above 95%.

![desktop](/images/desktop_lighthouse.png)

---

### Deployment Guide for Django Project on Heroku (Using Git Bash)

For this project, I deployed the Django application on Heroku, a cloud platform that makes it easy to build, run, and scale apps. I used **Git Bash** to manage the deployment process, and I selected the Europe region when setting up the app.

The project is deployed on **Heroku**. You can access the live application here:  
[Live Application](https://boutique-shop-9cbda2d44e62.herokuapp.com/)


Here’s a step-by-step guide on how I did it:

- **Install Required Packages**:
  Open Git Bash and run the following commands to install the necessary tools:
  ```bash
  pip install gunicorn dj-database-url psycopg2 whitenoise python-decouple django-heroku



**Settings**

1. **Update `settings.py`**:
   - Add your Heroku app to `ALLOWED_HOSTS`:
     ```python
      ALLOWED_HOSTS = ['your-app-name.herokuapp.com']
     ```
   - Install `whitenoise` for handling static files:
     ```bash
     pip install whitenoise
     ```
     Add it to your middleware:
     ```python
     MIDDLEWARE = [
         'whitenoise.middleware.WhiteNoiseMiddleware',
         # other middleware...
     ]
     ```
     Configure static files:
     ```python
     STATIC_ROOT = BASE_DIR / 'staticfiles'
     ```
     Run `python manage.py collectstatic` during deployment.
   - Install `psycopg2` and `dj-database-url` for database configuration:
     ```bash
     pip install psycopg2 dj-database-url
     ```
     Update database settings:
     ```python
     import dj_database_url
     DATABASES = {'default': dj_database_url.config()}
     ```
   - Set `DEBUG = False` and move `SECRET_KEY` to Config Vars.

2. **Install Gunicorn**:
   - Install Gunicorn:
     ```bash
     pip install gunicorn
     ```
   - Create a `Procfile` in the root directory:
     ```
     web: gunicorn your_project_name.wsgi
     ```

3. **Config Vars**          
    
  Both in the root level .env file and on Heroku, these are the config vars:

  CLOUDINARY_URL = Your value
  CLOUDINARY_CLOUD_NAME = Your value
  CLOUDINARY_API_KEY = Your value
  CLOUDINARY_API_SECRET = Your value
  DATABASE_URL = Your value
  SECRET_KEY = Your value

  Access these vars in your settings.py as follows 

  ```python
          from decouple import config
          SECRET_KEY = config('SECRET_KEY')
  ```


---

## Future Enhancements

- **Wishlist Feature**: Allow users to save favorite products.
- **Product Reviews**: Enable users to leave reviews and ratings.
- **Multi-Address Support**: Add functionality for multiple shipping addresses.
- **Order Notifications**: Notify users of order status updates.

---

## Acknowledgements

- **Code Institute**: For the structured learning experience and project guidelines.
- **My Mentor**: For valuable feedback and guidance.
- **Django Documentation**: For clear and detailed references.
- **Community Support**: For providing tips and answering questions.

---

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Stripe API Documentation](https://stripe.com/docs)
