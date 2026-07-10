import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DeleteMappingDemo {
    @DeleteMapping("/delete-demo")
    public String deleteDemo() {
        return "DELETE mapping demo";
    }
}
