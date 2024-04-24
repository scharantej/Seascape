## Flask Application Design

### HTML Files

- **`index.html`**: Home page with a form to input altitude and view description.
- **`results.html`**: Display ranked points with the highest altitudes and the corresponding view descriptions.

### Routes

#### **`/`**:
- **Method**: GET
- **Purpose**: Display the home page (`index.html`).

#### **`/submit`**:
- **Method**: POST
- **Purpose**: Collects input altitude and view description, and redirects to the results page (`/results`).

#### **`/results`**:
- **Method**: GET
- **Purpose**: Displays the ranked list of points with the highest altitudes and their corresponding view descriptions. Accepts query parameters for sorting and filtering.