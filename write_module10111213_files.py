from pathlib import Path

base = Path(r'c:\Users\ydaya\Desktop\Cognizant Deep Skilling')
modules = [
    'Module_10_ReactJS',
    'Module_11_Spring_Core',
    'Module_12_Spring_Boot',
    'Module_13_Git_GitHub_Maven',
]

jsx_files = {}
java_files = {}
txt_files = {}

# React code files
jsx_files.update({
    'HelloReact': '''import React from 'react';

function HelloReact() {
  return <h1>Hello, React!</h1>;
}

export default HelloReact;
''',
    'JSXDemo': '''import React from 'react';

function JSXDemo() {
  const message = 'This is JSX syntax.';
  return (
    <div>
      <h2>{message}</h2>
      <p>JSX combines JavaScript and HTML-like syntax.</p>
    </div>
  );
}

export default JSXDemo;
''',
    'ReactStructure': '''import React from 'react';

function ReactStructure() {
  return (
    <div>
      <h1>React App Structure</h1>
      <ul>
        <li>Components</li>
        <li>State</li>
        <li>Props</li>
      </ul>
    </div>
  );
}

export default ReactStructure;
''',
    'CreateReactApp': '''import React from 'react';

function CreateReactApp() {
  return (
    <div>
      <h1>Create React App Example</h1>
      <p>Use npx create-react-app my-app</p>
    </div>
  );
}

export default CreateReactApp;
''',
    'FunctionalComponent': '''import React from 'react';

function FunctionalComponent() {
  return <div>This is a functional component.</div>;
}

export default FunctionalComponent;
''',
    'ClassComponent': '''import React, { Component } from 'react';

class ClassComponent extends Component {
  render() {
    return <div>This is a class component.</div>;
  }
}

export default ClassComponent;
''',
    'NestedComponent': '''import React from 'react';

function Child() {
  return <p>I am a child component.</p>;
}

function NestedComponent() {
  return (
    <div>
      <h2>Nested Component</h2>
      <Child />
    </div>
  );
}

export default NestedComponent;
''',
    'ReusableComponent': '''import React from 'react';

function Button({ label }) {
  return <button>{label}</button>;
}

function ReusableComponent() {
  return (
    <div>
      <Button label="Save" />
      <Button label="Cancel" />
    </div>
  );
}

export default ReusableComponent;
''',
    'PropsDemo': '''import React from 'react';

function Greeting({ name }) {
  return <h3>Hello, {name}</h3>;
}

function PropsDemo() {
  return <Greeting name="Amit" />;
}

export default PropsDemo;
''',
    'StateDemo': '''import React, { useState } from 'react';

function StateDemo() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default StateDemo;
''',
    'StudentComponent': '''import React from 'react';

function StudentComponent({ student }) {
  return (
    <div>
      <h3>{student.name}</h3>
      <p>Roll: {student.roll}</p>
    </div>
  );
}

function StudentComponentWrapper() {
  const student = { name: 'Riya', roll: 12 };
  return <StudentComponent student={student} />;
}

export default StudentComponentWrapper;
''',
    'CounterApp': '''import React, { useState } from 'react';

function CounterApp() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Counter App</h1>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}

export default CounterApp;
''',
    'ButtonClick': '''import React from 'react';

function ButtonClick() {
  const handleClick = () => alert('Button clicked!');

  return <button onClick={handleClick}>Click Me</button>;
}

export default ButtonClick;
''',
    'FormSubmit': '''import React, { useState } from 'react';

function FormSubmit() {
  const [name, setName] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Submitted: ${name}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <button type="submit">Submit</button>
    </form>
  );
}

export default FormSubmit;
''',
    'InputEvent': '''import React, { useState } from 'react';

function InputEvent() {
  const [text, setText] = useState('');

  return (
    <div>
      <input value={text} onChange={(event) => setText(event.target.value)} />
      <p>You typed: {text}</p>
    </div>
  );
}

export default InputEvent;
''',
    'MouseEvent': '''import React, { useState } from 'react';

function MouseEvent() {
  const [status, setStatus] = useState('Mouse out');

  return (
    <div>
      <button onMouseEnter={() => setStatus('Mouse over')} onMouseLeave={() => setStatus('Mouse out')}>
        Hover me
      </button>
      <p>{status}</p>
    </div>
  );
}

export default MouseEvent;
''',
    'UseStateDemo': '''import React, { useState } from 'react';

function UseStateDemo() {
  const [value, setValue] = useState('Hello');

  return (
    <div>
      <p>{value}</p>
      <button onClick={() => setValue('React Hooks')}>Change</button>
    </div>
  );
}

export default UseStateDemo;
''',
    'UseEffectDemo': '''import React, { useState, useEffect } from 'react';

function UseEffectDemo() {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const interval = setInterval(() => setTime(new Date().toLocaleTimeString()), 1000);
    return () => clearInterval(interval);
  }, []);

  return <div>Current time: {time}</div>;
}

export default UseEffectDemo;
''',
    'UseRefDemo': '''import React, { useRef } from 'react';

function UseRefDemo() {
  const inputRef = useRef(null);

  const focusInput = () => inputRef.current && inputRef.current.focus();

  return (
    <div>
      <input ref={inputRef} placeholder="Focus me" />
      <button onClick={focusInput}>Focus input</button>
    </div>
  );
}

export default UseRefDemo;
''',
    'CustomHookDemo': '''import React, { useState, useEffect } from 'react';

function useCurrentTime() {
  const [time, setTime] = useState(new Date().toLocaleTimeString());
  useEffect(() => {
    const interval = setInterval(() => setTime(new Date().toLocaleTimeString()), 1000);
    return () => clearInterval(interval);
  }, []);
  return time;
}

function CustomHookDemo() {
  const time = useCurrentTime();
  return <div>Current time: {time}</div>;
}

export default CustomHookDemo;
''',
    'FetchAPI': '''import React, { useState, useEffect } from 'react';

function FetchAPI() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((response) => response.json())
      .then((result) => setData(result.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Posts</h1>
      <ul>{data.map((item) => <li key={item.id}>{item.title}</li>)}</ul>
    </div>
  );
}

export default FetchAPI;
''',
    'AxiosDemo': '''import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AxiosDemo() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then((response) => setPosts(response.data.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Axios Posts</h1>
      <ul>{posts.map((post) => <li key={post.id}>{post.title}</li>)}</ul>
    </div>
  );
}

export default AxiosDemo;
''',
    'AsyncAwaitDemo': '''import React, { useState, useEffect } from 'react';

function AsyncAwaitDemo() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      const result = await response.json();
      setUsers(result.slice(0, 3));
    }
    fetchData();
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <ul>{users.map((user) => <li key={user.id}>{user.name}</li>)}</ul>
    </div>
  );
}

export default AsyncAwaitDemo;
''',
    'JSONPlaceholder': '''import React, { useState, useEffect } from 'react';

function JSONPlaceholder() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos')
      .then((response) => response.json())
      .then((data) => setTodos(data.slice(0, 3)));
  }, []);

  return (
    <div>
      <h1>Todos</h1>
      <ul>{todos.map((todo) => <li key={todo.id}>{todo.title}</li>)}</ul>
    </div>
  );
}

export default JSONPlaceholder;
''',
    'ValidationDemo': '''import React, { useState } from 'react';

function ValidationDemo() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!email.includes('@')) {
      setError('Please enter a valid email');
    } else {
      setError('');
      alert('Form submitted');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <button type="submit">Submit</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
}

export default ValidationDemo;
''',
    'RegistrationForm': '''import React, { useState } from 'react';

function RegistrationForm() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Registered ${name}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit">Register</button>
    </form>
  );
}

export default RegistrationForm;
''',
    'LoginForm': '''import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Logged in as ${username}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <button type="submit">Login</button>
    </form>
  );
}

export default LoginForm;
''',
    'ControlledComponent': '''import React, { useState } from 'react';

function ControlledComponent() {
  const [value, setValue] = useState('');
  return (
    <div>
      <input value={value} onChange={(e) => setValue(e.target.value)} />
      <p>Current value: {value}</p>
    </div>
  );
}

export default ControlledComponent;
''',
    'NavigationDemo': '''import React from 'react';
import { Link } from 'react-router-dom';

function NavigationDemo() {
  return (
    <nav>
      <Link to="/">Home</Link> | <Link to="/about">About</Link>
    </nav>
  );
}

export default NavigationDemo;
''',
    'ProtectedRoute': '''import React from 'react';
import { Navigate } from 'react-router-dom';

function ProtectedRoute({ isAuth, children }) {
  return isAuth ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
''',
    'ReactRouter': '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function Home() { return <h2>Home</h2>; }
function About() { return <h2>About</h2>; }

function ReactRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default ReactRouter;
''',
    'RouteParameters': '''import React from 'react';
import { useParams } from 'react-router-dom';

function RouteParameters() {
  const { id } = useParams();
  return <div>Route parameter: {id}</div>;
}

export default RouteParameters;
''',
    'TodoApp': '''import React, { useState } from 'react';

function TodoApp() {
  const [task, setTask] = useState('');
  const [todos, setTodos] = useState([]);

  const addTask = () => {
    if (task) {
      setTodos([...todos, task]);
      setTask('');
    }
  };

  return (
    <div>
      <input value={task} onChange={(e) => setTask(e.target.value)} placeholder="New task" />
      <button onClick={addTask}>Add</button>
      <ul>{todos.map((item, index) => <li key={index}>{item}</li>)}</ul>
    </div>
  );
}

export default TodoApp;
''',
    'StudentPortal': '''import React from 'react';

function StudentPortal() {
  const student = { name: 'Maya', course: 'Java' };
  return (
    <div>
      <h1>Student Portal</h1>
      <p>Name: {student.name}</p>
      <p>Course: {student.course}</p>
    </div>
  );
}

export default StudentPortal;
''',
    'WeatherApp': '''import React, { useState, useEffect } from 'react';

function WeatherApp() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    setWeather({ temp: 25, condition: 'Sunny' });
  }, []);

  return (
    <div>
      <h1>Weather App</h1>
      {weather ? <p>{weather.condition}, {weather.temp}°C</p> : <p>Loading...</p>}
    </div>
  );
}

export default WeatherApp;
''',
    'EmployeeCRUD': '''import React, { useState } from 'react';

function EmployeeCRUD() {
  const [employees, setEmployees] = useState([{ id: 1, name: 'Amit' }]);
  const [name, setName] = useState('');

  const addEmployee = () => {
    if (name) {
      setEmployees([...employees, { id: employees.length + 1, name }]);
      setName('');
    }
  };

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <button onClick={addEmployee}>Add</button>
      <ul>{employees.map((emp) => <li key={emp.id}>{emp.name}</li>)}</ul>
    </div>
  );
}

export default EmployeeCRUD;
''',
    'Assessment1': '''import React from 'react';

function Assessment1() {
  return <div>Assessment 1: React component</div>;
}

export default Assessment1;
''',
    'Assessment2': '''import React from 'react';

function Assessment2() {
  return <div>Assessment 2: React component</div>;
}

export default Assessment2;
''',
    'Assessment3': '''import React from 'react';

function Assessment3() {
  return <div>Assessment 3: React component</div>;
}

export default Assessment3;
''',
    'Assessment4': '''import React from 'react';

function Assessment4() {
  return <div>Assessment 4: React component</div>;
}

export default Assessment4;
''',
})

# Spring Core code files
java_files.update({
    'SpringOverview': '''public class SpringOverview {
    public static void main(String[] args) {
        System.out.println("Spring overview: lightweight Java framework.");
    }
}
''',
    'SpringModules': '''public class SpringModules {
    public static void main(String[] args) {
        System.out.println("Core, MVC, Boot, Data, Security are major Spring modules.");
    }
}
''',
    'SpringBenefits': '''public class SpringBenefits {
    public static void main(String[] args) {
        System.out.println("Spring benefits: dependency injection, modular architecture, testability.");
    }
}
''',
    'SpringArchitecture': '''public class SpringArchitecture {
    public static void main(String[] args) {
        System.out.println("Spring architecture includes IoC container, AOP, and modules.");
    }
}
''',
    'IOCContainer': '''public class IOCContainer {
    public static void main(String[] args) {
        System.out.println("Inversion of Control means objects are created by the container.");
    }
}
''',
    'DependencyInjection': '''public class DependencyInjection {
    public static void main(String[] args) {
        System.out.println("Dependency injection can be constructor or setter based.");
    }
}
''',
    'ConstructorInjection': '''public class ConstructorInjection {
    private final String value;

    public ConstructorInjection(String value) {
        this.value = value;
    }

    public static void main(String[] args) {
        ConstructorInjection demo = new ConstructorInjection("Injected value");
        System.out.println(demo.value);
    }
}
''',
    'SetterInjection': '''public class SetterInjection {
    private String value;

    public void setValue(String value) {
        this.value = value;
    }

    public static void main(String[] args) {
        SetterInjection demo = new SetterInjection();
        demo.setValue("Injected value");
        System.out.println(demo.value);
    }
}
''',
    'XMLBeanConfig': '''public class XMLBeanConfig {
    public static void main(String[] args) {
        System.out.println("XML bean configuration example.");
    }
}
''',
    'AnnotationBean': '''public class AnnotationBean {
    public static void main(String[] args) {
        System.out.println("Annotation bean configuration example.");
    }
}
''',
    'JavaConfig': '''public class JavaConfig {
    public static void main(String[] args) {
        System.out.println("Java-based configuration example.");
    }
}
''',
    'BeanScope': '''public class BeanScope {
    public static void main(String[] args) {
        System.out.println("Spring bean scopes include singleton and prototype.");
    }
}
''',
    'AutowiredAnnotation': '''public class AutowiredAnnotation {
    public static void main(String[] args) {
        System.out.println("@Autowired injects dependencies automatically.");
    }
}
''',
    'AutowireByType': '''public class AutowireByType {
    public static void main(String[] args) {
        System.out.println("Autowire by type example.");
    }
}
''',
    'AutowireByName': '''public class AutowireByName {
    public static void main(String[] args) {
        System.out.println("Autowire by name example.");
    }
}
''',
    'QualifierAnnotation': '''public class QualifierAnnotation {
    public static void main(String[] args) {
        System.out.println("@Qualifier helps choose between multiple beans.");
    }
}
''',
    'ControllerDemo': '''public class ControllerDemo {
    public static void main(String[] args) {
        System.out.println("Controller stereotype indicates a web controller component.");
    }
}
''',
    'ServiceDemo': '''public class ServiceDemo {
    public static void main(String[] args) {
        System.out.println("Service stereotype indicates a service layer bean.");
    }
}
''',
    'RepositoryDemo': '''public class RepositoryDemo {
    public static void main(String[] args) {
        System.out.println("Repository stereotype indicates a data access bean.");
    }
}
''',
    'BeanAnnotation': '''public class BeanAnnotation {
    public static void main(String[] args) {
        System.out.println("@Bean annotated methods define beans in Java config.");
    }
}
''',
    'PropertyInjection': '''public class PropertyInjection {
    public static void main(String[] args) {
        System.out.println("Property injection reads values from configuration.");
    }
}
''',
    'ApplicationProperties': '''public class ApplicationProperties {
    public static void main(String[] args) {
        System.out.println("Application properties are stored in application.properties.");
    }
}
''',
    'PropertySourceDemo': '''public class PropertySourceDemo {
    public static void main(String[] args) {
        System.out.println("@PropertySource loads property files.");
    }
}
''',
    'EnvironmentDemo': '''public class EnvironmentDemo {
    public static void main(String[] args) {
        System.out.println("Environment object provides access to property values.");
    }
}
''',
    'LifecycleAnnotation': '''public class LifecycleAnnotation {
    public static void main(String[] args) {
        System.out.println("@PostConstruct and @PreDestroy manage bean lifecycle.");
    }
}
''',
    'InitMethodDemo': '''public class InitMethodDemo {
    public static void main(String[] args) {
        System.out.println("Init method example runs after bean creation.");
    }
}
''',
    'DestroyMethodDemo': '''public class DestroyMethodDemo {
    public static void main(String[] args) {
        System.out.println("Destroy method example runs before bean destruction.");
    }
}
''',
    'BeanPostProcessor': '''public class BeanPostProcessor {
    public static void main(String[] args) {
        System.out.println("BeanPostProcessor modifies beans after initialization.");
    }
}
''',
    'StudentSpringApp': '''public class StudentSpringApp {
    public static void main(String[] args) {
        System.out.println("Student Spring application example.");
    }
}
''',
    'LibrarySpringApp': '''public class LibrarySpringApp {
    public static void main(String[] args) {
        System.out.println("Library Spring application example.");
    }
}
''',
    'EmployeeSpringApp': '''public class EmployeeSpringApp {
    public static void main(String[] args) {
        System.out.println("Employee Spring application example.");
    }
}
''',
    'BankSpringApp': '''public class BankSpringApp {
    public static void main(String[] args) {
        System.out.println("Bank Spring application example.");
    }
}
''',
    'Assessment1': '''public class Assessment1 {
    public static void main(String[] args) {
        System.out.println("Spring Core assessment 1.");
    }
}
''',
    'Assessment2': '''public class Assessment2 {
    public static void main(String[] args) {
        System.out.println("Spring Core assessment 2.");
    }
}
''',
    'Assessment3': '''public class Assessment3 {
    public static void main(String[] args) {
        System.out.println("Spring Core assessment 3.");
    }
}
''',
    'Assessment4': '''public class Assessment4 {
    public static void main(String[] args) {
        System.out.println("Spring Core assessment 4.");
    }
}
''',
})

# Spring Boot code files
java_files.update({
    'SpringBootOverview': '''public class SpringBootOverview {
    public static void main(String[] args) {
        System.out.println("Spring Boot is an opinionated framework for Spring applications.");
    }
}
''',
    'SpringBootFeatures': '''public class SpringBootFeatures {
    public static void main(String[] args) {
        System.out.println("Spring Boot features include auto configuration and starter dependencies.");
    }
}
''',
    'SpringBootArchitecture': '''public class SpringBootArchitecture {
    public static void main(String[] args) {
        System.out.println("Spring Boot applications run on an embedded server.");
    }
}
''',
    'FirstSpringBootApp': '''public class FirstSpringBootApp {
    public static void main(String[] args) {
        System.out.println("This is a sample Spring Boot application entry point.");
    }
}
''',
    'SpringInitializer': '''public class SpringInitializer {
    public static void main(String[] args) {
        System.out.println("Use Spring Initializr to bootstrap a Spring Boot project.");
    }
}
''',
    'MavenProject': '''public class MavenProject {
    public static void main(String[] args) {
        System.out.println("Maven project uses pom.xml to manage dependencies.");
    }
}
''',
    'GradleProject': '''public class GradleProject {
    public static void main(String[] args) {
        System.out.println("Gradle project uses build.gradle for project setup.");
    }
}
''',
    'ApplicationProperties': '''public class ApplicationProperties {
    public static void main(String[] args) {
        System.out.println("application.properties stores configuration values.");
    }
}
''',
    'HelloController': '''import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello from Spring Boot";
    }
}
''',
    'StudentController': '''import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StudentController {
    @GetMapping("/students")
    public String getStudents() {
        return "Student list";
    }
}
''',
    'ProductController': '''import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ProductController {
    @GetMapping("/products")
    public String getProducts() {
        return "Product list";
    }
}
''',
    'EmployeeController': '''import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EmployeeController {
    @GetMapping("/employees")
    public String getEmployees() {
        return "Employee list";
    }
}
''',
    'GetMappingDemo': '''import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GetMappingDemo {
    @GetMapping("/get-demo")
    public String getDemo() {
        return "GET mapping demo";
    }
}
''',
    'PostMappingDemo': '''import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PostMappingDemo {
    @PostMapping("/post-demo")
    public String postDemo() {
        return "POST mapping demo";
    }
}
''',
    'PutMappingDemo': '''import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PutMappingDemo {
    @PutMapping("/put-demo")
    public String putDemo() {
        return "PUT mapping demo";
    }
}
''',
    'DeleteMappingDemo': '''import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DeleteMappingDemo {
    @DeleteMapping("/delete-demo")
    public String deleteDemo() {
        return "DELETE mapping demo";
    }
}
''',
    'ValidationException': '''public class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}
''',
    'ErrorResponse': '''public class ErrorResponse {
    private String message;

    public ErrorResponse(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }
}
''',
    'CustomException': '''public class CustomException extends RuntimeException {
    public CustomException(String message) {
        super(message);
    }
}
''',
    'GlobalExceptionHandler': '''import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(CustomException.class)
    public ResponseEntity<ErrorResponse> handleCustomException(CustomException ex) {
        return ResponseEntity.badRequest().body(new ErrorResponse(ex.getMessage()));
    }
}
''',
    'BankService': '''public class BankService {
    public String getBankDetails() {
        return "Bank service response";
    }
}
''',
    'EmployeeService': '''public class EmployeeService {
    public String getEmployeeDetails() {
        return "Employee service response";
    }
}
''',
    'ProductService': '''public class ProductService {
    public String getProductDetails() {
        return "Product service response";
    }
}
''',
    'StudentService': '''public class StudentService {
    public String getStudentDetails() {
        return "Student service response";
    }
}
''',
    'CrudRepositoryDemo': '''public class CrudRepositoryDemo {
    public static void main(String[] args) {
        System.out.println("CrudRepository demo.");
    }
}
''',
    'JpaRepositoryDemo': '''public class JpaRepositoryDemo {
    public static void main(String[] args) {
        System.out.println("JpaRepository demo.");
    }
}
''',
    'StudentEntity': '''import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class StudentEntity {
    @Id
    private Long id;
    private String name;

    public StudentEntity() {}
}
''',
    'EmployeeEntity': '''import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class EmployeeEntity {
    @Id
    private Long id;
    private String name;

    public EmployeeEntity() {}
}
''',
    'EmployeeManagementAPI': '''public class EmployeeManagementAPI {
    public static void main(String[] args) {
        System.out.println("Employee management REST API.");
    }
}
''',
    'BankManagementAPI': '''public class BankManagementAPI {
    public static void main(String[] args) {
        System.out.println("Bank management REST API.");
    }
}
''',
    'LibraryManagementAPI': '''public class LibraryManagementAPI {
    public static void main(String[] args) {
        System.out.println("Library management REST API.");
    }
}
''',
    'StudentManagementAPI': '''public class StudentManagementAPI {
    public static void main(String[] args) {
        System.out.println("Student management REST API.");
    }
}
''',
    'BasicSecurity': '''public class BasicSecurity {
    public static void main(String[] args) {
        System.out.println("Basic Spring Security example.");
    }
}
''',
    'PasswordEncoder': '''public class PasswordEncoder {
    public static void main(String[] args) {
        System.out.println("Password encoder example.");
    }
}
''',
    'RoleBasedAccess': '''public class RoleBasedAccess {
    public static void main(String[] args) {
        System.out.println("Role-based access control example.");
    }
}
''',
    'UserAuthentication': '''public class UserAuthentication {
    public static void main(String[] args) {
        System.out.println("User authentication example.");
    }
}
''',
    'Assessment1': '''public class Assessment1 {
    public static void main(String[] args) {
        System.out.println("Spring Boot assessment 1.");
    }
}
''',
    'Assessment2': '''public class Assessment2 {
    public static void main(String[] args) {
        System.out.println("Spring Boot assessment 2.");
    }
}
''',
    'Assessment3': '''public class Assessment3 {
    public static void main(String[] args) {
        System.out.println("Spring Boot assessment 3.");
    }
}
''',
    'Assessment4': '''public class Assessment4 {
    public static void main(String[] args) {
        System.out.println("Spring Boot assessment 4.");
    }
}
''',
})

# Git / Maven text files
txt_files.update({
    'GitInit': 'git init\n',
    'GitClone': 'git clone <repository-url>\n',
    'GitStatus': 'git status\n',
    'GitAdd': 'git add .\n',
    'GitCommit': 'git commit -m "Initial commit"\n',
    'GitPush': 'git push origin main\n',
    'GitPull': 'git pull origin main\n',
    'CreateBranch': 'git branch feature-branch\n',
    'SwitchBranch': 'git checkout feature-branch\n',
    'MergeBranch': 'git checkout main\ngit merge feature-branch\n',
    'DeleteBranch': 'git branch -d feature-branch\n',
    'ForkRepository': 'Use the GitHub UI to fork the repository into your account.\n',
    'CreateRepository': 'Use the GitHub UI or gh repo create to create a new repository.\n',
    'PushProject': 'git add .\ngit commit -m "Add project files"\ngit push origin main\n',
    'PullRequest': 'Create a pull request from your branch into main on GitHub.\n',
    'RepositoryDemo': 'mvn dependency:resolve\n',
    'DependencyTree': 'mvn dependency:tree\n',
    'AddSpring': 'Add spring-boot-starter-web dependency to pom.xml.\n',
    'AddJUnit': 'Add junit-jupiter dependency to pom.xml.\n',
    'InstallProject': 'mvn install\n',
    'CompileProject': 'mvn compile\n',
    'PackageProject': 'mvn package\n',
    'CleanProject': 'mvn clean\n',
    'PomBasics': 'A pom.xml defines groupId, artifactId, version, dependencies, and build settings.\n',
    'Profiles': 'Define profiles in pom.xml to build with different environments.\n',
    'Plugins': 'Add plugins in pom.xml under the build element, such as maven-compiler-plugin.\n',
    'Dependencies': 'Declare external libraries in pom.xml dependencies section.\n',
    'MavenStructure': 'src/main/java - application code\nsrc/main/resources - application resources\nsrc/test/java - test code\n',
    'MavenLifecycle': 'validate, compile, test, package, verify, install, deploy\n',
    'MavenGoals': 'mvn compile, mvn test, mvn package, mvn install\n',
    'InstallMaven': 'Download and install Maven, then verify with mvn -v\n',
    'GitMavenProject': 'Initialize project with git and build using Maven commands.\n',
    'EmployeeManagement': 'Create Employee management application with Git and Maven.\n',
    'StudentManagement': 'Create Student management application with Git and Maven.\n',
    'SpringMavenProject': 'Create Spring Boot project and manage it with Maven.\n',
    'GitPush': 'git push origin main\n',
})

# write helper functions

def jsx_content(name: str) -> str:
    return jsx_files.get(name, f"import React from 'react';\n\nfunction {name}() {{\n  return <div>{name} component</div>;\n}}\n\nexport default {name};\n")


def java_content(name: str) -> str:
    return java_files.get(name, f"public class {name} {{\n    public static void main(String[] args) {{\n        System.out.println(\"{name} executed.\");\n    }}\n}}\n")


def txt_content(name: str) -> str:
    return txt_files.get(name, f"{name} example command or description.\n")


def write_files():
    updated = 0
    for module in modules:
        root = base / module
        for path in root.rglob('*'):
            if not path.is_file():
                continue
            if path.suffix == '.jsx':
                content = jsx_content(path.stem)
            elif path.suffix == '.java':
                content = java_content(path.stem)
            elif path.suffix == '.txt':
                content = txt_content(path.stem)
            else:
                continue
            path.write_text(content, encoding='utf-8')
            updated += 1
    print(f'Updated {updated} code files in modules 10-13.')


if __name__ == '__main__':
    write_files()
