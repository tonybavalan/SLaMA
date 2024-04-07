## Overview

This repository is home to the codebase for an innovative web application designed to transform data analysis through dynamic visualization and intelligent model-based suggestions. The application is structured into three main components, each housed in its own sub-repository:

## Sub-repositories

### 1. Frontend (Next.js)

Developed with Next.js, the frontend features an advanced dashboard that dynamically generates a variety of graphs based on user requirements. This is achieved through a seamless integration with the backend machine learning model, which provides recommendations on the most effective visualization techniques for different datasets. The frontend is responsible for presenting these insights through a user-friendly interface, incorporating components, pages, and styles that enable intuitive interaction and exploration.

### 2. Backend (Python with Random Forest Algorithm)

At the core of the backend is a machine learning model powered by the Random Forest algorithm. This model analyzes incoming datasets to suggest the most appropriate chart types for data visualization, enhancing the decision-making process. The backend is built using Python and handles server-side logic, API management, database interactions, and the execution of the machine learning model. It plays a critical role in processing client requests, managing data flow, and generating actionable insights for the frontend.

### 3. Streamlit (Python for Data Visualization)

The Streamlit sub-repository is dedicated to data visualization and exploration, leveraging Python to create interactive data applications. It complements the frontend by providing an alternative platform for visualizing data insights, making it easier for users to analyze and interpret their data. Streamlit's intuitive framework enables the rapid development of data applications that can interact with the machine learning model for enhanced analytical capabilities.

1. Clone this repository:

```
  git clone https://github.com/tonybavalan/SLaMA.git
```

2. Navigate to the respective sub-repositories:

- For frontend:
  ```
  cd frontend
  ```
- For backend:
  ```
  cd backend
  ```
- For Streamlit:
  ```
  cd streamlit
  ```

3. Install dependencies:

## Contributing

Contributions are welcome!
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the LICENSE file for details.
