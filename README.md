# Boutique-Ecommerce

![Home Page](<!-- Add your image link here -->)

## About the Project

Boutique-Ecommerce is a fully functional e-commerce platform where users can browse products, create accounts, and make purchases effortlessly. Designed with simplicity and functionality in mind, it offers a smooth and intuitive shopping experience.

The platform also provides admin tools for managing products, orders, and user accounts, making it a complete solution for running an online store.

---

## Objectives

- Provide an easy-to-use online shopping platform.
- Allow users to browse products, place orders, and manage their profiles seamlessly.
- Enable administrators to manage inventory, users, and orders efficiently.
- Deliver a responsive, visually appealing design across all devices.

---

## Built With

This project uses modern technologies to ensure scalability, performance, and user satisfaction:

- **Python**: Backend logic.
- **Django**: Web development framework.
- **HTML5**: For structured and semantic content.
- **CSS3**: For responsive and aesthetic styling.
- **JavaScript**: For enhanced interactivity.
- **PostgreSQL**: For managing the database.
- **Bootstrap**: For a consistent and modern UI.

---

## Key Features

- **Product Browsing**: Explore products with detailed descriptions, images, and prices.
- **User Authentication**: Register, log in, and manage secure user accounts.
- **Profile Management**: Users can edit their details, including addresses, in their profiles.
- **Order Management**: View, edit, or cancel orders directly from the dashboard.
- **Admin Panel**: Manage products, users, and orders efficiently.
- **Responsive Design**: Optimized for mobile, tablet, and desktop devices.
- **Integrated Payment System**: (To be implemented in the future for secure online payments).

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

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

4. Set up your `.env` file with the following keys:
    - `DATABASE_URL`
    - `SECRET_KEY`
    - `STRIPE_KEYS` (if applicable)
    - `CLOUDINARY_KEYS` (for media storage)

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
![Home Page](<!-- Add your image link here -->)

### Product Page
![Product Page](<!-- Add your image link here -->)

### Cart Page
![Cart Page](<!-- Add your image link here -->)

### Edit Profile Page
![Edit Profile Page](<!-- Add your image link here -->)

---

## Testing

### Automated Testing

- **HTML Validation**: All pages validated with no major errors or warnings.
- **CSS Validation**: Passed with clean, valid styles.
- **Python Testing**: High test coverage using Django’s test framework.
- **JavaScript Testing**: Verified dynamic elements work across pages.

### Manual Testing

- Registration, login, and logout workflows tested successfully.
- Profile editing verified to ensure all fields (username, email, address, etc.) update correctly.
- Product browsing, cart functionality, and order placement tested thoroughly.

---

## Accessibility

The website was tested using Lighthouse to ensure accessibility:

- **Mobile Accessibility**: Scored above 90%.
- **Desktop Accessibility**: Scored above 95%.

### Example Accessibility Screenshot
![Lighthouse Score](<!-- Add your image link here -->)

---

## Deployment

The project is deployed on **Heroku**. You can access the live application here:

[Live Application](<!-- Add your Heroku app link here -->)

### Steps for Deployment

1. Create a new Heroku app:
    ```bash
    heroku create <app-name>
    ```

2. Push your code to Heroku:
    ```bash
    git push heroku main
    ```

3. Set up environment variables:
    ```bash
    heroku config:set DATABASE_URL=<your-database-url>
    ```

4. Run database migrations:
    ```bash
    heroku run python manage.py migrate
    ```

---

## Wireframes

### Home Page
![Wireframe Home Page](<!-- Add your wireframe image link here -->)

### User Flow
![Wireframe User Flow](<!-- Add your wireframe image link here -->)

---

## Future Enhancements

- **Add Wishlist Feature**: Allow users to save their favorite products.
- **Product Reviews**: Enable users to leave reviews and ratings for products.
- **Multi-Address Support**: Allow users to save multiple addresses for shipping and billing.
- **Order Notifications**: Notify users about order status updates.

---

## Acknowledgements

- **Code Institute**: For providing a structured learning experience.
- **My Mentor**: For valuable feedback and guidance throughout the project.
- **Django Documentation**: For detailed references and best practices.
- **Community Support**: For answering questions and sharing knowledge.

---

## References

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Stripe API Documentation](https://stripe.com/docs)
