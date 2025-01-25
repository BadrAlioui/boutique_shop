# Boutique-Ecommerce

![Home Page](<!-- Add your image link here -->)

## About the Project

Boutique-Ecommerce is a user-friendly online store designed to provide a seamless shopping experience. Customers can explore a variety of products, manage their profiles, and make purchases with ease. The platform also includes an admin panel for managing inventory, users, and orders efficiently.

---

## Objectives

- Deliver a simple yet powerful e-commerce platform.
- Allow customers to browse, search, and purchase products effortlessly.
- Provide administrators with tools to manage the store effectively.
- Ensure the platform is fully responsive across all devices.

---

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
![Home Page](<!-- Add your image link here -->)

### Product Page
![Product Page](<!-- Add your image link here -->)

### Edit Profile Page
![Edit Profile Page](<!-- Add your image link here -->)

---

## SEO Strategy

To improve the platform's discoverability on search engines, the following SEO strategies were implemented:

### Keyword Research
- **Short-tail keywords**:
  - "Online fashion store"
  - "Affordable clothing"
- **Long-tail keywords**:
  - "Where to buy trendy slim-fit jeans"
  - "Elegant crop tops for women"

### On-Page SEO
1. **Meta Tags**:  
   - Home Page: "Boutique-Ecommerce - Affordable Fashion for Everyone"  
   - Product Page: "Slim-Fit Jeans for Men - Shop Online at Boutique-Ecommerce"
2. **Clean URLs**:  
   - `/products/men`  
   - `/products/slim-fit-jeans`
3. **Alt Text**: All images include descriptive alt text for better accessibility.
4. **Optimized Headings**:  
   - H1: "Affordable Clothing for Men and Women"  
   - H2: "Explore Categories - Fashion for Everyone"

### Content Optimization
- **Detailed Product Descriptions**: Informative and engaging descriptions for each product.
- **Internal Linking**: Links between related products and categories for easy navigation.

### Future Plans
- Add structured data (schema.org) for rich snippets in search results.
- Implement a blog for fashion tips and seasonal trends.

---

## Testing

### Automated Testing

- **HTML Validation**: No errors detected.
- **CSS Validation**: Passed with clean code.
- **Python Testing**: High test coverage using Django’s test framework.
- **JavaScript Testing**: Verified interactive elements across all pages.

### Manual Testing

- User workflows, including registration, login, and profile management, tested successfully.
- Products and categories load correctly with accurate filtering and sorting.

---

## Accessibility

Lighthouse tests ensured high accessibility scores:

- **Mobile Accessibility**: Scored above 90%.
- **Desktop Accessibility**: Scored above 95%.

---

## Project Management

This project is managed using the **Kanban methodology** for streamlined task organization and tracking. You can view the project board here:  
[Kanban Board - GitHub Projects](https://github.com/users/BadrAlioui/projects/9)

---

## Deployment

The project is deployed on **Heroku**. You can access the live application here:  
[Live Application](<!-- Add your Heroku app link here -->)

### Deployment Steps
1. Create a Heroku app:
    ```bash
    heroku create <app-name>
    ```

2. Push the code:
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
