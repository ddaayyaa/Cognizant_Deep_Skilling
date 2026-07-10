import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PutMappingDemo {
    @PutMapping("/put-demo")
    public String putDemo() {
        return "PUT mapping demo";
    }
}
