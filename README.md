
# BookShop: Empowering Sellers with Predictive Pricing and Seamless Interaction

## Overview

BookShop is a dynamic platform designed to help book sellers set optimal prices using predictive algorithms. The platform provides a seamless interaction system that is scalable and performant, ensuring a smooth user experience even under high loads. The project attracted over 500 new users within the first three months of deployment and significantly boosted visibility for sellers.

## Features

- **Predictive Pricing Algorithms**: Uses data-driven strategies to help sellers set optimal prices.
- **Scalable Interaction System**: Ensures smooth operation under high user loads, enhancing the user experience.
- **Advanced Visualizations**: The decision tree model used for pricing predictions is visualized for better understanding.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Machine Learning**: Scikit-learn (Decision Tree Regressor)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tulika-5/BookShop.git
   cd BookShop
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage

- The platform allows sellers to set prices dynamically based on predictive models and engage with users via a clean and responsive interface.
- To access the platform, run the application and visit `http://localhost:5000` in your browser.

## Model Details

The decision tree model predicts the selling price of books based on several features:
- **Price**: The original price of the book.
- **Year Old**: The age of the book.
- **Availability**: Binary feature indicating whether the book is available.
- **Stars**: Customer rating (out of 5).

The model has been trained and evaluated using Mean Squared Error (MSE) and R² score, and a visualization of the decision tree is available in the repository as `decisiontree.png`.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License.

---
