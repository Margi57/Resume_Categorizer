import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .utils import clean_text

nltk.download('stopwords')
nltk.download('wordnet')

# Sample training data
texts = [
    "Python, Java, C++, Django, Flask, Node.js, Express.js, API, REST, PostgreSQL, MySQL, MongoDB, Redis, GraphQL,Celery, RabbitMQ, Kafka, SQL, ORM, authentication, authorization, server-side, unit testing,Docker, microservices, scalability, security",
    "HTML, CSS, JavaScript, React, Redux, Angular, Vue.js, Bootstrap, Tailwind, jQuery, UI/UX,TypeScript, responsive design, Figma, Adobe XD, REST APIs, Webpack, Babel, npm, AJAX, DOM,Cross-browser compatibility, CSS3 animations, frontend testing, Jest, Vite, Next.js",
    "CI/CD, Jenkins, GitLab CI, Docker, Kubernetes, Ansible, Terraform, AWS, Azure, GCP, monitoring,Prometheus, Grafana, ELK stack, Bash, shell scripting, Linux, EC2, Lambda, CloudFormation,deployment, pipelines, load balancing, Nginx, logging, scalability, automation, system administration",
    "Python, pandas, NumPy, scikit-learn, TensorFlow, PyTorch, machine learning, deep learning,NLP, computer vision, statistics, data analysis, regression, classification, clustering,data visualization, matplotlib, seaborn, SQL, data wrangling, data preprocessing, A/B testing,model evaluation, ML pipelines, Jupyter, notebooks, BigQuery, Hadoop, Spark",
    "HTML, CSS, JavaScript, UI design, UX design, Figma, Adobe XD, Sketch, InVision, wireframes,mockups, prototypes, responsive design, user research, usability testing, interaction design,animations, CSS transitions, accessibility, Bootstrap, Tailwind, Material UI, color theory,typography, user flows, design systems, frontend",
    "WordPress, PHP, MySQL, themes, plugins, WooCommerce, Elementor, Divi, Gutenberg, shortcodes,ACF (Advanced Custom Fields), HTML, CSS, JavaScript, cPanel, hosting, SEO, CMS, REST API,custom post types, hooks, filters, WP CLI, site optimization, page builders, cross-browser",
    "sales, lead generation, CRM, client handling, cold calling, business strategy, communication,negotiation, market research, B2B, B2C, email marketing, presentation skills, revenue growth,target achievement, networking, relationship management, pipeline management, closing deals,proposal writing, business planning",
    "manual testing, automation testing, Selenium, JUnit, TestNG, regression testing, bug tracking,JIRA, SDLC, STLC, test cases, test plans, unit testing, integration testing, functional testing,black box, white box, performance testing, load testing, UAT, defect logging, scripts, test suites,Postman, REST API testing",
    "Android, Java, Kotlin, XML, Android Studio, Firebase, REST API, SQLite, Room, MVVM, Jetpack,RecyclerView, Retrofit, LiveData, Coroutines, Push notifications, background services, Gradle,Material Design, debugging, unit tests, Google Play Store, app performance, UI testing",
    "HTML, CSS, JavaScript, React, Node.js, Express.js, MongoDB, MySQL, PostgreSQL, Python, Django,REST API, GraphQL, Git, Docker, AWS, authentication, JWT, frontend, backend, CI/CD, MVC,testing, deployment, security, scalability, API integration, full stack"
]
labels = [
    "Backend Developer", "Frontend Developer", "DevOps Engineer",
    "Data Scientist", "UI/UX Developer", "WordPress Developer",
    "Business Development (BD) Executive", "QA / Software Tester",
    "Android Developer", "Full Stack Developer"
]

# Clean the training texts
cleaned_texts = [clean_text(text) for text in texts]

# Vectorize the cleaned data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_texts)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

# Role prediction 
def predict_role(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    predicted_role = model.predict(vec)[0]
    probabilities = model.predict_proba(vec)[0]
    predicted_index = model.classes_.tolist().index(predicted_role)
    confidence_score = probabilities[predicted_index]
    return predicted_role, confidence_score
