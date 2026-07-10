from pathlib import Path

base = Path(r'c:\Users\ydaya\Desktop\Cognizant Deep Skilling')
modules = [
    'Module_06_File_Handling',
    'Module_07_JDBC',
    'Module_08_SQL_MySQL',
    'Module_09_HTML_CSS_JavaScript',
]

java_paths = []
sql_paths = []
html_paths = []
for module in modules:
    for path in (base / module).rglob('*'):
        if path.is_file():
            if path.suffix == '.java':
                java_paths.append(path)
            elif path.suffix == '.sql':
                sql_paths.append(path)
            elif path.suffix == '.html':
                html_paths.append(path)


def java_content(rel_path: str) -> str:
    name = Path(rel_path).stem
    if name == 'CreateFile':
        return '''import java.io.File;
import java.io.IOException;

public class CreateFile {
    public static void main(String[] args) {
        try {
            File file = new File("sample.txt");
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException ex) {
            System.out.println("An error occurred: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeleteFile':
        return '''import java.io.File;

public class DeleteFile {
    public static void main(String[] args) {
        File file = new File("sample.txt");
        if (file.delete()) {
            System.out.println("Deleted the file: " + file.getName());
        } else {
            System.out.println("Failed to delete the file.");
        }
    }
}
'''
    if name == 'CreateDirectory':
        return '''import java.io.File;

public class CreateDirectory {
    public static void main(String[] args) {
        File dir = new File("sampleDir");
        if (dir.mkdir()) {
            System.out.println("Directory created: " + dir.getName());
        } else {
            System.out.println("Failed to create directory.");
        }
    }
}
'''
    if name == 'CheckFileExists':
        return '''import java.io.File;

public class CheckFileExists {
    public static void main(String[] args) {
        File file = new File("sample.txt");
        if (file.exists()) {
            System.out.println("File exists: " + file.getAbsolutePath());
        } else {
            System.out.println("File does not exist.");
        }
    }
}
'''
    if name == 'FileWriterDemo':
        return '''import java.io.FileWriter;
import java.io.IOException;

public class FileWriterDemo {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("output.txt")) {
            writer.write("Hello, FileWriter!\n");
            System.out.println("Data written to output.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BufferedWriterDemo':
        return '''import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BufferedWriterDemo {
    public static void main(String[] args) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("buffered.txt"))) {
            writer.write("BufferedWriter example\n");
            System.out.println("Data written to buffered.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PrintWriterDemo':
        return '''import java.io.PrintWriter;
import java.io.IOException;

public class PrintWriterDemo {
    public static void main(String[] args) {
        try (PrintWriter writer = new PrintWriter("printwriter.txt")) {
            writer.println("PrintWriter example");
            System.out.println("Data written to printwriter.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'AppendFileDemo':
        return '''import java.io.FileWriter;
import java.io.IOException;

public class AppendFileDemo {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("append.txt", true)) {
            writer.write("Appended line\n");
            System.out.println("Data appended to append.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'FileReaderDemo':
        return '''import java.io.FileReader;
import java.io.IOException;

public class FileReaderDemo {
    public static void main(String[] args) {
        try (FileReader reader = new FileReader("output.txt")) {
            int character;
            while ((character = reader.read()) != -1) {
                System.out.print((char) character);
            }
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BufferedReaderDemo':
        return '''import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BufferedReaderDemo {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("output.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ReadLineByLine':
        return '''import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadLineByLine {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("output.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            System.out.println("Error reading file: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ScannerFileReader':
        return '''import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ScannerFileReader {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(new File("output.txt"))) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (FileNotFoundException ex) {
            System.out.println("File not found: " + ex.getMessage());
        }
    }
}
'''
    if name == 'CopyFileDemo':
        return '''import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyFileDemo {
    public static void main(String[] args) {
        try (FileInputStream in = new FileInputStream("output.txt");
             FileOutputStream out = new FileOutputStream("copy.txt")) {
            int byteData;
            while ((byteData = in.read()) != -1) {
                out.write(byteData);
            }
            System.out.println("File copied successfully.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'MoveFileDemo':
        return '''import java.io.File;

public class MoveFileDemo {
    public static void main(String[] args) {
        File source = new File("copy.txt");
        File destination = new File("moved.txt");
        if (source.renameTo(destination)) {
            System.out.println("File moved successfully.");
        } else {
            System.out.println("Failed to move file.");
        }
    }
}
'''
    if name == 'RenameFileDemo':
        return '''import java.io.File;

public class RenameFileDemo {
    public static void main(String[] args) {
        File file = new File("moved.txt");
        File renamed = new File("renamed.txt");
        if (file.renameTo(renamed)) {
            System.out.println("File renamed successfully.");
        } else {
            System.out.println("Failed to rename file.");
        }
    }
}
'''
    if name == 'DeleteDirectoryDemo':
        return '''import java.io.File;

public class DeleteDirectoryDemo {
    public static void main(String[] args) {
        File dir = new File("sampleDir");
        if (dir.exists() && dir.isDirectory()) {
            if (dir.delete()) {
                System.out.println("Directory deleted.");
            } else {
                System.out.println("Directory not empty or could not be deleted.");
            }
        }
    }
}
'''
    if name == 'BufferedInputStreamDemo':
        return '''import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class BufferedInputStreamDemo {
    public static void main(String[] args) {
        try (BufferedInputStream in = new BufferedInputStream(new FileInputStream("output.txt"))) {
            int data;
            while ((data = in.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BufferedOutputStreamDemo':
        return '''import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class BufferedOutputStreamDemo {
    public static void main(String[] args) {
        try (BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream("buffered_out.txt"))) {
            out.write("Buffered output example\n".getBytes());
            System.out.println("Written to buffered_out.txt");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DataInputStreamDemo':
        return '''import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class DataInputStreamDemo {
    public static void main(String[] args) {
        try (DataInputStream in = new DataInputStream(new FileInputStream("data.bin"))) {
            int value = in.readInt();
            System.out.println("Read integer: " + value);
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DataOutputStreamDemo':
        return '''import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class DataOutputStreamDemo {
    public static void main(String[] args) {
        try (DataOutputStream out = new DataOutputStream(new FileOutputStream("data.bin"))) {
            out.writeInt(2024);
            System.out.println("Written integer to data.bin");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SerializableDemo':
        return '''import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Person implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;

    public Person(String name) {
        this.name = name;
    }
}

public class SerializableDemo {
    public static void main(String[] args) {
        Person person = new Person("Amit");
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("person.ser"))) {
            out.writeObject(person);
            System.out.println("Serialized person object.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ObjectOutputDemo':
        return '''import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class ObjectOutputDemo {
    public static void main(String[] args) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("object.bin"))) {
            out.writeObject("Hello ObjectOutputStream");
            System.out.println("Object written to object.bin");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'StudentSerialization':
        return '''import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Student implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int roll;

    public Student(String name, int roll) {
        this.name = name;
        this.roll = roll;
    }
}

public class StudentSerialization {
    public static void main(String[] args) {
        Student student = new Student("Pooja", 12);
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("student.ser"))) {
            out.writeObject(student);
            System.out.println("Student serialized.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'EmployeeSerialization':
        return '''import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int id;

    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }
}

public class EmployeeSerialization {
    public static void main(String[] args) {
        Employee employee = new Employee("Neha", 105);
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("employee.ser"))) {
            out.writeObject(employee);
            System.out.println("Employee serialized.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeserializeDemo':
        return '''import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class DeserializeDemo {
    public static void main(String[] args) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("person.ser"))) {
            Object obj = in.readObject();
            System.out.println("Deserialized object: " + obj);
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'StudentDeserialization':
        return '''import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class StudentDeserialization {
    public static void main(String[] args) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("student.ser"))) {
            Object obj = in.readObject();
            System.out.println("Student deserialized: " + obj);
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'EmployeeDeserialization':
        return '''import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class EmployeeDeserialization {
    public static void main(String[] args) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("employee.ser"))) {
            Object obj = in.readObject();
            System.out.println("Employee deserialized: " + obj);
        } catch (IOException | ClassNotFoundException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PathDemo':
        return '''import java.nio.file.Path;
import java.nio.file.Paths;

public class PathDemo {
    public static void main(String[] args) {
        Path path = Paths.get("sample.txt");
        System.out.println("Path: " + path);
        System.out.println("File name: " + path.getFileName());
    }
}
'''
    if name == 'FilesCopyDemo':
        return '''import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesCopyDemo {
    public static void main(String[] args) {
        Path source = Paths.get("output.txt");
        Path target = Paths.get("copy2.txt");
        try {
            Files.copy(source, target);
            System.out.println("File copied successfully.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'FilesMoveDemo':
        return '''import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesMoveDemo {
    public static void main(String[] args) {
        Path source = Paths.get("copy2.txt");
        Path target = Paths.get("moved2.txt");
        try {
            Files.move(source, target);
            System.out.println("File moved successfully.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'FilesDeleteDemo':
        return '''import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FilesDeleteDemo {
    public static void main(String[] args) {
        Path path = Paths.get("moved2.txt");
        try {
            Files.deleteIfExists(path);
            System.out.println("File deleted if it existed.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'Assessment1':
        if 'Module_06_File_Handling' in rel_path:
            return '''import java.io.File;

public class Assessment1 {
    public static void main(String[] args) {
        File file = new File("assessment1.txt");
        System.out.println("Can read: " + file.canRead());
    }
}
'''
        return '''public class Assessment1 {
    public static void main(String[] args) {
        System.out.println("Assessment1 example.");
    }
}
'''
    if name == 'Assessment2':
        if 'Module_06_File_Handling' in rel_path:
            return '''import java.io.FileWriter;
import java.io.IOException;

public class Assessment2 {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("assessment2.txt")) {
            writer.write("Assessment2 data\n");
            System.out.println("Assessment2 file created.");
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
        return '''public class Assessment2 {
    public static void main(String[] args) {
        System.out.println("Assessment2 example.");
    }
}
'''
    if name == 'Assessment3':
        if 'Module_06_File_Handling' in rel_path:
            return '''import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Assessment3 {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new FileReader("assessment2.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
        return '''public class Assessment3 {
    public static void main(String[] args) {
        System.out.println("Assessment3 example.");
    }
}
'''
    if name == 'Assessment4':
        if 'Module_06_File_Handling' in rel_path:
            return '''import java.io.File;

public class Assessment4 {
    public static void main(String[] args) {
        File dir = new File("assessmentDir");
        if (!dir.exists()) {
            dir.mkdir();
        }
        System.out.println("Directory path: " + dir.getAbsolutePath());
    }
}
'''
        return '''public class Assessment4 {
    public static void main(String[] args) {
        System.out.println("Assessment4 example.");
    }
}
'''
    if name == 'ConnectionDemo':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionDemo {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            System.out.println("Connected successfully.");
        } catch (SQLException ex) {
            System.out.println("Connection failed: " + ex.getMessage());
        }
    }
}
'''
    if name == 'JdbcConnection':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JdbcConnection {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            System.out.println("JDBC connection created.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'LoadDriver':
        return '''public class LoadDriver {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver loaded.");
        } catch (ClassNotFoundException ex) {
            System.out.println("Driver not found: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DatabaseInfo':
        return '''import java.sql.DatabaseMetaData;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseInfo {
    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            DatabaseMetaData meta = connection.getMetaData();
            System.out.println("Database product: " + meta.getDatabaseProductName());
            System.out.println("Driver version: " + meta.getDriverVersion());
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'InsertStudent':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertStudent {
    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 1);
            stmt.setString(2, "Riya");
            stmt.executeUpdate();
            System.out.println("Student inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'InsertProduct':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertProduct {
    public static void main(String[] args) {
        String sql = "INSERT INTO product (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 1);
            stmt.setString(2, "Laptop");
            stmt.executeUpdate();
            System.out.println("Product inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'InsertEmployee':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertEmployee {
    public static void main(String[] args) {
        String sql = "INSERT INTO employee (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 101);
            stmt.setString(2, "Amit");
            stmt.executeUpdate();
            System.out.println("Employee inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'InsertDepartment':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class InsertDepartment {
    public static void main(String[] args) {
        String sql = "INSERT INTO department (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 10);
            stmt.setString(2, "HR");
            stmt.executeUpdate();
            System.out.println("Department inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SelectStudent':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class SelectStudent {
    public static void main(String[] args) {
        String sql = "SELECT id, name FROM student";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SelectProduct':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class SelectProduct {
    public static void main(String[] args) {
        String sql = "SELECT id, name FROM product";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SelectEmployee':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class SelectEmployee {
    public static void main(String[] args) {
        String sql = "SELECT id, name FROM employee";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SelectDepartment':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class SelectDepartment {
    public static void main(String[] args) {
        String sql = "SELECT id, name FROM department";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'UpdateStudent':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UpdateStudent {
    public static void main(String[] args) {
        String sql = "UPDATE student SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, "Riya Sharma");
            stmt.setInt(2, 1);
            stmt.executeUpdate();
            System.out.println("Student updated.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'UpdateProduct':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UpdateProduct {
    public static void main(String[] args) {
        String sql = "UPDATE product SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, "Gaming Laptop");
            stmt.setInt(2, 1);
            stmt.executeUpdate();
            System.out.println("Product updated.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'UpdateEmployee':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UpdateEmployee {
    public static void main(String[] args) {
        String sql = "UPDATE employee SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, "Amit Kumar");
            stmt.setInt(2, 101);
            stmt.executeUpdate();
            System.out.println("Employee updated.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'UpdateDepartment':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UpdateDepartment {
    public static void main(String[] args) {
        String sql = "UPDATE department SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, "Human Resources");
            stmt.setInt(2, 10);
            stmt.executeUpdate();
            System.out.println("Department updated.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeleteStudent':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteStudent {
    public static void main(String[] args) {
        String sql = "DELETE FROM student WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 1);
            stmt.executeUpdate();
            System.out.println("Student deleted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeleteProduct':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteProduct {
    public static void main(String[] args) {
        String sql = "DELETE FROM product WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 1);
            stmt.executeUpdate();
            System.out.println("Product deleted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeleteEmployee':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteEmployee {
    public static void main(String[] args) {
        String sql = "DELETE FROM employee WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 101);
            stmt.executeUpdate();
            System.out.println("Employee deleted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'DeleteDepartment':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteDepartment {
    public static void main(String[] args) {
        String sql = "DELETE FROM department WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 10);
            stmt.executeUpdate();
            System.out.println("Department deleted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PreparedInsert':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PreparedInsert {
    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name) VALUES (?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, 2);
            pstmt.setString(2, "Neha");
            pstmt.executeUpdate();
            System.out.println("Prepared insert completed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PreparedSelect':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PreparedSelect {
    public static void main(String[] args) {
        String sql = "SELECT name FROM student WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, 2);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.println(rs.getString("name"));
                }
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PreparedUpdate':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PreparedUpdate {
    public static void main(String[] args) {
        String sql = "UPDATE student SET name = ? WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "Neha Sharma");
            pstmt.setInt(2, 2);
            pstmt.executeUpdate();
            System.out.println("Prepared update completed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'PreparedDelete':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class PreparedDelete {
    public static void main(String[] args) {
        String sql = "DELETE FROM student WHERE id = ?";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, 2);
            pstmt.executeUpdate();
            System.out.println("Prepared delete completed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ResultSetDemo':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class ResultSetDemo {
    public static void main(String[] args) {
        String sql = "SELECT id, name FROM student";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") + ", Name: " + rs.getString("name"));
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ScrollableResultSet':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class ScrollableResultSet {
    public static void main(String[] args) throws SQLException {
        String sql = "SELECT id, name FROM student";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
             ResultSet rs = stmt.executeQuery(sql)) {
            rs.afterLast();
            while (rs.previous()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        }
    }
}
'''
    if name == 'MetaDataDemo':
        return '''import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MetaDataDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            DatabaseMetaData meta = conn.getMetaData();
            System.out.println("Database product name: " + meta.getDatabaseProductName());
            System.out.println("Driver name: " + meta.getDriverName());
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'ColumnInfoDemo':
        return '''import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ColumnInfoDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password")) {
            DatabaseMetaData meta = conn.getMetaData();
            try (ResultSet columns = meta.getColumns(null, null, "student", null)) {
                while (columns.next()) {
                    System.out.println(columns.getString("COLUMN_NAME") + " - " + columns.getString("TYPE_NAME"));
                }
            }
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'AutoCommitDemo':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class AutoCommitDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (3, 'Arjun')");
            conn.commit();
            System.out.println("Transaction committed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'CommitRollback':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class CommitRollback {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (4, 'Sara')");
            conn.rollback();
            System.out.println("Transaction rolled back.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BatchProcessing':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class BatchProcessing {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.addBatch("INSERT INTO student (id, name) VALUES (5, 'Ina')");
            stmt.addBatch("INSERT INTO student (id, name) VALUES (6, 'Neil')");
            stmt.executeBatch();
            conn.commit();
            System.out.println("Batch executed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'SavepointDemo':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Savepoint;
import java.sql.Statement;

public class SavepointDemo {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             Statement stmt = conn.createStatement()) {
            conn.setAutoCommit(false);
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (7, 'John')");
            Savepoint savepoint = conn.setSavepoint();
            stmt.executeUpdate("INSERT INTO student (id, name) VALUES (8, 'Lisa')");
            conn.rollback(savepoint);
            conn.commit();
            System.out.println("Rolled back to savepoint and committed.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'BankManagementJDBC':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class BankManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO bank_account (id, owner, balance) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 100);
            stmt.setString(2, "Kumar");
            stmt.setDouble(3, 1200.0);
            stmt.executeUpdate();
            System.out.println("Bank account inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'EmployeeManagementJDBC':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class EmployeeManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO employee (id, name, department) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 201);
            stmt.setString(2, "Rina");
            stmt.setString(3, "Sales");
            stmt.executeUpdate();
            System.out.println("Employee inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'LibraryManagementJDBC':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class LibraryManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO library_book (id, title, author) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 301);
            stmt.setString(2, "1984");
            stmt.setString(3, "George Orwell");
            stmt.executeUpdate();
            System.out.println("Book inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'StudentManagementJDBC':
        return '''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentManagementJDBC {
    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name, course) VALUES (?, ?, ?)";
        try (Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, 401);
            stmt.setString(2, "Nina");
            stmt.setString(3, "Computer Science");
            stmt.executeUpdate();
            System.out.println("Student inserted.");
        } catch (SQLException ex) {
            System.out.println("Error: " + ex.getMessage());
        }
    }
}
'''
    if name == 'Assessment1' and 'Module_07_JDBC' in rel_path:
        return '''public class Assessment1 {
    public static void main(String[] args) {
        System.out.println("JDBC Assessment 1.");
    }
}
'''
    if name == 'Assessment2' and 'Module_07_JDBC' in rel_path:
        return '''public class Assessment2 {
    public static void main(String[] args) {
        System.out.println("JDBC Assessment 2.");
    }
}
'''
    if name == 'Assessment3' and 'Module_07_JDBC' in rel_path:
        return '''public class Assessment3 {
    public static void main(String[] args) {
        System.out.println("JDBC Assessment 3.");
    }
}
'''
    if name == 'Assessment4' and 'Module_07_JDBC' in rel_path:
        return '''public class Assessment4 {
    public static void main(String[] args) {
        System.out.println("JDBC Assessment 4.");
    }
}
'''
    # Generic fallback for java files
    return f'''public class {name} {{
    public static void main(String[] args) {{
        System.out.println("{name} executed successfully.");
    }}
}}
'''


def sql_content(rel_path: str) -> str:
    name = Path(rel_path).stem
    if name == 'CreateDatabase':
        return 'CREATE DATABASE IF NOT EXISTS sample_db;'
    if name == 'CreateTable':
        return '''CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);'''
    if name == 'InsertData':
        return '''INSERT INTO student (student_id, name, age) VALUES
(1, 'Riya', 20),
(2, 'Amit', 22);'''
    if name == 'SelectData':
        return 'SELECT student_id, name, age FROM student;'
    if name == 'DeleteCommand':
        return 'DELETE FROM student WHERE student_id = 2;'
    if name == 'UpdateCommand':
        return "UPDATE student SET age = 21 WHERE student_id = 1;"
    if name == 'SelectWhere':
        return 'SELECT name FROM student WHERE age > 18;'
    if name == 'UniqueConstraint':
        return '''CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) UNIQUE
);'''
    if name == 'PrimaryKeyDemo':
        return '''CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);'''
    if name == 'ForeignKeyDemo':
        return '''CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    dept_id INT,
    emp_name VARCHAR(100),
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);'''
    if name == 'CheckConstraint':
        return '''CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    amount DECIMAL(10,2) CHECK (amount > 0)
);'''
    if name == 'SelectStudent':
        return 'SELECT student_id, name FROM student;'
    if name == 'SelectDepartment':
        return 'SELECT dept_id, dept_name FROM department;'
    if name == 'SelectEmployee':
        return 'SELECT emp_id, emp_name FROM employee;'
    if name == 'SelectProduct':
        return 'SELECT product_id, product_name FROM product;'
    if name == 'InsertStudent':
        return "INSERT INTO student (student_id, name, age) VALUES (3, 'Sara', 19);"
    if name == 'InsertDepartment':
        return "INSERT INTO department (dept_id, dept_name) VALUES (10, 'HR');"
    if name == 'InsertEmployee':
        return "INSERT INTO employee (emp_id, dept_id, emp_name) VALUES (101, 10, 'Nina');"
    if name == 'InsertProduct':
        return "INSERT INTO product (product_id, product_name) VALUES (1, 'Laptop');"
    if name == 'UpdateCommand':
        return "UPDATE student SET age = 23 WHERE student_id = 3;"
    if name == 'GroupByDemo':
        return '''SELECT dept_id, COUNT(*) AS count
FROM employee
GROUP BY dept_id;'''
    if name == 'HavingClause':
        return '''SELECT dept_id, COUNT(*) AS count
FROM employee
GROUP BY dept_id
HAVING COUNT(*) > 1;'''
    if name == 'OrderByDemo':
        return 'SELECT name, age FROM student ORDER BY age DESC;'
    if name == 'DistinctDemo':
        return 'SELECT DISTINCT dept_id FROM employee;'
    if name == 'StringFunctions':
        return "SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM student;"
    if name == 'NumericFunctions':
        return 'SELECT AVG(age) AS average_age FROM student;'
    if name == 'DateFunctions':
        return "SELECT CURRENT_DATE AS todays_date;"
    if name == 'AggregateFunctions':
        return 'SELECT COUNT(*) AS total_students FROM student;'
    if name == 'InnerJoin':
        return '''SELECT s.name, d.dept_name
FROM student s
INNER JOIN department d ON s.dept_id = d.dept_id;'''
    if name == 'LeftJoin':
        return '''SELECT s.name, d.dept_name
FROM student s
LEFT JOIN department d ON s.dept_id = d.dept_id;'''
    if name == 'RightJoin':
        return '''SELECT s.name, d.dept_name
FROM student s
RIGHT JOIN department d ON s.dept_id = d.dept_id;'''
    if name == 'FullJoin':
        return '''SELECT s.name, d.dept_name
FROM student s
LEFT JOIN department d ON s.dept_id = d.dept_id
UNION
SELECT s.name, d.dept_name
FROM student s
RIGHT JOIN department d ON s.dept_id = d.dept_id;'''
    if name == 'SingleRowSubQuery':
        return '''SELECT name
FROM student
WHERE dept_id = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'HR'
);'''
    if name == 'MultiRowSubQuery':
        return '''SELECT name
FROM student
WHERE dept_id IN (
    SELECT dept_id
    FROM department
    WHERE dept_name IN ('HR', 'Sales')
);'''
    if name == 'NestedQuery':
        return '''SELECT name
FROM student
WHERE age > (
    SELECT AVG(age)
    FROM student
);'''
    if name == 'CorrelatedSubQuery':
        return '''SELECT s.name
FROM student s
WHERE s.age > (
    SELECT AVG(age)
    FROM student
    WHERE dept_id = s.dept_id
);'''
    if name == 'CreateIndex':
        return 'CREATE INDEX idx_student_name ON student(name);'
    if name == 'DropIndex':
        return 'DROP INDEX idx_student_name ON student;'
    if name == 'CreateView':
        return '''CREATE VIEW student_summary AS
SELECT student_id, name, age
FROM student;'''
    if name == 'UpdateView':
        return '''CREATE OR REPLACE VIEW student_summary AS
SELECT student_id, name, age
FROM student
WHERE age > 18;'''
    if name == 'BankDatabase':
        return '''CREATE TABLE bank_account (
    account_id INT PRIMARY KEY,
    owner VARCHAR(100),
    balance DECIMAL(10,2)
);'''
    if name == 'EmployeeDatabase':
        return '''CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT
);'''
    if name == 'LibraryDatabase':
        return '''CREATE TABLE library_book (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(150)
);'''
    if name == 'StudentDatabase':
        return '''CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(150)
);'''
    if name.startswith('Assessment'):
        return f'-- SQL {name} example\nSELECT 1 AS sample;'
    # generic fallback
    return f'-- SQL for {name}\nSELECT 1;'


def html_content(rel_path: str) -> str:
    name = Path(rel_path).stem
    if name == 'BasicPage':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Basic Page</title>
</head>
<body>
    <h1>Welcome to the Basic Page</h1>
    <p>This is a simple HTML page.</p>
</body>
</html>
'''
    if name == 'Forms':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Form Example</title>
</head>
<body>
    <h1>Contact Form</h1>
    <form>
        <label>Name: <input type="text" name="name"></label><br>
        <label>Email: <input type="email" name="email"></label><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''
    if name == 'Lists':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lists</title>
</head>
<body>
    <h1>HTML Lists</h1>
    <ul>
        <li>Item one</li>
        <li>Item two</li>
        <li>Item three</li>
    </ul>
</body>
</html>
'''
    if name == 'Tables':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Table Example</title>
</head>
<body>
    <h1>Student Table</h1>
    <table border="1">
        <tr><th>Name</th><th>Age</th></tr>
        <tr><td>Riya</td><td>20</td></tr>
        <tr><td>Amit</td><td>22</td></tr>
    </table>
</body>
</html>
'''
    if name == 'InlineCSS':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Inline CSS</title>
</head>
<body>
    <h1 style="color: blue;">Inline CSS Example</h1>
</body>
</html>
'''
    if name == 'InternalCSS':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Internal CSS</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .highlight { color: green; }
    </style>
</head>
<body>
    <h1 class="highlight">Internal CSS Example</h1>
</body>
</html>
'''
    if name == 'ExternalCSS':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>External CSS</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1 class="page-title">External CSS Example</h1>
</body>
</html>
'''
    if name == 'ResponsiveLayout':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Responsive Layout</title>
    <style>
        .container { display: flex; flex-wrap: wrap; }
        .box { flex: 1 1 200px; border: 1px solid #333; margin: 8px; padding: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">Box 1</div>
        <div class="box">Box 2</div>
        <div class="box">Box 3</div>
    </div>
</body>
</html>
'''
    if name == 'PositionDemo':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Position Demo</title>
    <style>
        .relative { position: relative; left: 20px; top: 10px; }
    </style>
</head>
<body>
    <div class="relative">This box is positioned relatively.</div>
</body>
</html>
'''
    if name == 'GridDemo':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Grid Demo</title>
    <style>
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
        .item { background: #f0f0f0; padding: 10px; }
    </style>
</head>
<body>
    <div class="grid">
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
        <div class="item">4</div>
    </div>
</body>
</html>
'''
    if name == 'FlexboxDemo':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Flexbox Demo</title>
    <style>
        .flex { display: flex; gap: 10px; }
        .item { background: lightblue; padding: 10px; }
    </style>
</head>
<body>
    <div class="flex">
        <div class="item">A</div>
        <div class="item">B</div>
        <div class="item">C</div>
    </div>
</body>
</html>
'''
    if name == 'Variables':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JavaScript Variables</title>
</head>
<body>
    <h1>Variables</h1>
    <script>
        const name = 'Amit';
        let age = 22;
        document.write('Name: ' + name + '<br>Age: ' + age);
    </script>
</body>
</html>
'''
    if name == 'Operators':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JavaScript Operators</title>
</head>
<body>
    <h1>Operators</h1>
    <script>
        let x = 5 + 3;
        document.write('5 + 3 = ' + x);
    </script>
</body>
</html>
'''
    if name == 'Functions':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JavaScript Functions</title>
</head>
<body>
    <h1>Functions</h1>
    <script>
        function greet(name) {
            return 'Hello, ' + name;
        }
        document.write(greet('Riya')); 
    </script>
</body>
</html>
'''
    if name == 'Arrays':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>JavaScript Arrays</title>
</head>
<body>
    <h1>Arrays</h1>
    <script>
        let fruits = ['Apple', 'Banana', 'Cherry'];
        document.write(fruits.join(', '));
    </script>
</body>
</html>
'''
    if name == 'ButtonClick':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Button Click</title>
</head>
<body>
    <button onclick="document.getElementById('message').textContent = 'Button clicked!';">Click Me</button>
    <p id="message"></p>
</body>
</html>
'''
    if name == 'ChangeText':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Change Text</title>
</head>
<body>
    <p id="text">Original text.</p>
    <button onclick="document.getElementById('text').textContent = 'Text changed!';">Change Text</button>
</body>
</html>
'''
    if name == 'ImageChanger':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Image Changer</title>
</head>
<body>
    <img id="image" src="https://via.placeholder.com/150" alt="placeholder">
    <button onclick="document.getElementById('image').src='https://via.placeholder.com/200';">Change Image</button>
</body>
</html>
'''
    if name == 'FormValidation':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Form Validation</title>
    <script>
        function validate() {
            const name = document.getElementById('name').value;
            if (!name) {
                alert('Name is required');
                return false;
            }
            alert('Form submitted');
            return false;
        }
    </script>
</head>
<body>
    <form onsubmit="return validate()">
        <input id="name" type="text" placeholder="Name">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''
    if name == 'WindowEvents':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Window Events</title>
    <script>
        window.onload = function() {
            document.body.innerHTML += '<p>Window loaded</p>';
        };
    </script>
</head>
<body>
    <h1>Window Events</h1>
</body>
</html>
'''
    if name == 'MouseEvents':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mouse Events</title>
</head>
<body>
    <button onmouseover="document.getElementById('status').textContent='Mouse over'" onmouseout="document.getElementById('status').textContent='Mouse out'">Hover Me</button>
    <p id="status"></p>
</body>
</html>
'''
    if name == 'KeyboardEvents':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Keyboard Events</title>
    <script>
        document.addEventListener('keydown', function(event) {
            document.getElementById('output').textContent = 'Pressed: ' + event.key;
        });
    </script>
</head>
<body>
    <h1>Keyboard Events</h1>
    <p id="output"></p>
</body>
</html>
'''
    if name == 'EventListenerDemo':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Event Listener Demo</title>
    <script>
        function showMessage() {
            document.getElementById('message').textContent = 'Event listener executed';
        }
        window.addEventListener('load', function() {
            document.getElementById('button').addEventListener('click', showMessage);
        });
    </script>
</head>
<body>
    <button id="button">Click</button>
    <p id="message"></p>
</body>
</html>
'''
    if name == 'SaveData':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Save to Local Storage</title>
    <script>
        function save() {
            localStorage.setItem('note', document.getElementById('note').value);
            alert('Saved');
        }
    </script>
</head>
<body>
    <textarea id="note"></textarea><br>
    <button onclick="save()">Save</button>
</body>
</html>
'''
    if name == 'RetrieveData':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Retrieve from Local Storage</title>
    <script>
        function load() {
            const value = localStorage.getItem('note') || 'No data saved';
            document.getElementById('output').textContent = value;
        }
    </script>
</head>
<body onload="load()">
    <p id="output"></p>
</body>
</html>
'''
    if name == 'UpdateData':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Update Local Storage</title>
    <script>
        function update() {
            localStorage.setItem('note', document.getElementById('note').value);
            alert('Updated');
        }
    </script>
</head>
<body>
    <input id="note" type="text" placeholder="Update note"><br>
    <button onclick="update()">Update</button>
</body>
</html>
'''
    if name == 'DeleteData':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Delete Local Storage</title>
    <script>
        function remove() {
            localStorage.removeItem('note');
            alert('Deleted');
        }
    </script>
</head>
<body>
    <button onclick="remove()">Delete Data</button>
</body>
</html>
'''
    if name == 'Calculator':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Calculator</title>
    <script>
        function calculate() {
            const x = parseFloat(document.getElementById('x').value);
            const y = parseFloat(document.getElementById('y').value);
            document.getElementById('result').textContent = x + y;
        }
    </script>
</head>
<body>
    <input id="x" type="number"> + <input id="y" type="number"><br>
    <button onclick="calculate()">Add</button>
    <p>Result: <span id="result"></span></p>
</body>
</html>
'''
    if name == 'DigitalClock':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Digital Clock</title>
    <script>
        function updateClock() {
            document.getElementById('clock').textContent = new Date().toLocaleTimeString();
        }
        setInterval(updateClock, 1000);
    </script>
</head>
<body>
    <h1 id="clock"></h1>
</body>
</html>
'''
    if name == 'StudentForm':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Student Form</title>
</head>
<body>
    <form>
        <label>Student Name: <input type="text"></label><br>
        <label>Course: <input type="text"></label><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''
    if name == 'ToDoApp':
        return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ToDo App</title>
    <script>
        function addItem() {
            const task = document.getElementById('task').value;
            const list = document.getElementById('tasks');
            const item = document.createElement('li');
            item.textContent = task;
            list.appendChild(item);
        }
    </script>
</head>
<body>
    <input id="task" type="text" placeholder="New task">
    <button onclick="addItem()">Add</button>
    <ul id="tasks"></ul>
</body>
</html>
'''
    if name.startswith('Assessment') and rel_path.endswith('.html'):
        return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{name}</title>
</head>
<body>
    <h1>{name} Page</h1>
    <p>This is a sample assessment page.</p>
</body>
</html>
'''
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{name}</title>
</head>
<body>
    <h1>{name}</h1>
    <p>Sample page for {name}.</p>
</body>
</html>
'''


def write_files():
    for path in java_paths:
        rel = str(path.relative_to(base)).replace('\\', '/')
        path.write_text(java_content(rel), encoding='utf-8')
    for path in sql_paths:
        rel = str(path.relative_to(base)).replace('\\', '/')
        path.write_text(sql_content(rel), encoding='utf-8')
    for path in html_paths:
        rel = str(path.relative_to(base)).replace('\\', '/')
        path.write_text(html_content(rel), encoding='utf-8')
    print(f'Updated {len(java_paths)} Java files, {len(sql_paths)} SQL files, {len(html_paths)} HTML files.')

if __name__ == '__main__':
    write_files()
