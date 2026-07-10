import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class StudentEntity {
    @Id
    private Long id;
    private String name;

    public StudentEntity() {}
}
