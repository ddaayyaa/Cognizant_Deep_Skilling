import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PostMappingDemo {
    @PostMapping("/post-demo")
    public String postDemo() {
        return "POST mapping demo";
    }
}
