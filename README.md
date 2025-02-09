# Boutique-Ecommerce

![Home Page](/images/responsive.png)


## Table of Contents
1. [About the Project](#about-the-project)
2. [Objectives](#objectives)
3. [Project Overview](#project-overview)
4. [Testing Overview](#testing-overview)
5. [User Stories & Project Management](#user-stories--project-management)
6. [Built With](#built-with)
7. [Database Model](#database-model)
8. [Bugs Resolved](#bugs-resolved)
9. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
10. [Screenshots](#screenshots)
11. [Wireframes](#wireframes)
12. [SEO Strategy](#seo-strategy)
13. [Marketing Strategy](#marketing-strategy)
14. [Facebook Page for Boutique VitaleVibes](#facebook-page-for-boutique-vitalevibes)
15. [Testing](#testing)
16. [Code Quality](#code-quality)
17. [HTML Coverage](#html-coverage)
18. [Accessibility](#accessibility)
19. [Deployment Guide](#deployment-guide-for-django-project-on-heroku-using-git-bash)
20. [Future Enhancements](#future-enhancements)
21. [Acknowledgements](#acknowledgements)
22. [References](#references)

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
  - Utilizes custom forms like `SignUpForm` and `EditProfileForm` along with Django’s built-in authentication system.
- **Tests:**
  - Comprehensive tests ensure that all authentication views (login, logout, registration, etc.) work as expected.

### Home (`home` app)
- **Features:**
  - Contains the homepage and a contact page.
  - The contact page has a form that sends emails using Django’s email system.
- **Tests:**
  - Tests verify that both the homepage and contact page render correctly and that the contact form properly sends emails.

### Newsletter (`newsletter` app)
- **Features:**
  - Allows users to subscribe to the newsletter.
  - Sends a welcome email when someone subscribes.
  - Prevents duplicate subscriptions and validates email addresses.
- **Tests:**
  - Tests ensure that subscriptions are handled correctly, duplicate entries are blocked, and invalid emails are rejected.

### Store (`store` app)
- **Features:**
  - Lets users browse products, view detailed product pages, and submit reviews.
  - Provides admin functionality to add, update, or delete products.
  - Integrates with Stripe for payment processing.
  - Manages orders and processes refund requests.
  - Uses Cloudinary to handle product images.
- **Models & Validations:**
  - **Category:** Organizes products into groups.
  - **Product:** Manages product details, including stock and price validations.
  - **Review:** Allows users to rate and comment on products.
  - **Order:** Tracks order details and statuses.
  - **Refund:** Handles refund requests and tracks their status.
- **Tests:**
  - Extensive tests cover forms (e.g., `ProductForm`, `ReviewForm`, `RefundForm`), model validations, and view functionality (product listing, payment processing, refund requests, etc.).

## Testing Overview

The project includes a robust test suite that covers:
- **View Tests:** To ensure every page (authentication, home, newsletter, and store) loads correctly and behaves as expected.
- **Form Tests:** To validate both correct and erroneous input cases.
- **Model Tests:** To check model relationships and custom validations.
- **Integration Tests:** To simulate complete user workflows—such as payment processing and refund requests—while integrating with external services like Stripe and email systems.

---

## User Stories & Project Management

GitHub Projects was used as my project management tool to track user stories. Using a Kanban board helped me focus on specific tasks and monitor the progress of the project efficiently. You can view the board [here](https://github.com/users/BadrAlioui/projects/9).

#### Sprint1

![sprint1](/images/sprint1.png)

#### Sprint2

![sprint1](/images/sprint2.png)

#### Sprint3

![sprint1](/images/sprint3.png)

## Built With

This project uses modern technologies to ensure functionality and scalability:

- **Python**: Backend logic and data handling.
- **Django**: Framework for rapid and robust development.
- **HTML5**: Semantic structure and content.
- **CSS3**: Responsive styling.
- **JavaScript**: Interactive elements.
- **PostgreSQL**: Database for storing data.
- **Bootstrap**: Modern and responsive user interface.

---

## Database Model

The database model has been designed using drawsql. The type of database being used is a relational database managed with SQLite3 during development and deployed using PostgreSQL.

![Database Model](/images/database_model.png)

---

## Bugs Resolved

During the development and deployment of this project, the following major bugs were encountered and resolved:

### **1. IP Address Mismatch on Heroku**
- **Problem**: While deploying the application on Heroku, an "IP address mismatch" error occurred, causing deployment failures.
- **Solution**: 
  - The issue was resolved by removing the following line from `settings.py`:
    ```python
    django_heroku.settings(locals())
    ```
  - This line was causing unnecessary configurations to override the local settings, leading to conflicts during deployment.
- **Outcome**: Once removed, the deployment worked flawlessly.

### **2. Media Files Not Persisting on Heroku**
- **Problem**: Images uploaded to the platform were lost after deployments or server restarts due to Heroku’s ephemeral file system.
- **Solution**: Cloudinary was integrated for external storage of media files:
  - Installed `django-cloudinary-storage`:
    ```bash
    pip install django-cloudinary-storage
    ```
  - Configured Cloudinary in `settings.py`:
    ```python
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    cloudinary.config(
        cloud_name='your_cloud_name',
        api_key='your_api_key',
        api_secret='your_api_secret'
    )
    ```
  - Media files are now securely stored in the cloud.
- **Outcome**: Media files are permanently stored and reliably served, even after redeployments.

### **3. CSS Not Loading Locally**
- **Problem**: CSS files were not loading on `localhost` because the `collectstatic` command had not been run.
- **Solution**: The following command was executed to collect all static files:
  ```bash
  python manage.py collectstatic

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

### Register Page

![HTML Register Page](/images/register_page.png)

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



### CSS Code Example
![CSS Code Example](/images/css_code_example.png)


---

## HTML Coverage

To ensure code robustness, here’s the HTML coverage report:
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
