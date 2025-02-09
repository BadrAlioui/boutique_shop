# Boutique-Ecommerce

![Home Page](/images/responsive.png)


## Table of Contents
1. [About the Project](#about-the-project)
2. [Objectives](#objectives)
3. [Key Features](#key-features)
4. [Technologies Used](#technologies-used)
5. [Installation Guide](#installation-guide)
6. [Screenshots](#screenshots)
7. [SEO Strategy](#seo-strategy)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Future Enhancements](#future-enhancements)
11. [Acknowledgements](#acknowledgements)

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

## Key Features

- **Product Browsing**: View detailed product descriptions, prices, and images.
- **User Authentication**: Register, log in, and manage accounts securely.
- **Order Management**: Place orders and track them in the user dashboard.
- **Admin Panel**: Manage inventory, orders, and user accounts efficiently.
- **Responsive Design**: Optimized for mobile, tablet, and desktop devices.
- **Integrated Payment System**: (Planned for future development).

---

## **Authentication**

In this project, Django's built-in authentication system makes it easy for users to sign up, log in, and log out securely. Once logged in, users can:

- Update their profile information.
- View and manage their orders.
- Request refunds for eligible purchases.
- Edit or even delete their accounts if they choose.

Django takes care of the heavy lifting, like password security and session management, so everything stays safe and reliable. This way, users have a smooth and secure experience while interacting with the site.

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
